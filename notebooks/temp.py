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
    src_lm = da.array([[0, 0]])
    for xds in xds_from_ms('/fastpool/data/W-800-iono.ms',
                           columns=["UVW", "ANTENNA1", "ANTENNA2", "TIME", "DATA"],
                           group_cols=["FIELD_ID", "DATA_DESC_ID"],
                           chunks={"row": 5e3}):
        freq_arr = (da.arange(800) * 1625e3) + 0.7e9
        src_coh = wsclean_predict(xds['UVW'], src_lm, da.array(['POINT']), da.array([1.0]),
                        da.array([[0]]), da.array([True]), da.array([1.35e9]), da.array([[0,0,0]]), freq_arr)
        # Assign visibilities to DATA array on the dataset
        vis = src_coh * da.array([1, 0, 0, 1])
        xds = xds.assign(MODEL_DATA=(("row", "chan", "corr"), vis))
        writes.append(xds_to_table(xds, '/fastpool/data/W-800-iono.ms.ms', ['MODEL_DATA']))

    with ProgressBar():
        dask.compute(writes)
