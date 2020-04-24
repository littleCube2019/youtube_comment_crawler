#!/bin/bash
#get all video_info by main page url
python get_video_Info_by_url.py &  echo "get channel information successfully,clean urls" ; cat /dev/null > urls 

#input urls   ; output: video_info

#clean the urls file 

sh parser.sh & echo "get video id successfully,clean vido_info.json" ; cat /dev/null > video_info.json 
#input video_info ; output video_IDs


python downloader.py 
echo "get video comment successfully,clean video_IDs" ; cat /dev/null > video_IDs 
#input video_IDs

sh get_text.sh & echo "finished"


