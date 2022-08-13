#list_8Ball.py
import random
messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

while True:
    question = input("Do you wish an answer, O seeker of wisdom? Y/N ")
    if question.upper() == "Y":
        print( "\nThe Magic 8 Ball says...")
        print(messages[random.randint(0, len(messages) - 1)]+ "\n")
        continue
    
    else:
        print("\nGoodbye! Don't let the beads hit you in the ass on the way out.")
        break
    
