#!bin/bash
for dir in ./video_comment_raw/pending/*
do 
    Name=$(echo $dir | cut -d "/" -f 4)
    
    cut -d , -f 3 ./video_comment_raw/pending/$Name/*.csv 2> /dev/null >> ./video_text/$Name.txt
    cut -d , -f 2 ./video_comment_raw/pending/$Name/*.json 2> /dev/null |cut  --complement -c 1-8 2> /dev/null | tr -d \" >> ./video_text/$Name.txt
    
    mv $dir ./video_comment_raw/done
    
    

done;