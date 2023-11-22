#1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: 
# You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_age = int(input('Enter your age'))
left_ages = 18 - user_age
if user_age == 0:
    print('Error')
else:
    if user_age == 18:
        print('You are old enough to drive.')
    else:
        print(f'wait for {left_ages} years.')
# 2nd version
user_age = int(input('Enter your age'))
if user_age > 0 and user_age >= 18:
    print('You are old enough to drive.')
elif user_age > 0 and user_age < 18:
    print(f'You need {18 - user_age} years to learn to drive')
else:
    print('Age should be greater than zero')
#2
# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age =  11
print('Hello I\'m 11 years old. How about you?')
your_age = int(input("Enter your age: "))
if my_age > your_age:
    print(f"I\'m older than you over {my_age - your_age} years")
elif my_age < your_age:
    print(f'You\'re older than me over {your_age - my_age} years')
else:
    print('We\'re both the same year')
#3 Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
if a > b and  b < a:
    print(f'{a} is greater than {b}')
elif b >a and a < b:
    print(f'{b} is greater than {a}')
else:
    print(f'{a}is equal to{b}')
### Exercises: Level 2
#1 Write a code which gives grade to students according to theirs scores:
A = 80-100
B = 70-89
C = 60-69
D = 50-59 
F = 0-49
user_grade = int(input('How many scores are you get?'))
if user_grade >= 80 and user_grade <= 100:
    print('You get grade A')
elif user_grade >= 70 and user_grade <= 79:
    print('You get grade B')
elif user_grade >= 60 and user_grade <= 69:
    print('You get grade C')
elif user_grade >= 50 and user_grade <= 59:
    print('You get grade D')
else:
    print('You get grade F')
#2
user_mounth = input('Please enter three mounth: ').split(' ')
if user_mounth is 'September' or 'October' or 'November':
    print('the season is Autumn')
elif user_mounth is 'December' or 'January' or 'February':
    print('the season is Winter')
elif user_mounth is 'March' or 'April' or 'May':
    print('the season is Spring')
elif user_mounth is'June' or 'July' or 'August':
    print('the season is Summer')
else:
    print('Error')
#3 If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruits = input('Enter your fruits')
if user_fruits not in fruits :
    fruits.append(user_fruits)
    print(fruits)
else:
    print('That fruit already exist in the list')
#4
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#4.1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
check_item = 'skills' in person
len_skills = len(person['skills']) % 2
if check_item is True:
    if len_skills == 1:
        print(person['skills'][2])
    else:
        print('Who am I?')
else:
    print('Not in')

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
person_keys = person.keys()
if 'skills' in person_keys:
    if 'Python' in person['skills']:
        print('it has')

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if len(person['skills']) == 2:
    if 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print('He is a front end developer')
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
    print('He is a backend developer')
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB'in person['skills']:
    print('He is a fullstack developer')
else:
    print('unknown title')

#  * If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person['is_marred'] == True and 'Finland' in person['country']:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')
else:
    print('Who am I?')