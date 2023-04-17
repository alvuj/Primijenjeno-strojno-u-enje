counter = 0
rez = 0
fhand = open('mbox-short.txt')
for line in fhand:
    
    line = line.rstrip()
    if (line.startswith("X-DSPAM-Confidence")):
        
        counter += 1
        words = line.split()
        rez = rez + float(words[1])
print(counter)
mid = float (rez)/float(counter)
fhand.close()
print("X-DSPAM-Confidence" + str(mid))