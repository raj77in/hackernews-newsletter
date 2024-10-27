#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
File: hackernews.py
Author: Amit Agarwal
Date: 2024-10-27
Description: 
    This script fetches the top trending stories from Hacker News using the public Hacker News API. 
    It retrieves the top 50 story IDs, then fetches details for each story, including the title, 
    author, and either the URL or text content if no URL is available.
    
Requirements:
    - requests: Install via `pip install requests`

Usage:
    Run this script to display the top 50 trending stories on Hacker News in the console.
"""

import requests

# URL to retrieve the top stories on Hacker News
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"
STORY_DETAIL_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"

def fetch_top_story_ids(limit=50):
    """
    Fetches the list of top story IDs from Hacker News.
    
    Args:
        limit (int): The number of top story IDs to retrieve. Default is 50.

    Returns:
        list: A list of top story IDs if successful; otherwise, an empty list.
    """
    try:
        response = requests.get(url=TOP_STORIES_URL)
        response.raise_for_status()  # Raise an error for unsuccessful status codes
        return response.json()[:limit]
    except requests.RequestException as e:
        print(f"Error fetching top story IDs: {e}")
        return []

def fetch_story_details(story_id):
    """
    Fetches details of a specific story by its ID.
    
    Args:
        story_id (int): The ID of the story to retrieve.

    Returns:
        dict: The story details in JSON format if successful; otherwise, None.
    """
    try:
        response = requests.get(url=STORY_DETAIL_URL.format(story_id))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching story details for ID {story_id}: {e}")
        return None

def display_trending_stories():
    """
    Retrieves and displays the top 50 trending stories from Hacker News. 
    For each story, it prints the title, author, and either the URL or text content.
    """
    trending_list = fetch_top_story_ids()

    print("\nTop 50 Trending Stories on Hacker News\n" + "-"*40)

    for story_id in trending_list:
        post = fetch_story_details(story_id)
        
        # Check if post data is available and has required fields
        if post and 'title' in post and 'by' in post:
            title = post['title']
            author = post['by']
            additional_info = f"URL: {post.get('url', post.get('text', 'No URL or text available'))}"
            
            print(f"""
Title: {title}
By: {author}
Text/URL: {additional_info}
---
""")
        else:
            print(f"Story with ID {story_id} is missing expected fields.\n")

if __name__ == "__main__":
    display_trending_stories()

