# 🤖 Reddit MCP Server

A Model Context Protocol (MCP) server that provides AI assistants with access to Reddit data through three powerful tools: subreddit posts, post comments, and Reddit-wide search capabilities.

## 📁 Project Structure

```
reddit-mcp-server/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── setup_reddit_mcp.py               # Quick setup script
│
├── src/                               # Core source code
│   ├── reddit_mcp_server.py          # Main MCP server
│   └── reddit_html_generator.py      # HTML report generator
│
├── config/                            # Configuration files
│   └── .env.example                   # Environment template
│
├── docs/                              # Documentation
│   └── MCP_SERVER_GUIDE.md           # Comprehensive usage guide
│
├── examples/                          # Usage examples
│   ├── reddit_report_example.py      # Integration examples
│   ├── bing_research_report_generator.py  # Research demo
│   └── reddit_analysis_demo.html     # Sample HTML output
│
└── output/                            # Generated reports
    └── bing_multimedia_search_research_report.html  # Real research example
```

## 🚀 Quick Start

### 1. **Setup**
```bash
# Run the interactive setup script
python setup_reddit_mcp.py
```

### 2. **Configure Reddit API**
- Copy `config/.env.example` to project root as `.env`
- Add your Reddit API credentials
- Get credentials at: https://www.reddit.com/prefs/apps

### 3. **Start Server**
```bash
# Standard Python
python src/reddit_mcp_server.py

# Or with conda
C:/Users/tianzijiang/AppData/Local/anaconda3/python.exe src/reddit_mcp_server.py
```

### 4. **Use with AI Assistant**
Ask Claude Code:
- "Get the top posts from r/Python"
- "Search Reddit for machine learning discussions"
- "Create an HTML report with this Reddit data"

## 🛠️ Available Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `get_subreddit_posts` | Get posts from a specific subreddit | `subreddit_name`, `sort_by`, `limit` |
| `get_post_comments` | Get comments from a Reddit post | `post_url`, `limit` |
| `search_reddit` | Search across all Reddit subreddits | `query`, `sort`, `time_filter`, `limit` |

## 📊 Features

- **🔍 Comprehensive Search** - Access to all of Reddit's content
- **🎨 Beautiful Reports** - Notion-style HTML output
- **⚡ Real-time Data** - Current Reddit discussions and trends
- **🔧 Easy Integration** - Works with Claude Code and other MCP clients
- **📈 Analytics** - Engagement metrics, sentiment analysis
- **🛡️ Rate Limiting** - Built-in protection against API abuse

## 📖 Documentation

- **[Complete Setup Guide](docs/MCP_SERVER_GUIDE.md)** - Detailed installation and usage instructions
- **[Integration Examples](examples/)** - Real-world usage scenarios
- **[API Reference](#api-reference)** - Tool parameters and responses

## 🎯 Use Cases

### Research & Analysis
- Market research and competitor analysis
- Trend identification and sentiment tracking
- Academic research and content analysis

### Business Intelligence
- Brand monitoring and customer feedback
- Industry discussions and expert opinions
- Product launch feedback and reception

### Content Creation
- Topic research and inspiration
- Community insights and trending discussions
- User-generated content analysis

## 📝 Example Usage

```python
# Using with Reddit HTML Generator
from src.reddit_html_generator import RedditHTMLGenerator

# Collect data via MCP server tools, then:
generator = RedditHTMLGenerator()
html_report = generator.generate_complete_report(reddit_data)

# Save beautiful Notion-style report
with open("report.html", "w") as f:
    f.write(html_report)
```

## 🔧 Configuration

### Environment Variables (.env)
```bash
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_client_secret_here
REDDIT_USER_AGENT=RedditMCPCrawler/1.0
```

### Rate Limiting
- Max 60 requests per minute
- Recommended limits: 10-25 items per request
- Built-in error handling and retry logic

## 🐛 Troubleshooting

### Common Issues
1. **"Reddit API credentials not found"** → Check `.env` file
2. **"403 Forbidden"** → Verify API credentials or rate limiting
3. **"Import errors"** → Run `pip install -r requirements.txt`

### Getting Help
- Check the [Complete Guide](docs/MCP_SERVER_GUIDE.md)
- Review [examples](examples/) for usage patterns
- Verify Reddit API setup at https://www.reddit.com/prefs/apps

## 🔐 Security

- Never commit `.env` files to version control
- Use read-only Reddit API access
- Respect Reddit's API terms of service
- Follow rate limiting guidelines

## 📄 License

This project is provided as-is for educational and research purposes. Please respect Reddit's API terms of service and rate limits.

## 🤝 Contributing

This is a personal project, but feel free to fork and adapt for your own use cases.

---

**Built with ❤️ using Model Context Protocol and Reddit API**