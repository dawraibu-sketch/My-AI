from knowledge import save_knowledge

def teach_fact(knowledge, sentence):
    if " is " not in sentence:
        print("AI: I don't know what to learn.")
        return

    question, answer = sentence.split(" is ", 1)

    knowledge[question.lower()] = answer

    save_knowledge(knowledge)

    print("AI: Okay! I've learned that.")
