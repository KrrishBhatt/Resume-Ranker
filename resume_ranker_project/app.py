# app to use all methods

import os
from modules.fileparser import extract_text_from_pdf
from modules.keyword_extractor import extract_keywords
from modules.keyword_matcher import match_keywords
from modules.similarity import compute_similarity
from modules.grammar_checker import check_grammar
from modules.utils import save_results_to_csv

# loading paths 
JD_PATH = "job_descriptions/job_description.pdf"
RESUME_FOLDER = "resumes/"
OUTPUT_CSV = "results.csv"

# extract text out of JD and keyword from text
jd_text = extract_text_from_pdf(JD_PATH)
jd_keywords = extract_keywords(jd_text)

# processing each resume
results = []

for filename in os.listdir(RESUME_FOLDER):
    if filename.endswith(".pdf"):
        resume_path = os.path.join(RESUME_FOLDER, filename)
        resume_text = extract_text_from_pdf(resume_path)

        # Match keywords
        matched, missing, match_percent = match_keywords(jd_keywords, resume_text)
        match_percent = float(match_percent)

        # Similarity score
        similarity_score = compute_similarity(jd_text, resume_text)
        similarity_score=float(similarity_score)

        # Grammar and spelling check
        grammar_report = check_grammar(resume_text)

        # Final combined score
        final_score = (match_percent * 0.5) + (similarity_score * 100 * 0.5)

        # Append result
        results.append({
            "resume_name": filename,
            "match_percent": round(match_percent, 2),
            "similarity_score": round(similarity_score, 4),
            "final_score": round(final_score, 2),
            
            "grammar_issues": grammar_report["grammar_count"],
            "spelling_issues": grammar_report["spelling_count"],
            "total_issues": grammar_report["issues_count"],
            "issue_types": list({issue["type"] for issue in grammar_report["details_of_issues"]}),
            "grammar_details": grammar_report["details_of_issues"][:3],
            
            "matched_keywords": matched[:3],
            "missing_keywords": missing[:3]
        })
        
# sorting the resumes in decreasing order based on score
results.sort(key=lambda x: x["final_score"], reverse=True)

# saving to csv file
OUTPUT_CSV="screening_results.csv"
save_results_to_csv(results, OUTPUT_CSV)
print("Results successfully saved to csv")