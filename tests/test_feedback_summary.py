def summarize_feedback(feedback_list):
    grades = {"A": 0, "B": 0, "C": 0}
    top_score = 0

    for entry in feedback_list:
        score = entry["score"]
        if score >= 85:
            grades["A"] += 1
        elif score >= 70:
            grades["B"] += 1
        else:
            grades["C"] += 1
        top_score = max(top_score, score)

    return {"top_score": top_score, "grade_counts": grades}
