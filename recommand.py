# 추천.


cantbuy=[]
cantbuypit=[]

myteam = []


def goodplayer(filename, team, myteamindex):
    rec = []
    f = open('./'+filename+'obp정렬.txt', 'r' )

    algobp = []
    samepos = 0
    
    while 1 :
        line = f.readline()
        if not line:
            break
        line=line.split('\t')
        index=0
        for _ in range(len(line)):
            if index == len(line)-1:
                tmp = line[_].replace('\n',"")
                line.pop()
                line.append(tmp)
                index=0
                algobp.append(line)
            else:
                index+=1
        #print(line)
    f.close()

    #print(algobp)
    print()
    #print(algops)

    for i in range(len(algobp)):
        if team == algobp[i][1]:
            for k in range(len(myteam)):
                
                if myteam[k][0] == algobp[i][0]:
                    samepos=1
                    break
                elif k+1 == len(myteam):
                    myteam.append(algobp[i])
            if len(myteam) == 0 :
                myteam.append(algobp[i])
            if samepos ==0:
                break
            else:
                samepos = 0
        else:
            rec.append(algobp[i])
    dellist =[]
    for i in range(len(rec)):
        for j in range(len(cantbuy)):
            if cantbuy[j][0] == rec[i][0] and cantbuy[j][1] == rec[i][1] :
                dellist.append(rec[i])

    for _ in dellist:
        del rec[rec.index(_)]
    
    
    print("- "+ filename+" -" )
    print(myteam[myteamindex])            
    print(team + "에게 추천하는 선수 " + "- "+ filename+" -")
    print(rec)
    myteamindex+=1
    return myteamindex
    
def goodplayerops(filename, team, myteamindex):
    rec = []
    f = open('./'+filename+'ops정렬.txt', 'r' )

    algops = []
    samepos = 0
    
    while 1 :
        line = f.readline()
        if not line:
            break
        line=line.split('\t')
        index=0
        for _ in range(len(line)):
            if index == len(line)-1:
                tmp = line[_].replace('\n',"")
                line.pop()
                line.append(tmp)
                index=0
                algops.append(line)
            else:
                index+=1
        #print(line)
    f.close()

    #print(algobp)
    print()
    #print(algops)

    for i in range(len(algops)):
        if team == algops[i][1]:
            for k in range(len(myteam)):
                
                if myteam[k][0] == algops[i][0]:
                    samepos=1
                    break
                elif k+1 == len(myteam):
                    myteam.append(algops[i])
            if len(myteam) == 0 :
                myteam.append(algops[i])
            if samepos ==0:
                break
            else:
                samepos = 0
        else:
            rec.append(algops[i])
    dellist =[]
    for i in range(len(rec)):
        for j in range(len(cantbuy)):
            if cantbuy[j][0] == rec[i][0] and cantbuy[j][1] == rec[i][1] :
                dellist.append(rec[i])

    for _ in dellist:
        del rec[rec.index(_)]
    
    print("- "+ filename+" -" )
    print(myteam[myteamindex])            
    print(team + "추천하는 선수 " + "- "+ filename+" -")
    print(rec)
    myteamindex+=1
    return myteamindex

def goodplayerkk(filename, team, myteamindex):
    rec = []
    f = open('./'+filename+'kk정렬.txt', 'r' )

    algops = []
    samepos = 0
    
    while 1 :
        line = f.readline()
        if not line:
            break
        line=line.split('\t')
        index=0
        for _ in range(len(line)):
            if index == len(line)-1:
                tmp = line[_].replace('\n',"")
                line.pop()
                line.append(tmp)
                index=0
                algops.append(line)
            else:
                index+=1
        #print(line)
    f.close()

    #print(algobp)
    print()
    #print(algops)

    for i in range(len(algops)):
        if team == algops[i][1]:
            for k in range(len(myteam)):
                
                if myteam[k][0] == algops[i][0]:
                    samepos=1
                    break
                elif k+1 == len(myteam):
                    myteam.append(algops[i])
            if len(myteam) == 0 :
                myteam.append(algops[i])
            if samepos ==0:
                break
            else:
                samepos = 0
        else:
            rec.append(algops[i])
    dellist =[]
    for i in range(len(rec)):
        for j in range(len(cantbuy)):
            if cantbuy[j][0] == rec[i][0] and cantbuy[j][1] == rec[i][1] :
                dellist.append(rec[i])

    for _ in dellist:
        del rec[rec.index(_)]
    
    print("- "+ filename+" -" )
    print(myteam[myteamindex])            
    print(team + "에게 추천하는 선수 " + "- "+ filename+" -")
    print(rec)
    myteamindex+=1
    return myteamindex

