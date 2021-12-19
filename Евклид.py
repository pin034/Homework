cha,chb,nod,n=[0]*5,[0]*5,[0]*5,[0]*5
for i in range(5):
    a,b = map(int,input("").split())
    cha[i]=a
    chb[i]=b
    c=0
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
        c+=1
    nod[i]=a
    n[i]=c
print("a        ",cha[0],cha[1],cha[2],cha[3],cha[4])
print("b        ",chb[0],chb[1],chb[2],chb[3],chb[4])
print("НОД(a,b) ",nod[0],nod[1],nod[2],nod[3],nod[4])
print("Шагов    ",n[0],n[1],n[2],n[3],n[4])
