#1
my_list = []
print(my_list)
#2
my_list = ['pop', 'remove', 'append', 'del', 'extend']
print(my_list)
#3
my_list = ['pop', 'remove', 'append', 'del', 'extend']
print(len(my_list))
#4
my_list = ['pop', 'remove', 'append', 'del', 'extend']
print(my_list[0])
print(my_list[2])
print(my_list[-1])
#5
mixed_data_types = ['Bekarys', 162, 'Separated','Tole Bi 42']
print(mixed_data_types)
#6,7,8,9,10,11,12
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(f'{it_companies[0]}-is first company, {it_companies[3]}-is middle and {it_companies[-1]}-is last company')
it_companies[-3] = 'Samsung'
print(it_companies)
it_companies.append('Black Rock')
print(it_companies)
it_companies.insert(4, 'Lenovo')
print(it_companies)
#13
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
x = it_companies[6].upper()
print(x)
#14
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('# '.join(it_companies))
#15
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Pepsi' in it_companies)
#16
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)
#17
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies = sorted(it_companies, reverse = True)
print(it_companies)
#18
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[:3])
#19
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[-3:])
#20
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies[2:4])
#21
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(0)
print(it_companies)
#22
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies[2:4]
print(it_companies)
#23
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.pop(-1)
print(it_companies)
#24
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)
#25
it_companies = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
del it_companies
#26,27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
full_stack = front_end.copy()
full_stack.insert(5, 'Python ' 'SQL')
print(full_stack)
#Exrcises 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
min_age = ages[0]
max_age = ages[-1]
range_age = max_age- min_age
Median_age = ages[4]
total_med_age = int(Median_age) //2
average_age = sum(ages) // len(ages)
min_compare_the_value = abs(min_age - average_age)
max_compare_the_value = abs(max_age - average_age)
print(f'''min age is - {min_age}, max age is - {max_age}. Median age {total_med_age}, average age {average_age},  
      range of the ages{range_age} сompare  of the min value {min_compare_the_value}, сompare  of the max value {max_compare_the_value}''')
#level 2
countries =  ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(countries[3])
countries_len = len(countries)
first_half = []
second_half = []
for i in range(countries_len):
    if i % 2 == 0:
        first_half.append(countries[i])
    else:
        second_half.append(countries[i])
print(first_half)
print(second_half)
countries =  ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country , second_country , third_country, *scandic_countries = countries
print(f'{first_country}, {second_country}, {third_country} and scandic_countries :{scandic_countries}')