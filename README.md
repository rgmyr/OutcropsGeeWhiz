# OutcropsGeeWhiz
Agile Geoscience Hackathon project -- 5/18-5/20, 2018

## Data Parsing

[PyMesh](https://github.com/qnzhou/PyMesh)
    - Reads `.stl`, `.ply`, or `.obj` files. 
    - `pymesh.slice_mesh(mesh, direction, N)` creates `N` slices of mesh data structure along `direction` (orthogonal to slices). We would need to slice multiple times if we have an outcrop that curves in the x-y plane. (How should we decide on a sequence of segments/`directions` to approximate a curved outcroup?)
    - `pymesh.distance_to_mesh(mesh, pts)` computes distances from set of points to mesh (+ closest mesh faces/points). Maybe we could use this with a vertical sequence of points to compute the weathering profile for each slice (e.g., straight up from the most protruding point on the slice?)? 

[pycollada](https://github.com/pycollada/pycollada)
