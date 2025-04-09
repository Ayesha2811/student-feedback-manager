def compute_average(feedback):
    if not feedback:
        return 0.0
    total = sum(entry['score'] for entry in feedback)
    return total / len(feedback)
