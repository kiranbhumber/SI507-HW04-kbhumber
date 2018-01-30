
def question():
        quest= input("What is your question?:")
        return quest
while True:
    the_question = question()
    if the_question == "quit":
        break
    elif '?' not in the_question:
        print("Im sorry, I can only answer questions.")
    else:
        print(the_question)
