def clean_input(user):
    user = user.lower().strip()

    user = user.replace("what's", "what is")

    punctuation = "!?.,"

    for mark in punctuation:
        user = user.replace(mark, "")

    user = user.replace("whats ", "what is ")
    user = user.replace("whos ", "who is ")
    user = user.replace("wheres ", "where is ")
    user = user.replace("whens ", "when is ")
    user = user.replace("hows ", "how is ")
    user = user.replace("whys ", "why is ")
    user = user.replace("youre ", "you are ")
    user = user.replace("im ", "i am ")
    user = user.replace("ive ", "i have ")
    user = user.replace("ill ", "i will ")
    user = user.replace("id ", "i would ")
    user = user.replace("dont ", "do not ")
    user = user.replace("doesnt ", "does not ")
    user = user.replace("didnt ", "did not ")
    user = user.replace("cant ", "cannot ")
    user = user.replace("couldnt ", "could not ")
    user = user.replace("wont ", "will not ")
    user = user.replace("wouldnt ", "would not ")
    user = user.replace("isnt ", "is not ")
    user = user.replace("arent ", "are not ")
    user = user.replace("wasnt ", "was not ")
    user = user.replace("werent ", "were not ")
    user = user.replace("havent ", "have not ")
    user = user.replace("hasnt ", "has not ")
    user = user.replace("hadnt ", "had not ")
    user = user.replace("shouldnt ", "should not ")

    return user
    
def normalize_question(user):
    if user.startswith("what is "):
        return user

    if user.startswith("tell me the "):
        return "what is " + user[8:]

    if user.startswith("do you know the "):
        return "what is " + user[12:]

    return user
