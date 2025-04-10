str = input()
new_str =""
for i in str:
    if i.isupper():
        i=i.lower()
        new_str+=i
    else:
        i=i.upper()
        new_str+=i
# new_str=str(new_str)
print(new_str)
    
