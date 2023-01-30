import dftsource
import numpy as np
import glob

RMS_SCALE_DEG = 1.

l = sorted(glob.glob('/fastpool/data/W-15int-8000chan/*ms'))
rng = np.random.default_rng(seed=20230116)

for ms in l:
    print(ms)
    gains = np.exp(2*np.pi * 1j * rng.normal(scale=RMS_SCALE_DEG/360, size=(2048, 8000, 2)))
    gains = (np.identity(2)[(np.newaxis,) * 3  + (...,)] * gains[...,np.newaxis])
    dftsource.point_src_with_gain(gains, ms)
