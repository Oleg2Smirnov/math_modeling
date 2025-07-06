import yt

unit_base = {
    "UnitLength_in_cm":  100,
    "UnitMass_in_g": 1000,
    "UnitVelocity_in_cm_per_s": 100,
}

ae = 1.49e11
box_size = 20 * ae

ds = yt.load("./IC.hdf5", unit_base=unit_base)
plot = yt.SlicePlot(ds, "z", ("gas", "density"), width=(box_size, "m"))
plot.set_cmap(field=("gas", "density"), cmap="inferno")
plot.save("plot.png")


p = yt.SlicePlot(ds, "x", ("gas", "density"))

# Draw a velocity vector every 15 pixels.
p.annotate_velocity(factor=15)
p.save("plot_vectors.png")