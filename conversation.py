def clean_input(user):
    user = user.lower().strip()

    if user.endswith("?"):
        user = user[:-1]

    return user
