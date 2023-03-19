# python3

def parallel_processing(n, m, t):
    
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    output=[]
    n1=[0]*n
    time=[0]*n
    
    i=0
    while i<m:
        for j in range(n):
            if n1[j]==0:
                output.append([j,time[j]])             
                n1[j]=t[i]
                time[j]+=t[i]
                i+=1
            if n1[j]!=0:
                n1[j]=n1[j]-1          
            
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int,input().split())
    t = list(map(int, input().split()))
    
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,t)
    for i, j in result:
        print(i, j)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
