import os
super_villians = {'Fiddler' : 'Isaac Brown',
'Captain Cold' : 'Leonard Snart'}
print(super_villians)

del super_villians['Captain Cold']
print(len(super_villians))
print(super_villians.get('Isaac Brown'))
