# for i in range(1,11):
#   if i %2 ==0:
#     print('even',i)
#   else:
#     print('odd',i)

start= int(input("enter start number: "))
stop=int(input("enter stop number: "))

skip=int(input("enter skip number:  "))

for i in range(start, stop):
  if i == skip:
    print(i)