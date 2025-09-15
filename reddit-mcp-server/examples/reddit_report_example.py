#!/usr/bin/env python3

"""
Example script showing how to use the Reddit HTML Generator
with data from the Reddit MCP server
"""

import json
from reddit_html_generator import RedditHTMLGenerator

def parse_mcp_response(mcp_output: str) -> dict:
    """
    Parse the text output from Reddit MCP server into structured data
    This is a simple parser - in practice you'd want more robust parsing
    """
    # This function would parse the actual MCP server output
    # For demo purposes, we'll return sample structured data

    if "r/" in mcp_output and "posts" in mcp_output.lower():
        # Parse subreddit posts
        return {
            "type": "subreddit_posts",
            "data": {
                "subreddit": "example",
                "posts": []  # Would contain parsed post data
            }
        }
    elif "comments" in mcp_output.lower():
        # Parse comments
        return {
            "type": "comments",
            "data": {
                "post_title": "Example Post",
                "comments": []  # Would contain parsed comment data
            }
        }
    elif "search results" in mcp_output.lower():
        # Parse search results
        return {
            "type": "search_results",
            "data": {
                "query": "example",
                "results": []  # Would contain parsed search results
            }
        }

    return {"type": "unknown", "data": {}}

def create_report_from_mcp_data(subreddit_output: str = None,
                               comments_output: str = None,
                               search_output: str = None,
                               output_filename: str = "reddit_report.html") -> str:
    """
    Create an HTML report from Reddit MCP server outputs

    Args:
        subreddit_output: Output from get_subreddit_posts tool
        comments_output: Output from get_post_comments tool
        search_output: Output from search_reddit tool
        output_filename: Name of the output HTML file

    Returns:
        Path to the generated HTML file
    """

    generator = RedditHTMLGenerator()

    # Initialize report data structure
    report_data = {
        "subreddit_posts": {},
        "comments": {},
        "search_results": {}
    }

    # Parse each type of data if provided
    if subreddit_output:
        parsed = parse_mcp_response(subreddit_output)
        if parsed["type"] == "subreddit_posts":
            report_data["subreddit_posts"] = parsed["data"]

    if comments_output:
        parsed = parse_mcp_response(comments_output)
        if parsed["type"] == "comments":
            report_data["comments"] = parsed["data"]

    if search_output:
        parsed = parse_mcp_response(search_output)
        if parsed["type"] == "search_results":
            report_data["search_results"] = parsed["data"]

    # Generate HTML report
    html_content = generator.generate_complete_report(report_data)

    # Save to file
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    return output_filename

# Example usage
if __name__ == "__main__":
    print("Reddit HTML Generator - Usage Example")
    print("=" * 50)

    # Example 1: Generate report with sample data
    print("1. Generating demo report with sample data...")
    demo_file = create_report_from_mcp_data(
        output_filename="demo_report.html"
    )
    print(f"   Demo report saved as: {demo_file}")

    # Example 2: Show how you would use with actual MCP data
    print("\n2. Example with simulated MCP server data:")

    # Simulate MCP server responses (in practice, these would come from your MCP server)
    simulated_subreddit_data = """
    Found 5 posts from r/Python:

    Title: Best Python Libraries for 2024
    Author: pythondev
    Score: 1500 (upvote ratio: 0.95)
    Comments: 89
    URL: https://example.com
    ---
    """

    simulated_comments_data = """
    Comments from post: Best Python Libraries for 2024

    Author: user1
    Score: 250
    Comment: Great list! I'd also recommend FastAPI for web development...
    Replies: 5
    ---
    """

    simulated_search_data = """
    Search results for 'machine learning' (found 3 posts):

    r/MachineLearning: Introduction to Neural Networks
    Author: ml_expert
    Score: 2000 | Comments: 156
    ---
    """

    # In a real scenario, you'd pass actual MCP server outputs here
    report_file = create_report_from_mcp_data(
        subreddit_output=simulated_subreddit_data,
        comments_output=simulated_comments_data,
        search_output=simulated_search_data,
        output_filename="mcp_data_report.html"
    )
    print(f"   MCP data report saved as: {report_file}")

    print("\n3. Integration with Reddit MCP Server:")
    print("   To use with your actual Reddit MCP server:")
    print("   - Run your MCP server tools (get_subreddit_posts, etc.)")
    print("   - Pass the text outputs to create_report_from_mcp_data()")
    print("   - The generator will create a beautiful Notion-style HTML report")

    print(f"\nAll reports generated successfully! 🎉")
    print("Open the HTML files in your browser to view the reports.")