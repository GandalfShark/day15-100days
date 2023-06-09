"""
coffee machine simulator, day 15, 100 days of python

approach to problem:
holds values of milk ml, water ml, coffee g  and recipes- DONE
print report -DONE
check the resources against recipe -DONE
give back money if not enough resources -DONE
process coins and calculate value - DONE
and give change - # of coins -DONE
check the resources against recipe -DONE
subtract the recipie values from the storage values - DONE
TODO - fix bugs: not enough money still lets you "buy" a coffee
"""
from time import sleep
print('''
___________________________________
Welcome to the fake coffee machine!
                                                            
       ██    ██    ██                                    
     ██       ██  ██                                      
       ██    ██    ██                                      
        ██  ██      ██                                    
       ██    ██    ██                                    
                                                                                        
  ████████████████████                                  
  ██                ██████                              
  ██                ██  ██                              
  ██                ██  ██                              
   ██              ██████                              
    ██            ██                                    
████████████████████████                                
██                    ██                                
  ████████████████████   
___________________________________
''')
recipie = [{'name': 'espresso', 'water': 50, 'milk': 0, 'coffee': 18, 'price': 1.25},
           {'name': 'latte', 'water': 200, 'milk': 150, 'coffee': 24, 'price': 2.25},
           {'name': 'cappuccino', 'water': 50, 'milk': 0, 'coffee': 18, 'price': 1.85}]

storage = {'water': 300, 'milk': 200, 'coffee': 100}
options = []
# blank list used to create a list of options from recipe
coin_values = {'quarters': 0.25, 'dimes': 0.10, 'nickels': 0.05 }
bank = 0

def resource_report():
    """prints the total resources in machine """
    print(f"There is {storage['water']}ml of water.")
    print(f"There is {storage['milk']}ml of milk.")
    print(f"There is {storage['coffee']}g of coffee.")
    print('---------------------------------------')
    print(f'The machine has made: ${bank:.2f} so far.')


def how_much_is_coin_worth(coin_name = 'nickels', coin_number=2):
    """ takes the name of coin and number as input returns value as float"""
    return coin_values[coin_name]*coin_number


def total_value_of_coins_inserted():
    """take input from the user and return the total value of coins """
    q = int(input('how many quarters: '))
    qval = how_much_is_coin_worth('quarters', q)
    d = int(input('how many dimes: '))
    dval = how_much_is_coin_worth('dimes', d)
    n = int(input('how many nickels: '))
    nval = how_much_is_coin_worth('nickels', n)
    return qval+dval+nval


def can_buy(money):
    """checks money to see what customer can buy """
    afordable_drinks = []
    for index in range(len(recipie)):
        if recipie[index]['price'] <= money:
            afordable_drinks.append(f"{recipie[index]['name']}")
    return afordable_drinks


def give_change(drink_name, money_in):
    global bank
    """ checks drink names and subtracts price from money in"""
    for num in range(len(recipie)):
        if recipie[num]['name'] == drink_name:
            money_out = money_in - recipie[num]['price']
            bank += recipie[num]['price']
            print(f'Buying a {drink_name} gives you ${money_out:.2f} back.')
    coin_combo(money_out)
    print('coins returned\nENJOY YOUR PRETEND COFFEE!')


def coin_combo(change_to_be_given):
    """takes in total value of change to de given prints out coin values back """
    quarters_out = 0
    dimes_out = 0
    nickles_out = 0
    if change_to_be_given >= 0.25:
        while change_to_be_given >= 0.25:
            quarters_out += 1
            change_to_be_given -= 0.25
            # TEST PRINTS BELOW
            # print(quarters_out, 'Qs')
            # print(change_to_be_given, 'total $ stored')
    change_to_be_given += 0.01
    # compensate for binary math by adding to the 0.09999999999999998 value generated by a single dime
    if change_to_be_given >= 0.10:
        while change_to_be_given >= 0.10:
            dimes_out += 1
            change_to_be_given -= 0.10
            # TEST PRINTS BELOW
            # print(dimes_out, 'Ds')
            # print(change_to_be_given, 'total $ stored')
    if change_to_be_given >= 0.05:
        while change_to_be_given >= 0.05:
            nickles_out += 1
            change_to_be_given -= 0.05
            # TEST PRINTS BELOW
            # print(nickles_out, 'Ns')
            # print(change_to_be_given, 'total $ stored')
    sleep(1)
    print(f'You get: {quarters_out} Quarters back.')
    print(f'You get: {dimes_out} Dimes back.')
    print(f'You get: {nickles_out} Nickles back.')


def remove_resources(name_of_drink):
    print('\n Starting:')
    # resource_report()
    for num in range(len(recipie)):
        if recipie[num]['name'] == name_of_drink:
            storage['water'] -= recipie[num]['water']
            storage['milk'] -= recipie[num]['milk']
            storage['coffee'] -= recipie[num]['coffee']
    print('COMPLETE:')
    # resource_report()


def check_resource_against_recipie(drink_recipie_to_check):
    """Returns true or false based on storage levels compared to drink recipie"""
    for num in range(len(recipie)):
        if recipie[num]['name'] == drink_recipie_to_check:
            if storage['water'] < recipie[num]['water']:
                print('checking water')
                return False
            if storage['milk'] < recipie[num]['milk']:
                return False
            if storage['coffee'] < recipie[num]['coffee']:
                return False
            else:
                return True

while True:
    # main section #
    customer_money = total_value_of_coins_inserted()
    print(f'You have inserted ${customer_money:.2f}\n')

    for n in range(len(recipie)):
        print(recipie[n]['name'], end=' ')
        print('$', recipie[n]['price'], end=' ')

    print('\nYou have enough money for:')
    options = can_buy(customer_money)
    print(options)
    options.append('report')

    coffee_choice = input(f"\nWhat coffee would you like?")
    if coffee_choice == 'report':
        resource_report()
        # options.remove('report')
        # clears the entire list for some reason

    while coffee_choice not in options:
        print(f'Your options are: {options}')
        coffee_choice = input(f"\nPick a coffee: ")

    # make sure coffee can be made if not return money
    if check_resource_against_recipie(coffee_choice):
        remove_resources(coffee_choice)
        print('')
        give_change(coffee_choice, customer_money)
    else:
        print('\nSorry not enough resources to make your drink')
        print('Here is your money back')
        coin_combo(customer_money)

    more = input('more coffee?').lower().strip()
    if more == 'yes':
        continue
    if more == 'no':
        print('fine be that way')
        break
    else:
        print('INVALID INPUT!!!\n I will explode now. ')
        break

print('\n\n That\'s All Folks!')
