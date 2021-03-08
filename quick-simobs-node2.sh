dir='/lustre/yuping/2021-03-01-dsa2000-configs/1600chan-20210226M/'
conf='20210226-configs/20210226M.cfg'

python simobs.py $dir/08.ms 30s 90s $conf &
sleep 2
python simobs.py $dir/09.ms 90s 150s $conf &
sleep 2
python simobs.py $dir/10.ms 150s 210s $conf &
sleep 2
python simobs.py $dir/11.ms 210s 270s $conf &
sleep 2
python simobs.py $dir/12.ms 270s 330s $conf &
sleep 2
python simobs.py $dir/13.ms 330s 390s $conf &
sleep 2
python simobs.py $dir/14.ms 390s 450s $conf &
