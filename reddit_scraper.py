import os
import praw
from dotenv import load_dotenv

load_dotenv()

def scrape_user_content(profile_url):
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("REDDIT_USER_AGENT"),
    )

    username = profile_url.rstrip('/').split('/')[-1]
    redditor = reddit.redditor(username)

    posts = []
    comments = []

    # Fetch submissions (posts)
    for submission in redditor.submissions.new(limit=50):
        posts.append({
            'text': submission.title + "\n" + (submission.selftext or ""),
            'permalink': f"https://www.reddit.com{submission.permalink}"
        })

    # Fetch comments
    for comment in redditor.comments.new(limit=50):
        comments.append({
            'text': comment.body,
            'permalink': f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments 