import csv

#saving the results
def save_results_to_csv(results, output_path):
    headers=[
        "resume_name",
        "match_percent",
        "similarity_score",
        "final_score",
        "grammar_issues",
        "spelling_issues",
        "total_issues",
        "issue_types",
        "matched_keywords",
        "missing_keywords",
        "grammar_details"
    ]
    
    with open(output_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for row in results:
            writer.writerow({
                "resume_name": row["resume_name"],
                "match_percent": row["match_percent"],
                "similarity_score": row["similarity_score"],
                "final_score": row["final_score"],
                "grammar_issues": row["grammar_issues"],
                "spelling_issues": row["spelling_issues"],
                "total_issues": row["total_issues"],
                "issue_types": ", ".join(row["issue_types"]),
                "matched_keywords": ", ".join(row["matched_keywords"]),
                "missing_keywords": ", ".join(row["missing_keywords"]),
                "grammar_details": "; ".join(
                    f"{e['type']}: {e['message']} ({', '.join(e['suggestions'])})"
                    for e in row["grammar_details"]  
                )})