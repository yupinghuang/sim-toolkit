from casatasks import applycal 
import sys
ms = sys.argv[1]
cal = sys.argv[2]

applycal(vis=ms, gaintable=cal, applymode='calonly', flagbackup=False, calwt=False)
