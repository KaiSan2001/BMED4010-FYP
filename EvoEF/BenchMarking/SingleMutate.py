'''
Starting Date: 2022.02.04
Ending Date: 2022.02.04
Coder: Chan Kai San
E-mail: u3556373@connect.hku.hk
Description: This script aims to create the mutant files for single point mutation
             V39 D40 G41 V54
Reference: - 
'''
#Initialization#
import openpyxl
import os
AAList = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']


print("Your file is generating automatically......")

#The single point mutation on position V39#
with open("V39.txt","w") as f:
    for i in AAList:
        if i != 'V':
            f.write("VA39%s;\r\n"%i)
path = os.path.abspath('.')
name = 'V39.txt'
content='Your file "%s" had been saved into %s' %(name,path)
print('-'*len(content));print(content);print('-'*len(content))
print('\n')

#The single point mutation on position D40#
with open("D40.txt","w") as f:
    for i in AAList:
        if i != 'D':
            f.write("DA40%s;\r\n"%i)
path = os.path.abspath('.')
name = 'D40.txt'
content='Your file "%s" had been saved into %s' %(name,path)
print('-'*len(content));print(content);print('-'*len(content))
print('\n')

#The single point mutation on position G41#
with open("G41.txt","w") as f:
    for i in AAList:
        if i != 'G':
            f.write("GA41%s;\r\n"%i)
path = os.path.abspath('.')
name = 'G41.txt'
content='Your file "%s" had been saved into %s' %(name,path)
print('-'*len(content));print(content);print('-'*len(content))
print('\n')

#The single point mutation on position V54#
with open("V54.txt","w") as f:
    for i in AAList:
        if i != 'V':
            f.write("VA54%s;\r\n"%i)
path = os.path.abspath('.')
name = 'V54.txt'
content='Your file "%s" had been saved into %s' %(name,path)
print('-'*len(content));print(content);print('-'*len(content))
print('\n')

#Integrated single mutation file#
with open("all.txt","w") as file:
    for i in AAList:
        if i != 'V':
            file.write("VA39%s;\r\n"%i)
    for i in AAList:
        if i != 'D':
            file.write("DA40%s;\r\n"%i)
    for i in AAList:
        if i != 'G':
            file.write("GA41%s;\r\n"%i)
    for i in AAList:
        if i != 'V':
            file.write("VA54%s;\r\n"%i)
name = 'all.txt'
content='Your file "%s" had been saved into %s' %(name,path)
print('-'*len(content));print(content);print('-'*len(content))
print('\n')