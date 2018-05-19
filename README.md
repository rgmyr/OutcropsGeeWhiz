# OutcropsGeeWhiz
Agile Geoscience Hackathon project -- 5/18-5/20, 2018

## Github Usage

To get started, clone the repo:

```bash
$ git clone https://github.com/rgmyr/OutcropsGeeWhiz.git
```

To make changes, `add` all new changes + `commit` them + `pull` any updates + `push` your changes. **ALWAYS pull before you push!**(But after you commit your changes locally.)

```bash
$ git add -A
$ git commit -m "brief message describing changes"
$ git pull origin master
$ git push origin master
```

Strictly speaking, if we're all only working on one branch, the `origin master` arguments are unnecessary, but I usually just use them anyway.

## Data Parsing

[PyMesh](https://github.com/qnzhou/PyMesh)

- Reads `.stl`, `.ply`, or `.obj` files. 
- `pymesh.slice_mesh(mesh, direction, N)` creates `N` slices of mesh data structure along `direction` (orthogonal to slices).
    - Would need to slice multiple times if we have an outcrop that curves in the x-y plane. (How should we decide on a sequence of segments/`directions` to approximate a curved outcroup... curvature tolerance?)
- `pymesh.distance_to_mesh(mesh, pts)` computes distances from set of points to mesh (and returns closest mesh face + vertex for each point). 
    - We could use this with a vertical sequence of points to compute the weathering profile for each slice (e.g., straight up in the `z`-direction from the most protruding vertex on the slice)? 

[pycollada](https://github.com/pycollada/pycollada)
