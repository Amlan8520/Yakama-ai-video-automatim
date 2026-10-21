def metadata(idea):
    title = f"{idea['topic']} | Hindi Animal Story"
    description = (
        f"जानवरों की एक मौलिक, परिवार के साथ देखने योग्य कहानी। "
        f"इस कहानी की सीख: {idea['lesson']}। "
        "वीडियो प्रकाशित करने से पहले कहानी, दृश्य, संगीत और लाइसेंस की समीक्षा करें।"
    )
    tags = ["Hindi animal story", "animal stories", "Hindi kahani", "family friendly story"]
    return {"title_draft": title, "description_draft": description, "tags_draft": tags}
