def recommend_action(message, priority, category):

    text = message.lower()

    if priority == "High":

        if category == "Academic":
            return "Complete the academic task immediately and check the deadline."

        elif category == "Financial":
            return "Review the financial issue immediately and take the required action."

        elif category == "Work/Professional":
            return "Review the message immediately and respond or escalate if necessary."

        elif category == "Personal":
            return "Review the message and respond as soon as possible."

        else:
            return "Review the message immediately and take appropriate action."

    elif priority == "Medium":

        if category == "Academic":
            return "Review the academic message and complete the task before the deadline."

        elif category == "Financial":
            return "Review the financial information and respond when required."

        elif category == "Work/Professional":
            return "Review the message and respond during your normal working time."

        elif category == "Personal":
            return "Review the message and respond when convenient."

        else:
            return "Review the message and take action if required."

    else:

        if category == "Promotional":
            return "No immediate action required. Review or ignore the promotional message."

        elif category == "Personal":
            return "No immediate action required. Respond when convenient."

        elif category == "Academic":
            return "Review the message and complete the task before its deadline."

        elif category == "Work/Professional":
            return "Review when convenient and respond if necessary."

        else:
            return "No immediate action required. Review when convenient."