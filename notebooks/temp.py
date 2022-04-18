from operator import getitem

from dask.diagnostics import ProgressBar
import dask
import dask.array as da
from daskms import xds_from_ms, xds_from_table, xds_to_table
from africanus.coordinates.dask import radec_to_lm
from africanus.rime.dask import wsclean_predict, predict_vis
from astropy.coordinates import SkyCoord
import astropy.units as u

import numpy as np

def main():
    writes = []
    rms = 0.366268
    for xds in xds_from_ms('/fastpool/data/gh/W-snapshot-8000chan-iono.ms',
                           columns=["UVW", "ANTENNA1", "ANTENNA2", "TIME", "DATA"],
                           group_cols=["FIELD_ID", "DATA_DESC_ID"],
                           chunks={"row": 5e3}):
        vis = da.ones_like(xds.DATA)
        # Assign visibilities to DATA array on the dataset
        xds = xds.assign(MODEL_DATA=(("row", "chan", "corr"), vis))
        writes.append(xds_to_table(xds, '/fastpool/data/gh/W-snapshot-8000chan-iono.ms', ['MODEL_DATA']))

    with ProgressBar():
        dask.compute(writes)
