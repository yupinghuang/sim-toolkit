import numpy as np
import matplotlib.pyplot as plt

from skimage import draw
from astropy.io import fits
from typing import Tuple, List, Optional

def get_psf_stats(fn, extent_deg):
    im, header = read_image_fits(fn)
    pixel_scale = abs(header['CDELT1'])
    num_pix = abs(header['NAXIS1'])
    max_radius = int(extent_deg/pixel_scale)
    assert max_radius <= num_pix // 2
    radial_avgabs=np.zeros(max_radius)
    radial_std = np.zeros(max_radius)
    radial_maxabs = np.zeros(max_radius)
    for i in range(max_radius):
        circle_perimeter = draw.circle_perimeter(num_pix // 2, num_pix // 2, i)
        radial_avgabs[i] = np.mean(np.abs(im[circle_perimeter]))
        radial_std[i] = np.std(im[circle_perimeter])
        radial_maxabs[i] = np.abs(im[circle_perimeter]).max()
    dist = np.linspace(0, max_radius*pixel_scale*60, num=max_radius)
    return dist, radial_avgabs, radial_std, radial_maxabs


def get_psf_stats2(fn, extent_deg):
    im, header = read_image_fits(fn)
    pixel_scale = abs(header['CDELT1'])
    num_pix = abs(header['NAXIS1'])
    max_radius = int(extent_deg/pixel_scale)
    assert max_radius <= num_pix // 2
    radial_avgabs=np.zeros(max_radius)
    radial_std = np.zeros(max_radius)
    radial_maxabs = np.zeros(max_radius)
    radial_avg = np.zeros(max_radius)
    for i in range(max_radius):
        circle_perimeter = draw.circle_perimeter(num_pix // 2, num_pix // 2, i)
        radial_avgabs[i] = np.mean(np.abs(im[circle_perimeter]))
        radial_avg[i] = np.mean(im[circle_perimeter])
        radial_std[i] = np.std(im[circle_perimeter])
        radial_maxabs[i] = np.abs(im[circle_perimeter]).max()
    dist = np.linspace(0, max_radius*pixel_scale*60, num=max_radius)
    return dist, radial_avgabs, radial_std, radial_maxabs, radial_avg


def read_image_fits(fn: str) -> Tuple[np.array, fits.Header]:
    with fits.open(fn) as hdulist:
        image = hdulist[0].data[0, 0]
        header = hdulist[0].header
    return image, header