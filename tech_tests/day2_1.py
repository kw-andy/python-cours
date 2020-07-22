'''
import collections

d = collections.defaultdict(int)

def day2_1(inputfile):
	with open(inputfile) as file:
		counter2 = 0
		counter3 = 0
		counter1 = 0
		countfinal = 0
		for line in file:
			frequencies = collections.Counter(line)
			countfinal +=1 #ok
			for key,value in frequencies.items():
				#print(key,value)
				if (value // 2) > 1:
					if value % 3 == 0:
						counter3 += 1
					elif value % 2 == 0:
						counter2 +=1			
				elif value == 3:
					counter3 += 1
				elif value ==2:
					counter2 +=2	
				elif value == 1:
					counter1 += 1						
	
	
	#print(frequencies)
	print(counter2*counter3,counter1,countfinal)		
			


day2_1("inputday2_1.txt")	

'''

from collections import Counter
import fileinput

lines = [x.strip() for x in fileinput.input(["inputday2_1.txt"])]

#print(lines)

def part1():
    has2 = 0
    has3 = 0
    for line in lines:
        c = Counter(line).values()
        #print(c)
        has2 += 2 in c
        #print(has2)
        has3 += 3 in c
        #print(has3)
    return has2 * has3

def part2():
    for line1 in lines:
        for line2 in lines:
            x = ''.join(a for a, b in zip(line1, line2) if a == b)
            #print(x)
            if len(x) == len(line1) - 1:
                return x

print(part1())
print(part2())		

