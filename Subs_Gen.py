import csv
from googleapiclient.discovery import build

api_key = "AIzaSyBq7pdzzhjCKeYYsRM6XHSOD-nVA3pI8lI"

youtube = build("youtube", "v3", developerKey=api_key)

x_val = 1

fieldnames = ["x_value", "pewdipie", "t-series"]
csv_file = open("data.csv", "w")
csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
csv_writer.writeheader()

while True:
    csv_file = open("data.csv", "a")
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    request_1 = youtube.channels().list(part="statistics",
                                        forUsername="PewDiePie",
                                        )

    request_2 = youtube.channels().list(part="statistics",
                                        forUsername="tseries",
                                        )

    response_1 = request_1.execute()
    response_2 = request_2.execute()

    csv_writer.writerow({"x_value": x_val, "pewdipie": response_1["items"][0]["statistics"]["subscriberCount"],
                         "t-series": response_2["items"][0]["statistics"]["subscriberCount"]})

    print(x_val)
    print(response_1["items"][0]["statistics"]["subscriberCount"])
    print(response_2["items"][0]["statistics"]["subscriberCount"])

    x_val += 1
