## Notebook Contents

`ShapefileReprojectDensify`: Convert outcrop orientation line from Lat/Long to UTM coordinates, create dense set of points along line to use as slice boundaries.

`dense_slicing`: Load the pointcloud and the densified line points, slice the pointcloud between each adjacent pair of line points.For each slice, project points to distance in the X-Y plane along a line perpendicular to the orientation line. Slices `pickle`d as a `dict` of `{cumulative_distance: slice_data}`, where `slice_data` is a `dict` of `{ds: recesses, zs: elevations, clr: RGB_colors}`.

`color_classifier`: Train a decision tree ensemble with Adaptive Boosting (`sklearn.ensemble.AdaBoost`) to predict facies class (Sand/Shale/Heterolithic) using HSV values extracted from manually selected facies blocks.

`make_slice_frames`: For each slice, classify all the points using the ensemble model; create a figure by scattering `ds` vs. `zs` w/ colors of predicted classes, and generating barplots of current slice & cumulative class distribution. Save all the frames with zero-padded names such that alphabetic sorting gives the correct order. (See `../media/` directory to find `ffmpeg` movie generation script.)
