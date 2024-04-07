st=[]
st.append({"name":"a","sex":"male"})

st.append({"name":"b","sex":"female"})

st[1]["age"]=23

for s in st:

    print(s["name"],s["sex"],s["age"])