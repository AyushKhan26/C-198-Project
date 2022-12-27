print('Choose any item or vegetables')
print('1.Potato')
print('2.Tomato')
print('3.Cauliflower')

Total = 0
while True:
    customer_name = input('Enter Customer Name:-  ')
    while True:
      item =input('Enter the item:- ')
      Quantity = input('Enter Quantity of item(Kg):- ')
   
      if item == 'Potato':
         Total = Quantity*20
      elif item == 'Tomato':
         Total = Quantity*10
      elif item == 'Cauliflower':
         item_no = input('Enter no of item:- ')
         Total = item_no*25
       

      new_customer=('Is there A new customer?(y/Y/n/N):- ')
      if new_customer == 'n' or new_customer == 'N':
         break      
    print('Food Market')
    print('_'*50)
    print('Customer Name:- ',customer_name)
    print('Total',Total)
    print('*'*10)