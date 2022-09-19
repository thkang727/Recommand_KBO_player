

team = ['롯데','삼성', '키움', 'LG', 'KIA', '두산', 'NC', '한화', 'KT']
position = ['투수', '포수','1루수','2루수','3루수','유격수','좌익수','우익수','중견수']
pos1=[]
pos2=[]
pos3=[]
pos4=[]
pos5=[]
pos6=[]
pos7=[]
pos8=[]
pos9=[]
f = open('./선수포지션.txt', 'r', encoding='UTF8')


while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    index=0
    for _ in range(len(line)):
        if index == 2:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            for pos in range (len(position)):
                if position[pos] == tmp:
                    if pos == 0:
                        pos1.append(line)
                    elif pos ==1:
                        pos2.append(line)
                    elif pos ==2:
                        pos3.append(line)
                    elif pos ==3:
                        pos4.append(line)
                    elif pos ==4:
                        pos5.append(line)
                    elif pos ==5:
                        pos6.append(line)
                    elif pos ==6:
                        pos7.append(line)
                    elif pos ==7:
                        pos8.append(line)
                    elif pos ==8:
                        pos9.append(line)
            index=0
        else:
            index+=1
    #print(line)

f.close()


# print(pos1)
# print()
# print(pos2)
# print()
# print(pos3)
# print()
# print(pos4)
# print()
# print(pos5)
# print()
# print(pos6)
# print()
# print(pos7)
# print()
# print(pos8)
# print()
# print(pos9)




f = open('./타자obp,ops.txt', 'r', encoding='UTF8')

while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    #print(line)
    index=0
    for _ in range(len(line)):
        if index == 4:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            #print(line[0])
            for j in range(len(pos1)):
                if pos1[j][0] == line[0] and pos1[j][1] == line[1]:
                    #print(pos1[j][1])
                    pos1[j].append(line[3])
                    pos1[j].append(line[4])
                
            for j in range(len(pos2)) :
                if pos2[j][0] == line[0] and pos2[j][1] == line[1]:
                    #print(pos2[j][1])
                    pos2[j].append(line[3])
                    pos2[j].append(line[4])
               
            for j in range(len(pos3)) :
                if pos3[j][0] == line[0] and pos3[j][1] == line[1]:
                    #print(pos3[j][1])
                    pos3[j].append(line[3])
                    pos3[j].append(line[4])
                   
            for j in range(len(pos4)) :
                if pos4[j][0] == line[0] and pos4[j][1] == line[1]:
                    #print(pos4[j][1])
                    pos4[j].append(line[3])
                    pos4[j].append(line[4])
                  
            for j in range(len(pos5)) :
                if pos5[j][0] == line[0] and pos5[j][1] == line[1]:
                   # print(pos5[j][1])
                    pos5[j].append(line[3])
                    pos5[j].append(line[4])
                   
            for j in range(len(pos6)) :
                if pos6[j][0] == line[0] and pos6[j][1] == line[1]:
                   # print(pos6[j][1])
                    pos6[j].append(line[3])
                    pos6[j].append(line[4])
                   
            for j in range(len(pos7)) :
                if pos7[j][0] == line[0] and pos7[j][1] == line[1]:
                   # print(pos7[j][1])
                    pos7[j].append(line[3])
                    pos7[j].append(line[4])
                   
            for j in range(len(pos8)) :
                if pos8[j][0] == line[0] and pos8[j][1] == line[1]:
                   # print(pos8[j][1])
                    pos8[j].append(line[3])
                    pos8[j].append(line[4])
                    
            for j in range(len(pos9)) :
                if pos9[j][0] == line[0] and pos9[j][1] == line[1]:
                   # print(pos9[j][1])
                    pos9[j].append(line[3])
                    pos9[j].append(line[4])
                    
            index=0
        else:
            index+=1
    #print(line)

f.close()



f = open('./2020타자obp,ops.txt', 'r', encoding='UTF8')

