from math import pi


def volume_of_sphere(r):
    volume = (4 / 3) * (pi * r**3)
    print("Volume is of sphere with radius %.3f = %.3f " % (r, volume))


volume_of_sphere(4)

