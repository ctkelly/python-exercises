import re

testfile = open('regex_sum.txt')

big_num_list = list()
for line in testfile:
    num = re.findall('[0-9]+', line)
    if len(num) > 0:
        big_num_list.append(num)

flat_list = list()
for sublist in big_num_list:
    for item in sublist:
        flat_list.append(item)

int_list = list()
for item in flat_list:
    intnum = int(item)
    int_list.append(intnum)

print(sum(int_list))    


        
