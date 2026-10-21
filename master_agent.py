import json
from pathlib import Path
from .research_agent import get_ideas
from .audience_agent import assess
from .scoring_agent import score
from .story_agent import make_script
from .quality_agent import review
from .seo_agent import metadata

def run_pipeline(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    candidates = []
    for idea in get_ideas():
        audience = assess(idea)
        candidates.append((score(idea, audience)["score_out_of_100"], idea, audience))
    candidates.sort(key=lambda item: item[0], reverse=True)

    score_value, idea, audience = candidates[0]
    script = make_script(idea)
    quality = review(script, audience)
    seo = metadata(idea)

    package = {
        "channel": "YAKAMA Animal Tales",
        "idea": idea,
        "idea_score": score_value,
        "audience_assessment": audience,
        "quality_review": quality,
        "metadata": seo,
        "publishing": {
            "status": "DRAFT_ONLY",
            "human_approval_required": True,
            "uploaded": False
        }
    }
    script_path = output_dir / "story_draft.txt"
    script_path.write_text(script, encoding="utf-8")
    json_path = output_dir / "video_package.json"
    json_path.write_text(json.dumps(package, ensure_ascii=False, indent=2), encoding="utf-8")
    report_path = output_dir / "review_report.md"
    report_path.write_text(
        "# Draft Review Report\n\n"
        f"- Idea score (heuristic): **{score_value}/100**\n"
        f"- Basic checks passed: **{quality['passed_basic_checks']}**\n"
        f"- Human review required: **Yes**\n"
        "- Upload performed: **No**\n\n"
        "## Review checklist\n"
        "- [ ] Expand the draft into an original, engaging story\n"
        "- [ ] Check all characters and scenes for consistency\n"
        "- [ ] Use only original or properly licensed visuals, music, and voice\n"
        "- [ ] Check child safety and audience setting\n"
        "- [ ] Review title and thumbnail for accuracy\n"
        "- [ ] Approve manually before upload\n",
        encoding="utf-8"
    )
    return [script_path, json_path, report_path]
