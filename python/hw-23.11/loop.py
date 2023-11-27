# count = 0
# while count != 10:
#     if count % 2 !=0:
#         count +=1
#         continue
#     print(count)
#     count+=1


# while count != 10:
#     if count % 2 !=1:
#         count +=1
#         continue
#     print(count, end=', ')
#     count+=1

# for i in range(0,10):
#     if i % 2 ==0:
#         print(i)
# while count < 10:
#     if count == 5:
#         count = count + 1
#         continue
#     elif count == 8:
#         print(count)
#         break
#     print(count)
#     count = count + 1
    
# person = {
#     'first_name':'Asabeneh',
#     'last_name':'Yetayeh',
#     'age':250,
#     'country':'Finland',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Space street',
#         'zipcode':'02210'
#     }
# }
# for i in person:
#     if i == "skill":
#         for j in person[i]:
#             print(j)
        
# # Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(0,11):
    print(i, end=', ')

count = 0
while count != 11:
    print(count)
    count +=1

# #Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(0, 11):
    for j in range(i, -1, -1):
        print(j ,end =' ')

count = 11
while count != 0:
    print(count)
    count -=1

#  

#Use nested loops to create the following:
person = {
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
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
        
nested_loops = {
    'first_loop' : [' 1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'second_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'third_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'fourth_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'fifth_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'sixth_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'seventh_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
    'eighth_loop' : ['1', '2', '3', '4', '5', '6', '7', '8 \n'],
}
for key in nested_loops:
    if key == 'first_loop':
        for loop in nested_loops['first_loop']:
            print(loop, end=' ')
    elif key == 'second_loop':
        for loop in nested_loops['second_loop']:
            print(loop, end=' ')
    elif key == 'third_loop':
        for loop in nested_loops['third_loop']:
            print(loop, end=' ')
    elif key == 'fourth_loop':
        for loop in nested_loops['fourth_loop']:
            print(loop, end=' ')
    elif key == 'fifth_loop':
        for loop in nested_loops['fifth_loop']:
            print(loop, end=' ')
    elif key == 'sixth_loop':
        for loop in nested_loops['sixth_loop']:
            print(loop, end=' ')
    elif key == 'seventh_loop':
        for loop in nested_loops['seventh_loop']:
            print(loop, end=' ')
    elif key == 'eighth_loop':
        for loop in nested_loops['eighth_loop']:
            print(loop, end=' ')

# #Print the following pattern:
num = 0
for i in range(11):
    print(f'{i} x {i} = {i * i}')
    i += 1

#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
My_loop = {
    'length' : 6,
    'IT_languages' : ['Python', 'Numpy','Pandas','Django', 'Flask']
}
for key in My_loop:
    if key is 'IT_languages':
        for keys in My_loop['IT_languages']:
            print(keys, end = ', ')

# #Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i, end= (' '))

# #Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 == 1:
        print(i, end= (' '))  

# #Exercises: Level 2
# #Use for loop to iterate from 0 to 100 and print the sum of all numbers.
k =1
for i in range(101):
    k += i
print(f'The sum of all numbers is {k}')

# #Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
p = 0
j = 0
for i in range(101):
    if i % 2== 0:
        p += i
    
    elif i % 2 == 1:
        j += i
print(f'The sum of all evens is{p}. And the sum of all odds is {j}')

# #Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
for i in countries:
    if 'land' in i:
        print(i)

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
rev_fruits = []
for i in fruits:
    rev_fruits = [i] + rev_fruits
print(rev_fruits)

