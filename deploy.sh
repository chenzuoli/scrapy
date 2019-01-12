#!/bin/bash

cd /usr/local/software/hexo/source/_posts/
python /usr/local/software/scrapy/write_md.py /usr/local/software/scrapy/ifeng/ifenghuang_content_decode.jl /usr/local/software/scrapy/ifeng/etl_file.json

hexo generate
hexo deploy

git add .
git commit -m "add scrapy ifeng.com at " + date
git push origin master
