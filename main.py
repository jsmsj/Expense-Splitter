# bill splitter | jsmsj

class Person:
    def __init__(self,name) -> None:
        self.name = name
        self.total_paid = 0
        self.balance = 0


num = int(input('Enter the number of people: '))
print('Enter name followed by amount, separated by a space " " : ')
pers = []

for i in range(1,num+1):
    name,amt = input().split(' ')
    p = Person(name)
    p.total_paid = int(amt)
    pers.append(p)

avg = int(sum([i.total_paid for i in pers]))/len(pers)

balance = []


# take = +ve
# give = -ve

for i in pers:
    i.balance = int(i.total_paid - avg)
    balance.append(i.balance)

lowers = [  ]
for i in balance:
    if i < 0:
        aadmi = pers[balance.index(i)]
        lowers.append(aadmi)
        aadmi.balance =   i

uppers = [  ]
for i in balance:
    if i > 0:
        aadmi = pers[balance.index(i)]
        uppers.append(aadmi)
        aadmi.balance =  i



delta = {i:int(abs(i.total_paid-avg)) for i in lowers}
delta_2 = {}

for person,to_give in delta.items():
    for p2 in uppers:

        if p2.balance >=0 and to_give!=0:
            if p2.balance >= to_give:
                print(f'{person.name} gives {to_give} to {p2.name}')
                p2.balance= int(p2.balance-to_give)
                to_give = 0
            elif p2.balance < to_give:
                print(f'{person.name} gives {p2.balance} to {p2.name}')
                t = p2.balance
                p2.balance=int(p2.balance-to_give)
                to_give=int(to_give-t)
            delta_2.update({person:to_give})