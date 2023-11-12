# . Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
# . Add 'Twitter' to it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(it_companies.add('Twitter'))
# . Insert multiple IT companies at once to the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
new_it_companies = {'Apple', 'Samsung','OnePlus'}
it_companies.update(new_it_companies)
print(it_companies)
# . Remove one of the companies from the set it_companies
it_companies = {'Apple', 'Amazon', 'OnePlus', 'Facebook', 'IBM', 'Google', 'Microsoft', 'Oracle', 'Samsung'}
it_companies.remove('Apple')
print(it_companies)
# . What is the difference between remove and discard
# discard will be work if the specified element is not in set remove doesn't work in this way

# Exercises: Level 2
# . Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
# . Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))
# . Is A subset of B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.issubset(B))
# . Are A and B disjoint sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.isdisjoint(B))
# . Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
D = B.union(A)
print(C)
print(D)
# . What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.symmetric_difference(B))
# 7. Delete the sets completely
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del A, B
# Exercises: Level 3
# . Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages= set(age)
print(ages)
if len(age) >=len(ages):
    print(f'{len(age)}is bigger than {len(ages)}')
else:
    print(f'{len(ages)}is bigger than {len(age)}')
# . Explain the difference between the following data types: string, list, tuple and set
    # list is oredered and changeable also it has square brackets []
    # tuple is ordered and unchangeable it has normal brackets ()
    # set is unordered and it has unige elements it has curly bracket {}
    # string is ordered and unchangeable it has quotation marks ''
# . I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
text = 'I am a teacher and I love to inspire and teach people.'
splitted_text =  text.split()
splitted_text = set(splitted_text)
splitted_text = len(splitted_text)
print(f'{splitted_text} - the len of unique words in text')