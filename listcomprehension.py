#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 18:15:41 2017

@author: Aidan Draper and Brian Matejevich
"""
import re

def main():
    wordsFile = open("/Users/Draper/Desktop/lowerwords.txt", 'r')
    words = wordsFile.read()
    wordsFile.close()
    wordList = words.split()
    #userInt = int(input("Enter a question a number: "))
    #print(userInt)
    #filterList(userInt, createDict(wordList), wordList)
    #dict=createDict(wordList)
    #print(dict[userInt])
    
    #sentences to use
    first = ['I', 'am', 'playing', 'xbox', 'and', 'trying', 'hard']
    second = ['I', 'am', 'trying', 'hard', 'for', 'a', 'win']
    both = first + second

#question 1
    line1 = [x for x in both if len(x)>2]
    print("Problem 1:", line1)
#question 2
    line2 = [x for x in first if x[0]=='a']
    print("Problem 2:", line2)
#question 3
    line3 = [x[-2:] for x in first]
    print("Problem 3:", line3)
#question 4
    line4 = [x for x in both if len(x)%2==0]
    print("Problem 4:", line4)
#question 5
    line5 = [first.index(x) for x in first if len(x)%2==0]
    print("Problem 5:", line5)
#question 6
    line6 = [x for x in both if len(x)>5]
    print("Problem 6:", line6)
#question 7
    line7 = [x for x, y in zip(first, second) if x==y]
    print("Problem 7:", line7)
#question 8
    line8 = [x for x in first if x in second]
    print("Problem 8: ", line8)
#question 9
    line9 = [x[0].upper()+ x[1:] for x in first]
    print("Problem 9: ", line9)
#question 10
    line10 = [x.replace('a','ee') for x in first]
    print("Problem 10: ", line10)
#question 11
    line11 = [(x,y) for x, y in zip(first, second) if len(x)>2]
    print("Problem 11: ", line11)
#question 12
    line12 = [(x,x) for x in first if x in second and len(x)%2==0 or len(x)==1]
    print("Problem 12: ", line12)
#question 13
    line13 = [x+y for x in first for y in second if len(y)>len(x)] 
    print("Problem 13: ", line13)
#question 14
    line14 = [first.index(x) for x in first for y in second if x == y]
    print("Problem 14: ", line14)
#question 15
    line15 = [(x[0].lower(),y[0].lower()) for x in first for y in second] #close!
    print("Problem 15: ",line15)

#part 2
#1: 898 words
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'\b(\w+a$)',wordList[x])
        if f!= []:
            count.append(f)
        x=x+1
    print(len(count), "words end with the letter 'a'.")

#2: 4711 words
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'\w{4,}d$',wordList[x])
        if f!= []:
            count.append(f)
        x=x+1
    print(len(count), "words are atleast 5 letters long and end with the letter 'd'.")
#3: 6988 words
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'\w{1,}[aeiou]$',wordList[x])
        if f!= []:
            count.append(f)
        x=x+1
    print(len(count), "words end in a vowel.")

#4: 1654 words
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'^[aeiou][a-z]+[aeiou]$',wordList[x])
        if f!= []:
            count.append(f)
        x=x+1
    print(len(count), "words start and end in a vowel.")
#5: 398 words  
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'(^[aeiou])\w*\1$',wordList[x])
        if f!= []:
            count.append(f)
        x=x+1
    print(len(count), "words start and ends with the same vowel")
    
#6: 14 words  
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'[a-z]+[aeiou]{4,}[a-z]+',wordList[x])
        if f!= []:
            count.append(f)
        x=x+1
    print(len(count), "words have four vowels in a row.")
    
    
    
#7: 8 words 
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'(in).*\1.*\1',wordList[x])
        if f!= []:
            count.append(wordList[x])
        x=x+1
    print(len(count), "words conntain 'in' 3 times")
    
 #8: 23 words
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'([a-z][a-z]).*\1.*\1',wordList[x])
        if f!= []:
            count.append(wordList[x])
        x=x+1
    print(len(count), "words have a two letter sequence in it 3 times")
#9: 34 words
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'([a-z])([a-z]).*(\2\1).*(\1\2)',wordList[x])
        if f!= []:
            count.append(wordList[x])
        x=x+1
    print(len(count), "words with a combo and then the reverse combo")
#10: 39 words 
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'([a-z])\1([a-z])*\2([a-z])*\3\w*',wordList[x])
        if f!= []:
            count.append(wordList[x])
        x=x+1
    print(len(count), "words with three pairs of double letters") 
#11: 0 words  
    x=0
    count=[]
    while x< len(wordList):
        f = re.findall(r'(([a-z])\[a-z]\2)[a-z]*\1',wordList[x])
        if f!= []:
            count.append(wordList[x])
        x=x+1
    print(len(count), "words contain the same triple twice")
#12: 2 words    
    x=0
    count=[]
    
    while x< len(wordList):
        f = re.findall(r'([a-z])\w\1([a-z])\w\2([a-z])\w\3',wordList[x])
        if f!= []:
            count.append(wordList[x])
        x=x+1
    
    print(len(count), "words have three triples in a row")


#doesnt fully work: supposed to have user enter number and return specific regex
def createDict(words_list):
    d = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    d[1]=[r'\b(\w+a$)'] 
    d[2]=[r'\w{4,}d$']
    d[3]=[r'\w{1,}[aeiou]$']
    d[4]=[r'^[aeiou][a-z]+[aeiou]$']
    d[5]=[r'(^[aeiou])\w*\1$']
    d[6]=[r'[a-z]+[aeiou]{4,}[a-z]+']
    d[7]=[r'(in).*\1.*\1']
    d[8]=[r'([a-z][a-z]).*\1.*\1']
    d[9]=[r'([a-z])([a-z]).*(\2\1).*(\1\2)']
    d[10]=[r'([a-z])\1([a-z])*\2([a-z])*\3\w*']
    d[11]=[r'(([a-z])\w\2)\w*\1']
    d[12]=[r'([a-z])\w\1([a-z])\w\2([a-z])\w\3']
    return d

#doesnt work because dictionary doesnt work
def filterList(num, dictionary, wordList):
    #print(dictionary[num])
    print(num,'. ', len(list(filter(re.compile(dictionary[num]).match,wordList)))) 

main()
    
    