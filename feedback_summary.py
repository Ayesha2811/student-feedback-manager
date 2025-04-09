def summarize_feedback(feedback):
    if not feedback:
        return {"top_score": None, "grade_counts": {}}

    top_score = max(entry['score'] for entry in feedback)

    grade_counts = {'A': 0, 'B': 0, 'C': 0, 'F': 0}
    for entry in feedback:
        score = entry['score']
        if score >= 85:
            grade_counts['A'] += 1
        elif score >= 70:
            grade_counts['B'] += 1
        elif score >= 50:
            grade_counts['C'] += 1
        else:
            grade_counts['F'] += 1

    return {"top_score": top_score, "grade_counts": grade_counts}
