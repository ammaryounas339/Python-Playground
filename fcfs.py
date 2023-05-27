if __name__ == '__main__': 
    proc = int(input("Enter the number of processses :" ))
    bt = [0]*proc
    for i in range(0,proc):
        bt[i]  = int(input(f"Enter the burst time for {i+1}: "))
    
    wt = [0]*proc
    wt[0] = 0
    for i in range (1,proc):
        wt[i]= wt[i-1]+bt[i-1]
    
    avgwt = sum(wt)/len(wt)
    avgbt = sum(bt)/len(bt)
    
    tt = [0]*proc
    for i in range(0,proc):
        tt[i] = bt[i]+wt[i]
        
    print("Process Sid " + "         "+ "bt"+  "          "+ "wt"+"         "+"tt" )
    for i in range(0,proc):
         print(str(i+1) + "                    "+ str(bt[i])+  "            "+ str(wt[i])+"          "+str(tt[i]) )
    avgtt = sum(tt)/len(tt)

    print("The avergae wait time is : "+str(avgwt))
    print("The avergae burst time is : "+str(avgbt))
    print("The avergae turnaround time is : "+str(avgtt))