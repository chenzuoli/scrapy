#!/bin/bash

# run this shell file at 0:00 o'clock everyday.

cur_time=`date "+%Y%m%d%H%M%S"`
cur_date=`date "+%Y%m%d"`
echo "################ current time is: $cur_time"

backup_md_path=/mnt/md
hexo_path=/mnt/hexo

echo "move hexo source file to backup directory at $cur_time."
mv $hexo_path/source/_posts/* $backup_md_path/
