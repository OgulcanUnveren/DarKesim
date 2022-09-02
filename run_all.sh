#!/bin/sh
cd /data/data/com.termux/dar_kesim/
source env/bin/activate
python /data/data/com.termux/dar_kesim/deterics.py & 
#python3 deterist.py &  
bash /data/data/com.termux/dar_kesim/webapp/runinpath.sh 
