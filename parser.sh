#!/bin/bash
grep -E "channelTitle|title|videoId|publishedAt" video_info.json | tr -d ",\""  |cut -d ":" -f 2  | tr -d " " > video_IDs
cat video_info.json >> ./used_video_info/used.json
cat /dev/null > video_info.json
