ik=""
while len(ik)!=11 or ik.isdigit()!=True:
    try:
        ik=input("Isikukood:")
    except ValueError:
        print("Viga andmetega!")
print("Isikukoodi analüüs:".center(50,"-"))
print("Esimene sümbol:")
ik_list=list(ik) #["4","7","6","1","0"..]
if int(ik_list[0]) not in [1,2,3,4,5,6]:
    print(ik_list[0]," - ei ole õige!")
else:
    print(ik_list[0]," - õige arv!")
    kuu=ik_list[3]+ik_list[4] #1+0=10
    kuu=int(kuu)
    if kuu>0 and kuu<13:
        print(ik_list[3],ik_list[4],"õiged andmed!")
    else:
        print(ik_list[3],ik_list[4],"ei ole õiged andmed!")
#aasta ik_list[1],ik_list[2]
#kuu ik_list[3],ik_list[4]
#paev ik_list[5],ik_list[6]
