ffmpeg -framerate 8 -pattern_type glob -i '../data/slice_figs/*.png' -r 30 -pix_fmt yuv420p example_video.mp4
