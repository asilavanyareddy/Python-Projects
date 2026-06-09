print("Welcome to Quiz Game:")
questions=[
    ("Capital of India?","b"),
    ("2 + 2 = ?", "b"),
    ("Python is a ___ ?", "a"),
    ("Sun rises in the ___ ?", "c"),
    ("HTML full form?", "a"),
    ("10 x 5 = ?", "a"),
    ("Which is a fruit?", "b"),
    ("Water formula?", "b"),
    ("Which is a programming language?", "a"),
    ("CPU stands for?", "a")
]

options=[
    ["a) Mumbai", "b) Delhi", "c) Chennai"],
    ["a) 3", "b) 4", "c) 5"],
    ["a) Programming Language", "b) Snake", "c) Movie"],
    ["a) West", "b) North", "c) East"],
    ["a) Hyper Text Markup Language", "b) High Text Machine Language", "c) Home Tool Mark Language"],
    ["a) 50", "b) 15", "c) 100"],
    ["a) Carrot", "b) Apple", "c) Potato"],
    ["a) CO2", "b) H2O", "c) O2"],
    ["a) Python", "b) Mango", "c) Table"],
    ["a) Central Processing Unit", "b) Computer Power Unit", "c) Central Print Unit"]
]
score=0
for i in range(len(questions)):
    print("Q:",questions[i][0])
    for opt in options[i]:
        print(opt)

    ans=input("enetr your option: ")
    if(ans==questions[i][1]):
            print("correct ans")
            score+=1
    else:
            print("wrong answer")
print("Game Over")
print("your score is" ,score,"/10")