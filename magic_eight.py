import random

def question():
    quest= input("What is your question? ")
    possible_answers = random.choice(["It is certain",
                        "It is decidedly so",
                        "Without a doubt",
                        "Yes definitely",
                        "You may rely on it",
                        "As I see it, yes",
                        "Most likely",
                        "Outlook good",
                        "Yes",
                        "Signs point to yes",
                        "Reply hazy try again",
                        "Ask again later",
                        "Better not tell you now",
                        "Cannot predict now",
                        "Concentrate and ask again",
                        "Don't count on it",
                        "My reply is no",
                        "My sources say no",
                        "Outlook not so good",
                        "Very doubtful"])
    return possible_answers

while True:
    the_question = question()
    if the_question == "quit":
        break
    elif '?' not in the_question:
        print("Im sorry, I can only answer questions.")
    else:
        print(the_question)
