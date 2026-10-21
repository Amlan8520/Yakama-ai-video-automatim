def score(idea, assessment):
    # Heuristic prototype only. This is not YouTube's ranking algorithm.
    originality = 7
    emotional_arc = 7 if idea.get("lesson") else 4
    feasibility = 8 if len(idea.get("characters", [])) <= 4 else 5
    audience_interest = assessment.get("audience_fit", 5)
    clarity = assessment.get("clarity", 5)
    weighted = (
        audience_interest * 25 +
        originality * 25 +
        emotional_arc * 20 +
        clarity * 15 +
        feasibility * 15
    ) / 10
    return {
        "score_out_of_100": round(weighted, 1),
        "components_out_of_10": {
            "audience_interest": audience_interest,
            "story_originality": originality,
            "emotional_arc": emotional_arc,
            "clarity": clarity,
            "production_feasibility": feasibility
        }
    }
