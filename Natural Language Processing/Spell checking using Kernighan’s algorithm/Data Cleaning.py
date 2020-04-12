#!/usr/bin/python3
import sys
import re
import argparse
import collections
import time
import pickle
from collections import defaultdict
def preprocess():
    recordread = 0;
    noofwordread=0;
    i=0;
    uniquewords = defaultdict(int);
    unigramcount  = defaultdict(int);
    wordlist =[];
    bigramcount = defaultdict(int);
    t1 = time.perf_counter();    
    p1 = time.process_time();
    print("Start at elapsed time      "+"{:20f}".format(t1) +",     cpu time  "+"{:6f}".format(p1));
    file_handle = open("/home/turing/t90rkf1/dnl/dhw/data/ap88.txt","r",encoding='iso-8859-1');
    t2 = time.perf_counter();    
    p2 = time.process_time();
    print("Finish reading at elapsed time    "+"{:11f}".format(t2) +",     cpu time  "+"{:6f}".format(p2));
    print("Total elapsed time  " +"{:23f}".format(t2-t1)+",         cpu time  "+"{:6f}".format(p2-p1));
    for vbl in file_handle:
        recordread +=1;
        vbl = re.sub("AP88....-....",'',vbl);
        vbl = re.sub("[^A-Za-z]"," ",vbl);
        split2 = [i.strip() for i in vbl.split(" ")];
        for words in split2:
            if(len(words)>0):
                noofwordread +=1;
                words = words.lower();
                uniquewords[words] +=1;
    print("\nNumber of records:     "+"{:9d}".format(recordread));
    print("Number of words:        "+"{:11d}".format(noofwordread));
    print("Number of unique words:    "+"{:4d}".format(len(uniquewords)));
    uniquewordsfrequency = collections.OrderedDict(sorted(uniquewords.items(),reverse=False,key = lambda t:(t[1])));
    print("Ten most common words");
    c =0;
    for key,value in uniquewordsfrequency.items():
        c+=1;
        if(c <= 10):
            print("{0:<16}".format(key)+"  "+"{:5d}".format(value));
        else:
            break;
    for key,value in uniquewords.items():
        for i in range(value):
            angleword = "<"+str(key)+">";
            for i in angleword:
                unigramcount[i] +=1;
            for counter,i in enumerate(angleword):
                if(counter != len(angleword)-1):
                    new_i = angleword[counter:counter+2];
                    bigramcount[new_i] +=1;
    print("\nUnigram counts:");
    unigramfrequency = collections.OrderedDict(sorted(unigramcount.items(),reverse=False,key = lambda t:t[0]));
    for key,value in unigramfrequency.items():
        if(len(key)>0):
            print("{0:<10}".format(key)+"  "+"{:5d}".format(value));
    bigramfrequency = collections.OrderedDict(sorted(bigramcount.items(),reverse=False,key = lambda t:t[0]));
    print("\nBigram counts:");
    for k,v in bigramfrequency.items():
        print("{0:<16}".format(k)+"  "+"{:5d}".format(v));
    my_file = open("pickled_data2.dat", 'wb');
    first = list(unigramfrequency.items());
    second = list(bigramfrequency.items());
    third = list(uniquewords.items());
    final = [];
    final.append(first);
    final.append(second);
    final.append(third);
    final.append(noofwordread);
    final.append(recordread);
    final.append(uniquewords);
    pickle.dump(final, my_file);
if __name__ == "__main__":
    preprocess();        
            
            
            
            
            
            
            
            
            
            
    
    
