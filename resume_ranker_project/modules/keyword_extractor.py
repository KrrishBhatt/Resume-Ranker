import spacy

# loading a pre-trained english NLP model called en_core_web_sm
nlp = spacy.load("en_core_web_sm")

# method to extract the nouns, noun phrases and adjectives from the JD
'''
example: token.text="MongoDB"
         token.pos_="PROPN" (part of speech is proper noun)
         token.ent_type_="ORG"
'''
def extract_keywords(text):
    doc = nlp(text)
    keywords = []
    for token in doc:
        if token.pos_ in ["NOUN", "ADJ", "PROPN"]:
            word = token.text.lower().strip()
            if len(word) > 2 and word not in keywords:
                keywords.append(word)
    return keywords