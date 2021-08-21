import math
from math import log as In


def approx_val_pi_using_log():
    pi = (In(640320**3 + 744))/(math.sqrt(163))
    return pi


result = approx_val_pi_using_log()
print("The approximate value of Pi using Log is:", result)

