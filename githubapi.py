import sys
import urllib.request
import requests
import json



def get_repo_name(UserID):
    r=requests.get("https://api.github.com/users/{}/repos".format(UserID))
    return [i['name'] for i in r.json()]

def get_commits_num(userId, repoName):
    r2 = requests.get("https://api.github.com/repos/{}/{}/commits".format(userId,repoName))
    return len(r2.json())

def getRepositories(UserID):
    res = []
    repo_json = get_repo_name(UserID)
    for i in repo_json:
        res.append([i,get_commits_num(UserID,i)])
    return res

if __name__=="__main__":
    UserID = input("User ID : ")
    res = getRepositories(UserID)
    for i in res:
        print("Repo: {} Number of commits: {}".format(i[0],i[1]))
