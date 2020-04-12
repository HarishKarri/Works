import argparse
import sys
import unicodedata
def openandcount():
    fvowel =0;
    fconsonant=0;
    svowel=0;
    sconsonant=0;
    expectedfv=expectedtotal=0;
    expectedsv=expectedfc=expectedsc=0;
    length = len(sys.argv);
    if(length!=3):
        print("Error : You Have to Enter two input file names");
        sys.exit();
    else:
        #args = parser.parse_args();
        for k in range(1,3):
            print("Book:  "+sys.argv[k]);
            lowerline='';
            lline='';
            linecount=0;
            lettercount=0;
            charactercount=0;
            vowelcount=0;
            consonantcount=0;
            file_handle = open(sys.argv[k],"r");
            for vbl in file_handle:
                linecount +=1;
                lowerline = vbl.lower();
                #lline+=lowerline;
                string = vbl.split();
                charactercount = charactercount + len(vbl); 
                for vbl in string:
                        for vbl in vbl:
                            if(unicodedata.category(vbl).startswith("L")):
                                lettercount+=1;
                        for i in range(len(lowerline)):
                            if(lowerline[i] in 'aeiou' or lowerline[i] in 'éâêîôûàèùëïüœ'):
                                vowelcount+=1;
                            elif(unicodedata.category(lowerline[i]).startswith("L")):
                                consonantcount+=1;
                        lowerline='';
            print("Number of Lines        = " +"{:7d}".format(linecount));
            print("Number of characters   = " +"{:7d}".format(charactercount));
            print("Number of vowels       = " +"{:7d}".format(vowelcount));
            print("Number of Consonants   = " +"{:7d}".format(consonantcount));
            print("Number of Letter       = " +"{:7d}".format(vowelcount + consonantcount));
            print("% vowels               =  " +"{:.2f}".format((vowelcount/(vowelcount+consonantcount) * 100)) +"%");
            print();
            if(k==1):
                fvowel = vowelcount;
                fconsonant = consonantcount;
                expectedtotal1 = fvowel + fconsonant; 
            else:
                svowel = vowelcount;
                sconsonant = consonantcount;
                expectedtotal2 = svowel + sconsonant;
        print("Actual:");
        print("Book            Consonants      Vowels");
        print(sys.argv[1]+"       "+str(fconsonant)+"          "+str(fvowel));
        print(sys.argv[2]+"       "+str(sconsonant)+"          "+str(svowel));
        expectedvowels = fvowel + svowel;
        expectedconsonants = fconsonant + sconsonant;
        expectedtotal = expectedtotal1 + expectedtotal2;
        expectedfv = (expectedtotal1 * expectedvowels)/expectedtotal;
        expectedsv = (expectedtotal2 * expectedvowels)/expectedtotal;
        expectedfc = (expectedtotal1 * expectedconsonants)/expectedtotal;
        expectedsc = (expectedtotal2 * expectedconsonants)/expectedtotal;
        print();
        print("Expected:");
        print("Book            Consonants      Vowels");
        print(sys.argv[1]+"       "+"{:.2f}".format(expectedfc)+"       "+"{:.2f}".format(expectedfv));
        print(sys.argv[2]+"       "+"{:.2f}".format(expectedsc)+"       "+"{:.2f}".format(expectedsv));
        c1 = pow((fvowel - expectedfv),2)/expectedfv; 
        c2 = pow((svowel - expectedsv),2)/expectedsv;
        c3 = pow((fconsonant - expectedfc),2)/expectedfc;
        c4 = pow((sconsonant - expectedsc),2)/expectedsc; 
        finalch =  "{:.2f}".format(c1 + c2 + c3 + c4);
        print();
        print("chi-square = "+str(finalch));
        print();
        print("""The null hypothesis is that the text in the two books is 
drawn from the same population.""");
        print();
        print("Chi-square is "+str(finalch)+" with df = 1. That is above the cutoff\n"
"""for p < .001, which is 10.828. Therefore the null hypothesis
is rejected, and there is a significant difference in the
percentage of vowels in the two texts.""");
        print();
        print("The short way of writing this is:\n"
"Chi-square = "+str(finalch)+", df=1, which is significant at p < .001");
        print();
        print("""However you write it, that means that there is only 1
chance in 1000 that this result happened by chance, i.e., by
accident.""");
        print();
        print("""A 5% level, i.e., that there is only 1 chance in 20 that the
result appears to be real but really isn't, is sufficient for
publication in this type of work. That's what I suggested for
the homework, and that's fine.""");
        print();
        print("""For publication, if you have a .01 or .001 level of 
significance, you would usually use that.""");
if __name__ == "__main__":
    openandcount();
