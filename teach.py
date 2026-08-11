from knowledge import save_knowledge

def teach_fact(knowledge, sentence):
    if " is " not in sentence:
        print("AI: I don't know what to learn.")
        return

    question, answer = sentence.split(" is ", 1)

    knowledge[question.lower()] = answer

    save_knowledge(knowledge)

    print("AI: Okay! I've learned that.")

def recall_fact(knowledge, question):
    question = question.lower().strip()

    if question.startswith("what is "):
        question = question[8:]

    if question.endswith("?"):
        question = question[:-1]

    if question in knowledge:
        print("AI:", question.capitalize(), "is", knowledge[question])
    else:
        print("AI: I don't know that yet.")

def show_knowledge(knowledge):
    if len(knowledge) == 0:
        print("AI: I haven't learned anything yet.")
    else:
        print("AI: Here's what I've learned:")

        for question, answer in knowledge.items():
            print("-", question.capitalize(), "is", answer)

def forget_fact(knowledge, question):
    question = question.lower().strip()

    if question.startswith("what is "):
        question = question[8:]

    if question.endswith("?"):
        question = question[:-1]

    if question in knowledge:
        del knowledge[question]
        save_knowledge(knowledge)
        print("AI: Okay, I've forgotten that.")
    else:
        print("AI: I don't know that yet.")


