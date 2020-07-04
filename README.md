# Autocomplete engine with max count suggestions

Project Description:

This project is built to suggest the user a set of words as standard output to the user for the given input word matching the prefix given by the user, also based on the max count input given by the user. Built with python this project builds a trie data structure for efficient implementation of autocomplete by taking each word and converting it into lower case from the corpus text file provided where each word is stored in a new line. The text document also contains words with repetitions, so a heap is used to match the words obtained from trie after prefix matching with based on their frequency of occurrence. Thus, if a prefix and max count is given by the user, most frequently occurring words matching the prefix and the max count appear as output. The input query is converted into lower case for comparison into the trie data structure to maintain case insensitivity. 

Reason for choosing trie: Trie is idle for easy insertion, deletion and searching in O(k) where k is the length of the word as this is nothing but a tree with multiple nodes since here the input is words we can have a tree with 26 nodes in the first level which keeps expanding.

Testing method: Used a data set consisting of approximately 1500 multiple words starting with almost all the alphabets and made sure that certain words are repeated multiple times to check for max frequency which evaluates the working of heap data structure which sorts and outputs the words based on their frequency of occurrence. Also output words matching the prefix evaluate the working of the trie data structure.

Further improvement: Can improve the speed of the program by implementing in other programming language like C++ which is much faster than Python also some optimization to the trie in terms of memory utilization can be provided by sorting based alphabetically and build nodes by classifying certain sets of alphabets rather than having 26 nodes but might worsen time complexity. 

Getting Started:

Once the contents in tar ball are extracted the python code autocomp.py can run using puthon3 complier over Linux the program requires any text document where each word or phrase is in a new line to build the trie data structure and suggests the most frequently matching words from the text document based on the prefix and max count given as input. A sample text document test_words.txt is provided.
The following prompt is used to take a file as input: "Enter the corpus filename: "
Once the file is loaded prompts the following prompt is used each time to take the input (prefix and max count) from the user: "Enter Prefix and Max count with ',' separation: "   

Example of execution:

Here the test_words.txt is loaded which has various words with varying frequencies. Let’s consider the following input and output cases:

Input: 
1:: c,1
2:: c,2
3:: ciq,7
4:: c,0
5:: c,a
6::

Output:
1:: circus
2:: circus,clock
3:: 
4:: cappuccino,car,car-race,carpet,carrot,cave,chair,chess board,chief,child,chisel,chocolates,church,circle,circus,clock,clown,coffee,coffee-shop,comet,compact disc,compass,computer,crystal,cup,cycle
5:: 

For the above example the test_words.txt has the suggested words based on their frequency:

circus - 204 
clock - 102
cappuccino - 1
car - 1
car-race - 1
carpet - 1
carrot - 1
cave - 1
chair - 1
chess board - 1
chief - 1
child - 1
chisel - 1
chocolates - 1
church - 2
circle - 34
clown - 1
coffee - 1
coffee-shop - 1
comet - 1
compact disc - 1
compass - 1
computer - 1
crystal - 1
cup - 1
cycle - 1

Since 'circus' is repeated 204 times and clock for 102 times we see that the output as circus and circus & clock respectively for the first and second queries in the third case since there is no match we see a blank line and for the fourth case since max count is 0 all the outputs matching prefixes are printed. For the fifth line since the input is an alphabet in place of max count the output is blank and in the last case since the is no input the main function in called to perform the output.


Libraries

    copy and heapq - The libraries used
