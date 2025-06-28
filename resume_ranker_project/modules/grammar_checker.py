import language_tool_python 

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text):
    
    matches = tool.check(text)
    
    grammar_count=0
    spelling_count=0
    issues_details=[]
    
    for match in matches:
        if match.ruleIssueType == "grammar":
            grammar_count += 1
        elif match.ruleIssueType == "misspelling":
            spelling_count += 1
            
        issues_details.append({
            "message": match.message,  # mistake 
            "suggestions": match.replacements,  # correction
            "type": match.ruleIssueType  # type of mistake
        })

    return {
        "issues_count": len(matches),
        "grammar_count": grammar_count,
        "spelling_count": spelling_count,
        "details_of_issues":issues_details
    }