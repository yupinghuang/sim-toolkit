#!/usr/bin/env python
import casatasks
import casatools
import sys
import os.path

# set up
msname=sys.argv[1]

conf_file = '/opt/casa-release-5.7.2-4.el7/data/alma/simmos/vla.b.cfg'

# get antenna positions
tabname='antenna_positions_'+os.path.basename(conf_file.split('.cfg')[0])+'.tab'
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

pos_vla=me.observatory('vla')
sm.setconfig(telescopename='vla', x=xx, y=yy, z=zz, dishdiameter=diam, mount='alt-az', antname=list(anames), padname=list(anames), coordsystem='global', referencelocation=pos_vla)

sm.setspwindow(spwname='SBand', freq='2GHz', deltafreq='2MHz', freqresolution='2MHz', nchannels=1000, stokes='RR RL LR LL')
sm.setfeed('perfect R L')
# With rotated.cfg I got 6.11x6.02 with natural weighting.
# sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+85.00.00.000'])
# declination from wsclean
sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+37.07.47.400'])
sm.setauto(autocorrwt=0.0)

# simulate time
# sm.setlimits(shadowlimit=0.001, elevationlimit='8.0deg')
integrationtime='0.45s'
sm.settimes(integrationtime=integrationtime, usehourangle=True, referencetime=me.epoch('utc', '58562.0d'))
startha='-30s'
endha='30s'
sm.setoptions(ftmachine='ft')
sm.observe('source', 'SBand', starttime=startha, stoptime=endha)

from casacore import tables
tables.removeImagingColumns(msname)
