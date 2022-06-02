class Beam(object):
    def __init__(self, ref: str):
        if ref == 'fit':
            pass
        elif ref == 'sim':
            beam_2_0_data = np.loadtxt('/fastpool/yuping/jonas-beams/Jonas_f=2.00.csv', delimiter=',',
                                       skiprows=1,
                                       dtype={'names': ('phi', 'theta', 'Xamp', 'Xph', 'Yamp', 'Yph'),
                                       'formats': ['f'] * 6})
        else:
            raise ValueError
    