import sys
import re
import os
lst = sys.argv
path = lst[1]
fil = os.listdir(path)
derv_class = list()
base_class = list()
for item in fil :
    if item.endswith(".py") :
        fh = open(item)
        for line in fh :
            line = line.strip()
            line = line.split()
            if "class" in line :
                if "(" in line[1] :
                    names = re.findall(r"[\w']+",line[1])
                    #names = line[1].split("(")
                    derv_class.append((names,item))
                else :
                    base_class.append((re.findall(r"[\w']+",line[1]),item))
for i_b in base_class :
    print i_b[0][0],"["+i_b[1]+"]",":"
    for i_d in derv_class :
        if i_b[0][0] in i_d[0] :
            print "\t",i_d[0][0],"["+i_d[1]+"]"
    print("\n")
