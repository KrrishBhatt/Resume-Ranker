import re

def match_keywords(jd_keywords, resume_text):
    if isinstance(resume_text, list):
        resume_text = " ".join(resume_text)
    resume_text = resume_text.lower()
    resume_words = re.findall(r'\b\w+\b', resume_text)

    matched = []
    missing = []

    for keyword in jd_keywords:
        keyword_lower = keyword.lower()
        if all(word in resume_words for word in keyword_lower.split()):
            matched.append(keyword)
        else:
            missing.append(keyword)

    match_percent = (len(matched) / len(jd_keywords)) * 100 if jd_keywords else 0
    return matched, missing, float(match_percent) 