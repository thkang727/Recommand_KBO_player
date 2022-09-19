#alg


# 버블 정렬의 범용성을 높이기 위해 함수로 만듬
def bubbleSort(arr, num):
    n = len(arr) # 배열의 크기를 측정
    
    if num == 0:
        # 배열의 크기만큼 반복
        for i in range(n):
            obpi = 0
            obpj = 0
            # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
            for j in range(0, n - i - 1):
                if len(arr[j]) > 7:
                    obpj = 7
                else:
                    obpj = 5
                if len(arr[j+1]) > 7:
                    obpi = 7
                else:
                    obpi = 5
                # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
                if arr[j][obpj] < arr[j + 1][obpi]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환

    elif num == 1:
        # 배열의 크기만큼 반복
        for i in range(n):
            opsi = 0
            opsj = 0
                
            # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
            for j in range(0, n - i - 1):
                if len(arr[j]) > 7:
                    opsj = 8
                else:
                    opsj = 6
                if len(arr[j+1]) > 7:
                    opsi = 8
                else:
                    opsi = 6
                
                # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
                if arr[j][opsj] < arr[j + 1][opsi]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환
    
    elif num == 2:
        # 배열의 크기만큼 반복
        for i in range(n):
            opsi = 0
            opsj = 0
                
            # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
            for j in range(0, n - i - 1):
                if len(arr[j]) > 8:
                    opsj = 8
                else:
                    opsj = 5
                if len(arr[j+1]) > 8:
                    opsi = 8
                else:
                    opsi = 5
                
                # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
                if arr[j][opsj] < arr[j + 1][opsi]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환
    
    elif num == 3:
        # 배열의 크기만큼 반복
        for i in range(n):
            opsi = 0
            opsj = 0
                
            # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
            for j in range(0, n - i - 1):
                if len(arr[j]) > 8:
                    opsj = 9
                else:
                    opsj = 6
                if len(arr[j+1]) > 8:
                    opsi = 9
                else:
                    opsi = 6
                
                # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
                if arr[j][opsj] < arr[j + 1][opsi]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환
    elif num == 4:
        # 배열의 크기만큼 반복
        for i in range(n):
            opsi = 0
            opsj = 0
                
            # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
            for j in range(0, n - i - 1):
                if len(arr[j]) > 8:
                    opsj = 10
                else:
                    opsj = 7
                if len(arr[j+1]) > 8:
                    opsi = 10
                else:
                    opsi = 7
                
                # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
                if arr[j][opsj] < arr[j + 1][opsi]: 
                    arr[j], arr[j + 1] = arr[j + 1], arr[j] # 서로 위치를 변환  
                

def goodplayer(filename):
    f = open('./'+filename+'.txt', 'r' )

    algobp = []
    algops = []
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

    print(algobp)
    algops = algobp.copy()
    print()
    print(algops)

    bubbleSort(algobp,0)
    bubbleSort(algops,1)
    print()
    print(algobp)
    print()
    print(algops)

    f = open(filename+'obp정렬.txt','w')
    for _ in algobp:
        f.write("\t".join(_))
        f.write("\n")
    f.close()
    f = open(filename+'ops정렬.txt','w')
    for _ in algops:
        f.write("\t".join(_))
        f.write("\n")
    f.close()

def goodplayerpit(filename):
    f = open('./'+filename+'볼삼비.txt', 'r' )

    algbb = []
    algkk = []
    algbbk = []
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
                algbb.append(line)
            else:
                index+=1
        #print(line)
    f.close()

    print(algbb)
    algkk = algbb.copy()
    algbbk = algbb.copy()
    print()
    

    bubbleSort(algbb,2)
    bubbleSort(algkk,3)
    algkk.reverse()
    bubbleSort(algbbk,4)
    print()
    print(algbb)
    print()
    print(algkk)
    print()
    print(algbbk)

# bb/ k 반대로 넣음.
    f = open(filename+'kk정렬.txt','w')
    for _ in algbb:
        f.write("\t".join(_))
        f.write("\n")
    f.close()
    f = open(filename+'bb정렬.txt','w')
    for _ in algkk:
        f.write("\t".join(_))
        f.write("\n")
    f.close()
    f = open(filename+'bbk정렬.txt','w')
    for _ in algbbk:
        f.write("\t".join(_))
        f.write("\n")
    f.close()

goodplayer('1루수')
goodplayer('2루수')
goodplayer('3루수')
goodplayer('유격수')
goodplayer('중견수')
goodplayer('우익수')
goodplayer('좌익수')
goodplayer('포수')
goodplayerpit('투수')