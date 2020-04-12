#!/usr/bin/python3
import sys
import re
import argparse
import collections
import time
import pickle
from collections import defaultdict
from functools import reduce
from decimal import Decimal
from fractions import Fraction
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];        
def preprocess1():
    length = len(sys.argv);
    #print(length);
    if(length!=2):
        print("Error: You Haven't entered word");
        exit();
    word = sys.argv[1];
    del_table = [['a',0,7,58,21,3,5,18,8,61,0,4,43,5,53,0,9,0,98,28,53,62,1,0,0,2,0],
['b',2,2,1,0,22,0,0,0,183,0,0,26,0,0,2,0,0,6,17,0,6,1,0,0,0,0],
['c',37,0,70,0,63,0,0,24,320,0,9,17,0,0,33,0,0,46,6,54,17,0,0,0,1,0],
['d',12,0,7,25,45,0,10,0,62,1,1,8,4,3,3,0,0,11,1,0,3,2,0,0,6,0],
['e',80,1,50,74,89,3,1,1,6,0,0,32,9,76,19,9,1,237,223,34,8,2,1,7,1,0],
['f',4,0,0,0,13,46,0,0,79,0,0,12,0,0,4,0,0,11,0,8,1,0,0,0,1,0],
['g',25,0,0,2,83,1,37,25,39,0,0,3,0,29,4,0,0,52,7,1,22,0,0,0,1,0],
['h',15,12,1,3,20,0,0,25,24,0,0,7,1,9,22,0,0,15,1,26,0,0,1,0,1,0],
['i',26,1,60,26,23,1,9,0,1,0,0,38,14,82,41,7,0,16,71,64,1,1,0,0,1,7],
['j',0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0],
['k',4,0,0,1,15,1,8,1,5,0,1,3,0,17,0,0,0,1,5,0,0,0,1,0,0,0],
['l',24,0,1,6,48,0,0,0,217,0,0,211,2,0,29,0,0,2,12,7,3,2,0,0,11,0],
['m',15,10,0,0,33,0,0,1,42,0,0,0,180,7,7,31,0,0,9,0,4,0,0,0,0,0],
['n',21,0,42,71,68,1,160,0,191,0,0,0,17,144,21,0,0,0,127,87,43,1,1,0,2,0],
['o',11,4,3,6,8,0,5,0,4,1,0,13,9,70,26,20,0,98,20,13,47,2,5,0,1,0],
['p',25,0,0,0,22,0,0,12,15,0,0,28,1,0,30,93,0,58,1,18,2,0,0,0,0,0],
['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,0,0,0,0,0],
['r',63,4,12,19,188,0,11,5,132,0,3,33,7,157,21,2,0,277,103,68,0,10,1,0,27,0],
['s',16,0,27,0,74,1,0,18,231,0,0,2,1,0,30,30,0,4,265,124,21,0,0,0,1,0],
['t',24,1,2,0,76,1,7,49,427,0,0,31,3,3,11,1,0,203,5,137,14,0,4,0,2,0],
['u',26,6,9,10,15,0,1,0,28,0,0,39,2,111,1,0,0,129,31,66,0,0,0,0,1,0],
['v',9,0,0,0,58,0,0,0,31,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,1,0],
['w',40,0,0,1,11,1,0,11,15,0,0,1,0,2,2,0,0,2,24,0,0,0,0,0,0,0],
['x',1,0,17,0,3,0,0,1,0,0,0,0,0,0,0,6,0,0,0,5,0,0,0,0,1,0],
['y',2,1,34,0,2,0,1,0,1,0,0,1,2,1,1,1,0,0,17,1,0,0,1,0,0,0],
['z',1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
['@',20,14,41,31,20,20,7,6,20,3,6,22,16,5,5,17,0,28,26,6,2,1,24,0,0,2]];
                     
    add_table = [['a',15,1,14,7,10,0,1,1,33,1,4,31,2,39,12,4,3,28,134,7,28,0,1,1,4,1],
['b',3,11,0,0,7,0,1,0,50,0,0,15,0,1,1,0,0,5,16,0,0,3,0,0,0,0],
['c',19,0,54,1,13,0,0,18,50,0,3,1,1,1,7,1,0,7,25,7,8,4,0,1,0,0],
['d',18,0,3,17,14,2,0,0,9,0,0,6,1,9,13,0,0,6,119,0,0,0,0,0,5,0],
['e',39,2,8,76,147,2,0,1,4,0,3,4,6,27,5,1,0,83,417,6,4,1,10,2,8,0],
['f',1,0,0,0,2,27,1,0,12,0,0,10,0,0,0,0,0,5,23,0,1,0,0,0,1,0],
['g',8,0,0,0,5,1,5,12,8,0,0,2,0,1,1,0,1,5,69,2,3,0,1,0,0,0],
['h',4,1,0,1,24,0,10,18,17,2,0,1,0,1,4,0,0,16,24,22,1,0,5,0,3,0],
['i',10,3,13,13,25,0,1,1,69,2,1,17,11,33,27,1,0,9,30,29,11,0,0,1,0,1],
['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
['k',2,4,0,1,9,0,0,1,1,0,1,1,0,0,2,1,0,0,95,0,1,0,0,0,4,0],
['l',3,1,0,1,38,0,0,0,79,0,2,128,1,0,7,0,0,0,97,7,3,1,0,0,2,0],
['m',11,1,1,0,17,0,0,1,6,0,1,0,102,44,7,2,0,0,47,1,2,0,1,0,0,0],
['n',15,5,7,13,52,4,17,0,34,0,1,1,26,99,12,0,0,2,156,53,1,1,0,0,1,0],
['o',14,1,1,3,7,2,1,0,28,1,0,6,3,13,64,30,0,16,59,4,19,1,0,0,1,1],
['p',23,0,1,1,10,0,0,20,3,0,0,2,0,0,26,70,0,29,52,9,1,1,1,0,0,0],
['q',0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
['r',15,2,1,0,89,1,1,2,64,0,0,5,9,7,10,0,0,132,273,29,7,0,1,0,10,0],
['s',13,1,7,20,41,0,1,50,101,0,2,2,10,7,3,1,0,1,205,49,7,0,1,0,7,0],
['t',39,0,0,3,65,1,10,24,59,1,0,6,3,1,23,1,0,54,264,183,11,0,5,0,6,0],
['u',15,0,3,0,9,0,0,1,24,1,1,3,3,9,1,3,0,49,19,27,26,0,0,2,3,0],
['v',0,2,0,0,36,0,0,0,10,0,0,1,0,1,0,1,0,0,0,0,1,5,1,0,0,0],
['w',0,0,0,1,10,0,0,1,1,0,1,1,0,2,0,0,1,1,8,0,2,0,4,0,0,0],
['x',0,0,18,0,1,0,0,6,1,0,0,0,1,0,3,0,0,0,2,0,0,0,0,1,0,0],
['y',5,1,2,0,3,0,0,0,2,0,0,1,1,6,0,0,0,1,33,1,13,0,1,0,2,0],
['z',2,0,0,0,5,1,0,0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,4],
['@',46,8,9,8,26,11,14,3,5,1,17,5,6,2,2,10,0,6,23,2,11,1,2,1,1,2]];

    sub_table = [['a',0,0,7,1,342,0,0,2,118,0,1,0,0,3,76,0,0,1,35,9,9,0,1,0,5,0],
['b',0,0,9,9,2,2,3,1,0,0,0,5,11,5,0,10,0,0,2,1,0,0,8,0,0,0],
['c',6,5,0,16,0,9,5,0,0,0,1,0,7,9,1,10,2,5,39,40,1,3,7,1,1,0],
['d',1,10,13,0,12,0,5,5,0,0,2,3,7,3,0,1,0,43,30,22,0,0,4,0,2,0],
['e',388,0,3,11,0,2,2,0,89,0,0,3,0,5,93,0,0,14,12,6,15,0,1,0,18,0],
['f',0,15,0,3,1,0,5,2,0,0,0,3,4,1,0,0,0,6,4,12,0,0,2,0,0,0],
['g',4,1,11,11,9,2,0,0,0,1,1,3,0,0,2,1,3,5,13,21,0,0,1,0,3,0],
['h',1,8,0,3,0,0,0,0,0,0,2,0,12,14,2,3,0,3,1,11,0,0,2,0,0,0],
['i',103,0,0,0,146,0,1,0,0,0,0,6,0,0,49,0,0,0,2,1,47,0,2,1,15,0],
['j',0,1,1,9,0,0,1,0,0,0,0,2,1,0,0,0,0,0,5,0,0,0,0,0,0,0],
['k',1,2,8,4,1,1,2,5,0,0,0,0,5,0,2,0,0,0,6,0,0,0,.4,0,0,3],
['l',2,10,1,4,0,4,5,6,13,0,1,0,0,14,2,5,0,11,10,2,0,0,0,0,0,0],
['m',1,3,7,8,0,2,0,6,0,0,4,4,0,180,0,6,0,0,9,15,13,3,2,2,3,0],
['n',2,7,6,5,3,0,1,19,1,0,4,35,78,0,0,7,0,28,5,7,0,0,1,2,0,2],
['o',91,1,1,3,116,0,0,0,25,0,2,0,0,0,0,14,0,2,4,14,39,0,0,0,18,0],
['p',0,11,1,2,0,6,5,0,2,9,0,2,7,6,15,0,0,1,3,6,0,4,1,0,0,0],
['q',0,0,1,0,0,0,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['r',0,14,0,30,12,2,2,8,2,0,5,8,4,20,1,14,0,0,12,22,4,0,0,1,0,0],
['s',11,8,27,33,35,4,0,1,0,1,0,27,0,6,1,7,0,14,0,15,0,0,5,3,20,1],
['t',3,4,9,42,7,5,19,5,0,1,0,14,9,5,5,6,0,11,37,0,0,2,19,0,7,6],
['u',20,0,0,0,44,0,0,0,64,0,0,0,0,2,43,0,0,4,0,0,0,0,2,0,8,0],
['v',0,0,7,0,0,3,0,0,0,0,0,1,0,0,1,0,0,0,8,3,0,0,0,0,0,0],
['w',2,2,1,0,1,0,0,2,0,0,1,0,0,0,0,7,0,6,3,3,1,0,0,0,0,0],
['x',0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0],
['y',0,0,2,0,15,0,1,7,15,0,0,0,2,0,6,1,0,7,36,8,5,0,0,1,0,0],
['z',0,0,0,7,0,0,0,0,0,0,0,7,5,0,0,0,0,2,21,3,0,0,0,0,3,0]];


    transpose_table = [['a',0,0,2,1,1,0,0,0,19,0,1,14,4,25,10,3,0,27,3,5,31,0,0,0,0,0],
['b',0,0,0,0,2,0,0,0,0,0,0,1,1,0,2,0,0,0,2,0,0,0,0,0,0,0],
['c',0,0,0,0,1,0,0,1,85,0,0,15,0,0,13,0,0,0,3,0,7,0,0,0,0,0],
['d',0,0,0,0,0,0,0,0,7,0,0,0,0,0,0,0,0,1,0,0,2,0,0,0,0,0],
['e',1,0,4,5,0,0,0,0,60,0,0,21,6,16,11,2,0,29,5,0,85,0,0,0,2,0],
['f',0,0,0,0,0,0,0,0,12,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['g',4,0,0,0,2,0,0,0,0,0,0,1,0,15,0,0,0,3,0,0,3,0,0,0,0,0],
['h',12,0,0,0,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0],
['i',15,8,31,3,66,1,3,0,0,0,0,9,0,5,11,0,1,13,42,35,0,6,0,0,0,3],
['j',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['k',0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['l',11,0,0,12,20,0,1,0,4,0,0,0,0,0,1,3,0,0,1,1,3,9,0,0,7,0],
['m',9,0,0,0,20,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,4,0,0,0,0,0],
['n',15,0,6,2,12,0,8,0,1,0,0,0,3,0,0,0,0,0,6,4,0,0,0,0,0,0],
['o',5,0,2,0,4,0,0,0,5,0,0,1,0,5,0,1,0,11,1,1,0,0,7,1,0,0],
['p',17,0,0,0,4,0,0,1,0,0,0,0,0,0,1,0,0,5,3,6,0,0,0,0,0,0],
['q',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['r',12,0,0,0,24,0,3,0,14,0,2,2,0,7,30,1,0,0,0,2,10,0,0,0,2,0],
['s',4,0,0,0,9,0,0,5,15,0,0,5,2,0,1,22,0,0,0,1,3,0,0,0,16,0],
['t',4,0,3,0,4,0,0,21,49,0,0,4,0,0,3,0,0,5,0,0,11,0,2,0,0,0],
['u',22,0,5,1,1,0,2,0,2,0,0,2,1,0,20,2,0,11,11,2,0,0,0,0,0,0],
['v',0,0,0,0,1,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
['w',0,0,0,0,0,0,0,4,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,8,0],
['x',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
['y',0,1,2,0,0,0,1,0,0,0,0,3,0,0,0,2,0,1,10,0,0,0,0,0,0,0],
['z',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]];
    #word = "acress";
    dup_word = word;
    final_list= [];
    filedata = {};
    my_file = open("pickled_data2.dat", 'rb');
    file_data = pickle.load(my_file);
    unigram = dict(file_data[0]);
    bigram = dict(file_data[1]);
    filedata = dict(file_data[2]);
    noofwords = file_data[3];
    unique_words = file_data[5];
    add = collections.defaultdict(str);
    delete = defaultdict(str);
    sub = defaultdict(str);
    transpose = defaultdict(str);
    length = len(word);   
    new_word1 = [dup_word[:i] + alphabet[c] + dup_word[i:] for i in range(length +1) for c,v in enumerate(alphabet)];
    new_word2= [dup_word.replace(dup_word[i],'',1) for i,j in enumerate(dup_word)];
    new_word3 = [(dup_word[:i] + alphabet[c] + dup_word[i+1:]) for i in range(length) for c,v in enumerate(alphabet)];
    new_word4 = [dup_word[:x] + dup_word[x+1] + dup_word[x] +dup_word[x+2:] for x in range(0,length,1) if not x == (length-1)];
    matching1 = [s for s in filedata.keys() for checkword1 in new_word1 if checkword1 == s];
    matching2 = [s for s in filedata.keys() for checkword2 in new_word2 if checkword2==s];
    matching3 = [s for s in filedata.keys() for checkword3 in new_word3 if checkword3==s];
    matching4 = [s for s in filedata.keys() for checkword4 in new_word4 if checkword4==s];
    print("Category          Count           Pruned");
    print("add                "+str(len(new_word2))+"                "+str(len(matching2)));
    print("delete            "+str(len(new_word1))+"               "+str(len(matching1)));
    print("substitute        "+str(len(new_word3))+"               "+str(len(matching3)));
    print("transpose          "+str(len(new_word4))+"                "+str(len(matching4)));
    submatching1 = [[i] for i in matching1];
    for i in range(len(submatching1)): 
        submatching1[i].append("del");
    submatching2 = [[i] for i in matching2];
    for i in range(len(submatching2)):
        submatching2[i].append("ins");
    submatching3 = [[i] for i in matching3];
    for i in range(len(submatching3)): 
        submatching3[i].append("sub");
    submatching4 = [[i] for i in matching4];
    for i in range(len(submatching4)):
        submatching4[i].append("trans");
    flattenlist = [];
    flattenlist.extend(submatching1);
    flattenlist.extend(submatching2);
    flattenlist.extend(submatching3);
    flattenlist.extend(submatching4);
    klist =[];
    k=1;
    for i,data in enumerate(flattenlist):
        for j in flattenlist[:i]:
            if data[0] not in j[0]:
                k = 1;
            else:
                k += 1;
        klist.append(k);
    flattenlist1 = [i for i in flattenlist];
    for i in range(len(flattenlist1)):
        flattenlist1[i].append(klist[i]);
    word_length = len(word);
    uncommon_list = [];
    for i in range(0,len(flattenlist),1):
        convert = flattenlist[i][0];
        k=0;
        uncommon_index =0;
        for v in range(len(flattenlist[i][0])):
            if convert[v] != word[k]:
                if(v == len(flattenlist[i][0])-1):
                    uncommon_index = v;
                else:
                    uncommon_index = v;
                    break;
                k=v;
            else:
                k +=1;
                if(v == len(flattenlist[i][0])-1):
                    uncommon_index = v+1; 
                    if((flattenlist[i][2])!=1):
                        uncommon_index = (uncommon_index+1) - flattenlist[i][2]; 
                    break;
        uncommon_list.append(uncommon_index);
    xlist=[];
    wlist=[];
    f=(10 ** 9);
    flattenlist2 = [i for i in flattenlist1];
    for i in range(len(flattenlist2)):
        flattenlist2[i].append(uncommon_list[i]);
        if(flattenlist2[i][1] == "ins"):
            flattenlist2[i].append('-');
            flattenlist2[i].append(word[uncommon_list[i]]);
            x = word[uncommon_list[i]-1] + word[uncommon_list[i]];
            w = word[uncommon_list[i]-1];
            xlist.append(x);
            wlist.append(w);
            xw = x +"|"+ w;
            flattenlist2[i].append(xw);
            track_position = flattenlist2[i][3];
            first = word[track_position-1];
            second = flattenlist2[i][5];
            third = first;
            count=0;
            for key,value in unigram.items():
                if third == key:
                    count = value;
            flattenlist2[i].append("{:.10f}".format((add_table[findposition(first)-1][findposition(second)])/count));
        if(flattenlist2[i][1] == "trans"):
            flattenlist2[i].append(flattenlist2[i][0][:uncommon_list[i]+2]);
            flattenlist2[i].append(word[:uncommon_list[i]+2]);
            x = flattenlist2[i][5];
            w =flattenlist2[i][4];
            xlist.append(x);
            wlist.append(w);
            xw = x +"|"+ w;
            flattenlist2[i].append(xw);
            track_position = flattenlist2[i][3];
            first = flattenlist2[i][0][track_position];
            second = flattenlist2[i][0][track_position+1];
            third = first + second;
            count=0;
            for key,value in bigram.items():
                if third == key:
                    count = value;
            flattenlist2[i].append("{:.10f}".format((transpose_table[findposition(first)-1][findposition(second)])/count));
        if(flattenlist2[i][1] == "del"):
            flattenlist2[i].append(flattenlist2[i][0][uncommon_list[i]]);    
            flattenlist2[i].append(flattenlist2[i][0][uncommon_list[i]-1]); 
            x =flattenlist2[i][5];
            w =flattenlist2[i][5]+flattenlist2[i][4];
            xlist.append(x);
            wlist.append(w);
            xw = x +"|"+ w;
            flattenlist2[i].append(xw);
            track_position = flattenlist2[i][3];
            first = flattenlist2[i][0][track_position-1];
            second = flattenlist2[i][4];
            third = first + second;
            count=0;
            for key,value in bigram.items():
                if third ==key:
                    count = value;
            flattenlist2[i].append("{:.10f}".format((del_table[findposition(first)-1][findposition(second)])/count));
        if(flattenlist2[i][1] == "sub"):
            flattenlist2[i].append(flattenlist2[i][0][uncommon_list[i]]);
            flattenlist2[i].append(word[uncommon_list[i]]);
            x =flattenlist2[i][5];
            w =flattenlist2[i][4];
            xlist.append(x);
            wlist.append(w);
            xw = x +"|"+ w;
            flattenlist2[i].append(xw);
            track_position = flattenlist2[i][3];
            first =  flattenlist2[i][5];
            second = flattenlist2[i][0][track_position];
            third = second;
            count=0;
            for key,value in unigram.items():
                if third == key:
                    count = value;
            flattenlist2[i].append("{:.10f}".format((sub_table[findposition(first)-1][findposition(second)])/count));
        prob = 0;
        for key,value in filedata.items():
            if flattenlist2[i][0] == key:
                prob = "{:.10f}".format((value+0.5)/(noofwords+ (0.5 * len(unique_words))));
        flattenlist2[i].append(prob);
        total_probability = float("{:.6f}".format(f * float(flattenlist2[i][7]) * float(flattenlist2[i][8])));
        flattenlist2[i].append(total_probability);    
    final_list =[];
    final_list = sorted(flattenlist2,key=lambda x: x[9],reverse=True);
    final_list.insert(0, ["Candidate","Error"," ","Error","Correct","Error","x|w","P(x|word)","P(word)","10^9*P(x|w)P(w)"])
    final_list.insert(1,["Correction","Type"," ","Pos","Letter","Letter"]);
    for data in final_list:
        for counter,i in enumerate(data):
            if(counter!=2):
                print(str(i).ljust(10, ' '), end =  "   ");
        print("\n");
def findposition(s):
    for i in range(len(alphabet)):
        if s == alphabet[i]:
            return i+1;
if __name__ == "__main__":
    preprocess1();        
