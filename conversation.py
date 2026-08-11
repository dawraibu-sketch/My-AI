def clean_input(user):
    user = user.lower().strip()

    punctuation = "!?.,"

    for mark in punctuation:
        user = user.replace(mark, "")

    return user
