#question 1
lst = [30,75,9,97,50,-4,70,59]
print(max(lst))
lst.remove(min(lst))
print(lst)
lst.sort()
print(lst)
print(lst[3: ])
# question2
main_lst = [["python",3],[5,7.8],["python",11],["python",1]]
counter = 0
for python_item in main_lst:
    if 'python' in python_item:
        counter += python_item.count('python')
print(counter)
#question 3
my_lst = ["I","LOvE","GAZa","sKy","GEEKs"]
name = my_lst
name = " ".join(name)
print(name.title())
#question 4
my_lst = [12,3.8,"GSG",["sKy","zak"]]
my_lst1 = list([my_lst])
print(my_lst1)
#question 5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[4], my_lst[2] = my_lst[2], my_lst[4]
print(my_lst)
#question 6
nums = [33,5.9,6,-43,9,7,39,0,-40]
print(sum(nums))
#question 7

tuple1 = (4,'python','GSG',[8,3,1])
N_tuple = tuple1 + (9,)
print(N_tuple)
#question 8
tuple1 = 4,'python','GSG',[8,3,1]
tuple2 = 'java','c++',7.8
N_tuple = tuple1 + tuple2
print(N_tuple)







