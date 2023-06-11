import pyinputplus as pyip
import time, random


def Quiz(questions):
    a = 0
    b = 0
    answer = 0
    score = 0

    for i in range(questions):
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        answer = a * b

        try:
            pyip.inputStr(
                allowRegexes=[f"^{answer}$"],
                blockRegexes=[r".+"],
                prompt=f" Question number {i + 1}. What is {a} * {b}? \n",
                timeout=8,
                limit=3,
            )

        except pyip.TimeoutException:
            print("Out of time!")

        except pyip.RetryLimitException:
            print("Out of tries!")

        else:
            score += 1
            print("Correct!")
            print(f"Your actual score is {score}/{questions}")
            time.sleep(1)
    print(f"Nice! your final score is {score}/{questions}")


while True:
    numberOfQuestions = pyip.inputInt(prompt="How many questions do you want?\n")
    if numberOfQuestions > 0:
        Quiz(numberOfQuestions)
    else:
        print("Uh, ok...")
        quit()
