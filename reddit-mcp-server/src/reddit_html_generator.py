#!/usr/bin/env python3

import json
from datetime import datetime
from typing import Dict, List, Any
import re

class RedditHTMLGenerator:
    """
    Generates Notion-style HTML summaries for Reddit data from MCP server results
    """

    def __init__(self):
        self.style = self._get_notion_style()

    def _get_notion_style(self) -> str:
        """Returns Notion-inspired CSS styling"""
        return """
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, 'Apple Color Emoji', Arial, sans-serif;
                line-height: 1.5;
                color: rgb(55, 53, 47);
                background-color: rgb(255, 255, 255);
                margin: 0;
                padding: 40px 20px;
                max-width: 900px;
                margin: 0 auto;
            }

            .page-header {
                margin-bottom: 40px;
                border-bottom: 1px solid rgb(227, 226, 224);
                padding-bottom: 20px;
            }

            .page-title {
                font-size: 40px;
                font-weight: 700;
                line-height: 1.2;
                margin-bottom: 8px;
                color: rgb(55, 53, 47);
            }

            .page-subtitle {
                font-size: 16px;
                color: rgb(120, 119, 116);
                margin-bottom: 16px;
            }

            .meta-info {
                display: flex;
                gap: 20px;
                font-size: 14px;
                color: rgb(120, 119, 116);
            }

            .section {
                margin-bottom: 48px;
            }

            .section-header {
                display: flex;
                align-items: center;
                margin-bottom: 24px;
                padding-bottom: 8px;
                border-bottom: 1px solid rgb(227, 226, 224);
            }

            .section-icon {
                font-size: 24px;
                margin-right: 12px;
            }

            .section-title {
                font-size: 24px;
                font-weight: 600;
                color: rgb(55, 53, 47);
            }

            .section-count {
                margin-left: auto;
                background: rgb(227, 226, 224);
                padding: 4px 8px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: 500;
            }

            .card {
                background: rgb(255, 255, 255);
                border: 1px solid rgb(227, 226, 224);
                border-radius: 8px;
                padding: 20px;
                margin-bottom: 16px;
                transition: all 0.2s ease;
            }

            .card:hover {
                box-shadow: 0 4px 8px rgba(15, 15, 15, 0.1);
                border-color: rgb(55, 53, 47);
            }

            .card-header {
                display: flex;
                justify-content: between;
                align-items: flex-start;
                margin-bottom: 12px;
            }

            .post-title {
                font-size: 18px;
                font-weight: 600;
                line-height: 1.3;
                margin-bottom: 8px;
                color: rgb(55, 53, 47);
            }

            .post-title a {
                color: inherit;
                text-decoration: none;
            }

            .post-title a:hover {
                text-decoration: underline;
            }

            .post-meta {
                display: flex;
                flex-wrap: wrap;
                gap: 16px;
                font-size: 14px;
                color: rgb(120, 119, 116);
                margin-bottom: 12px;
            }

            .meta-item {
                display: flex;
                align-items: center;
                gap: 4px;
            }

            .score {
                background: rgb(46, 170, 220);
                color: white;
                padding: 2px 6px;
                border-radius: 4px;
                font-weight: 500;
                font-size: 12px;
            }

            .score.negative {
                background: rgb(235, 87, 87);
            }

            .subreddit-tag {
                background: rgb(227, 226, 224);
                padding: 2px 6px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: 500;
            }

            .post-content {
                color: rgb(55, 53, 47);
                line-height: 1.6;
                margin-top: 12px;
            }

            .comment {
                border-left: 3px solid rgb(227, 226, 224);
                padding-left: 16px;
                margin-bottom: 16px;
            }

            .comment-author {
                font-weight: 600;
                color: rgb(55, 53, 47);
                margin-bottom: 4px;
            }

            .comment-body {
                color: rgb(55, 53, 47);
                line-height: 1.5;
                margin-bottom: 8px;
            }

            .comment-meta {
                font-size: 12px;
                color: rgb(120, 119, 116);
            }

            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 16px;
                margin-bottom: 24px;
            }

            .stat-card {
                background: rgb(247, 246, 243);
                padding: 16px;
                border-radius: 8px;
                text-align: center;
            }

            .stat-number {
                font-size: 24px;
                font-weight: 700;
                color: rgb(55, 53, 47);
                display: block;
            }

            .stat-label {
                font-size: 12px;
                color: rgb(120, 119, 116);
                text-transform: uppercase;
                letter-spacing: 0.5px;
            }

            .empty-state {
                text-align: center;
                padding: 40px;
                color: rgb(120, 119, 116);
                font-style: italic;
            }

            .timestamp {
                font-size: 12px;
                color: rgb(120, 119, 116);
            }

            @media (max-width: 768px) {
                body {
                    padding: 20px 16px;
                }

                .page-title {
                    font-size: 28px;
                }

                .section-title {
                    font-size: 20px;
                }

                .post-meta {
                    flex-direction: column;
                    gap: 8px;
                }

                .stats-grid {
                    grid-template-columns: 1fr;
                }
            }
        </style>
        """

    def _format_timestamp(self, timestamp: float) -> str:
        """Convert Unix timestamp to readable format"""
        try:
            dt = datetime.fromtimestamp(timestamp)
            return dt.strftime("%B %d, %Y at %I:%M %p")
        except:
            return "Unknown time"

    def _truncate_text(self, text: str, max_length: int = 300) -> str:
        """Truncate text to specified length with ellipsis"""
        if len(text) <= max_length:
            return text
        return text[:max_length].rsplit(' ', 1)[0] + "..."

    def _format_score(self, score: int) -> str:
        """Format score with appropriate styling"""
        css_class = "score negative" if score < 0 else "score"
        return f'<span class="{css_class}">{score:,}</span>'

    def generate_subreddit_section(self, subreddit_data: Dict[str, Any]) -> str:
        """Generate HTML for subreddit posts section"""
        if not subreddit_data.get('posts'):
            return f"""
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">📋</span>
                    <h2 class="section-title">Subreddit Posts</h2>
                    <span class="section-count">0 posts</span>
                </div>
                <div class="empty-state">No subreddit posts data available</div>
            </div>
            """

        posts = subreddit_data['posts']
        subreddit_name = subreddit_data.get('subreddit', 'Unknown')

        # Generate stats
        total_score = sum(post.get('score', 0) for post in posts)
        total_comments = sum(post.get('num_comments', 0) for post in posts)
        avg_ratio = sum(post.get('upvote_ratio', 0) for post in posts) / len(posts) if posts else 0

        stats_html = f"""
        <div class="stats-grid">
            <div class="stat-card">
                <span class="stat-number">{len(posts)}</span>
                <span class="stat-label">Posts</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{total_score:,}</span>
                <span class="stat-label">Total Score</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{total_comments:,}</span>
                <span class="stat-label">Comments</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{avg_ratio:.1%}</span>
                <span class="stat-label">Avg Upvote Ratio</span>
            </div>
        </div>
        """

        posts_html = ""
        for post in posts:
            post_html = f"""
            <div class="card">
                <div class="card-header">
                    <div style="flex: 1;">
                        <h3 class="post-title">
                            <a href="{post.get('url', '#')}" target="_blank">{post.get('title', 'Untitled')}</a>
                        </h3>
                        <div class="post-meta">
                            <div class="meta-item">
                                <span>👤</span>
                                <span>{post.get('author', 'Unknown')}</span>
                            </div>
                            <div class="meta-item">
                                <span>📊</span>
                                {self._format_score(post.get('score', 0))}
                            </div>
                            <div class="meta-item">
                                <span>💬</span>
                                <span>{post.get('num_comments', 0):,} comments</span>
                            </div>
                            <div class="meta-item">
                                <span>📈</span>
                                <span>{post.get('upvote_ratio', 0):.1%} upvoted</span>
                            </div>
                            <div class="meta-item">
                                <span>🕒</span>
                                <span class="timestamp">{self._format_timestamp(post.get('created_utc', 0))}</span>
                            </div>
                        </div>
                    </div>
                    <span class="subreddit-tag">r/{post.get('subreddit', subreddit_name)}</span>
                </div>
                {f'<div class="post-content">{self._truncate_text(post.get("selftext", ""))}</div>' if post.get('selftext') else ''}
            </div>
            """
            posts_html += post_html

        return f"""
        <div class="section">
            <div class="section-header">
                <span class="section-icon">📋</span>
                <h2 class="section-title">r/{subreddit_name} Posts</h2>
                <span class="section-count">{len(posts)} posts</span>
            </div>
            {stats_html}
            {posts_html}
        </div>
        """

    def generate_comments_section(self, comments_data: Dict[str, Any]) -> str:
        """Generate HTML for post comments section"""
        if not comments_data.get('comments'):
            return f"""
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">💬</span>
                    <h2 class="section-title">Post Comments</h2>
                    <span class="section-count">0 comments</span>
                </div>
                <div class="empty-state">No comments data available</div>
            </div>
            """

        comments = comments_data['comments']
        post_title = comments_data.get('post_title', 'Unknown Post')

        # Generate stats
        total_score = sum(comment.get('score', 0) for comment in comments)
        avg_score = total_score / len(comments) if comments else 0
        total_replies = sum(comment.get('replies_count', 0) for comment in comments)

        stats_html = f"""
        <div class="stats-grid">
            <div class="stat-card">
                <span class="stat-number">{len(comments)}</span>
                <span class="stat-label">Comments</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{total_score:,}</span>
                <span class="stat-label">Total Score</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{avg_score:.1f}</span>
                <span class="stat-label">Avg Score</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{total_replies:,}</span>
                <span class="stat-label">Total Replies</span>
            </div>
        </div>
        """

        comments_html = ""
        for comment in comments:
            comment_html = f"""
            <div class="card">
                <div class="comment">
                    <div class="comment-author">{comment.get('author', 'Unknown')}</div>
                    <div class="comment-body">{self._truncate_text(comment.get('body', ''))}</div>
                    <div class="comment-meta">
                        {self._format_score(comment.get('score', 0))} •
                        {comment.get('replies_count', 0)} replies •
                        {self._format_timestamp(comment.get('created_utc', 0))}
                    </div>
                </div>
            </div>
            """
            comments_html += comment_html

        return f"""
        <div class="section">
            <div class="section-header">
                <span class="section-icon">💬</span>
                <h2 class="section-title">Comments: {self._truncate_text(post_title, 50)}</h2>
                <span class="section-count">{len(comments)} comments</span>
            </div>
            {stats_html}
            {comments_html}
        </div>
        """

    def generate_search_section(self, search_data: Dict[str, Any]) -> str:
        """Generate HTML for search results section"""
        if not search_data.get('results'):
            return f"""
            <div class="section">
                <div class="section-header">
                    <span class="section-icon">🔍</span>
                    <h2 class="section-title">Search Results</h2>
                    <span class="section-count">0 results</span>
                </div>
                <div class="empty-state">No search results available</div>
            </div>
            """

        results = search_data['results']
        query = search_data.get('query', 'Unknown')

        # Generate stats
        subreddits = set(result.get('subreddit', '') for result in results)
        total_score = sum(result.get('score', 0) for result in results)
        total_comments = sum(result.get('num_comments', 0) for result in results)

        stats_html = f"""
        <div class="stats-grid">
            <div class="stat-card">
                <span class="stat-number">{len(results)}</span>
                <span class="stat-label">Results</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{len(subreddits)}</span>
                <span class="stat-label">Subreddits</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{total_score:,}</span>
                <span class="stat-label">Total Score</span>
            </div>
            <div class="stat-card">
                <span class="stat-number">{total_comments:,}</span>
                <span class="stat-label">Comments</span>
            </div>
        </div>
        """

        results_html = ""
        for result in results:
            result_html = f"""
            <div class="card">
                <div class="card-header">
                    <div style="flex: 1;">
                        <h3 class="post-title">
                            <a href="{result.get('url', '#')}" target="_blank">{result.get('title', 'Untitled')}</a>
                        </h3>
                        <div class="post-meta">
                            <div class="meta-item">
                                <span>👤</span>
                                <span>{result.get('author', 'Unknown')}</span>
                            </div>
                            <div class="meta-item">
                                <span>📊</span>
                                {self._format_score(result.get('score', 0))}
                            </div>
                            <div class="meta-item">
                                <span>💬</span>
                                <span>{result.get('num_comments', 0):,} comments</span>
                            </div>
                        </div>
                    </div>
                    <span class="subreddit-tag">r/{result.get('subreddit', 'Unknown')}</span>
                </div>
                {f'<div class="post-content">{self._truncate_text(result.get("selftext", ""))}</div>' if result.get('selftext') else ''}
            </div>
            """
            results_html += result_html

        return f"""
        <div class="section">
            <div class="section-header">
                <span class="section-icon">🔍</span>
                <h2 class="section-title">Search: "{query}"</h2>
                <span class="section-count">{len(results)} results</span>
            </div>
            {stats_html}
            {results_html}
        </div>
        """

    def generate_complete_report(self, data: Dict[str, Any]) -> str:
        """Generate complete HTML report combining all sections"""
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")

        # Calculate overall stats
        total_items = 0
        if data.get('subreddit_posts', {}).get('posts'):
            total_items += len(data['subreddit_posts']['posts'])
        if data.get('comments', {}).get('comments'):
            total_items += len(data['comments']['comments'])
        if data.get('search_results', {}).get('results'):
            total_items += len(data['search_results']['results'])

        html = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reddit Analysis Report</title>
            {self.style}
        </head>
        <body>
            <div class="page-header">
                <h1 class="page-title">🗃️ Reddit Analysis Report</h1>
                <p class="page-subtitle">Comprehensive summary of Reddit data analysis</p>
                <div class="meta-info">
                    <span>📅 Generated on {timestamp}</span>
                    <span>📊 {total_items} total items analyzed</span>
                    <span>🤖 Powered by Reddit MCP Server</span>
                </div>
            </div>

            {self.generate_subreddit_section(data.get('subreddit_posts', {}))}
            {self.generate_comments_section(data.get('comments', {}))}
            {self.generate_search_section(data.get('search_results', {}))}
        </body>
        </html>
        """

        return html

# Demo function with sample data
def create_demo_report():
    """Create a demo report with sample Reddit data"""
    sample_data = {
        "subreddit_posts": {
            "subreddit": "Python",
            "posts": [
                {
                    "title": "Best practices for Python web development in 2024",
                    "author": "pythondev123",
                    "score": 1284,
                    "upvote_ratio": 0.92,
                    "num_comments": 87,
                    "created_utc": 1704067200,
                    "url": "https://reddit.com/r/Python/example1",
                    "permalink": "/r/Python/comments/example1/",
                    "selftext": "I've been working with Python web development for several years and wanted to share some best practices I've learned. Flask vs Django considerations, async programming patterns, and modern deployment strategies.",
                    "subreddit": "Python"
                },
                {
                    "title": "New Python 3.13 features you should know about",
                    "author": "python_enthusiast",
                    "score": 2156,
                    "upvote_ratio": 0.96,
                    "num_comments": 143,
                    "created_utc": 1704153600,
                    "url": "https://reddit.com/r/Python/example2",
                    "permalink": "/r/Python/comments/example2/",
                    "selftext": "Python 3.13 introduces several exciting features including improved error messages, performance optimizations, and new typing features. Let's explore what's new and how it affects your code.",
                    "subreddit": "Python"
                },
                {
                    "title": "Debugging memory leaks in large Python applications",
                    "author": "performance_guru",
                    "score": 892,
                    "upvote_ratio": 0.89,
                    "num_comments": 56,
                    "created_utc": 1704240000,
                    "url": "https://reddit.com/r/Python/example3",
                    "permalink": "/r/Python/comments/example3/",
                    "selftext": "Memory management in Python can be tricky for large applications. Here are tools and techniques I use to identify and fix memory leaks in production systems.",
                    "subreddit": "Python"
                }
            ]
        },
        "comments": {
            "post_title": "Best practices for Python web development in 2024",
            "comments": [
                {
                    "author": "webdev_pro",
                    "score": 234,
                    "created_utc": 1704067800,
                    "body": "Great post! I'd also add that using type hints consistently throughout your codebase makes a huge difference in maintainability. Tools like mypy can catch so many bugs before they reach production.",
                    "replies_count": 12
                },
                {
                    "author": "django_fan",
                    "score": 156,
                    "created_utc": 1704068400,
                    "body": "For anyone starting out, I highly recommend Django for most web projects. The admin interface alone saves hours of development time, and the ORM is fantastic for rapid prototyping.",
                    "replies_count": 8
                },
                {
                    "author": "flask_lover",
                    "score": 189,
                    "created_utc": 1704069000,
                    "body": "While Django is great, don't overlook Flask for smaller projects or when you need more control. The flexibility it offers is unmatched, especially with modern extensions like Flask-SQLAlchemy and Flask-Migrate.",
                    "replies_count": 15
                }
            ]
        },
        "search_results": {
            "query": "machine learning",
            "results": [
                {
                    "title": "Getting started with machine learning in 2024",
                    "author": "ml_beginner",
                    "subreddit": "MachineLearning",
                    "score": 1567,
                    "num_comments": 98,
                    "url": "https://reddit.com/r/MachineLearning/example1",
                    "permalink": "/r/MachineLearning/comments/example1/",
                    "selftext": "A comprehensive guide for beginners looking to break into machine learning. Covers essential math, programming languages, and practical projects to build your portfolio."
                },
                {
                    "title": "PyTorch vs TensorFlow: Which to choose in 2024?",
                    "author": "deep_learning_expert",
                    "subreddit": "deeplearning",
                    "score": 2341,
                    "num_comments": 187,
                    "url": "https://reddit.com/r/deeplearning/example2",
                    "permalink": "/r/deeplearning/comments/example2/",
                    "selftext": "An in-depth comparison of the two major deep learning frameworks, including performance benchmarks, ease of use, and ecosystem considerations."
                },
                {
                    "title": "Best datasets for practicing machine learning projects",
                    "author": "data_scientist_pro",
                    "subreddit": "datasets",
                    "score": 1823,
                    "num_comments": 134,
                    "url": "https://reddit.com/r/datasets/example3",
                    "permalink": "/r/datasets/comments/example3/",
                    "selftext": "Curated list of high-quality datasets perfect for machine learning practice, from beginner-friendly to advanced challenges across various domains."
                }
            ]
        }
    }

    generator = RedditHTMLGenerator()
    return generator.generate_complete_report(sample_data)

if __name__ == "__main__":
    # Generate demo report
    demo_html = create_demo_report()

    # Save to file
    with open("reddit_analysis_demo.html", "w", encoding="utf-8") as f:
        f.write(demo_html)

    print("Demo HTML report generated: reddit_analysis_demo.html")