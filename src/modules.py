# import custom class (as module) that we created before
# and use it
from my_classes import MyAge


age = MyAge('1927-04-22', 'Mr. Henry')
print(age.show_me_my_age())
