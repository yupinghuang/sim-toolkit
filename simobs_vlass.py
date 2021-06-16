#!/usr/bin/env python
import casatasks
import casatools
import sys
import os.path

# set up
msname=sys.argv[1]
start_ha=sys.argv[2]
end_ha=sys.argv[3]

# simulate setup
sm = casatools.simulator()
me = casatools.measures()
sm.open(msname)
sm.setknownconfig('vla.b')
sm.setspwindow(spwname='LBand', freq='0.7GHz', deltafreq='325kHz', freqresolution='325kHz', nchannels=4000, stokes='RR RL LR LL')
sm.setfeed('perfect R L')
# With rotated.cfg I got 6.11x6.02 with natural weighting.
# sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+85.00.00.000'])
# declination from wsclean
sm.setfield(sourcename='source', sourcedirection=['J2000', '00h00m0.0', '+37.07.47.400'])
sm.setauto(autocorrwt=0.0)

# simulate time
sm.setlimits(shadowlimit=0.001, elevationlimit='8.0deg')
integrationtime='60s'
sm.settimes(integrationtime=integrationtime, usehourangle=True, referencetime=me.epoch('utc', '58562.0d'))
startha=start_ha
endha=end_ha
sm.setoptions(ftmachine='ft')
sm.observe('source', 'LBand', starttime=startha, stoptime=endha)
