#! python3
# madlibs.py - Reads a madlibs text file and prompts the user to input
#              appropriate words. Allows the user to save the final
#              story as a separate text file.

import os
import re

def createStory():
    '''Creates a new story based on chosen template and optionally
    saves the result to the Stories folder'''
    # Display possible story templates and allow user to choose one
    templatePath = os.path.join(os.getcwd(), 'Templates')
    print('Choose a template:')
    for file in os.listdir(templatePath):
        print(file)
    while True:
        selection = input('> ')
        if selection in os.listdir(templatePath):
            story = open(os.path.join(templatePath, selection))
            break
        else:
            print('Invalid selection')

    # Create a list of all instances from story template in need of replacing
    storyContent = story.read()
    madlibsRegex = re.compile(r'NOUN\d+|PERSON\d+|CITY\d+|VERB\d+|ADJECTIVE\d+')
    mo = madlibsRegex.findall(storyContent)

    # Remove duplicates
    subs = []
    for word in mo:
        if not word in subs:
            subs.append(word)

    # Prompt user for replacement for each instance
    for word in subs:
        print('Enter a ' + word[:-1])
        entry = input('> ')
        storyContent = re.sub(word, entry, storyContent)

    # Display finished story and prompt user to save
    # If 'yes' save story in 'stories' folder
    print(storyContent)
    print('Would you like to save this story?')
    res = input('> ')

    if res == 'y' or res == 'yes':
        print('Enter a name for your story: ')
        title = input('> ')
        location = os.path.join(os.getcwd(), 'stories', title + '.txt')
        savedStory = open(location, 'w')
        savedStory.write(storyContent)
        savedStory.close()
        print('Story saved!')

def readStory():
    '''Displays list of saved stories and prints chosen story'''
    storyPath = os.path.join(os.getcwd(), 'Stories')
    print('Choose a saved story to read:')
    for file in os.listdir(storyPath):
        print(file)
    while True:
        selection = input('> ')
        if selection in os.listdir(storyPath):
            story = open(os.path.join(storyPath, selection))
            break
        else:
            print('Invalid selection')
    storyContent = story.read()
    print(storyContent)
    story.close()

def mainMenu():
    print('Welcome to Mad Libs!\n')
    while True:
        print('What would you like to do?\n1. Read saved stories\n2. Create a new story\n3. Quit')
        res = input('> ')
        if res == '1':
            readStory()
        elif res == '2':
            createStory()
        elif res == '3':
            playing = False
            break
        else:
            print('Invalid selection')

if __name__ == '__main__':
    mainMenu()
