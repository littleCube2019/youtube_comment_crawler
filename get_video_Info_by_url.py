import requests
import json
with open("urls","r") as URL:
    while 1:
        url = URL.readline()
        print(url)
        if url == "":
             print("Done")
             break
        """
        ex:
        https://www.youtube.com/channel/UCnXLslDRBPExnUBunhM918Q
        if 賀龍Hello`s youtube main page
        """
        url = url.split("/")
        #parse the url

        #assertion
        if(len(url)< 3):
            print("please input correct url")
        #error message

        else:
            IdType = url[-2]
            id = url[-1]
            channelId = ""
            # get parsed info

            APIkey = "AIzaSyDvKzWMI2B5VtnG9DWpxTkNiizQvqn7TYo"
            #my API key to access query response

            if IdType == "user": #user id 

                UserId = id

                """
                UserID:at  the end of url
                ex: 黃大謙
                https://www.youtube.com/user/fuckingtinyhippo
                fuckingtinyhippo is his userId

                some youtuber can directly acces their channel id
                ex:Stand up, Brian! 博恩站起來！
                https://www.youtube.com/channel/UCUGlE8lf5qH--_XlsabI2XQ
                """



                findChannelID = "https://www.googleapis.com/youtube/v3/channels?key="+ APIkey + "&forUsername=" + UserId + "&part=id"
                # get channel id by user id
                
                res = requests.get(findChannelID)
                # query through http get method
                
                data = json.loads(res.text)
                #parse data str => dic


                channelId = data["items"][0]["id"]

            elif IdType == "channel":
                channelId = id

            else:
                print("unknow type!")
                print("url is :{},type is: {} , id is {}, please check your input".format(url,IdType,id))

            if channelId != "":
                res = requests.get("https://www.googleapis.com/youtube/v3/search?key="+ APIkey+ "&channelId=" +channelId+"&part=snippet,id&sort=publishedAt%20asc&maxResults=50")
                f = open("video_info.json","a",encoding="utf-8")
                f.write(res.text)
                print("fetch data successfully!")
            else:
                print("some error occurs")
