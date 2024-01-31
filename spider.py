import requests
import json


# 获取部分信息
def get_data(repo_owner, repo_name, data_type):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/{data_type}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + "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",
    }
    page = 1
    per_page = 30
    issues = []

    while page <= 900:
        params = {"state": "all", "page": page, "per_page": per_page}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            issues += response.json()
            page += 1
        else:
            print(f"获取第 {page} 页issue失败")
            break

    return issues


# 获取全部信息
def get_all_data(repo_owner, repo_name, data_type):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/{data_type}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + "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",
    }
    issues = []
    params = {"state": "all"}
    # 发起GET请求获取第一页的信息
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        issues += response.json()

        # 检查是否有更多的页码，如果有，继续请求下一页的信息
        while "Link" in response.headers and 'rel="next"' in response.headers["Link"]:
            for row in response.headers["Link"].split(", "):
                if 'rel="next"' in row:
                    next_page_url = row.split("; ")[0].strip("<>")
            response = requests.get(next_page_url, headers=headers, params=params)
            if response.status_code == 200:
                issues += response.json()

        # 返回获取的所有信息
        return issues

    # 如果请求失败，则返回空列表
    else:
        return []


def save(all_data, data_type):
    # 将所有信息保存到文件中
    if data_type == "issues":
        with open("data/issues.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(all_data, indent=4))
    elif data_type == "commits":
        with open("data/commits.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(all_data, indent=4))
    else:
        print("数据类型错误！")


repo_owner = "pandas-dev"  # 用户名
repo_name = "pandas"  # 仓库名
data_type = "commits"  # issues / commits
all_data = get_data(repo_owner, repo_name, data_type)
save(all_data, data_type)
print("获取{}条data！".format(len(all_data)))
