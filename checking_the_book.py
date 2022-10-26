import os 
from datetime import datetime
import csv
from tabulate import tabulate

# Create a record for the checkbook
if os.path.exists('./transactions.csv') == True:
    with open('transactions.csv', 'r') as file:
        reader = csv.reader(file)
        
# If it doesn't exist, create the .csv        
else:
    with open('transactions.csv', 'w') as file:
        csvwriter = csv.writer(file, delimiter=',', quotechar='|')
        csvwriter.writerow(['Date', 'Description', 'Amount', 'Balance'])
        csvwriter.writerow(['0000-00-00', 'Initial Creation', '0', '0'])

# Will print when only when firstopened
print('\n\
~~~ Welcome to your checkbook! ~~~')

#https://stackoverflow.com/questions/3754620/what-does-while-true-mean-in-python
# Creating an indefinite loop
while True:
    print('\n\
1) View Current Balance\n\
2) Record a Withdrawal\n\
3) Record a Deposit\n\
4) View Historical Transactions\n\
5) Exit\n')

    q = input('What would you like to do? ')
    
# View Balance
    if q == '1':
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                balance = (row[-1])
        print('Your current balance is: $',balance)
        
# Record Withdrawal
    elif q == '2':
        description = input('Description: ')
        withdraw = input('Withdrawal Amount: ')
        while not withdraw.isdigit():
            print('That is not a number')
            withdraw = input('Withdrawal Amount: ')
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                balance = (row[-1])
        with open('transactions.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|')
            csvwriter.writerow([datetime.now().strftime('%Y-%m-%d'), description, '-' + withdraw, int(balance)-int(withdraw)])
            
# Record Deposit
    elif q == '3':
        description = input('Description: ')
        deposit = input('Deposit Amount: ')
        while not deposit.isdigit():
            print('That is not a number')
            deposit = input('Deposit Amount: ')
        with open('transactions.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                balance = (row[-1])
        with open('transactions.csv', 'a') as file:
            csvwriter = csv.writer(file, delimiter=',', quotechar='|')
            csvwriter.writerow([datetime.now().strftime('%Y-%m-%d'), description, deposit, int(balance)+int(deposit)])
            
# View previous transactions            
    elif q == '4':
            with open('transactions.csv', 'r') as file:
                reader = csv.reader(file)
                data = list(reader)
                print(tabulate(data))
# Quit        
    elif q == '5':
        break
# Wrong answer, bro        
    else:
        print('That is an incorrect entry')