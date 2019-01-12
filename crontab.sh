#!/bin/bash

etldate=`date "%Y-%m-%d"`
echo "########## etl date is $etldate"

sh /mnt/scrapy/thrump/yicai/run.sh
sh /mnt/scrapy/thrump/run.sh
