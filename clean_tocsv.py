import json
import csv

with open("data/issues.json", "r") as f:
    data = json.load(f)

with open("data/data_all.csv", "w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)

    # 提取的内容
    header = [
        "number",
        "title",
        "user",
        "labels",
        "state",
        "locked",
        "created_at",
        "updated_at",
        "closed_at",
        "comments",
    ]
    csvwriter.writerow(header)

    for item in data:
        number = item["number"]
        title = item["title"]
        user = item["user"]["login"]
        labels = [label["name"] for label in item["labels"]]
        state = item["state"]
        locked = item["locked"]
        created_at = item["created_at"]
        updated_at = item["updated_at"]
        closed_at = item["closed_at"]
        comments = item["comments"]

        csvwriter.writerow(
            [
                number,
                title,
                user,
                labels,
                state,
                locked,
                created_at,
                updated_at,
                closed_at,
                comments,
            ]
        )
