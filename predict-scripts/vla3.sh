model='/lustre/yuping/2020-12-28-dsa2000-take2/model-images/SKAMid_B1_1000h_v3_bright'
msparent='/lustre/yuping/2020-12-28-dsa2000-take2/130chan_60x15s_bright'
for i in {08..11}; do
    wsclean -nwlayers 1 -j 4 -weight natural -predict -name $model $msparent/${i}.ms &
done
wait
