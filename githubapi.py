import sys
import urllib.request
import requests
import json



def getRepositories(UserID):
    r=requests.get(f"https://api.github.com/users/{UserID}/repos")
    res = []
    for i in r.json():
        url2 = f"https://api.github.com/repos/{UserID}/{i['name']}/commits"
        r2 = requests.get(url2)
        
        #print(f"Repo: {i['name']} Number of commits: {len(r2.json())}" )
        res.append(i['name'],len(r2.json()))
    return res

if __name__=="__main__":
    UserID = input("User ID : ")
    res = getRepositories(UserID)
    for i in res:
        print(f"Repo: {i[0]} Number of commits: {i[1]}" )

    print(res)