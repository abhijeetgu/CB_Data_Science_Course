t =int(input())

for i in range(t):
    m, n = [int(x) for x in input().split()] 
    
    for j in range(m,n+1):
        flag = True 
        if(j==1):
            flag = False
            
           
        for k in range(2,j):
            if(j%k==0):
                flag=False
                break
        k=k*k        
        if(flag==True):
            print(j,end =" ")
    
