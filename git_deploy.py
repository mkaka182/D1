from github import Github
print("Import successful")
g = Github("mkaka182","Vasavi_0405")
print("ID Password successful")
repos =g.search_repositories(query="language : python")
print("query")
for repo in repos:
	print(repo)
