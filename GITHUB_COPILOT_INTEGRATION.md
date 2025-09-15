# GitHub Copilot Extension Setup Guide

## Overview
This Reddit MCP Server can be integrated with GitHub Copilot as an extension to provide AI assistants with Reddit data analysis capabilities for user sentiment analysis and product research.

## Prerequisites
- GitHub account with Copilot Pro, Copilot Pro+, or Copilot Free plan
- Reddit API credentials (Client ID and Secret)
- Python 3.8+ installed

## Setup Instructions

### 1. Create GitHub App

1. Go to [GitHub Developer Settings](https://github.com/settings/developers)
2. Click "New GitHub App"
3. Fill in the following details:
   - **App name**: "Reddit MCP Server for Market Research"
   - **Homepage URL**: `https://github.com/xiaojinglingdeyanjing/MultimediaPmAgents`
   - **Callback URL**: `http://localhost:8080/callback`
   - **Webhook URL**: Leave empty for now
   - **Description**: "A GitHub Copilot Extension that provides AI assistants with access to Reddit data for user sentiment analysis and product research"

### 2. Configure Permissions

In the GitHub App settings, configure the following permissions:

#### GitHub Copilot Chat
- **Access**: Read-only

#### Copilot Editor Context
- **Access**: Read-only

#### App Type
- **Type**: Agent
- **URL**: Enter your server's hostname/forwarding endpoint

### 3. Install Dependencies

```bash
# Clone the repository
git clone https://github.com/xiaojinglingdeyanjing/MultimediaPmAgents.git
cd MultimediaPmAgents

# Install Python dependencies
pip install -r reddit-mcp-server/requirements.txt
```

### 4. Configure Environment

1. Copy the environment template:
```bash
cp reddit-mcp-server/config/.env.example .env
```

2. Edit `.env` with your Reddit API credentials:
```bash
REDDIT_CLIENT_ID=your_reddit_client_id_here
REDDIT_CLIENT_SECRET=your_reddit_client_secret_here
REDDIT_USER_AGENT=RedditMCPCrawler/1.0
```

### 5. Start the MCP Server

```bash
# Standard Python
python reddit-mcp-server/src/reddit_mcp_server.py

# Or with conda
C:/Users/tianzijiang/AppData/Local/anaconda3/python.exe reddit-mcp-server/src/reddit_mcp_server.py
```

### 6. Install Extension in GitHub Copilot

1. Go to your GitHub App settings
2. Click "Install App"
3. Select your account/organization
4. The extension will be available in GitHub Copilot Chat

## Available Commands

Once installed, you can use these commands in GitHub Copilot Chat:

### Get Subreddit Posts
```
@reddit-mcp-server get posts from r/Python sorted by hot, limit 10
```

### Get Post Comments
```
@reddit-mcp-server get comments from https://www.reddit.com/r/programming/comments/xyz123/
```

### Search Reddit
```
@reddit-mcp-server search for "machine learning frameworks" in the last month
```

## Use Cases

### Market Research
- "Analyze sentiment about our product on Reddit"
- "Find discussions about competitor products"
- "Track brand mentions across subreddits"

### User Feedback Analysis
- "Get user feedback on the latest iOS update"
- "Find complaints about Tesla vehicles"
- "Analyze gaming community reactions to new releases"

### Trend Identification
- "What are developers saying about AI tools?"
- "Find trending topics in r/technology"
- "Analyze startup discussions on Reddit"

## Advanced Configuration

### Custom Rate Limits
The server includes built-in rate limiting (60 requests/minute). You can modify this in the server code if needed.

### HTML Report Generation
The extension includes HTML report generation capabilities:

```python
from reddit_mcp_server.src.reddit_html_generator import RedditHTMLGenerator

generator = RedditHTMLGenerator()
html_report = generator.generate_complete_report(reddit_data)
```

### Context Passing
The extension supports GitHub Copilot's context passing feature, allowing it to use your local editor context for more tailored responses.

## Security Considerations

- Never commit `.env` files to version control
- Use read-only Reddit API access
- Respect Reddit's API terms of service and rate limits
- Enable GitHub App security features like OIDC authentication

## Troubleshooting

### Common Issues

1. **"Reddit API credentials not found"**
   - Check your `.env` file exists and contains valid credentials
   - Verify environment variables are loaded correctly

2. **"403 Forbidden" errors**
   - Check your Reddit API credentials are correct
   - Verify you're not hitting rate limits (max 60 requests/minute)

3. **Extension not appearing in Copilot**
   - Ensure your GitHub App is properly configured
   - Check that the MCP server is running
   - Verify GitHub App permissions are set correctly

4. **Import errors**
   - Run `pip install -r reddit-mcp-server/requirements.txt`
   - Check Python version compatibility (3.8+)

### Getting Help

- Review the [MCP Server Guide](reddit-mcp-server/docs/MCP_SERVER_GUIDE.md)
- Check [usage examples](reddit-mcp-server/examples/)
- Verify Reddit API setup at https://www.reddit.com/prefs/apps

## Resources

- [GitHub Copilot Extensions Documentation](https://docs.github.com/en/copilot/concepts/extensions/build-extensions)
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.