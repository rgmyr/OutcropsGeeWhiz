**NOTE ON UPDATES**: we are working on improvements and extensions to this weekend hackathon project in a private repository for now. This code will likely be open-sourced at a later date. Planned features include data stucture/format conversions, facies boundary modeling, visualization utilities, and GPU acceleration of raw point cloud processing.

# Outcrops, Gee Whiz!

3D digital outcrop models are cool. **Gee Whiz** is it fun to spin them around! Now let's do something interesting with them.

## Dependencies

Base: 

- `numpy`
- `matplotlib`
- `sklearn`

To do shapefile line projections:

- [pyproj](https://github.com/jswhit/pyproj)

To use `mesh` data instead of `[XYZ,RGBA]` point cloud:

- [PyMesh](https://github.com/qnzhou/PyMesh) (Fair Warning: install requires building *a lot* of `C++` dependencies.)

## Organization

`data/`: Input data, and slice frames directory (the latter not uploaded).

`media/`: Presentation slides, figures, movies, and simple `ffmpeg` movie generation script.

`notebooks/`: Jupyter notebooks. See `README` inside for more info.

`models/`: `pickle`d `sklearn.ensemble.AdaBoost` model for (HSV color) --> (sand/shale/heterolithic) classification

`mesh_process.py`: Data loading + point cloud slicing + some convenience functions. Should add some things, rename, and have `PyMesh` functionality in a seperate module.

