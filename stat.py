import datetime
import json
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import requests
from requests.exceptions import HTTPError

closed_time = []
page = 1

token = os.getenv("PAPER_GITHUB_TOKEN")

# Define the headers
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": f"Bearer {token}",
}

# Function to fetch issues
def fetch_issues(state):
    page = 1
    issues = []
    while True:
        response = requests.get(
            "https://api.github.com/repos/ihusharp/paper_reading/issues",
            params={"state": state, "per_page": "100", "page": page},
            headers=headers,
        )
        try:
            response.raise_for_status()
        except requests.HTTPError as http_error:
            print(f"HTTP error occurred: {http_error}")
            sys.exit(1)
        except Exception as err:
            print(f"Other error occurred: {err}")
            sys.exit(1)
        else:
            print("Success!")

        json_response = response.json()
        if not json_response:
            break
        issues.extend(json_response)
        page += 1
    return issues

# Fetch closed and all issues
created_issues = fetch_issues("open")
closed_issues = fetch_issues("closed")

# Extract closed times and created times
created_times = [item["created_at"] for item in created_issues]
closed_times = [item["closed_at"] for item in closed_issues]

# Convert times to datetime and create DataFrames
df_created = pd.DataFrame(index=pd.to_datetime(created_times))
df_closed = pd.DataFrame(index=pd.to_datetime(closed_times))

# Group by day
stat_created = df_created.groupby(pd.Grouper(freq='D')).size()
stat_closed = df_closed.groupby(pd.Grouper(freq='D')).size()

# Plotting
fig, ax = plt.subplots(figsize=(15, 10))
ax.bar(stat_created.index, stat_created.values, label='Open Issues', alpha=0.6, color='orange')
ax.bar(stat_closed.index, stat_closed.values, label='Closed Issues', alpha=0.6, color='purple')

# Set major locator and formatter
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

ax.figure.autofmt_xdate(rotation=30, ha='center')
ax.set_xlabel("Date")
ax.set_ylabel("# Papers")
ax.set_title("Statistics of Reading Papers (up to %s)" %
             datetime.datetime.today().strftime('%Y-%m-%d'))
ax.legend()
plt.savefig("stat.png")