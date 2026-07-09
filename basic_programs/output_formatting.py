names = ['Guru', 'Mahesh', 'Shrikanth', 'Usha']
locations = ['Mysuru', 'Chikkaballapura', 'Nelamangala', 'Mandya']

print('-' * 40)
print('%-2s %-15s %s'%('ID', 'NAME', 'LOCATION'))
print('-' * 40)
for i in range(1, len(names)+1):
    print('%-2d %15.3s %s'%(i, names[i-1], locations[i-1]))
print('-' * 40)
