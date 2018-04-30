import sys
import re
lst = sys.argv
path = lst[1]
fil = os.listdir()
for item in fil :
    if item.endswith(".py") :
        fh = open(item)
        for line in fh :
            line = line.strip()
            if line.beginswith("class") :
                if "(" in line[1] :
                    names = re.split('():',line[1])
                    derv_class.append((names[0],names[1],item))
                else :
                    base_class.append((re.findall('([^:]*)',line[1]),item))
