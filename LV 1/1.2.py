#2
print('Unesi broj od 0.0 do 1.0:')
my_str = input()
try:
  my_num = float(my_str)
except ValueError:
    #my_num = float(my_str)
    print('nije unijet cijeli broj') 

try:
    if 1<=my_num>=0:
        print("dobro je")
except:
    print("nije izemdju 0 i 1")


print(my_num) #  -2468


if (my_num >= 0.9):
    print("A")
elif (my_num >= 0.8):
    print("b")
elif (my_num >= 0.7):
    print("c")
elif (my_num >= 0.6):
    print("d")
elif (my_num <= 0.6):
    print("f")