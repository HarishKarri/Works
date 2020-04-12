#!/usr/bin/python3
import argparse
import re
import sys
import collections
from operator import itemgetter
from collections import Counter
from collections import defaultdict
def LetterandWord():
    length = len(sys.argv);
    alphabetfreq = defaultdict(int);
    distinctwords = defaultdict(int);
    freqofdistinctwords = defaultdict(int);
    wordlength = defaultdict(int);
    nonalpha = defaultdict(int);
    new_string = new_string1 = dictlist1= dictlist2 = [];
    rank =wordfreq=cumdistinctwords=dashcount=cumpercentwords=cumpercenttotal=cumtotalwords= 0;
    totalwords =recordread=charread=charcount=wordrank=0;
    if(length!=2):
        print(len(sys.argv));
        print("Error : You Have to Enter two input file names");
        sys.exit();
    else:
        print("no. of arguments = "+ str(len(sys.argv)));
        print("arguments are:  ['"+str(sys.argv[0])+"', '"+str(sys.argv[1])+"'];") 
        print("\n\nwords of length 16 or more");
        file_handle = open(sys.argv[1],"r",encoding='iso-8859-1');
        for vbl in file_handle:
            recordread +=1;
            charread +=len(vbl);
            s = vbl;
            c = s.count("--");
            if(c>0):
                dashcount += 1;
            vbl = vbl.replace("--","  ");
            string = vbl.split(" ");
            for words in string:
                replacedwords = re.sub("[^A-Za-z]"," ",words);
                new_string.append(re.sub("[a-zA-Z]","",words));
                lists = replacedwords.split(" ");
                for lists in lists:
                    lowerwords = lists.lower();
                    if(lowerwords.isalpha()):
                        if(len(lowerwords)>= 16):
                            print("*** "+lowerwords);
                        wordlength[len(lowerwords)] +=1;
                        charcount += len(lowerwords);
                        distinctwords[lowerwords] +=1;
                    for letter in lowerwords:
                        if(letter.isalpha()):
                            alphabetfreq[letter] += 1;
        for i in new_string:
            for j in i:
                nonalpha[j]+=1;
        nonalpha1 = collections.OrderedDict(sorted(nonalpha.items()));
        new_string1 = list(nonalpha1.keys());
        alphabetfreq1 = collections.OrderedDict(sorted(alphabetfreq.items()));
        dictlist1 = list(alphabetfreq1.items());
        print("\n\nLETTER FREQUENCIES (ALPHABETICAL)\n");
        table_wise_print(dictlist1);
        alphabetfrequency = collections.OrderedDict(sorted(alphabetfreq.items(),reverse=True,key=lambda t:t[1]));
        print("\n\nLETTER FREQUENCIES (BY FREQUENCY)\n");
        dictlist2 = list(alphabetfrequency.items());
        table_wise_print(dictlist2);
        print("\nWORD LENGTHS\n");
        wordlength1 = collections.OrderedDict(sorted(wordlength.items(),reverse=True,key = lambda t:t[1]));
        dictlist3 = list(wordlength.items());
        word_table(dictlist3);
        print("\n\nrank  length   freq  rank*freq");
        for key,value in wordlength1.items():
            rank = rank + 1;
            rank_freq = rank * value;
            totalwords = totalwords + value;
            print("{:4d}".format(rank)+"  "+"{:6d}".format(key)+"   "+"{:5d}".format(value)+"  "+"{:6d}".format(rank_freq));  
        print("\nTotal"+"{:13d}".format(totalwords));
        print("\n\nLines with --        "+str(dashcount));
        print("Invalid chars:     "+str(new_string1),end=" ");
        print("\n\nRecords read: "+"{:12d}".format(recordread));
        print("Characters read: "+"{:10d}".format(charread));    
        print("Character counted: "+"{:9d}".format(charcount));
        print("Distinct characters: "+"{:5d}".format(len(alphabetfreq)));
        print("Words counted: "+"{:11d}".format(totalwords));
        print("Distinct words: "+"{:10d}".format(len(distinctwords)));
        for key,value in distinctwords.items():
            freqofdistinctwords[value] += 1;
        print("Distinct word freqs: "+"{:5d}".format(len(freqofdistinctwords)));
        freqofdistinctwords1 = collections.OrderedDict(sorted(freqofdistinctwords.items(),reverse=False,key = lambda t:(-t[1],t[0])));
        print("""\n\nFREQUENCY OF FREQUENCIES (DESCENDING)
Shows that 50% of all words only occur once
But those words only cover 5% of the corpus
"Most words are rare"\n""");	
        print("  #   freq   count  cum distinct words   cum distinct %   cum words   cum word %");
        for key,value in freqofdistinctwords1.items():
            wordrank += 1;
            cumdistinctwords += value;
            cumtotalwords = cumtotalwords + key * value; 
            cumpercentdistinctwords =  cumdistinctwords / len(distinctwords);
            cumpercenttotalwords = cumtotalwords/ totalwords;
            print("{:3d}".format(wordrank) + "   " + "{:4d}".format(key) + "   " + "{:5d}".format(value) + "     " + "{:9d}".format(cumdistinctwords) +"              "+"{0:.2f}".format(round(cumpercentdistinctwords,2))+"         "+"{:7d}".format(cumtotalwords)+"         " +"{0:.2f}".format(round(cumpercenttotalwords,2))); 
        distinctwords1 = collections.OrderedDict(sorted(distinctwords.items(),reverse = False,key = lambda x:(-x[1],x[0])));
        c =zrank_freq=zcumwords=zcumpercentwords=0;
        print("""\nWORD FREQUENCIES AND ZIPF'S LAW
Note that you can read 2/3 of the words in the book with only 200 words of English.
Can you understand a book if you only know 200 words of English?\n""");
        print("rank    word 		freq 	rank*freq    cum words    cum word %");
        for key,value in distinctwords1.items():
            c= c+1;
            zrank_freq = c * value;
            zcumwords +=value;
            zcumpercentwords = zcumwords/totalwords;
            print(("{:4d}".format(c) + "    " +"{0:<16}".format(key)+""+"{:4d}".format(value)+"    " + "{:7d}".format(zrank_freq)+"       " +"{:6d}".format(zcumwords)+ "        "+"{0:.2f}".format(round(zcumpercentwords,2))));
def table_wise_print(dict):
    for row in range(6):
        col=row;
        for col in range(col,26,6):
            print("%s %5s" % (dict[col][0],dict[col][1]),end="   ");
        print();
def word_table(dict):
    l = int(len(dict)/4);
    for i in range(l):
        print("  len  count",end="  ");
    print();
    for row in range(4):
        col =row;
        for col in range(col,16,4):
            print("  "+"{:3d}".format(dict[col][0]) +"  ""{:5d}".format(dict[col][1]),end="  ");
        print();
        
if __name__ == "__main__":
	LetterandWord();
	                                                           
