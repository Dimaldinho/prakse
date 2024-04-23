import pyinputplus as pyip

price = {'wheat': 1,'white': 1,'sourdough': 1,
    'chicken': 2,'turkey': 2,'ham': 2,'tofu': 1,
    'cheddar': 3,'Swiss': 3,'mozzarella': 3,
    'mayo': 1
} 


def sandwichPreferences():
    cheese_type = None
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Bread type: \n')
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Protein type: \n')
    cheese = pyip.inputYesNo('Cheese? (yes/no): \n')
    
    if cheese == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='Select a cheese type: \n')

    mayo = pyip.inputYesNo('Want mayo, mustard, lettuce, or tomato? (yes/no): \n')
    howMany = pyip.inputInt('How many sandwiches? \n', min=1)
    #print(mayo)
    return bread, protein, cheese_type, mayo, howMany

def cost(bread, protein, cheese_type, mayo, howMany):
    total_cost = 0

    
    total_cost += price[bread]
    total_cost += price[protein]

    if cheese_type != None:
        total_cost += price[cheese_type]

    if mayo == 'yes':
        total_cost += price['mayo']

    return total_cost*howMany

def main():
    bread, protein, cheese_type, mayo, howMany = sandwichPreferences()
    total_cost = cost(bread, protein, cheese_type, mayo, howMany)
    print("Your total cost for %s sandwich is: $%s" %(howMany,total_cost))


main()