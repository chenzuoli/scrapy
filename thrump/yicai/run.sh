#!/bin/bash

cur_time=`date "+%Y%m%d%H%M%S"`
cur_date=`date "+%Y%m%d"`
echo "########## current time is $cur_time"

base_path=/mnt/scrapy/thrump/yicai
html_path=$base_path/html

cd $base_path
/usr/local/bin/scrapy crawl yicai_news -o $html_path/html_$cur_time.jl

python etl.py $html_path/html_$cur_time.jl ../html/html_$cur_date.json

rm $html_path/html_$cur_time.jl
