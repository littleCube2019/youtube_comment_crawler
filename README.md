# youtube_comment_crawler
U2 comment crawler
## 大致流程


將所有主頁url丟到urls

先透過get_video_Info_by_url.py  (main page url => 50 video information )
if 是 userid => 先透過api query轉成 channel id
else if 是 channelid => 直接取得五十部影片的json

儲存成videoInfo.json

再交給parser.sh處理需要的訊息
並製作video_IDs
格式:

videoId
timeStamp
videoTitle
channeltitle


將video_id傳入downloader取得該影片留言
製作成json檔，並放入video_comment_raw資料夾中  

格式:(csv 舊版)
名稱,留言時間,內容

最後交給get_text.sh 取得該影片所有留言

## 使用方法
將要爬的主頁url放入urls
然後呼叫main.sh即可