def goodplayerbb(filename, team, myteamindex):
    rec = []
    f = open('./'+filename+'bb정렬.txt', 'r' )

    algops = []
    samepos = 0
    
    while 1 :
        line = f.readline()
        if not line:
            break
        line=line.split('\t')
        index=0
        for _ in range(len(line)):
            if index == len(line)-1:
                tmp = line[_].replace('\n',"")
                line.pop()
                line.append(tmp)
                index=0
                algops.append(line)
            else:
                index+=1
        #print(line)
    f.close()

    #print(algobp)
    print()
    #print(algops)

    for i in range(len(algops)):
        if team == algops[i][1]:
            for k in range(len(myteam)):
                
                if myteam[k][0] == algops[i][0]:
                    samepos=1
                    break
                elif k+1 == len(myteam):
                    myteam.append(algops[i])
            if len(myteam) == 0 :
                myteam.append(algops[i])
            if samepos ==0:
                break
            else:
                samepos = 0
        else:
            rec.append(algops[i])
    dellist =[]
    for i in range(len(rec)):
        for j in range(len(cantbuy)):
            if cantbuy[j][0] == rec[i][0] and cantbuy[j][1] == rec[i][1] :
                dellist.append(rec[i])

    for _ in dellist:
        del rec[rec.index(_)]
    
    print("- "+ filename+" -" )
    print(myteam[myteamindex])            
    print(team + "에게 추천하는 선수 " + "- "+ filename+" -")
    print(rec)
    myteamindex+=1
    return myteamindex

def goodplayerbbk(filename, team, myteamindex):
    rec = []
    f = open('./'+filename+'bbk정렬.txt', 'r' )

    algops = []
    samepos = 0
    
    while 1 :
        line = f.readline()
        if not line:
            break
        line=line.split('\t')
        index=0
        for _ in range(len(line)):
            if index == len(line)-1:
                tmp = line[_].replace('\n',"")
                line.pop()
                line.append(tmp)
                index=0
                algops.append(line)
            else:
                index+=1
        #print(line)
    f.close()

    #print(algobp)
    print()
    #print(algops)

    for i in range(len(algops)):
        if team == algops[i][1]:
            for k in range(len(myteam)):
                
                if myteam[k][0] == algops[i][0]:
                    samepos=1
                    break
                elif k+1 == len(myteam):
                    myteam.append(algops[i])
            if len(myteam) == 0 :
                myteam.append(algops[i])
            if samepos ==0:
                break
            else:
                samepos = 0
        else:
            rec.append(algops[i])
    dellist =[]
    for i in range(len(rec)):
        for j in range(len(cantbuy)):
            if cantbuy[j][0] == rec[i][0] and cantbuy[j][1] == rec[i][1] :
                dellist.append(rec[i])

    for _ in dellist:
        del rec[rec.index(_)]
    
    print("- "+ filename+" -" )
    print(myteam[myteamindex])            
    print(team + "에게 추천하는 선수 " + "- "+ filename+" -")
    print(rec)
    myteamindex+=1
    return myteamindex


def searchplayer(team):

    print("** 타자 **")
    mindex = 0
    print("<<출루율 기준추천>>")
    print("기존 우리팀")
    mindex = goodplayer('1루수', team, mindex)
    mindex =goodplayer('2루수', team, mindex)
    mindex =goodplayer('3루수', team, mindex )
    mindex =goodplayer('유격수', team, mindex)
    mindex =goodplayer('중견수', team, mindex)
    mindex =goodplayer('우익수', team, mindex)
    mindex =goodplayer('좌익수', team, mindex)
    mindex =goodplayer('포수', team, mindex)

    myteam.clear()

    print()
    print()
    mindex = 0
    print("<<출루율 + 장타율 기준추천>>")
    print("기존 우리팀")
    mindex = goodplayerops('1루수', team, mindex)
    mindex =goodplayerops('2루수', team, mindex)
    mindex =goodplayerops('3루수', team, mindex )
    mindex =goodplayerops('유격수', team, mindex)
    mindex =goodplayerops('중견수', team, mindex)
    mindex =goodplayerops('우익수', team, mindex)
    mindex =goodplayerops('좌익수', team, mindex)
    mindex =goodplayerops('포수', team, mindex)

    myteam.clear()
    
    print("** 투수 **")
    mindex = 0
    print("<<kk 기준추천>>")
    print("기존 우리팀")
    mindex = goodplayerkk('투수', team, mindex)
    print(mindex)
    

    print()
    print()
    #mindex = 0
    print("<<bb 기준추천>>")
    print("기존 우리팀")
    mindex = goodplayerbb('투수', team, mindex)
    #myteam.clear()
    print(mindex)

    print()
    print()
    #mindex = 0
    print("<<bb/k 기준추천>>")
    print("기존 우리팀")
    mindex = goodplayerbbk('투수', team, mindex)





f = open('./'+'/영입어려움_타자.txt', 'r', encoding='UTF8')
while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    index=0
    for _ in range(len(line)):
        if index == len(line)-1:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            index=0
            cantbuy.append(line)
        else:
            index+=1
    #print(line)
f.close()

f = open('./'+'영입어려움_투수.txt', 'r', encoding='UTF8')
while 1 :
    line = f.readline()
    if not line:
        break
    line=line.split('\t')
    index=0
    for _ in range(len(line)):
        if index == len(line)-1:
            tmp = line[_].replace('\n',"")
            line.pop()
            line.append(tmp)
            index=0
            cantbuypit.append(line)
        else:
            index+=1
    #print(line)
f.close()

team = input("which team?")
searchplayer(team)
