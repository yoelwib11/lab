

def findSame(param):
    same=[]
    temp=[]
    new_same=[]
    if isinstance(param, list):
        for j in param:
            for k in param:
                if (set(j) == set(k)):
                    if( j not in temp ):
                        temp.append(j)
                    if( k not in temp ):
                        temp.append(k)
                    
                
            
            if(len(temp) > 1):
                same.append(set(temp.copy()))
                


            
            temp.clear()
        
        for num in same: 
            if num not in new_same: 
                new_same.append(num)    
        for j in range(len(new_same)):
            new_same[j] = list(new_same[j])
            
        if (len(new_same)!=0):
            for j in range(len(new_same)):
                print(new_same[j])
        else:
            print("Tidak ditemukan !")

    else: 
        return print("Parameter bukan array/list") 
 

findSame(["cat", "listen", "code", "act", "silent", "tac"])       