while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    print(line)
    index=0
    for _ in range(len(line)):
        if index == 4:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            #print(line[0])
            for j in range(len(pos1)):
                if pos1[j][0] == line[0] and pos1[j][1] == line[1]:
                    #print(pos1[j][1])
                    pos1[j].append(line[3])
                    pos1[j].append(line[4])
                
            for j in range(len(pos2)) :
                if pos2[j][0] == line[0] and pos2[j][1] == line[1]:
                    #print(pos2[j][1])
                    pos2[j].append(line[3])
                    pos2[j].append(line[4])
               
            for j in range(len(pos3)) :
                if pos3[j][0] == line[0] and pos3[j][1] == line[1]:
                    #print(pos3[j][1])
                    pos3[j].append(line[3])
                    pos3[j].append(line[4])
                   
            for j in range(len(pos4)) :
                if pos4[j][0] == line[0] and pos4[j][1] == line[1]:
                    #print(pos4[j][1])
                    pos4[j].append(line[3])
                    pos4[j].append(line[4])
                  
            for j in range(len(pos5)) :
                if pos5[j][0] == line[0] and pos5[j][1] == line[1]:
                   # print(pos5[j][1])
                    pos5[j].append(line[3])
                    pos5[j].append(line[4])
                   
            for j in range(len(pos6)) :
                if pos6[j][0] == line[0] and pos6[j][1] == line[1]:
                   # print(pos6[j][1])
                    pos6[j].append(line[3])
                    pos6[j].append(line[4])
                   
            for j in range(len(pos7)) :
                if pos7[j][0] == line[0] and pos7[j][1] == line[1]:
                   # print(pos7[j][1])
                    pos7[j].append(line[3])
                    pos7[j].append(line[4])
                   
            for j in range(len(pos8)) :
                if pos8[j][0] == line[0] and pos8[j][1] == line[1]:
                   # print(pos8[j][1])
                    pos8[j].append(line[3])
                    pos8[j].append(line[4])
                    
            for j in range(len(pos9)) :
                if pos9[j][0] == line[0] and pos9[j][1] == line[1]:
                   # print(pos9[j][1])
                    pos9[j].append(line[3])
                    pos9[j].append(line[4])
                    
            index=0
        else:
            index+=1
    #print(line)

f.close()

ansobp = 0
ansops = 0

dellist =[]

