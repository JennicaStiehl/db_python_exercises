import os
import sys
grocery_list = ['banana', 'zucchini']

print('First Item', grocery_list[0])
grocery_list[0] = 'Green Juice'
print('First Item', grocery_list[0])
other_events = ['wash car', 'pick up dry cleaning']
to_do_list = [other_events, grocery_list]

grocery_list.append('onions')
print(to_do_list)
grocery_list.insert(1, 'pickles')
grocery_list.remove('pickles')
grocery_list.sort()
print(to_do_list)
