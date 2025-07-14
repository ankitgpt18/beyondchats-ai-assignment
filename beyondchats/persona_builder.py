import re
from collections import Counter

def build_persona(posts, comments):
    persona = []
    citations = {}
    # Interests: most common keywords in posts/comments
    all_text = ' '.join([p['text'] for p in posts + comments]).lower()
    words = re.findall(r'\w+', all_text)
    stopwords = set(['the','and','to','a','of','in','is','it','for','on','that','with','as','this','i','you','my','at','be','are','was','but','have','not','they','from','or','so','if','an','by','has','just','like','about','what','do','can','me','we','your','all','one','will','would','there','their','more','when','out','up','how','some','who','get','which','them','he','she','his','her'])
    keywords = [w for w in words if w not in stopwords and len(w) > 3]
    top_interests = [w for w, _ in Counter(keywords).most_common(3)]
    if top_interests:
        persona.append(f"Top interests: {', '.join(top_interests)}.")
        for kw in top_interests:
            for item in posts + comments:
                if kw in item['text'].lower():
                    citations[f'Interest: {kw}'] = item['permalink']
                    break
    # Activity level
    total = len(posts) + len(comments)
    if total > 30:
        persona.append('Very active Redditor.')
    elif total > 10:
        persona.append('Moderately active Redditor.')
    else:
        persona.append('Occasionally active Redditor.')
    citations['Activity'] = posts[0]['permalink'] if posts else (comments[0]['permalink'] if comments else '')
    # Writing style: average length
    avg_len = sum(len(p['text']) for p in posts + comments) / (total or 1)
    if avg_len > 200:
        persona.append('Prefers detailed, long-form writing.')
    elif avg_len > 60:
        persona.append('Writes with moderate detail.')
    else:
        persona.append('Prefers short, concise messages.')
    citations['Writing style'] = posts[0]['permalink'] if posts else (comments[0]['permalink'] if comments else '')
    persona_text = '\n'.join(persona)
    return persona_text, citations 