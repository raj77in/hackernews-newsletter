# Hacker News Trending Stories

A simple Python script to fetch and display the top 50 trending stories on [Hacker News](https://news.ycombinator.com/) using the public Hacker News API.

## Overview

The `hackernews.py` script retrieves the latest top stories on Hacker News by:
1. Fetching the top 50 story IDs.
2. Displaying each story's title, author, and either the URL or the text content if a URL isn’t available.

This script is lightweight and can be used for quickly browsing what’s trending on Hacker News from the terminal or to send it to your email :).

## Getting Started

### Prerequisites

This script requires Python 3 and the `requests` library. You can install `requests` via pip if you don’t have it already:

```bash
pip install requests
```

### Usage

1. Clone this repository or download the `hackernews.py` script.
2. Run the script with Python:

   ```bash
   python hackernews.py
   ```

The script will output the top 50 stories in a readable format, including each story’s title, author, and link (if available).

### Example Output

```plaintext
Title: Understanding JavaScript Closures
By: john_doe
Text/URL: URL: https://example.com/js-closures
---
Title: New Release: Python 4.0
By: jane_doe
Text/URL: URL: https://example.com/python-4
---
```

Each story includes:
* **Title**: The story’s headline.
* **By**: The author’s username on Hacker News.
* **Text/URL**: The story URL if available, or a snippet of text if no URL is provided.

### Error Handling

The script will gracefully handle network or response errors and continue retrieving stories. If an individual story is missing data, the script will skip it and move to the next story.

## Additional Details

The script uses two API endpoints:
* `https://hacker-news.firebaseio.com/v0/topstories.json`: Retrieves the top story IDs.
* `https://hacker-news.firebaseio.com/v0/item/{id}.json`: Fetches detailed information for each story ID.

This is a simple, educational project for interacting with the Hacker News API, but it’s also useful for checking trending tech news from the command line.

### Notes

Feel free to extend this script by modifying the number of stories retrieved or enhancing the output formatting. Contributions are always welcome!
