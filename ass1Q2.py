values=[]
for i in range(5):
    value=int(input("Enter the number"))
    values.append(value)
    
if(len(values)!= len(set(values))):
 print("Duplicates")
else:
 print("All Unique!")
    
