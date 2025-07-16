import re
from collections import Counter

def build_persona(posts, comments):
    persona = []
    citations = {}
    all_text = ' '.join([p['text'] for p in posts + comments]).lower()
    words = re.findall(r'\w+', all_text)
    stopwords = set(['the','and','to','a','of','in','is','it','for','on','that','with','as','this','i','you','my','at','be','are','was','but','have','not','they','from','or','so','if','an','by','has','just','like','about','what','do','can','me','we','your','all','one','will','would','there','their','more','when','out','up','how','some','who','get','which','them','he','she','his','her'])
    keywords = [w for w in words if w not in stopwords and len(w) > 3]
    top_interests = [w for w, _ in Counter(keywords).most_common(3)]
    # --- Persona Sections ---
    persona.append("""============================
USER PERSONA
============================
""")
    # Basic Info (placeholders, as Reddit doesn't provide these)
    persona.append("Name: Reddit User\nAge: N/A\nOccupation: N/A\nStatus: N/A\nLocation: N/A\nTier: N/A\nArchetype: N/A\n")
    # Motivations (top keywords)
    persona.append("MOTIVATIONS:")
    if top_interests:
        persona.append(f"- Top interests: {', '.join(top_interests)}")
        for kw in top_interests:
            for item in posts + comments:
                if kw in item['text'].lower():
                    citations[f'Motivation: {kw}'] = item['permalink']
                    break
    else:
        persona.append("- Not enough data to infer motivations.")
    # Personality (writing style)
    total = len(posts) + len(comments)
    avg_len = sum(len(p['text']) for p in posts + comments) / (total or 1)
    persona.append("\nPERSONALITY:")
    if avg_len > 200:
        persona.append("- Prefers detailed, long-form writing.")
        citations['Personality: Writing style'] = posts[0]['permalink'] if posts else (comments[0]['permalink'] if comments else '')
    elif avg_len > 60:
        persona.append("- Writes with moderate detail.")
        citations['Personality: Writing style'] = posts[0]['permalink'] if posts else (comments[0]['permalink'] if comments else '')
    else:
        persona.append("- Prefers short, concise messages.")
        citations['Personality: Writing style'] = posts[0]['permalink'] if posts else (comments[0]['permalink'] if comments else '')
    # Behaviour & Habits (activity)
    persona.append("\nBEHAVIOUR & HABITS:")
    if total > 30:
        persona.append("- Very active Redditor.")
    elif total > 10:
        persona.append("- Moderately active Redditor.")
    else:
        persona.append("- Occasionally active Redditor.")
    citations['Behaviour & Habits: Activity'] = posts[0]['permalink'] if posts else (comments[0]['permalink'] if comments else '')
    # Frustrations (look for negative words)
    persona.append("\nFRUSTRATIONS:")
    negative_words = ['hate', 'problem', 'issue', 'annoy', 'frustrat', 'difficult', 'can\'t', 'cannot', 'fail', 'error', 'bug', 'confus']
    found = False
    for item in posts + comments:
        if any(nw in item['text'].lower() for nw in negative_words):
            persona.append(f"- {item['text'][:100]}...")
            citations['Frustration'] = item['permalink']
            found = True
            break
    if not found:
        persona.append("- No clear frustrations detected.")
    # Goals & Needs (look for 'need', 'want', 'wish', 'goal')
    persona.append("\nGOALS & NEEDS:")
    goal_words = ['need', 'want', 'wish', 'goal', 'hope', 'prefer']
    found = False
    for item in posts + comments:
        if any(gw in item['text'].lower() for gw in goal_words):
            persona.append(f"- {item['text'][:100]}...")
            citations['Goal/Need'] = item['permalink']
            found = True
            break
    if not found:
        persona.append("- No explicit goals/needs detected.")
    persona_text = '\n'.join(persona)
    return persona_text, citations 