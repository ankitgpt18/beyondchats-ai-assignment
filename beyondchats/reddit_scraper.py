import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import time

def scrape_user_content(profile_url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; PersonaBot/1.0)'}
    posts = []
    comments = []
    # Scrape posts
    posts_url = profile_url.rstrip('/') + '/submitted/'
    r = requests.get(posts_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for post in soup.select('div[data-testid="post-container"]'):
        title = post.select_one('h3')
        if title:
            link = post.find('a', href=True)
            permalink = link.get('href') if isinstance(link, Tag) else posts_url
            posts.append({
                'text': title.text.strip(),
                'permalink': permalink
            })
    # Scrape comments
    comments_url = profile_url.rstrip('/') + '/comments/'
    r = requests.get(comments_url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    for comment in soup.select('div[data-testid="comment"]'):
        body = comment.select_one('div[data-testid="comment"]')
        if body:
            link = comment.find('a', href=True)
            permalink = link.get('href') if isinstance(link, Tag) else comments_url
            comments.append({
                'text': body.text.strip(),
                'permalink': permalink
            })
    return posts, comments 