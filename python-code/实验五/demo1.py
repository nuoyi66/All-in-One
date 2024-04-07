li=["alec","Aric","Alex","Tony","rain"]
tu=["alec","Aric","Alex","Tony","rain"]
dic={'k1':"Alex",'k2':"aric",'k3':"Alex",'k4':"Tony"}
for i in li:
    b=i.strip()
    if(b.startswith("a")or b.startswith("A")and b.endswith("c")):
        print("li:"+b)
for i2 in tu:
    c=i2.strip()
    if(c.startswith("a")or c.startswith("A")and c.endswith("c")):
        print("tu:"+c)
