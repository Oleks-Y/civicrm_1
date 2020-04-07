import requests
import json

info  = requests.get("https://www.instagram.com/pycoders/?__a=1")
j = json.loads(info.content)
print("Name :"+j["graphql"]["user"]['full_name'])
print("Followers : "+str(j["graphql"]["user"]['edge_followed_by']["count"]))
print("Follow: "+str(j["graphql"]["user"]['edge_follow']["count"]))
print("Likes on the last post:")
#First and second posts ?????

