N, M= input().split()
N, M= int(N), int(M)
matrix1= []
matrix2= []
finaloutput=[]
if not (1<=N<=10 and 1<=M<=10):
    print("error")
else:
    for i in range(1,N+1):
        row= list(map(int,input().split()))
        matrix1.append(row) 
        
    for i in range(1,N+1):
        row= list(map(int,input().split()))
        matrix2.append(row)
        
    for i in range(N):
        output=[]
        for j in range(M):
            c = matrix1[i][j] + matrix2[i][j]
            output.append(c)
            
        finaloutput.append(output)
        
    for row in finaloutput: 
        print(*row)
            
            
            
    # print(matrix1)
    # print(matrix2)
    # print(output)
    # print(finaloutput)
    
    #------------------------Exercise1--------------------------------------
