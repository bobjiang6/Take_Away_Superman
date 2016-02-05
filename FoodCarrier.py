import sys,random,copy

namelist = (sys.argv[1::])
scorelist=[]
resultlist=[]

def verse(verser):
    for sl in range(len(verser)):
        scorelist.append(0)
    for i in range(1000000):
        choice = random.choice(verser)
        for n in range(len(verser)):
            if choice == verser[n]:
                scorelist[n] += 1
    return(verser[scorelist.index(max(scorelist))])
       
def seperate(x):
    x2 = copy.deepcopy(x)
    sep_list=[]
    sep_flist=[]
    if len(x2) % 2 != 0:
        x2rmv=random.choice(x2)
        x2.remove(x2rmv)
        print("The lucky dog is:",x2rmv)
    while len(x2) > 0:
        sep_list.append(x2.pop(random.randint(0,len(x2)-1)))
        sep_list.append(x2.pop(random.randint(0,len(x2)-1)))
        sep_flist.append(sep_list)
        sep_list=[]
    return(sep_flist)

namelist = seperate(namelist)
print("Next battle groups:",namelist,"\n")

while len(namelist) >= 2:
    for vi in range(len(namelist)):
        resultlist.append(verse(namelist[vi]))
    print("Winners of thus round",resultlist,"\n")
    namelist = seperate(resultlist)
    print("Next battle groups:",namelist,"\n")
    resultlist=[]

print("Our final winner is:",verse(namelist[0]),"!")