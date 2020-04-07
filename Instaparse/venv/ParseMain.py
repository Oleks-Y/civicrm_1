import requests
import bs4
import json

def getInfo(name):
    if(name[0]=="@"):
        name = name[1:]
    info  = requests.get("https://www.instagram.com/{}/?__a=1".format(name));
    j = json.loads(info.content)
    #Check if acoount is private!!!

    #Count of comments
    total_comments = 0
    for i in j["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
        total_comments+=int(i["node"]["edge_media_to_comment"]["count"])

    #count of likes
    total_likes=0
    for i in j["graphql"]["user"]["edge_owner_to_timeline_media"]["edges"]:
        total_likes+=int(i["node"]["edge_liked_by"]["count"])

    return {
        "biography":j["graphql"]["user"]["biography"],
        "followers":j["graphql"]["user"]["edge_followed_by"]["count"],
        "follow":j["graphql"]["user"]["edge_follow"]["count"],
        "full_name": j["graphql"]["user"]["full_name"],
        "is_business_account":j["graphql"]["user"]["is_business_account"],
        "business_category_name": j["graphql"]["user"]["business_category_name"],
        "Likes":total_likes,
        "Comments":total_comments

            }

