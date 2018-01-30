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
                        "Signs point to yes"])
    return possible_answers

print(question())
