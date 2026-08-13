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
    if user in ["what is my favorite game","what are my favorite games" ]:
        return "what are my favorite games"

    if user in ["what don't i like","what do i dislike" ]:
        return "what don't i like"

    if user in ["i don't like","i dislike" ]:
        return "i don't like"

    if user.startswith("i dislike "):
        return "i don't like " + user[10:]

    if user in ["what is the time","what time is it","tell me the time","do you know the time","current time"]:
        return "what time is it"

    if user in ["what is today's date","what is the date today","tell me today's date","tell me the date","what date is it","today's date","current date"]:
        return "what is today's date"

    if user in ["what is my favorite food","what are my favorite foods","what food is my favorite","what food do i like","what are the foods i like"]:
        return "what are my favorite foods"
    
    if user.startswith("what is "):
        return user

    if user.startswith("tell me the "):
        return "what is " + user[8:]

    if user.startswith("do you know the "):
        return "what is " + user[12:]
    
    return user

def normalize_greeting(user):
    if user in ["hello", "hey", "hi", "hi there", "hey there"]:
        return "hello"

    return user

def normalize_wellbeing(user):
    if user in [
        "how are you",
        "how are you doing",
        "how are things",
        "how is it going",
        "how is everything"
    ]:
        return "how are you"

    return user

