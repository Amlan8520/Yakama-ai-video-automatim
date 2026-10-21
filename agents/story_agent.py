from datetime import datetime, timezone

IDEAS = [
    {
        "title": "नन्हा हाथी और जादुई नदी",
        "hero": "मोटू हाथी",
        "friend": "चिंकी चिड़िया",
        "problem": "जंगल का तालाब सूखने लगा",
        "solution": "सभी जानवर मिलकर पानी का सुरक्षित रास्ता खोजते हैं",
        "lesson": "मिल-जुलकर काम करने से मुश्किलें आसान होती हैं"
    },
    {
        "title": "खरगोश और खोया हुआ खजाना",
        "hero": "गोलू खरगोश",
        "friend": "मीना हिरणी",
        "problem": "गोलू को जंगल में एक रहस्यमयी नक्शा मिलता है",
        "solution": "दोस्त मिलकर नक्शे का रहस्य सुलझाते हैं",
        "lesson": "सच्ची दोस्ती और ईमानदारी सबसे बड़ा खजाना हैं"
    },
    {
        "title": "बंदर की अनोखी तरकीब",
        "hero": "बंटी बंदर",
        "friend": "टिंकू तोता",
        "problem": "जंगल के दोस्तों का भोजन ऊंचे पेड़ पर फंस जाता है",
        "solution": "दोस्त मिलकर भोजन सुरक्षित नीचे उतारते हैं",
        "lesson": "समझदारी और सहयोग से समस्याएं हल होती हैं"
    }
]

def make_story_package():
    day = datetime.now(timezone.utc).timetuple().tm_yday
    idea = IDEAS[day % len(IDEAS)]

    story = f"""
शीर्षक: {idea['title']}

एक हरे-भरे जंगल में {idea['hero']} रहता था।
उसका सबसे अच्छा दोस्त {idea['friend']} था।

एक दिन {idea['problem']}।
सभी जानवर परेशान हो गए।

{idea['hero']} ने अपने दोस्तों के साथ मिलकर
समस्या का हल खोजने का फैसला किया।

कई कोशिशों के बाद {idea['solution']}।

जंगल में फिर से खुशी लौट आई।

सीख: {idea['lesson']}।
"""

    scenes = [
        f"Scene 1: हरा-भरा जंगल और {idea['hero']}",
        f"Scene 2: {idea['problem']}",
        f"Scene 3: {idea['hero']} और {idea['friend']} योजना बनाते हैं",
        f"Scene 4: दोस्त मिलकर समस्या हल करते हैं",
        f"Scene 5: सभी जानवर खुश होते हैं",
        f"Scene 6: कहानी की सीख"
    ]

    captions = [
        f"यह कहानी है {idea['hero']} की।",
        idea["problem"] + "।",
        "दोस्तों ने मिलकर योजना बनाई।",
        idea["solution"] + "।",
        "जंगल में खुशी लौट आई।",
        "सीख: " + idea["lesson"] + "।"
    ]

    subtitles = []

    for i, caption in enumerate(captions, 1):
        start = (i - 1) * 5
        end = i * 5

        subtitles.append(
            f"{i}\n"
            f"00:00:{start:02d},000 --> 00:00:{end:02d},000\n"
            f"{caption}\n"
        )

    metadata = f"""
Title: {idea['title']} | Hindi Animal Story

Description:
जानवरों की एक मनोरंजक हिंदी कहानी।
सीख: {idea['lesson']}।

Tags:
Hindi animal story, Hindi kahani, animal stories
"""

    return {
        "story": story,
        "scene_plan": "\n\n".join(scenes),
        "subtitles": "\n".join(subtitles),
        "metadata": metadata
    }
