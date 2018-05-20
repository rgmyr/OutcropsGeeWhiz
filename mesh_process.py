#import pymesh
import numpy as np
from scipy.spatial.distance import euclidean
import colorsys

def load_ascii_pts(fname):
    point_cloud = np.loadtxt(fname, skiprows=1)
    coords, rgb = point_cloud[:,:3], point_cloud[:,3:6]
    return coords, rgb


''' Convenience funcs for boundary checking.'''
def above_plane(pt, vec, query):
    return np.dot(query-pt, vec) > 0

def below_plane(pt, vec, query):
    return np.dot(query-pt, vec) < 0

def flatslice_pt_cloud(coords, endpts, colors=None):
    '''Points forms ~left~ and ~right~ boundary planes. Filter out vertices that arent b/t them.
    
    Parameters
    ----------
    coords: np.array, shape=(N, 3)
        Array of [X,Y,Z] point coords 
    endpts : np.array, shape=(2,2)
        The two boundary points defining the slice boundaries, row-wise [X,Y] layout.
        Boundary planes are perpendicular to the X-Y plane and to the line between endpts.
    colors: np.array, shape=(N,3) or (N,4) -- optional
        Array of RGB or RGBA colors associated with each vertex

    Returns
    -------
    zs: np.array, shape=(M,)
        Array of [Z] coordinates of the M points between the boundary planes
    ds: np.array, shape=(M,)
        Array of horizontal recess/depth corresponding to each z-coord
    selected_colors: np.array, size=(M,3) or (M, 4)
        Array of associated values from colors array -- if colors arg provided
    '''
    vec = endpts[1] - endpts[0]
    
    # select points between boundaries
    is_between = lambda v: (above_plane(endpts[0], vec, v) and below_plane(endpts[1], vec, v))
    good_idxs = np.where(np.apply_along_axis(is_between, 1, coords[:, :2]))

    if len(good_idxs) == 0:
        "NOTE: good_idxs is empty!"

    # compute a unit vector perpendicular to slice
    LHS_perp = np.array([-vec[1], vec[0]])
    in_norm =  LHS_perp / np.linalg.norm(LHS_perp)

    recesses = np.matmul(coords[good_idxs,:2], in_norm)
    try:
        recesses -= recesses.min()
    except ValueError:
        pass

    if colors is not None:
        return coords[good_idxs, 2], recesses, good_idxs, colors[good_idxs]
    else:
        return coords[good_idxs, 2], recesses, good_idxs


def slices_from_pt_sequence(coords, pt_rgb, ptseq):
    
    slices = {}
    cum_dist = 0.0
    for i in range(ptseq.shape[0]-1):
        print("Step: ", i, "\tAt cumulative distance: ", cum_dist)
        slice_dict = {}
        endpts = ptseq[i:i+2,:]
        z, d, good_idxs, c = flatslice_pt_cloud(coords, endpts, pt_rgb)
        slices[cum_dist] = {'zs': z, 'ds': d, 'clr': c} 
        cum_dist += euclidean(endpts[0], endpts[1])

        # remove used vertices, hopefully a little quicker
        coords  = np.delete(coords, good_idxs, 0)
        pt_rgb = np.delete(pt_rgb, good_idxs, 0)

    return slices

'''Color array conversion funcs.'''
def rgb_arr_to_hsv(rgb_clrs):
    r2h = lambda c: colorsys.rgb_to_hsv(*tuple(c))
    return np.apply_along_axis(r2h, 1, rgb_clrs)

def hsv_arr_to_rgb(hsv_clrs):
    h2r = lambda c: colorsys.hsv_to_rgb(*tuple(c))
    return np.apply_along_axis(h2r, 1, hsv_clrs)



