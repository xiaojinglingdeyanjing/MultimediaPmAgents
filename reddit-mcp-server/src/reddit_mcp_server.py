#!/usr/bin/env python3

import os
import sys
import asyncio
from typing import Dict, List, Any
import praw
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("reddit-crawler")

# Initialize Reddit client
def get_reddit_client():
    """Initialize and return Reddit client"""
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT", "RedditMCPCrawler/1.0")
    
    if not client_id or not client_secret:
        raise ValueError("Reddit API credentials not found in environment variables")
    
    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

@mcp.tool()
async def get_subreddit_posts(subreddit_name: str, sort_by: str = "hot", limit: int = 10) -> str:
    """
    Get posts from a Reddit subreddit.
    
    Args:
        subreddit_name: Name of the subreddit (without r/)
        sort_by: Sort method - 'hot', 'new', 'top', 'rising'
        limit: Maximum number of posts to retrieve (1-100)
    
    Returns:
        JSON string containing post data
    """
    try:
        reddit = get_reddit_client()
        subreddit = reddit.subreddit(subreddit_name)
        
        # Validate sort_by parameter
        valid_sorts = ['hot', 'new', 'top', 'rising']
        if sort_by not in valid_sorts:
            return f"Error: sort_by must be one of {valid_sorts}"
        
        # Limit the number of posts
        if limit < 1 or limit > 100:
            return "Error: limit must be between 1 and 100"
        
        # Get posts based on sort method
        if sort_by == "hot":
            posts = subreddit.hot(limit=limit)
        elif sort_by == "new":
            posts = subreddit.new(limit=limit)
        elif sort_by == "top":
            posts = subreddit.top(limit=limit)
        elif sort_by == "rising":
            posts = subreddit.rising(limit=limit)
        
        post_data = []
        for post in posts:
            post_info = {
                "title": post.title,
                "author": str(post.author) if post.author else "[deleted]",
                "score": post.score,
                "upvote_ratio": post.upvote_ratio,
                "num_comments": post.num_comments,
                "created_utc": post.created_utc,
                "url": post.url,
                "permalink": f"https://reddit.com{post.permalink}",
                "selftext": post.selftext[:500] + ("..." if len(post.selftext) > 500 else ""),
                "is_video": post.is_video,
                "is_self": post.is_self,
                "subreddit": str(post.subreddit)
            }
            post_data.append(post_info)
        
        return f"Found {len(post_data)} posts from r/{subreddit_name}:\n\n" + "\n".join([
            f"Title: {post['title']}\n"
            f"Author: {post['author']}\n"
            f"Score: {post['score']} (upvote ratio: {post['upvote_ratio']:.2f})\n"
            f"Comments: {post['num_comments']}\n"
            f"URL: {post['url']}\n"
            f"Reddit Link: {post['permalink']}\n"
            f"Text Preview: {post['selftext'][:200]}{'...' if len(post['selftext']) > 200 else ''}\n"
            f"---"
            for post in post_data
        ])
        
    except Exception as e:
        return f"Error fetching posts from r/{subreddit_name}: {str(e)}"

@mcp.tool()
async def get_post_comments(post_url: str, limit: int = 10) -> str:
    """
    Get comments from a specific Reddit post.
    
    Args:
        post_url: Full URL of the Reddit post
        limit: Maximum number of top-level comments to retrieve (1-50)
    
    Returns:
        String containing formatted comment data
    """
    try:
        reddit = get_reddit_client()
        
        # Validate limit
        if limit < 1 or limit > 50:
            return "Error: limit must be between 1 and 50"
        
        submission = reddit.submission(url=post_url)
        submission.comments.replace_more(limit=0)  # Remove "more comments" objects
        
        comments_data = []
        top_comments = submission.comments[:limit]
        
        for comment in top_comments:
            if hasattr(comment, 'body'):  # Ensure it's a comment, not MoreComments
                comment_info = {
                    "author": str(comment.author) if comment.author else "[deleted]",
                    "score": comment.score,
                    "created_utc": comment.created_utc,
                    "body": comment.body[:500] + ("..." if len(comment.body) > 500 else ""),
                    "replies_count": len(comment.replies) if hasattr(comment, 'replies') else 0
                }
                comments_data.append(comment_info)
        
        post_title = submission.title
        return f"Comments from post: {post_title}\n\n" + "\n".join([
            f"Author: {comment['author']}\n"
            f"Score: {comment['score']}\n"
            f"Comment: {comment['body']}\n"
            f"Replies: {comment['replies_count']}\n"
            f"---"
            for comment in comments_data
        ])
        
    except Exception as e:
        return f"Error fetching comments: {str(e)}"

@mcp.tool()
async def search_reddit(query: str, sort: str = "relevance", time_filter: str = "all", limit: int = 10) -> str:
    """
    Search Reddit posts across all subreddits.
    
    Args:
        query: Search query string
        sort: Sort method - 'relevance', 'hot', 'top', 'new', 'comments'
        time_filter: Time filter - 'all', 'day', 'week', 'month', 'year'
        limit: Maximum number of posts to retrieve (1-25)
    
    Returns:
        String containing formatted search results
    """
    try:
        reddit = get_reddit_client()
        
        # Validate parameters
        valid_sorts = ['relevance', 'hot', 'top', 'new', 'comments']
        valid_time_filters = ['all', 'day', 'week', 'month', 'year']
        
        if sort not in valid_sorts:
            return f"Error: sort must be one of {valid_sorts}"
        
        if time_filter not in valid_time_filters:
            return f"Error: time_filter must be one of {valid_time_filters}"
        
        if limit < 1 or limit > 25:
            return "Error: limit must be between 1 and 25"
        
        search_results = reddit.subreddit("all").search(
            query, 
            sort=sort, 
            time_filter=time_filter, 
            limit=limit
        )
        
        results_data = []
        for post in search_results:
            post_info = {
                "title": post.title,
                "author": str(post.author) if post.author else "[deleted]",
                "subreddit": str(post.subreddit),
                "score": post.score,
                "num_comments": post.num_comments,
                "url": post.url,
                "permalink": f"https://reddit.com{post.permalink}",
                "selftext": post.selftext[:300] + ("..." if len(post.selftext) > 300 else "")
            }
            results_data.append(post_info)
        
        return f"Search results for '{query}' (found {len(results_data)} posts):\n\n" + "\n".join([
            f"r/{result['subreddit']}: {result['title']}\n"
            f"Author: {result['author']}\n"
            f"Score: {result['score']} | Comments: {result['num_comments']}\n"
            f"URL: {result['url']}\n"
            f"Reddit Link: {result['permalink']}\n"
            f"Preview: {result['selftext'][:150]}{'...' if len(result['selftext']) > 150 else ''}\n"
            f"---"
            for result in results_data
        ])
        
    except Exception as e:
        return f"Error searching Reddit: {str(e)}"

if __name__ == "__main__":
    # Run the MCP server
    mcp.run(transport="stdio")