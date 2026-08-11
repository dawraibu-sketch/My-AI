def clean_input(user):
    user = user.lower().strip()

    punctuation = "!?.,"

    for mark in punctuation:
        user = user.replace(mark, "")

    user = user.replace("whats ", "what is ")
    user = user.replace("whats", "what is")

    return user
