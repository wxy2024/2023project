import requests
import json


# 获取部分issue
def get_issues(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {"Accept": "application/vnd.github.v3+json"}
    page = 1
    per_page = 30
    issues = []

    while page <= 3:
        params = {"page": page, "per_page": per_page}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            issues += response.json()
            page += 1
        else:
            print(f"获取第 {page} 页issue失败")
            break

    return issues


# 获取全部issue
def get_all_issues(repo_owner, repo_name):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {"Accept": "application/vnd.github.v3+json"}
    issues = []
    params = {
        "state": "all"
    }
    # 发起GET请求获取第一页的issue
    response = requests.get(url, headers=headers,params=params)
    if response.status_code == 200:
        issues += response.json()

        # 检查是否有更多的页码，如果有，继续请求下一页的issue
        while "Link" in response.headers and 'rel="next"' in response.headers["Link"]:
            next_page_url = (
                response.headers["Link"].split(", ")[1].split("; ")[0].strip("<>")
            )
            response = requests.get(next_page_url, headers=headers,params=params)
            if response.status_code == 200:
                issues += response.json()

        # 返回获取的所有issue
        return issues

    # 如果请求失败，则返回空列表
    else:
        return []


repo_owner = "BeyondDimension"  # 用户名
repo_name = "SteamTools"  # 仓库名

all_issues = get_issues(repo_owner, repo_name)
for issue in all_issues:
    print(issue["title"])

# 将所有issue保存到文件中
with open("data/issues.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(all_issues, indent=4))

print("获取{}条issue！".format(len(all_issues)))
