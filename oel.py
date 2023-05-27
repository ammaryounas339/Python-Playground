def bestFit(blockSize, m, processSize, n,arrival):
        given_block = [-1] * n 
        for i in range(n):
            to_check = list(processSize.values())[i]
            best_hole = -1
            for j in range(m):
                if blockSize[j] >= to_check:
                    if best_hole == -1: 
                        best_hole = j 
                    elif blockSize[best_hole] > blockSize[j]: 
                        best_hole = j

            if best_hole != -1:
                given_block[i] = best_hole 
                blockSize[best_hole] -= to_check
        print("Process No.  Arrival Time  Process Size     Block no.")
        for i in range(n):
            print( list(processSize.keys())[i], "         ",arrival[i],"               ", list(processSize.values())[i],  end = "         ") 
            if given_block[i] != -1: 
                print("       "+str(given_block[i] + 1)) 
            else:
                print("Not Given")
def firstFit(blockSize, m, processSize,n,arrival):
        given_block = [-1] * n
        for i in range(n):
            to_check = list(processSize.values())[i]
            for j in range(m):
                if blockSize[j] >= to_check:
                    given_block[i] = j
                    blockSize[j] -= to_check
                    break
        for i in range(n):
            print( list(processSize.keys())[i], "         ",arrival[i],"               ", list(processSize.values())[i],  end = "         ") 
            if given_block[i] != -1: 
                print("       "+str(given_block[i] + 1)) 
            else:
                print("Not Given")
def reqs(somelist):
    returnList = sorted(somelist)
    avg = sum(somelist)/len(somelist)
    return returnList[0],returnList[-1],avg

if __name__ == '__main__': 
   
    x = int(input("Enter number of processes : "))
    processSize=[0]*x
    arrivalTime = [0]*x
    processN = [f'P{i+1}' for i in range(x) ]
    print(processN)
    MM_SIZE = 1024
    blockSize = [100,112,54,96,150,66,77,151,120,98]
    for i in range(x):
        processSize[i] = int(input(f"Enter Size of P{i+1}: "))
        arrivalTime[i] = int(input(f"Arrival Time of P{i+1}: "))
    arrivalDict = dict(zip(processN,arrivalTime))

    sizeDict = dict(zip(processN,processSize))
    arrivalDict = dict(sorted(arrivalDict.items(), key=lambda x: x[1]))
    res = {key: sizeDict.get(key, arrivalDict[key]) for key in arrivalDict}

    arrivalTime= list(arrivalDict.values())
    processes = list(res.values())
    answers = reqs(processes)

    print("\n\nFixed Unequal Size Partitioning")
    print("BEST FIT ALGORITHM")
    print("\nMain memory size before allocating is : "+str(MM_SIZE)+"MB")
    print("Block Sizes before allocation are : ")
    print(blockSize)
    bestFit(blockSize,10,res,x,arrivalTime)
    print()
    print("After allocation memory remaining is : "+str(sum(blockSize))+"MB")
    print("Block Sizes after allocation are : ")
    print(blockSize)
    blockSize = [128]*8
    print("\n\n Fixed Equal Size Partitioning")
    print("FIRST FIT ALGORITHM")
    print("\nMain memory size before allocating is : "+str(MM_SIZE)+"MB")
    print("Block Sizes before allocation are : ")
    print(blockSize)
    firstFit(blockSize,10,res,x,arrivalTime)
    print()
    print("After allocation memory remaining is : "+str(sum(blockSize))+"MB")
    print("Block Sizes after allocation are : ")
    print(blockSize)
    print("The minimum process size is : "+str(answers[0]))
    print("The maximum process size is : "+str(answers[1]))
    print("The average process size is : "+str(answers[2]))
    
    
     
     