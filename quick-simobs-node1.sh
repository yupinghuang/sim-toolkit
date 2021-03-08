dir='/lustre/yuping/2021-03-01-dsa2000-configs/1600chan-20210226M'
conf='20210226-configs/20210226M.cfg'

python simobs.py $dir/00.ms -450s -390s $conf &
# Sleep seems to be needed so that log files are separate
sleep 2
python simobs.py $dir/01.ms -390s -330s $conf &
sleep 2
python simobs.py $dir/02.ms -330s -270s $conf &
sleep 2
python simobs.py $dir/03.ms -270s -210s $conf &
sleep 2
python simobs.py $dir/04.ms -210s -150s $conf &
sleep 2
python simobs.py $dir/05.ms -150s -90s $conf &
sleep 2
python simobs.py $dir/06.ms -90s -30s $conf &
sleep 2
python simobs.py $dir/07.ms -30s 30s $conf &
