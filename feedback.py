def collect_feedback():
    feedback = []
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        try:
            score = float(input("Enter score (0-100): "))
            feedback.append({'name': name, 'score': score})
        except ValueError:
            print("Invalid score. Please enter a number.")
    return feedback
