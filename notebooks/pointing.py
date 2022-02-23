from typing import Optional
from numpy.random import Generator, default_rng
import numpy as np

def get_pointing_error(error_rms_deg, size, generator: Optional[Generator]=None):
    if not generator:
        generator = default_rng()
    sep_deg = generator.normal(loc=0.0, scale=error_rms_deg, size=size)
    pa_deg = generator.uniform(low=0.0, high=360, size=size)
    return sep_deg, pa_deg