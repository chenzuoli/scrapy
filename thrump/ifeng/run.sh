#!/bin/bash

cur_time=`date "+%Y%m%d%H%M%S"`
cur_date=`date "+%Y%m%d"`
echo "########## current time is $cur_time, get the html start..."

base_path=/mnt/scrapy/thrump/ifeng
html_path=$base_path/html
content_path=$base_path/content
decode_content_path=$base_path/decoded_file
etl_path=$base_path/etl
md_path=$base_path/md
backup_md_path=/mnt/md
backup_etl_path=/mnt/etl
backup_decode_path=/mnt/decoded_file
backup_content_path=/mnt/content
backup_html_path=/mnt/html
hexo_path=/mnt/hexo
#website_path=/var/www/html

cd $base_path
/usr/local/bin/scrapy crawl ifeng_news -o $html_path/html_$cur_time.jl

python etl.py $html_path/html_$cur_time.jl $html_path/html_$cur_date.json


echo "########## get the html content start..."

cd $base_path
/usr/local/bin/scrapy crawl content -a filepath=$html_path/html_$cur_date.json -o $content_path/content_$cur_time.jl

echo "################ decode the result file with unicode to utf-8."
python $base_path/decode.py $content_path/content_$cur_time.jl $decode_content_path/content_$cur_time.json

echo "################ etl the content and write the md file."
cd $base_path/md
python $base_path/write_md.py $decode_content_path/content_$cur_time.json $etl_path/content_$cur_time.json

echo "################ insert the content into mysql."
python $base_path/tomysql.py $etl_path/content_$cur_time.json

echo "################ backup content/etl/decoded/md file."
#mv $hexo_path/source/_posts/* $backup_md_path/
rm $content_path/* $backup_content_path/
rm $etl_path/* $backup_etl_path/
rm $decode_content_path/* $backup_decode_path/
rm $html_path/* $backup_html_path/

echo "################ deploy the md file."
mv $md_path/*.md $hexo_path/source/_posts/

#echo "################ commit scrapy project."
#cd $parent_path
#git add .
#git commit -m "commit at $cur_time"
#git push origin master

cd $hexo_path
/usr/local/bin/hexo generate
/usr/local/bin/hexo deploy

echo "################ commit hexo project."
#git add .
#git commit -m "commit at $cur_time"
#git push origin master

#cd $website_path
#git pull origin master
