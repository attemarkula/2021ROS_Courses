#!/usr/bin/python3
""" ohjelma jakaa yhden csv tiedoston kolmeen, 1. 2. 3. rivi"""
import sys, os
import time

def main():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))

    if (len(sys.argv) < 2):
        print("need name of source filename, for example: \n",sys.argv[0]+" sourcefile.csv")
        exit(0)

    filename = sys.argv[1]
    output1 = filename.replace(".csv", "_1of3.csv")
    output2 = filename.replace(".csv", "_2of3.csv")
    output3 = filename.replace(".csv", "_3of3.csv")
    print (filename,output1, output2, output3, sep="\n")

    filename = sys.argv[1]
    handleS = open(filename,mode='r')
    handle1 = open(output1,mode='w')
    handle2 = open(output2,mode='w')
    handle3 = open(output3,mode='w')
    token=1
    line=0
    newline=False
    while (token != False):
        #time.sleep(0.1)
        line+=1
        print (line)
        newline=handleS.readline()
        if len(newline) == 0:
            newline=handleS.readline()
            if len(newline) == 0:
                break

        print(type(newline), len(newline))
        print((newline))
        if newline==False:
            print("WTH: NEWLINE == FALSE")
        if token==1:
            handle1.writelines(newline)
            newline=False
            token+=1
            continue
        if token==2:
            handle2.writelines(newline)
            newline=False
            token+=1
            continue
        if token==3:
            handle3.writelines(newline)
            newline=False
            token=1
            continue
    print("file ends, all ok? Check files")
    if token != 1:
        print("BTW, did not end even, so lines in files not equal")   
    

    

if __name__ == "__main__":
    main()
