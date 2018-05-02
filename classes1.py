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
                    names = re.split('( |) |: |, | ',line[1])
                    derv_class.append((names,item))
                    print(names[0])
                else :
                    base_class.append((re.findall('([^:]*)',line[1]),item))
for i_b in base_class :
    print (i_b,":")
    for i_d in derv_class :
        if i_b[0] in  i_d :
            print("\t",i_d[0],i_d[-1])
    print("\n")
