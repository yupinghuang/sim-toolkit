#!/usr/bin/env python
import casatasks
import casatools
import sys
import os.path

# set up
msname=sys.argv[1]
start_ha=sys.argv[2]
end_ha=sys.argv[3]
conf_file=sys.argv[4]

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
sm.setconfig(telescopename='ovro_mma', x=xx, y=yy, z=zz, dishdiameter=diam, mount='alt-az', antname=list(anames), padname=list(anames), coordsystem='local', referencelocation=pos_ovro_mma)
sm.setspwindow(spwname='LBand', freq='1.35GHz', deltafreq='0.8125MHz', freqresolution='0.8125MHz', nchannels=1, stokes='RR RL LR LL')
sm.setfeed('perfect R L')
# With rotated.cfg I got 6.11x6.02 with natural weighting.
# sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+85.00.00.000'])
# declination from wsclean
sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+37.07.47.400'])
sm.setauto(autocorrwt=0.0)

# simulate time
sm.setlimits(shadowlimit=0.001, elevationlimit='8.0deg')
integrationtime='1.5s'
sm.settimes(integrationtime=integrationtime, usehourangle=True, referencetime=me.epoch('utc', '58562.0d'))
startha=start_ha
endha=end_ha
sm.setoptions(ftmachine='ft')
sm.observe('source', 'LBand', starttime=startha, stoptime=endha)
