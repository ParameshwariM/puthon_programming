sentence=raw_input("")
count=0
for i in sentence:
    if(i.isdigit()):
        count=count+1
print(count)
