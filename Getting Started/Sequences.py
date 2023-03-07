# set: An unordered collection of unique values
a = {1, 2, 'a', 1}
a.add(3)
#a.remove(8)
a.discard(8)
# remove a random element
a.pop()
#a.clear()
print(a)
print(type(a))


# list mutable
a = list(a)

print(a)
print(type(a))

a = {1: 'one',
     2: 'two'}
b = {'a': [1, 2, 3],
     'b': 'a string'}

print (b['a'])

# Indexes
names = ['Alice', 'Bob', 'Craig', 'Diana', 'Eric']
print(names[-1])
print(names[-4])

names.append("Sia")
names.insert(1,"Nikki")
names.remove("Bob")

print(names)

#reverse

names.reverse()
print(names[ ::-1])

#dict

state_capitals = {
    'Arkansas': 'Little Rock',
    'Colorado': 'Denver',
    'California': 'Sacramento',
    'Georgia': 'Atlanta'
}

for k in state_capitals.keys():
    print('{} is the capital of {}'.format(state_capitals[k], k))