for j in range(len(pos1)):
    if len(pos1[j]) >= 5:
        if len(pos1[j]) >= 7:
            ansobp = (float(pos1[j][5])+float(pos1[j][3])) /2
            ansops = (float(pos1[j][6])+float(pos1[j][4])) /2
        else:
            ansobp = float(pos1[j][3])
            ansops = float(pos1[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos1[j].append(str(ansobp))
        pos1[j].append(str(ansops))
    else:
        dellist.append(pos1[j])

for _ in dellist:
    del pos1[pos1.index(_)]
        
#초기화
dellist =[]

for j in range(len(pos2)):
    if len(pos2[j]) >= 5:
        if len(pos2[j]) >= 7:
            ansobp = (float(pos2[j][5])+float(pos2[j][3])) /2
            ansops = (float(pos2[j][6])+float(pos2[j][4])) /2
        else:
            ansobp = float(pos2[j][3])
            ansops = float(pos2[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos2[j].append(str(ansobp))
        pos2[j].append(str(ansops))
    else:
        dellist.append(pos2[j])

for _ in dellist:
    del pos2[pos2.index(_)]
        
#초기화
dellist =[]

    
for j in range(len(pos3)) :
    if len(pos3[j]) >= 5:
        if len(pos3[j]) >= 7:
            ansobp = (float(pos3[j][5])+float(pos3[j][3])) /2
            ansops = (float(pos3[j][6])+float(pos3[j][4])) /2
        else:
            ansobp = float(pos3[j][3])
            ansops = float(pos3[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos3[j].append(str(ansobp))
        pos3[j].append(str(ansops))
    else:
        dellist.append(pos3[j])

for _ in dellist:
    del pos3[pos3.index(_)]
        
#초기화
dellist =[]
        
for j in range(len(pos4)) :
    if len(pos4[j]) >= 5:
        if len(pos4[j]) >= 7:
            ansobp = (float(pos4[j][5])+float(pos4[j][3])) /2
            ansops = (float(pos4[j][6])+float(pos4[j][4])) /2
        else:
            ansobp = float(pos4[j][3])
            ansops = float(pos4[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)

        pos4[j].append(str(ansobp))
        pos4[j].append(str(ansops))
    else:
        dellist.append(pos4[j])

for _ in dellist:
    del pos4[pos4.index(_)]
        
#초기화
dellist =[]
        
for j in range(len(pos5)) :
    if len(pos5[j]) >= 5:
        if len(pos5[j]) >= 7:
            ansobp = (float(pos5[j][5])+float(pos5[j][3])) /2
            ansops = (float(pos5[j][6])+float(pos5[j][4])) /2
        else:
            ansobp = float(pos5[j][3])
            ansops = float(pos5[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos5[j].append(str(ansobp))
        pos5[j].append(str(ansops))
    else:
        dellist.append(pos5[j])

for _ in dellist:
    del pos5[pos5.index(_)]
        
#초기화
dellist =[]
        
for j in range(len(pos6)) :
    if len(pos6[j]) >= 5:
        if len(pos6[j]) >= 7:
            ansobp = (float(pos6[j][5])+float(pos6[j][3])) /2
            ansops = (float(pos6[j][6])+float(pos6[j][4])) /2
        else:
            ansobp = float(pos6[j][3])
            ansops = float(pos6[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos6[j].append(str(ansobp))
        pos6[j].append(str(ansops))
    else:
        dellist.append(pos6[j])

for _ in dellist:
    del pos6[pos6.index(_)]
        
#초기화
dellist =[]
        
for j in range(len(pos7)) :
    if len(pos7[j]) >= 5:
        if len(pos7[j]) >= 7:
            ansobp = (float(pos7[j][5])+float(pos7[j][3])) /2
            ansops = (float(pos7[j][6])+float(pos7[j][4])) /2
        else:
            ansobp = float(pos7[j][3])
            ansops = float(pos7[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos7[j].append(str(ansobp))
        pos7[j].append(str(ansops))
    else:
        dellist.append(pos7[j])

for _ in dellist:
    del pos7[pos7.index(_)]

#초기화
dellist =[]
        
for j in range(len(pos8)) :
    if len(pos8[j]) >= 5:
        if len(pos8[j]) >= 7:
            ansobp = (float(pos8[j][5])+float(pos8[j][3])) /2
            ansops = (float(pos8[j][6])+float(pos8[j][4])) /2
        else:
            ansobp = float(pos8[j][3])
            ansops = float(pos8[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos8[j].append(str(ansobp))
        pos8[j].append(str(ansops))
    else:
        dellist.append(pos8[j])

for _ in dellist:
    del pos8[pos8.index(_)]

#초기화
dellist =[]
        
for j in range(len(pos9)) :
    if len(pos9[j]) >= 5:
        if len(pos9[j]) >= 7:
            ansobp = (float(pos9[j][5])+float(pos9[j][3])) /2
            ansops = (float(pos9[j][6])+float(pos9[j][4])) /2
        else:
            ansobp = float(pos9[j][3])
            ansops = float(pos9[j][4])
        ansobp = round(ansobp, 3)
        ansops = round(ansops, 3)
        pos9[j].append(str(ansobp))
        pos9[j].append(str(ansops))
    else:
        dellist.append(pos9[j])

for _ in dellist:
    del pos9[pos9.index(_)]

#초기화
dellist =[]


pos1.clear()

f = open('./2021투수볼삼비.txt', 'r', encoding='UTF8')

while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    index=0
    for _ in range(len(line)):
        if index == 4:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            pos1.append(line)

            index=0
        else:
            index+=1
    #print(line)

f.close()

f = open('./2020투수볼삼비.txt', 'r', encoding='UTF8')

while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    #print(line)
    index=0
    for _ in range(len(line)):
        if index == 4:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            #print(line[0])
            for j in range(len(pos1)):
                if pos1[j][0] == line[0] and pos1[j][1] == line[1]:
                    #print(pos1[j][1])
                    pos1[j].append(line[2])
                    pos1[j].append(line[3])
                    pos1[j].append(line[4])
            index=0
        else:
            index+=1
    #print(line)

f.close()


for j in range(len(pos1)):
    print(pos1[j])
    if len(pos1[j]) >= 5:
        if len(pos1[j]) >= 7:
            anskk9 = (float(pos1[j][5])+float(pos1[j][2])) /2
            ansbb9 = (float(pos1[j][6])+float(pos1[j][3])) /2
            ansbbk = (float(pos1[j][7])+float(pos1[j][4])) /2
        else:
            anskk9 = float(pos1[j][2])
            ansbb9 = float(pos1[j][3])
            ansbbk = float(pos1[j][4])
        anskk9 = round(anskk9, 3)
        ansbb9 = round(ansbb9, 3)
        ansbbk = round(ansbbk, 3)
        pos1[j].append(str(anskk9))
        pos1[j].append(str(ansbb9))
        pos1[j].append(str(ansbbk))
    else:
        dellist.append(pos1[j])

for _ in dellist:
    del pos1[pos1.index(_)]


f = open('투수볼삼비.txt','w')
for _ in pos1:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('포수.txt','w')
for _ in pos2:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('1루수.txt','w')
for _ in pos3:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('2루수.txt','w')
for _ in pos4:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('3루수.txt','w')
for _ in pos5:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('유격수.txt','w')
for _ in pos6:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('좌익수.txt','w')
for _ in pos7:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('우익수.txt','w')
for _ in pos8:
    f.write("\t".join(_))
    f.write("\n")
f.close()

f = open('중견수.txt','w')
for _ in pos9:
    f.write("\t".join(_))
    f.write("\n")
f.close()