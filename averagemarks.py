st_name=(input("enter a name of student"))
st_rollno=int(input("enter a student roll no"))
phy=int(input("enter a marks of physics"))
chem=int(input("enter a marks of chemistry"))
bio=int(input("enter a marks of biology"))

avg=(phy+bio+chem)/3

print("the average of 3 subjects ",phy,chem,bio,"=",avg)