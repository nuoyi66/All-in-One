dic={'k1':"Alex",'k2':' aric',"k3":"Alex","k4":"Tony"}
for i in dic:
    d=dic[i].strip()
    if(d.startswith("a") or d.startswith("A") and d.endswith("c")):
        print("dic:"+d)