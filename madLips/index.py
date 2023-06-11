#! python3
# madLips.py - reads a text file and let's you change the words ADJECTIVE, NOUN, ADVERB, or VERB.

from os import close
from pathlib import Path
import time, re

#This piece of code opens the txt.
file = open(str(Path.cwd()/"text.txt"))
fileContent= file.read().split()

#This piece of code defines the function to clean the list.
def depureContent():

    wordChar = re.compile(r"[A-Z,a-z]")

    for wordIndex in range(len(fileContent)):
        if len(fileContent[wordIndex]) > 1:
            for character in fileContent[wordIndex]:
                if re.match(wordChar, character):
                    continue
                
                else:
                    fileContent.insert(wordIndex+1 , character)
                    fileContent[wordIndex]= fileContent[wordIndex][:-1] 
        else:
            continue

#This piece of code checks the text has one or some of the keywordsand let's you input new words in their place.
def searchAndChange():
    keywords = ["ADJECTIVE" , "NOUN" , "VERB", "ADVERB"]
    wordCharacter = re.compile(r"\w")
    for x in range(len(fileContent)):
        try:
            if len(fileContent[x]) ==1 and fileContent[x] != wordCharacter:
                fileContent[x-1] = f"{fileContent[x-1]}" + f"{fileContent[x]}"
                del fileContent[x]

            elif fileContent[x] in keywords:
                fileContent[x] = input(f"write 1  {fileContent[x]}\n")
            else:
                continue
        except IndexError:
            break

#This piece of code prints the results and saves them on a new text file.
def SaveAndPrint():
    result = " ".join(fileContent)
    result= re.sub("\. \.\.","...", str(result))
    adventure = open(str(Path.cwd()/"YourAdventure.txt") , "w")
    adventure.write(result)

    print(result)
    time.sleep(3)

    adventure.close()
    file.close()

depureContent()
searchAndChange()
SaveAndPrint()