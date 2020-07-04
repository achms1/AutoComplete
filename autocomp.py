# -*- coding: utf-8 -*-
"""
Created on Tue Mar 09 19:43:19 2020

@author: Achyuth Maddala Sitaram
"""
import copy
import heapq
#from collections import Counter

#file code
corpus = str(input("Enter the corpus filename: "))
fil = open(corpus, 'r')
text = fil.read()
line = [text.lower()]
new_sort = open(corpus, 'w')      
new_sort.writelines(line)
new_sort.close()

#actual code for trie data structure
class init_trie(): 
    def __init__(self):
        self.leaf = {} 
        self.end = False
        
class trie(): 
    def __init__(self):
        self.root = init_trie() 
        self.key_list = []
        self.words = [] 
        self.thisdict = {}

    def trieformation(self, keys): 
        for key in keys: 
            self.insertion(key)
	
	#heap for max frequency 
        for rep in keys:
            if rep in self.thisdict.keys():
                self.thisdict[rep] = self.thisdict[rep]+1;
            else:
                self.thisdict[rep] = 1;

    #insertion operation in trie 
    def insertion(self, key): 
        sub = self.root 
        key_list = list(key)
        for letter in key_list: 
            if not sub.leaf.get(letter): 
                sub.leaf[letter] = init_trie() 
            sub = sub.leaf[letter] 
        sub.end = True

    #search operation in trie
    def searching(self, key): 
        sub = self.root 
        present = True
        key_list = list(key)
        for letter in key_list: 
            if not sub.leaf.get(letter): 
                present = False
                break
            sub = sub.leaf[letter] 
        return sub and sub.end and present 

    def wordcheck(self, sub, word): 
        if sub.end: 
            self.words.append(word) 
  
        for letter,n in sub.leaf.items(): 
            self.wordcheck(n, word + letter) 

    #autocomplete engine
    def autocomplete(self, key):  
        sub = self.root 
        absent = False
        temp = '' 
        key_list = list(key)
        for letter in key_list: 
            if not sub.leaf.get(letter): 
                absent = True
                break
            temp += letter
            sub = sub.leaf[letter] 
        if absent: 
            return 0

        self.wordcheck(sub, temp) 
        #s = 0  
        final = copy.deepcopy(self.words)
        #heap = [(-value, key) for key,value in self.thisdict.items()]
        heap = []
        for k in final:
            value = self.thisdict[k]
            heap.append((-value,k))
        maxfreq = heapq.nsmallest(max_out, heap)
	#for value, key in maxfreq:
	#maxfreq = key
        maxfreq = [key for value, key in maxfreq]
        
	#print(a for a in f)
        #for s in largest:
		#print(s)
         #r = [item for items, c in Counter(largest).most_common() for item in [items] * c] 

        if (max_out != 0) and  (max_out <= len(maxfreq)):
            #for getkey in range(max_out):
            for idx, val in enumerate(maxfreq):
                if (idx == len(maxfreq)-1):
                    print(val.rstrip('\n'))
                else:
                    print(val.rstrip('\n'),end=',')
		#out_str = getkey + ','
	    #print(out_str)
                #print(maxfreq[getkey], end =",")
        elif max_out >=len(maxfreq) or max_out==0:
            #for getkey in final:
            for idx, val in enumerate(final):
                if (idx == len(final)-1):
                    print(val.rstrip('\n'))
                else:
                    print(val.rstrip('\n'),end=',')
		#out_str = getkey + ','
	    #print(out_str)
                #print(getkey, end =",")
        return 1

#building trie from the corpus file 
out = open(corpus, 'r')
keys = out.readlines()
out.close()

# thisdict = {}
# for ad in keys:
#     if ad in thisdict.keys():
#         thisdict[ad] = thisdict[ad]+1;
#     else:
#         thisdict[ad] = 1;
# for i in thisdict.keys():
#     print(i)
#     print(thisdict[i])

#Driver code
while True:
    eachline = []
    query = []
    #numer = True
    while True:
        z = (input("Enter Prefix and Max count with ',' separation: "))
        eachline.append(z)
        if z == '':
            break
    for quer in eachline:
	#print(type(a))
        query = list(quer.split(","))
        if len(query)==2:
            #print (len(query))
            key = query[0]
            max_out = query[1]
            #numer = max_out.isnumeric()
            try:
                max_out = int(max_out)
            except: 
                pass
            #print(key),
            #print(max_out)
            if key == "":
                break
            key = key.lower()
            t = trie()
            t.trieformation(keys)
            comp = t.autocomplete(key)
            if comp == 0: 
                print("")
