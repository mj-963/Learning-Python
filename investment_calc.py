money = eval(input("Enter amount to invest (#): "))

interest = eval(input("Enter interest rate (%): "))

Years = eval(input("Enter number of years to invest: "))

money = float(money)
interest = float(interest) * 0.1

for i in range(Years):
    money = money + (money * interest) 

print(f'investment after {Years} is {money:.2f}')


interestAmount = money * interest * Years
print(f'Interest Amount{interestAmount:.2f}')
