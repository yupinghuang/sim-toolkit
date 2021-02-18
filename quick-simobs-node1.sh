python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/00.ms -450s -390s &
# Sleep seems to be needed so that log files are separate
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/01.ms -390s -330s &
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/02.ms -330s -270s &
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/03.ms -270s -210s &
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/04.ms -210s -150s &
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/05.ms -150s -90s &
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/06.ms -90s -30s &
sleep 2
python simobs.py /lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s/07.ms -30s 30s &
