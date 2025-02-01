import os
import random

# for i in range(10):
#     os.system("lsc 1000 19260817 <data/{}.txt >results/{}.txt".format(i, i))

def check(lsc):
    n = len(lsc)
    for i in range(n):
        for j in range(n):
            for k in range(j):
                if lsc[i][j] == lsc[i][k] or lsc[j][i] == lsc[k][i]:
                    return False
    return True


os.system('make')
print("build done")
for root, _, files in os.walk('./data/'):
    for file in files:
        # if file not in ['{}.txt'.format(i) for i in range(10)]:
        #     continue
        if file[:3] == 'QWH':
            continue
        # if file[:8] == 'qg.order':
        #     continue
        
        if file != "qwhdec.order33.holes381.bal.1.col":
            continue
        
        count = 0
        T = 30
        for i in range(T):
            os.system("lsc 600 {} {} <data/{} >temp.txt".format(i + 1, file, file))
            lines = []
            with open('temp.txt', 'r') as f:
                lines = f.readlines()
            n = len(lines)
            lsc = [[] for i in range(n)]
            for i in range(n):
                lsc[i] = list(map(int, lines[i].strip().split(' ')))
            if check(lsc):
                count += 1
            
        print("{}: {}/{}".format(file, count, T))