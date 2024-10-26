# Enter your code here. Read input from STDIN. Print output to STDOUT
while True:
    try:
        
        input_data=input().rstrip()
    except EOFError:
        break
    
    op=input_data[0]
    
    ot=input_data[2]
    
    string_Data=list(input_data[4:])
    
    if op=="S":
        temp=""
        if ot=="M":
            for i in string_Data[:-2]:
                
                if i.islower():
                    
                    temp+=i
                else:
                    temp+=f' {i.lower()}'
            print(temp)
        elif ot=="C":
            temp+=string_Data[0].lower()
            for i in string_Data[1:]:
                
                if i.islower():
                    
                    temp+=i
                else:
                    temp+=f' {i.lower()}'
            print(temp)
        elif ot=="V":
            for i in string_Data:
                
                if i.islower():
                    
                    temp+=i
                else:
                    temp+=f' {i.lower()}'
            print(temp)
    if op=="C":
        temp=string_Data.copy()
        for i in range(len(string_Data)):
            if string_Data[i]==" ":
                temp[i+1]=temp[i+1].upper()
        if ot=="M":
            temp="".join(temp)
            temp=temp.replace(" ","")
            print(temp + "()")
        elif ot=="C":
            temp[0]=temp[0].upper()
            temp="".join(temp)
            print(temp.replace(" ",""))
        elif ot=="V":
             temp="".join(temp)
             print(temp.replace(" ",""))
    