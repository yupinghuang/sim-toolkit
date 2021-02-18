from casatasks import bandpass
import sys
parent_dir = sys.argv[1]
ms = sys.argv[2]
bandpass(vis=f'{parent_dir}/{ms}', caltable=f'{parent_dir}/{ms}.gcal', solint='15s, 10MHz', refant='dsa0', uvrange='>7000m')
