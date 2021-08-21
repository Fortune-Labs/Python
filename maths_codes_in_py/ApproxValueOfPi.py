from math import atan as archtan


def approx_val_pi():
    pi = 16*(archtan(1/5)) - 4*(archtan(1/239))
    return pi


result = approx_val_pi()
print("The approximate value of Pi using arc tangent is:", result)

