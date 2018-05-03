import sys
import threading
q = []
class myThread(threading.Thread) :
    def __init__(self,f_name,fh) :
        threading.Thread.__init__(self)
        self.f_name = f_name
        self.fh = fh
        self.line_count=0
        self.word_count=0
        self.char_count=0
    def run(self) :
        for line in self.fh :
            self.line_count += 1
            line = line.strip()
            words = line.split()
            self.word_count += len(words)
            for word in words :
                for letter in word :
                    self.char_count += 1
        q.append((self.f_name,self.line_count,self.word_count,self.char_count))

lst = sys.argv
lst.pop(0)
fhl = list()

#creating file handles
for i in range(len(lst)) :
    fhl.append(open(lst[i]))

thread = list()

#creating new threads
for i in range(len(lst)) :
    thread.append(myThread(lst[i],fhl[i]))

#starting threads
for i in range(len(lst)) :
    thread[i].start()

#joining threads
for i in range(len(lst)) :
    thread[i].join()

q.sort()

for item in q :
    print item[0],item[1],item[2],item[3]
