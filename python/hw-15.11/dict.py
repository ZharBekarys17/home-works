#1Create an empty dictionary called dog
dog = dict()
#2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Barys'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = '4 mounth'
print(dog)
#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = dict()
student['first_name']= ['Aidar']
student['last_name'] = ['Spargaly']
student['gender'] = ['male']
student['age'] = [16]
student['martial_status'] = ['not bad']
student['skills'] = ['smart', 'strong', 'fast']
student['country'] = ['Kazakhstan']
student['city'] = ['Almaty']
student['address'] = ['Tole Bi 19']
print(student)
# 4. Get the length of the student dictionary
print(len(student))
# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
values = student.values()
print(values)
# 6. Modify the skills values by adding one or two skills
student['skills']= 'wise', 'quite'
print(student['skills'])
# 7. Get the dictionary keys as a list
print(student.keys())
# 8. Get the dictionary values as a list
print(student.values())
# 9. Change the dictionary to a list of tuples using items() method
print(student.items())
# 10. Delete one of the items in the dictionary
print(student.pop('martial_status'))
# 11. Delete one of the dictionaries
del student ['gender']
print(student)