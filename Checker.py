from git import Repo
import os
import glob
import pandas as pd

git_url = 'https://github.com/ITV/'
URL_Suffix = '.git'

df = pd.read_csv('/Users/timosmit/Downloads/Old repos - Old Repos.csv')
print(df)

commit_list = []

#Read dataframe and clone repo
for repo_dir in df['Repository Name']:
    print(repo_dir)
    repo = Repo.clone_from(git_url + repo_dir + URL_Suffix, f'/Users/timosmit/Documents/Cloned Repos/{repo_dir}') 
    print(repo_dir, "CLONED!")

    #Read the commmit history and return the last date
    commits = list(repo.iter_commits(repo.active_branch))
    latest_commit = commits[-1].committed_datetime
    latest_commit_date = pd.Timestamp(latest_commit)
    
    #add this date to the dataframe
    commit_list.append(latest_commit_date)
    print(latest_commit_date)

    
df['Last Committed Date'] = commit_list
print(df)

df.to_csv('commit_date.csv', encoding = 'utf-8')

