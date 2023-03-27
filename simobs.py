#!/usr/bin/env python
import casatasks
import casatools
import sys
import os.path

CHAN_WIDTH_KHZ = 134.0

def create_ms(msname: str, conf_file: str, n_chan: int = 1, n_integration: int = 1, integration_time_s: float = 1.5):

    # get antenna positions
    tabname=start_ha+'_antenna_positions_'+os.path.basename(conf_file.split('.cfg')[0])+'.tab'
    tb = casatools.table()
    tb.fromascii(tabname, conf_file, firstline=3, sep=' ', columnnames=['X', 'Y', 'Z', 'DIAM', 'NAME'], datatypes=['D', 'D', 'D', 'D', 'A'])
    xx=tb.getcol('X')
    yy=tb.getcol('Y')
    zz=tb.getcol('Z')
    diam=tb.getcol('DIAM')
    anames=tb.getcol('NAME')
    tb.close()

    # simulate setup
    sm = casatools.simulator()
    me = casatools.measures()
    sm.open(msname)
    pos_ovro_mma=me.observatory('ovro_mma')
    # add Earth radius to ITRF elevation.
    pos_ovro_mma['m2']['value'] += 6.3781e6
    sm.setconfig(telescopename='ovro_mma', x=xx, y=yy, z=zz, dishdiameter=diam, mount='alt-az', antname=list(anames),
                 padname=list(anames), coordsystem='local', referencelocation=pos_ovro_mma)
    sm.setspwindow(spwname='LBand', freq='0.7GHz', deltafreq=f'{CHAN_WIDTH_KHZ}kHz',
                   freqresolution=f'{CHAN_WIDTH_KHZ}kHz', nchannels=int(1.3e6/CHAN_WIDTH_KHZ) + 1,
                   stokes='XX XY YX YY')
    sm.setfeed('perfect X Y')
    sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+85.00.00.000'])
    # declination from wsclean
    sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+37.07.47.400'])
    sm.setauto(autocorrwt=0.0)

    # simulate time
    sm.setlimits(shadowlimit=0.001, elevationlimit='8.0deg')
    sm.settimes(integrationtime=f'{integration_time_s}s', usehourangle=True, referencetime=me.epoch('utc', '58562.0d'))
    total_time_s = integration_time_s * n_integration
    startha = f'-{total_time_s/2}s'
    endha = f'{total_time_s/2}s'
    sm.setoptions(ftmachine='ft')
    sm.observe('source', 'LBand', starttime=startha, stoptime=endha)
    sm.close()

    from casacore import tables
    tables.removeImagingColumns(msname)

if '__name__'=='__main__':
    create_ms()
