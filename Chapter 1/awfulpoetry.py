import random
#Defining components of the poem
articles = ("the", "a")
subjects = ("teapot", "tree", "helicopter", "car", "cow", "octopus")
verbs = ("yelped", "ran", "slept", "wobbled", "slid")
adverbs = ("erroneously", "vigorously", "tiredly", "gloriously")

#A loop for taking user input and using it to determine number of poetry lines,
#defaulting to 5
default = 5
while True:
    try:
        lines = input("Choose a number of lines between 1 and 10: ")
        line_number = int(lines)
        if not 0 < line_number < 11:
            print("Pick a number between 1 and 10")
            continue
        else:
            break
    except ValueError as err:
        if lines == '':
            line_number = default
            break
        else:
            print(err)

count = 0

#A loop for creating lines of poetry with a random choice of two formats
while count < line_number:
    sentence_choice = random.randint(0,1)
    if sentence_choice:
        print(random.choice(articles), random.choice(subjects), random.choice(verbs),
            random.choice(adverbs))
    else:
        print(random.choice(articles), random.choice(subjects), random.choice(verbs))
    count += 1
    continue