def assess(idea):
    text = " ".join([idea["topic"], idea["hook"], idea["lesson"]]).lower()
    safety_flags = []
    if any(word in text for word in ["kill", "blood", "weapon", "murder"]):
        safety_flags.append("Potential violence wording: review manually.")
    return {
        "audience_fit": 8 if idea.get("characters") else 5,
        "clarity": 8 if idea.get("lesson") else 5,
        "safety_flags": safety_flags,
        "review_required": True
    }
