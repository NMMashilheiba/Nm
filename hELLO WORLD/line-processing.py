def filterfile(oldfile, newfile):
    f1= open(oldfile,"r")
    f2= open(newfile,"w")
    while true:
        text = f1.readline()
        if text=="":
            break
        if text[0]=="#":
            continue
        f2.write(text)
        f1.close()
        f2.close()
        return
filterfile(oldfile, newfile)
f=open(newfile,"r")
print(f.read())