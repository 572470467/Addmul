y=[]
def addmul(r,q):
    S1=[0,0,0,0]
    S2=[0,0,0,0,0,0,0]
    for i in range(len(r)):
        A1=r[i]
        Y=B1=S2[-1]
        A2=S1[-1]
        S1=[A1+B1,S1[0],S1[1],S1[2]]
        B2=q[i]
        S2=[A2*B2,S2[0],S2[1],S2[2],S2[3],S2[4],S2[5]]
        y.append(Y)
    return y
print(addmul([4,1,9,5,7,3,5,2,9,6,4,7,5,3,8,3,9,6,4,6,3,9,3,6,8,5,2,3,7,9],[3,2,4,5,6,7,8,2,6,4,1,4,8,9,4,2,6,2,8,4,3,2,7,5,8,9,7,6,4,5]))
