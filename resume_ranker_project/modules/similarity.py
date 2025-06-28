# method that tells how semantically close is the resume to the JD
'''
TD-IDF converts text into numbers that respresen how important a word is in a doc relative to other
TF = Term Frequency 
IDF = Inverse Document Frequency
TF-IDF=TF*IDF(0.0-1.0)
'''
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(resume_text, jd_text):
    documents = [jd_text.lower(), resume_text.lower()]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents) # row 1 for JD and row 2 for resume

    # Similarity between JD and resume
    similarity_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] # similarity btw the two rws
    
    return round(similarity_score, 4)
