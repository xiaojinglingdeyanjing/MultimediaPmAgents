#!/usr/bin/env python3

"""
Quick setup script for Reddit MCP Server
This script helps you configure your Reddit API credentials and test the server
"""

import os
import sys
from pathlib import Path

def check_env_file():
    """Check if .env file exists and has the required variables"""
    env_file = Path(".env")

    if not env_file.exists():
        print("❌ .env file not found!")
        return False

    with open(env_file, 'r') as f:
        content = f.read()

    required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET']
    missing_vars = []

    for var in required_vars:
        if var not in content or f"{var}=your_" in content:
            missing_vars.append(var)

    if missing_vars:
        print(f"❌ Missing or placeholder values for: {', '.join(missing_vars)}")
        return False

    print("✅ .env file configured correctly!")
    return True

def setup_env_file():
    """Interactive setup of .env file"""
    print("\n🔧 Setting up Reddit API credentials...")
    print("You'll need to create a Reddit app first:")
    print("1. Go to https://www.reddit.com/prefs/apps")
    print("2. Click 'Create App' or 'Create Another App'")
    print("3. Choose 'script' as app type")
    print("4. Fill in a name and description")
    print("5. Use 'http://localhost:8080' as redirect URI")
    print()

    client_id = input("Enter your Reddit Client ID: ").strip()
    client_secret = input("Enter your Reddit Client Secret: ").strip()
    user_agent = input("Enter User Agent (or press Enter for default): ").strip()

    if not user_agent:
        user_agent = "RedditMCPCrawler/1.0"

    env_content = f"""# Reddit API Configuration
REDDIT_CLIENT_ID={client_id}
REDDIT_CLIENT_SECRET={client_secret}
REDDIT_USER_AGENT={user_agent}
"""

    with open(".env", "w") as f:
        f.write(env_content)

    print("✅ .env file created successfully!")

def test_reddit_connection():
    """Test connection to Reddit API"""
    print("\n🧪 Testing Reddit API connection...")

    try:
        import praw
        from dotenv import load_dotenv

        load_dotenv()

        client_id = os.getenv("REDDIT_CLIENT_ID")
        client_secret = os.getenv("REDDIT_CLIENT_SECRET")
        user_agent = os.getenv("REDDIT_USER_AGENT", "RedditMCPCrawler/1.0")

        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )

        # Test by getting a simple subreddit info
        subreddit = reddit.subreddit("Python")
        print(f"✅ Successfully connected to Reddit!")
        print(f"   Test subreddit: r/{subreddit.display_name}")
        print(f"   Subscribers: {subreddit.subscribers:,}")
        return True

    except Exception as e:
        print(f"❌ Failed to connect to Reddit: {e}")
        return False

def test_mcp_server():
    """Test if the MCP server can start"""
    print("\n🖥️  Testing MCP server startup...")

    try:
        # Import to check if all dependencies are available
        from mcp.server.fastmcp import FastMCP
        import praw
        from dotenv import load_dotenv

        print("✅ All dependencies are available!")
        print("✅ MCP server should start successfully!")
        return True

    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def show_usage_examples():
    """Show example usage"""
    print("\n📖 Usage Examples:")
    print("=" * 50)

    print("\n1. Starting the MCP Server:")
    print("   py src/reddit_mcp_server.py")
    print("   # Or with conda:")
    print("   C:/Users/tianzijiang/AppData/Local/anaconda3/python.exe src/reddit_mcp_server.py")

    print("\n2. Using with Claude Code:")
    print("   Ask Claude: 'Get the top posts from r/Python'")
    print("   Ask Claude: 'Search Reddit for machine learning discussions'")
    print("   Ask Claude: 'Create an HTML report of this Reddit data'")

    print("\n3. Available Tools:")
    print("   • get_subreddit_posts - Get posts from a subreddit")
    print("   • get_post_comments - Get comments from a post")
    print("   • search_reddit - Search across all of Reddit")

    print("\n4. Generating Reports:")
    print("   py src/reddit_html_generator.py  # Creates demo report")
    print("   py examples/reddit_report_example.py  # Shows integration examples")

def main():
    """Main setup routine"""
    print("🤖 Reddit MCP Server Setup")
    print("=" * 40)

    # Check if we're in the right directory
    if not Path("src/reddit_mcp_server.py").exists():
        print("❌ src/reddit_mcp_server.py not found!")
        print("   Make sure you're in the reddit-mcp-server directory.")
        return

    # Step 1: Check dependencies
    print("\n1️⃣  Checking dependencies...")
    try:
        import mcp
        import praw
        from dotenv import load_dotenv
        print("✅ All Python dependencies are installed!")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("   Run: pip install -r requirements.txt")
        return

    # Step 2: Check .env file
    print("\n2️⃣  Checking environment configuration...")
    if not check_env_file():
        setup_env = input("\nWould you like to set up your .env file now? (y/n): ").lower()
        if setup_env == 'y':
            setup_env_file()
        else:
            print("⚠️  You'll need to configure .env manually before using the server.")
            return

    # Step 3: Test Reddit connection
    print("\n3️⃣  Testing Reddit API connection...")
    if not test_reddit_connection():
        print("⚠️  Please check your Reddit API credentials.")
        return

    # Step 4: Test MCP server
    print("\n4️⃣  Testing MCP server...")
    if not test_mcp_server():
        return

    # Step 5: Show usage examples
    show_usage_examples()

    print("\n🎉 Setup Complete!")
    print("   Your Reddit MCP server is ready to use!")
    print("   Check MCP_SERVER_GUIDE.md for detailed instructions.")

if __name__ == "__main__":
    main()