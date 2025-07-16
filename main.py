import sys
import os
from reddit_scraper import scrape_user_content
from persona_builder import build_persona

OUTPUT_DIR = 'output'

def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <reddit_profile_url>')
        sys.exit(1)
    profile_url = sys.argv[1]
    username = profile_url.rstrip('/').split('/')[-1]
    print(f'Scraping Reddit user: {username}')
    posts, comments = scrape_user_content(profile_url)
    print(f'Fetched {len(posts)} posts and {len(comments)} comments.')
    persona, citations = build_persona(posts, comments)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f'{username}.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(persona)
        f.write('\n\nCitations:\n')
        for trait, cite in citations.items():
            f.write(f'- {trait}: {cite}\n')
    print(f'Persona written to {output_path}')

if __name__ == '__main__':
    main() 