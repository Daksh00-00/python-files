#arranging string
def arrange(s):
    str_s=""
    str_c=""
    str_d=""
    
    for i in s:
        if i.islower()==True:
            str_s+=i
        elif i.isupper()==True:
            str_c+=i
        elif i.isdigit()==True:
            str_d+=i
    str_list=str_s+str_c+str_d
    return str_list
s=input("enter a string")
print()
print("The modified list is ",arrange(s))




             

