# report_generator.py

def export_feedback_to_txt(feedback_list, filename="feedback_report.txt"):
    with open(filename, "w") as file:
        for feedback in feedback_list:
            file.write(feedback + "\n")
    print(f"Feedback exported to {filename}")
