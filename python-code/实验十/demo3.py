f=open("score.txt","r",encoding="utf-8")
a=f.readlines()
name=[]
s=[]
Max=0
Min=100
i=0
for line in a:
    line=line.strip()
    line=line.split(' ')
    print(line)
    name.append(line[0])
    s.append(line[1])
    if int(s[i])>Max:
        Max=int(s[i])
        Max_i=i
    if int(s[i])<Min:
        Min=int(s[i])
        Min_i=i
    i += 1
print("最高分学生的姓名:",name[Max_i],"最高分为:",s[Max_i])
print("最低分学生的姓名:",name[Min_i],"最低分为:",s[Min_i])