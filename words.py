import string
import random

def spliteFunc(word_list):
    gloList = []

    tmp = ''
    for c in word_list:
        if c == ' ':
            gloList.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        gloList.append(tmp) 
    return gloList
    

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    print "Loading a list from file"

    fileData = open("words.txt", 'r', 0)
    readingLine = fileData.readlines()
    word_list=[]
    for i in readingLine:
        word_list+=spliteFunc(i)
    print " ", len(word_list), "words loaded.\n"
    return word_list 


def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word