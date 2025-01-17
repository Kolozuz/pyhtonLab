my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
#

for i in range(len(my_list)-1):
    repeated = False
    print(i)
    print((((len(my_list)-1)-i)*-1))
    print(my_list)
    if my_list[i] in my_list[(((len(my_list)-1)-i)*-1):-2]:
        
        repeated = True
    
    if repeated:
        del my_list[i]
        

print("The list with unique elements only:")
print(my_list)
#print(my_list[0:])