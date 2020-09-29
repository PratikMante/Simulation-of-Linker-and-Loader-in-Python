f=open("prawns.c","r")
f1=open("emp.c","r")
f2=open("variable.txt","w")
local=list()
extern=list()
address=1000
address1=2000
for line in f:
    words=line.split()
    if "int" in words and "extern" not in words:
        
       
        for ele in words:
            if ele == "int":
                continue
            if ele != ";":
             if ele!=",":
                local.append(ele)
                local.append(str(4))
                address=address+4
                local.append(str(address))
             
    if "float" in words and "extern" not in words:
        for ele in words:
            if ele == "float":
                continue
            if ele != ";":
             if ele!=",":
                local.append(ele)
                local.append(str(4))
                address=address+4
                local.append(str(address))
    if "char" in words and "extern" not in words:
        for ele in words:
            if ele == "char":
                continue
            if ele != ";":
             if ele!=",":
                local.append(ele)
                local.append(str(1))
                address=address+1
                local.append(str(address))
            
f.seek(0)
for line in f:
    words=line.split()
    print("hi")
    if "extern" in words:
        print("hello")
        for ele in  words:
            if ele == "int":
                x=4 
                continue
            elif ele == "float":
                x=4 
                continue
            elif ele == "char":
                x=1
                continue
            print("yolo")
            if ele != ";":
             print("123")
             if ele!=",":
                print("456") 
                f1.seek(0)
                for line1 in f1:
                    words1=line1.split()
                    for ele1 in words1:
                        if "int" == ele1:
                            
                        
                            print("tuv")
                            continue
                        if ele in words1:
                                print("ccc")
                                extern.append(ele)
                                extern.append(str(x))
                                address1=address1+x
                                extern.append(str(address1))
                                break
    
i=0 
f2.write("Local :\n")
f2.write("Sym Size Address\n")
while i < len(local):
    f2.write(" "+local[i]+"    "+local[i+1]+"     "+local[i+2]+"\n")
    i=i+3 
f2.write("Extern :\n")
f2.write("Sym Size Address\n")
i=0 
while i < len(extern):
    f2.write(" "+extern[i]+"    "+extern[i+1]+"     "+extern[i+2]+"\n")
    i=i+3 