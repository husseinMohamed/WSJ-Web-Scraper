#!/bin/bash



while sleep 300s
do

d=`date '+%Y-%m-%d-%H-%M-%S'`;

wget -O $d.html http://wsj.com/mdc/public/page/2_3021-activnyse-actives.html

java -jar tagsoup-1.2.1.jar --files $d.html 

python3 idk.py "$d.xhtml" > "$d.csv"

done
