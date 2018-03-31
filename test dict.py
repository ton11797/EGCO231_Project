import operator
import json
text = open("Dict_wordcount.txt")
dict = {}
count = 0
for line in text:
    for word in line.split():
        if(word in dict):
            dict[word] += 1
        else:
            dict[word] = 1
        count+=1

print ("wordcounts:",dict)
print ("top 1 :",max(dict.items(),key=lambda k: k[1]))
print ("top 5 :",max(dict.items(),key=lambda k: k[1]),end=" ")

for x in range(0,4):
    del dict[max(dict, key=dict.get)]
    print (max(dict.items(),key=lambda k: k[1]),end=" ")
    
print ("\ntotal words in file:",count)
