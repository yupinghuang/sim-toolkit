from typing import Optional
from numpy.random import Generator, default_rng
import numpy as np

def get_pointing_error(error_rms_deg, size, generator: Optional[Generator]=None):
    if not generator:
        generator = default_rng()
    # should be fine since 1 arcmin = 3e-4 rad
    sep_deg = generator.normal(loc=0.0, scale=error_rms_deg/np.sqrt(2), size=size)
    pa_deg = generator.normal(loc=0.0, scale=error_rms_deg/np.sqrt(2), size=size)
    return sep_deg, pa_deg