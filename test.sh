#!/bin/bash
echo `date +%Y%m%d`
cur_date = `date +%Y%m%d`
echo "$cur_date"
echo "start scrapy ifeng.com news...\nplease enter one parameter: out put file path & file name."

#cd /usr/local/software/scrapy/get_ifeng_html
#scrapy crawl ifeng_html -o ifeng_html.jl

#cd /usr/local/software/scrapy/ifeng
#scrapy crawl ifenghuang -a filepath=/usr/local/software/scrapy/get_ifeng_html/ifeng_html.jl -o ifenghuang_content.jl 

#python /usr/local/software/scrapy/decode_file.py /usr/local/software/scrapy/ifeng/ifenghuang_content.jl ifenghuang_content_decode.jl

#cd /usr/local/software/hexo/source/_posts/ 
#python /usr/local/software/scrapy/write_md.py /usr/local/software/scrapy/ifeng/ifenghuang_content_decode.jl /usr/local/software/scrapy/ifeng/etl_file.json

#hexo generate
#hexo deploy

#git add .
#git commit -m "add scrapy ifeng.com at " + date
#git push origin master
