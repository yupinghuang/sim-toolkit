from astropy.io import fits

def scale_image(f, out_file, flux_scale):
    """
    Convert Jy/b to Jy/pixel and change the header

    """
    with fits.open(f) as hdul:
        dat = hdul[0].data
        print(f'Before max = {dat.max()}')
        h = hdul[0].header
        if 'JY/BEAM' in h['BUNIT']:
            assert abs(h['CDELT1']) == abs(h['CDELT2'])
            scale = abs(h['CDELT1'])
            bmaj = hdul[0].header['BMAJ'] / scale
            bmin = hdul[0].header['BMIN'] / scale
            to_jy_per_px = 1.0 / (1.1331 * bmaj * bmin)
            new = dat * flux_scale * to_jy_per_px
            hdul[0].data = new
            h['BUNIT'] = 'JY/PIXEL'
            hdul[0].header = h
            print(f'After max = {new.max()}')
        hdul.writeto(out_file)     
