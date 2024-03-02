'''f = open("final.txt", "r")
print(f.readline())'''

with open('final.txt') as f_in:
    lines = (line.rstrip() for line in f_in) # All lines including the blank ones
    lines = (line for line in lines if line)

f = open("final2.txt","a");
for line in lines:
    f.write(line)