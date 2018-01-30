import random

def question():
    quest= input("What is your question? ")
    possible_answers = random.choice(["Reply hazy try again",
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

print(question())