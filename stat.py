import datetime
import json
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import requests
from requests.exceptions import HTTPError

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
        except HTTPError as http_error:
            # Provide more context for failures in CI logs
            print(f"HTTP error occurred when fetching {state} issues (page={page}): {http_error}")
            print("Response content:", response.text)
            sys.exit(1)
        except Exception as err:
            print(f"Unexpected error occurred when fetching {state} issues (page={page}): {err}")
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
opened_issues = fetch_issues("open")
closed_issues = fetch_issues("closed")

# Extract closed times and created times
opened_times = [item["created_at"] for item in opened_issues]
closed_times = [item["closed_at"] for item in closed_issues]

# Convert times to datetime and create DataFrames
df_opened = pd.DataFrame(index=pd.to_datetime(opened_times))
df_closed = pd.DataFrame(index=pd.to_datetime(closed_times))

# Group by day
stat_opened = df_opened.groupby(pd.Grouper(freq='W')).size()
stat_closed = df_closed.groupby(pd.Grouper(freq='W')).size()

# Align the indices
stat_opened, stat_closed = stat_opened.align(stat_closed, fill_value=0)

# Calculate open papers and closed papers
open_papers = stat_opened.cumsum()
closed_papers = stat_closed.cumsum()

# Plotting
fig, ax = plt.subplots(figsize=(15, 10))

width = 0.4
dates = stat_opened.index

# Plot bars
ax.bar(dates - pd.Timedelta(days=width/2), stat_opened.values, width=width, 
       label='Started Papers', alpha=0.6, color='lightgreen')
ax.bar(dates + pd.Timedelta(days=width/2), stat_closed.values, width=width, 
       label='Finished Papers', alpha=0.6, color='lightblue')

# Plot the remaining papers line
ax2 = ax.twinx()
ax2.plot(dates, open_papers.values, color='orange', linewidth=2, 
         label='Remaining Papers', marker='o', markersize=4)
ax2.set_ylabel('# Remaining Papers', color='black')

# Plot the finished papers line
ax2.plot(dates, closed_papers.values, color='coral', linewidth=2, 
         label='Finished Papers', marker='o', markersize=4)
ax2.set_ylabel('# Finished Papers', color='black')

# Set major locator and formatter
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Combine legends
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

ax.figure.autofmt_xdate(rotation=30, ha='center')
ax.set_xlabel("Date")
ax.set_ylabel("# Papers")
ax.set_title("Statistics of Reading Papers (up to %s)" % datetime.datetime.today().strftime('%Y-%m-%d'))

plt.tight_layout()
plt.savefig("stat.png")