import sys
import urllib.request
import requests
import json



def getRepositories(UserID):
    r=requests.get("https://api.github.com/users/{}/repos".format(UserID))
    res = []
    for i in r.json():
        url2 = "https://api.github.com/repos/{}/{}/commits".format(UserID,i['name'])
        r2 = requests.get(url2)
        
        #print(f"Repo: {i['name']} Number of commits: {len(r2.json())}" )
        res.append([i['name'],len(r2.json())])
    return res

if __name__=="__main__":
    UserID = input("User ID : ")
    res = getRepositories(UserID)
    for i in res:
        print("Repo: {} Number of commits: {}".format(i[0],i[1]))
