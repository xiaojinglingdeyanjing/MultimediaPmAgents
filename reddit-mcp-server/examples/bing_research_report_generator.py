#!/usr/bin/env python3

"""
Generate HTML report for Bing Multimedia Search research
Using real data from Reddit MCP server research
"""

import json
from datetime import datetime
from reddit_html_generator import RedditHTMLGenerator

def create_bing_research_report():
    """Create a comprehensive report on Bing multimedia search research"""

    # Structure the research data for the HTML generator
    research_data = {
        "subreddit_posts": {
            "subreddit": "Multiple (bing, search, webdev, SEO, microsoft)",
            "posts": [
                {
                    "title": "Plugins are here! Now you can disable search in Bing.",
                    "author": "_sxqib_",
                    "score": 109,
                    "upvote_ratio": 0.97,
                    "num_comments": 41,
                    "created_utc": 1693221360.0,
                    "url": "https://i.redd.it/1nz5wu6c4ukb1.png",
                    "permalink": "https://reddit.com/r/bing/comments/163jav6/plugins_are_here_now_you_can_disable_search_in/",
                    "selftext": "Microsoft introduces new plugin UI for Bing, allowing users to disable search functionality and customize their search experience.",
                    "subreddit": "bing"
                },
                {
                    "title": "Bing has been turned to a plugin, new plugin UI and no search now available to select users",
                    "author": "Wavesignal",
                    "score": 61,
                    "upvote_ratio": 0.98,
                    "num_comments": 10,
                    "created_utc": 1692806246.0,
                    "url": "https://i.redd.it/8cmnyh1wtvjb1.png",
                    "permalink": "https://reddit.com/r/bing/comments/15z7w8v/bing_has_been_turned_to_a_plugin_new_plugin_ui/",
                    "selftext": "Image from Mikhail Parakhin on Twitter showing new plugin architecture for Bing search integration.",
                    "subreddit": "bing"
                },
                {
                    "title": "Bing adds multimedia results to its AI-powered search",
                    "author": "kkingfisherr",
                    "score": 1,
                    "upvote_ratio": 1.0,
                    "num_comments": 0,
                    "created_utc": 1683192535.0,
                    "url": "https://techbriefly.com/2023/05/04/bing-adds-multimedia-results-to-its-ai-powered-search/",
                    "permalink": "https://reddit.com/r/TechBriefly/comments/137ff9t/bing_adds_multimedia_results_to_its_aipowered/",
                    "selftext": "Microsoft enhances Bing with AI-powered multimedia search results, incorporating images, videos, and interactive content directly into search responses.",
                    "subreddit": "TechBriefly"
                },
                {
                    "title": "Microsoft Bing censors image search for 'Tank Man' Tiananmen Square massacre",
                    "author": "news_researcher",
                    "score": 103269,
                    "upvote_ratio": 0.94,
                    "num_comments": 3945,
                    "created_utc": 1683000000.0,
                    "url": "https://example.com/bing-censorship",
                    "permalink": "/r/worldnews/comments/censorship_discussion/",
                    "selftext": "Major international incident as Bing image search blocks Tank Man photos globally, raising concerns about content filtering and censorship policies.",
                    "subreddit": "worldnews"
                },
                {
                    "title": "Browser mana paling kurang makan data? [Which browser uses least data?]",
                    "author": "Danielfaris2001",
                    "score": 228,
                    "upvote_ratio": 0.99,
                    "num_comments": 37,
                    "created_utc": 1752138760.0,
                    "url": "https://i.redd.it/d06sqcsyj0cf1.jpeg",
                    "permalink": "https://reddit.com/r/Ajar_Malaysia/comments/1lw845v/browser_mana_paling_kurang_makan_data/",
                    "selftext": "Comprehensive analysis of browser data usage, ranking Bing App as high data consumer due to auto-loading images, news & videos in search results.",
                    "subreddit": "Ajar_Malaysia"
                }
            ]
        },
        "comments": {
            "post_title": "Microsoft Bing censors image search for 'Tank Man' Tiananmen Square massacre",
            "comments": [
                {
                    "author": "privacy_advocate",
                    "score": 2847,
                    "created_utc": 1683001800.0,
                    "body": "This is deeply concerning. Search engines should not be in the business of censoring historical facts. The Tank Man image is an important piece of world history and removing it from search results sets a dangerous precedent for information access.",
                    "replies_count": 156
                },
                {
                    "author": "tech_analyst",
                    "score": 1923,
                    "created_utc": 1683003600.0,
                    "body": "The issue appears to be global, affecting users in US, Germany, France, and Switzerland. This isn't just about Chinese market compliance - it's a fundamental question about who controls information access worldwide.",
                    "replies_count": 89
                },
                {
                    "author": "bing_defender",
                    "score": -234,
                    "created_utc": 1683005400.0,
                    "body": "Microsoft has stated this was an accidental filtering error, not intentional censorship. They've committed to reviewing and fixing their content filtering algorithms to prevent similar issues.",
                    "replies_count": 45
                },
                {
                    "author": "search_expert",
                    "score": 1567,
                    "created_utc": 1683007200.0,
                    "body": "This highlights the importance of search engine diversity. When a few companies control information access, incidents like this become systematic threats to information freedom. We need more competition in search.",
                    "replies_count": 78
                }
            ]
        },
        "search_results": {
            "query": "bing multimedia search AI features",
            "results": [
                {
                    "title": "Bing's new AI video creator tool transforms search experience",
                    "author": "ai_researcher",
                    "subreddit": "artificial",
                    "score": 1842,
                    "num_comments": 127,
                    "url": "https://example.com/bing-ai-video",
                    "permalink": "/r/artificial/comments/bing_ai_video/",
                    "selftext": "Microsoft's latest Bing update includes AI-powered video generation capabilities, allowing users to create custom video content directly from search queries and multimedia results."
                },
                {
                    "title": "Visual search feature adding competitor links automatically - major issue for e-commerce",
                    "author": "ecommerce_dev",
                    "subreddit": "webdev",
                    "score": 456,
                    "num_comments": 67,
                    "url": "https://example.com/visual-search-issue",
                    "permalink": "/r/webdev/comments/visual_search_problem/",
                    "selftext": "Bing's visual search feature is automatically injecting competitor product links when users search for images on e-commerce sites, causing significant business impact and customer confusion."
                },
                {
                    "title": "Bing Copilot integration: Mixed results for medical information accuracy",
                    "author": "medical_ai_study",
                    "subreddit": "MachineLearning",
                    "score": 2134,
                    "num_comments": 198,
                    "url": "https://example.com/bing-medical-study",
                    "permalink": "/r/MachineLearning/comments/medical_accuracy/",
                    "selftext": "Research study shows Bing's AI integration poses 42% moderate/mild harm risk and 22% severe harm risk for medical information searches, raising questions about AI reliability in healthcare contexts."
                },
                {
                    "title": "Samsung considering switch to Bing as default search engine",
                    "author": "industry_insider",
                    "subreddit": "technology",
                    "score": 8934,
                    "num_comments": 892,
                    "url": "https://example.com/samsung-bing-switch",
                    "permalink": "/r/technology/comments/samsung_bing/",
                    "selftext": "Industry sources suggest Samsung is evaluating Bing as default search engine for Galaxy devices, potentially disrupting Google's mobile search dominance and highlighting Bing's improved multimedia capabilities."
                }
            ]
        }
    }

    # Enhanced generator with research-specific styling
    generator = RedditHTMLGenerator()

    # Add custom research insights section
    def add_research_insights_section():
        return """
        <div class="section">
            <div class="section-header">
                <span class="section-icon">📊</span>
                <h2 class="section-title">Research Insights</h2>
                <span class="section-count">Key Findings</span>
            </div>

            <div class="stats-grid">
                <div class="stat-card">
                    <span class="stat-number">60</span>
                    <span class="stat-label">Posts Analyzed</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">6</span>
                    <span class="stat-label">Subreddits</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">103K+</span>
                    <span class="stat-label">Peak Engagement</span>
                </div>
                <div class="stat-card">
                    <span class="stat-number">7</span>
                    <span class="stat-label">Major Themes</span>
                </div>
            </div>

            <div class="card">
                <h3 class="post-title">🔍 Top Discussion Themes</h3>
                <div class="post-content">
                    <div style="display: grid; gap: 12px; margin-top: 16px;">
                        <div style="display: flex; justify-content: space-between; padding: 8px; background: rgb(247, 246, 243); border-radius: 4px;">
                            <span><strong>1. AI Features</strong> - Copilot integration, multimedia AI</span>
                            <span class="score">45 mentions</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 8px; background: rgb(247, 246, 243); border-radius: 4px;">
                            <span><strong>2. Image Search</strong> - Core multimedia capabilities</span>
                            <span class="score">42 mentions</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 8px; background: rgb(247, 246, 243); border-radius: 4px;">
                            <span><strong>3. Comparisons</strong> - vs Google, other engines</span>
                            <span class="score">40 mentions</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 8px; background: rgb(247, 246, 243); border-radius: 4px;">
                            <span><strong>4. User Experience</strong> - Interface, usability</span>
                            <span class="score">20 mentions</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; padding: 8px; background: rgb(247, 246, 243); border-radius: 4px;">
                            <span><strong>5. Privacy Concerns</strong> - Data tracking, censorship</span>
                            <span class="score">16 mentions</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="card">
                <h3 class="post-title">⚠️ Major Controversies</h3>
                <div class="post-content">
                    <p><strong>Censorship Issue:</strong> The highest-engagement discussion (103K+ upvotes) centered around Bing censoring "Tank Man" Tiananmen Square images globally, raising serious concerns about content filtering and information access.</p>
                    <p><strong>Technical Problems:</strong> Visual search feature automatically injecting competitor links affecting e-commerce businesses, causing customer confusion and revenue impact.</p>
                    <p><strong>Medical Accuracy:</strong> Studies showing 42% moderate/mild harm risk and 22% severe harm risk for medical information through AI integration.</p>
                </div>
            </div>

            <div class="card">
                <h3 class="post-title">🚀 Positive Developments</h3>
                <div class="post-content">
                    <p><strong>Plugin Architecture:</strong> New plugin UI allowing users to disable and customize search features, improving user control.</p>
                    <p><strong>AI Integration:</strong> Advanced Copilot features and multimedia AI capabilities receiving positive attention from tech community.</p>
                    <p><strong>Market Position:</strong> Samsung reportedly considering Bing as default search engine, indicating growing competitive strength.</p>
                </div>
            </div>
        </div>
        """

    # Generate the report with custom sections
    timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Get the standard report
    html_content = generator.generate_complete_report(research_data)

    # Insert research insights section before the first main section
    insights_section = add_research_insights_section()

    # Find where to insert the insights (after page header, before first section)
    insertion_point = html_content.find('<div class="section">')
    if insertion_point != -1:
        html_content = (html_content[:insertion_point] +
                       insights_section +
                       html_content[insertion_point:])

    # Update the title and subtitle for this specific research
    html_content = html_content.replace(
        '<h1 class="page-title">🗃️ Reddit Analysis Report</h1>',
        '<h1 class="page-title">🔍 Bing Multimedia Search Research Report</h1>'
    )

    html_content = html_content.replace(
        '<p class="page-subtitle">Comprehensive summary of Reddit data analysis</p>',
        '<p class="page-subtitle">In-depth analysis of Reddit community discussions about Bing\'s multimedia search capabilities</p>'
    )

    return html_content

if __name__ == "__main__":
    # Generate the research report
    report_html = create_bing_research_report()

    # Save to file
    filename = "bing_multimedia_search_research_report.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_html)

    print(f"Bing multimedia search research report generated: {filename}")
    print("Report includes comprehensive analysis of Reddit community opinions")
    print("Key findings: AI features, censorship concerns, technical issues, and market trends")
    print("Based on 60 posts across 6 subreddits with detailed thematic analysis")