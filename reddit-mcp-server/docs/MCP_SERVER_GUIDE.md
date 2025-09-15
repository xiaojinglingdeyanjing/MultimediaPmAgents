# 🤖 Reddit MCP Server - Complete Usage Guide

## 📋 Table of Contents

1. [What is MCP?](#what-is-mcp)
2. [Prerequisites](#prerequisites)
3. [Setup & Configuration](#setup--configuration)
4. [Reddit API Setup](#reddit-api-setup)
5. [Running the Server](#running-the-server)
6. [Using with MCP Clients](#using-with-mcp-clients)
7. [Available Tools](#available-tools)
8. [Usage Examples](#usage-examples)
9. [Integration with HTML Generator](#integration-with-html-generator)
10. [Troubleshooting](#troubleshooting)
11. [Advanced Usage](#advanced-usage)

---

## 🔍 What is MCP?

**MCP (Model Context Protocol)** is a standardized protocol that allows AI assistants (like Claude) to connect to external data sources and tools. Your Reddit MCP server acts as a bridge between AI assistants and Reddit's API, enabling:

- **Real-time Reddit data access** - Get current posts, comments, and search results
- **Structured data exchange** - Standardized format for AI consumption
- **Tool-based interactions** - AI can call specific functions to get Reddit data

---

## ⚙️ Prerequisites

### Required Software:
- **Python 3.8+** (you have Python 3.12 via Anaconda)
- **pip** (for package management)
- **Git** (for version control)

### Required Accounts:
- **Reddit Account** - For API access
- **Reddit App Registration** - To get API credentials

### Python Dependencies (already installed):
```
mcp>=1.2.0
praw>=7.7.1
python-dotenv>=1.0.0
```

---

## 🛠️ Setup & Configuration

### 1. **Environment Setup** ✅ (Already Done)

Your environment is already configured with:
- ✅ Python dependencies installed
- ✅ MCP server code ready
- ✅ Environment files created

### 2. **Project Structure**

Your current setup:
```
VIbeCoding/
├── reddit_mcp_server.py          # Main MCP server
├── requirements.txt               # Dependencies
├── .env                          # Environment variables (your credentials)
├── .env.example                  # Template for environment variables
├── reddit_html_generator.py      # HTML report generator
├── reddit_report_example.py      # Usage examples
└── MCP_SERVER_GUIDE.md          # This guide
```

---

## 🔑 Reddit API Setup

### Step 1: Create a Reddit App

1. **Go to Reddit App Preferences:**
   - Visit: https://www.reddit.com/prefs/apps
   - Log in to your Reddit account

2. **Create a New App:**
   - Click "Create App" or "Create Another App"
   - Choose **"script"** as the app type
   - Fill out the form:
     - **Name:** `Reddit MCP Server` (or any name you prefer)
     - **Description:** `MCP server for Reddit data access`
     - **About URL:** Leave blank
     - **Redirect URI:** `http://localhost:8080` (required but not used)

3. **Get Your Credentials:**
   After creating the app, you'll see:
   - **Client ID:** The string under your app name (looks like: `abcdefghijklmn`)
   - **Client Secret:** The "secret" string (looks like: `1234567890abcdefghijklmnop`)

### Step 2: Configure Environment Variables

Edit your `.env` file with your Reddit credentials:

```bash
# Reddit API Configuration
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=RedditMCPCrawler/1.0
```

**Important:**
- Replace `your_client_id_here` with your actual client ID
- Replace `your_client_secret_here` with your actual client secret
- Never commit the `.env` file to version control

---

## 🚀 Running the Server

### Method 1: Standard Python (Already Working)
```bash
py reddit_mcp_server.py
```

### Method 2: Using Conda Python (Recommended)
```bash
C:/Users/tianzijiang/AppData/Local/anaconda3/python.exe reddit_mcp_server.py
```

### What Happens When Running:
- Server starts in **stdio mode**
- Waits for MCP protocol messages on stdin/stdout
- No visible output (this is normal!)
- Ready to accept tool calls from MCP clients

---

## 🔗 Using with MCP Clients

### Option 1: Claude Code (Recommended)

1. **Configure in Claude Code:**
   Add to your MCP configuration:
   ```json
   {
     "mcpServers": {
       "reddit": {
         "command": "python",
         "args": ["C:/Users/tianzijiang/OneDrive - Microsoft/Desktop/VIbeCoding/reddit_mcp_server.py"],
         "env": {
           "REDDIT_CLIENT_ID": "your_client_id",
           "REDDIT_CLIENT_SECRET": "your_client_secret"
         }
       }
     }
   }
   ```

2. **Usage in Claude Code:**
   Once configured, you can ask Claude to:
   - "Get the top posts from r/Python"
   - "Search Reddit for machine learning discussions"
   - "Show me comments on this Reddit post: [URL]"

### Option 2: Direct MCP Client

You can also use any MCP-compatible client to connect to your server.

---

## 🛠️ Available Tools

Your Reddit MCP server provides three powerful tools:

### 1. **get_subreddit_posts**
**Purpose:** Get posts from a specific subreddit

**Parameters:**
- `subreddit_name` (required): Name without "r/" (e.g., "Python")
- `sort_by` (optional): "hot", "new", "top", "rising" (default: "hot")
- `limit` (optional): 1-100 posts (default: 10)

**Example:**
```json
{
  "tool": "get_subreddit_posts",
  "arguments": {
    "subreddit_name": "Python",
    "sort_by": "top",
    "limit": 20
  }
}
```

### 2. **get_post_comments**
**Purpose:** Get comments from a specific Reddit post

**Parameters:**
- `post_url` (required): Full Reddit post URL
- `limit` (optional): 1-50 comments (default: 10)

**Example:**
```json
{
  "tool": "get_post_comments",
  "arguments": {
    "post_url": "https://reddit.com/r/Python/comments/abc123/example_post/",
    "limit": 25
  }
}
```

### 3. **search_reddit**
**Purpose:** Search across all Reddit subreddits

**Parameters:**
- `query` (required): Search terms
- `sort` (optional): "relevance", "hot", "top", "new", "comments" (default: "relevance")
- `time_filter` (optional): "all", "day", "week", "month", "year" (default: "all")
- `limit` (optional): 1-25 results (default: 10)

**Example:**
```json
{
  "tool": "search_reddit",
  "arguments": {
    "query": "machine learning python",
    "sort": "top",
    "time_filter": "week",
    "limit": 15
  }
}
```

---

## 💡 Usage Examples

### Example 1: Getting Hot Posts from r/Python
```python
# This happens automatically when you ask Claude:
# "Get me the top 5 posts from r/Python"

# MCP tool call:
get_subreddit_posts(
    subreddit_name="Python",
    sort_by="hot",
    limit=5
)

# Response includes:
# - Post titles and URLs
# - Author information
# - Scores and upvote ratios
# - Number of comments
# - Post content preview
```

### Example 2: Analyzing Comments on a Viral Post
```python
# Ask Claude:
# "What are people saying about this post: https://reddit.com/r/Python/comments/example/"

# MCP tool call:
get_post_comments(
    post_url="https://reddit.com/r/Python/comments/example/",
    limit=20
)

# Response includes:
# - Top-level comments
# - Comment scores
# - Reply counts
# - Timestamps
```

### Example 3: Researching a Topic
```python
# Ask Claude:
# "Search Reddit for discussions about FastAPI vs Django"

# MCP tool call:
search_reddit(
    query="FastAPI vs Django",
    sort="top",
    time_filter="month",
    limit=10
)

# Response includes:
# - Relevant posts from multiple subreddits
# - Scores and engagement metrics
# - Post previews
```

---

## 📊 Integration with HTML Generator

### Automatic Report Generation

Your setup includes an HTML generator that creates beautiful Notion-style reports:

```python
from reddit_html_generator import RedditHTMLGenerator

# After getting data from MCP server
generator = RedditHTMLGenerator()

# Create comprehensive report
report_data = {
    "subreddit_posts": {...},  # Data from get_subreddit_posts
    "comments": {...},         # Data from get_post_comments
    "search_results": {...}    # Data from search_reddit
}

html_report = generator.generate_complete_report(report_data)
```

### Using with Claude Code

Ask Claude to:
1. **Gather data:** "Get posts from r/Python, comments from top post, and search for 'web frameworks'"
2. **Generate report:** "Create an HTML report with this data"
3. **Result:** Beautiful Notion-style HTML report with all data summarized

---

## 🔧 Troubleshooting

### Common Issues:

#### 1. **"Reddit API credentials not found"**
**Solution:** Check your `.env` file has correct credentials:
```bash
REDDIT_CLIENT_ID=your_actual_client_id
REDDIT_CLIENT_SECRET=your_actual_client_secret
```

#### 2. **"ImportError: cannot import name 'SessionResult'"**
**Solution:** ✅ Already fixed - this import was removed from the code

#### 3. **"403 Forbidden" errors**
**Causes:**
- Invalid API credentials
- Rate limiting (too many requests)
- Subreddit is private/restricted

**Solutions:**
- Verify credentials in Reddit app preferences
- Wait a few minutes and try again
- Try a different subreddit

#### 4. **"Command not found" errors**
**Solutions:**
- Use full Python path: `C:/Users/tianzijiang/AppData/Local/anaconda3/python.exe`
- Ensure you're in the correct directory
- Check Python installation

#### 5. **Server starts but no response**
**This is normal!** MCP servers run in stdio mode and don't show output until they receive tool calls.

### Rate Limiting Best Practices:

Reddit has rate limits. To avoid issues:
- **Don't exceed 60 requests per minute**
- **Use reasonable limits** (don't request 100 posts at once)
- **Add delays** between multiple requests
- **Cache results** when possible

---

## 🚀 Advanced Usage

### 1. **Batch Data Collection**

```python
# Collect comprehensive data about a topic
topic = "artificial intelligence"

# Step 1: Search for relevant posts
search_results = search_reddit(
    query=topic,
    sort="top",
    time_filter="week",
    limit=25
)

# Step 2: Get detailed data from top subreddits
ai_posts = get_subreddit_posts(
    subreddit_name="artificial",
    sort_by="top",
    limit=15
)

ml_posts = get_subreddit_posts(
    subreddit_name="MachineLearning",
    sort_by="hot",
    limit=15
)

# Step 3: Analyze comments on viral posts
# (Extract URLs from previous results and get comments)
```

### 2. **Monitoring Trends**

```python
# Track trending topics across multiple subreddits
subreddits = ["Python", "programming", "webdev", "MachineLearning"]

for subreddit in subreddits:
    hot_posts = get_subreddit_posts(
        subreddit_name=subreddit,
        sort_by="hot",
        limit=10
    )
    # Analyze and store trending topics
```

### 3. **Content Analysis Pipeline**

```python
# 1. Collect data from Reddit MCP server
# 2. Process with HTML generator
# 3. Save reports with timestamps
# 4. Build historical analysis

from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_filename = f"reddit_analysis_{timestamp}.html"

# Generate and save report
html_content = generator.generate_complete_report(data)
with open(report_filename, "w", encoding="utf-8") as f:
    f.write(html_content)
```

---

## 🎯 Next Steps

### Immediate Actions:
1. **✅ Set up Reddit API credentials** in your `.env` file
2. **✅ Test the server** with a simple subreddit request
3. **✅ Generate your first HTML report**

### Possible Enhancements:
- **Add authentication** for private subreddits
- **Implement caching** to avoid rate limits
- **Add data persistence** (save to database)
- **Create scheduled data collection**
- **Build a web interface** for easier access

### Integration Ideas:
- **Research tool** for market analysis
- **Content monitoring** for brand mentions
- **Trend analysis** for investment decisions
- **Social listening** for product feedback

---

## 📞 Support

### Getting Help:
- **Check this guide** for common solutions
- **Review error messages** carefully
- **Test with simple examples** first
- **Verify Reddit API credentials**

### Useful Resources:
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [PRAW Documentation](https://praw.readthedocs.io/)
- [MCP Protocol Specification](https://spec.modelcontextprotocol.io/)

---

**🎉 You're ready to use your Reddit MCP server!**

Start by setting up your Reddit API credentials, then ask Claude to help you explore Reddit data. The combination of the MCP server and HTML generator gives you a powerful toolkit for Reddit analysis and reporting.