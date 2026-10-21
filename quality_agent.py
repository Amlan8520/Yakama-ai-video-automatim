def review(script, assessment):
    checks = {
        "has_title": script.startswith("शीर्षक:"),
        "has_hook": "हुक:" in script,
        "has_lesson": "सीख:" in script,
        "minimum_length": len(script.split()) >= 80,
        "no_safety_flags": len(assessment.get("safety_flags", [])) == 0
    }
    return {
        "checks": checks,
        "passed_basic_checks": all(checks.values()),
        "human_review_required": True,
        "note": "Automated checks cannot confirm copyright originality or child suitability."
    }
