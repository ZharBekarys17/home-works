# 1. Create an empty tuple
any = tuple()
print(any)
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
homies = ('Balausa', 'Bahtyar')
print(homies)
# 3. Join brothers and sisters tuples and assign it to siblings
brothers = ('Bahtyar', 'Dastan')
sisters = ('Balausa', 'Maryam', 'Diana', 'Zhadyra')
siblings = brothers + sisters
print(siblings)
# 4. How many siblings do you have?
print(f'I have {len(siblings)} - siblings')
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('Serik', 'Zhuldyz',)
print(family_members)
# 1. Unpack siblings and parents from family_members
family_members= ('Bahtyar', 'Dastan', 'Balausa', 'Maryam', 'Diana', 'Zhadyra', 'Serik', 'Zhuldyz')
*siblings , parent1, parent2 = family_members
print(f'{siblings} are my siblings')
print(f'{parent1, parent2} are my parents')
# 1. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# 1. Change the about food_stuff_tp  tuple to a food_stuff_lt list
# 1. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# 1. Slice out the first three items and the last three items from food_staff_lt list
# 1. Delete the food_staff_tp tuple completely
# 1. Check if an item exists in  tuple:
fruits = ('Avocado', 'Banana', 'Coconut')
vegetables = ('Burdock Roots' ,'Broccoli' , 'Cabbage')
animal_products = ('Leather', 'Horne', 'Silk')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_tp=('Avocado', 'Banana', 'Coconut', 'Burdock Roots', 'Broccoli', 'Cabbage', 'Leather', 'Horne', 'Silk')
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[4])
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
del food_stuff_tp
print(food_stuff_lt)


# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' not in nordic_countries:
    print('Estonia not in nordic_countries')
elif 'Iceland' not in nordic_countries:
    print('Iceland not in nordic_countries')