#question 1 , 2
Name = "Lama"
Age = 20
street = 159
City = "Gaza"
country = "Palestine"
Address = (f"{street} , {City} , {country}")
print(f"Name : {Name}\nAge : {Age}\nAddress : {Address}")
#question 3
Name = "Lama"
Age = "15"
Street = "159"
City = "Gaza"
Country = "Palestine"
Address = (f"{Street} , {City} , {Country}")
print(f'Hello {Name} Your age isِ {Age} Years old, Your Address is {Address}')
#question 4
print(type(Name))
print(type(Age))
print(type(Street))
print(type(City))
print(type(Country))
# question 5
Name = "Lama"
Age = 15
Country = "Palestine"
print(f'Hello {Name} , How are you? \ """ Your Age Is "{Age}"" + And Youre Country Is: {Country}')
#question 6
City = "Gaza"
print(f'Hello {Name} , How are you? \ \n """ Your Age Is "{Age}"" + And\n Youre City Is: {City}')
#question 7 , 8
name = "ITF Gsg Python"
print(f'First Letter Is  "{name [0]}"')
print(f'Third Letter Is  "{name [2]}"')
print(f'Last Letter Is  "{name [-1]}"')
print(name[11: ])
print(name[ :3])
print(name[ :7:2])
print(name[13:7:-1])
#question 9
name = "$&$&Mohammed$&$&"
print(name.strip('$&'))
#question 10
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7", "Love"))
#question 11
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = ("87190")
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
#question 13
name = "ahmed talal"
print(name.title())
print(name.capitalize())
#question 14
first_name = 'Dana'
output='*'*11+first_name+'*'*11
print(output.rstrip('*'))
print(output)
print(output.lstrip('*'))
print(first_name)
#question 15 , 16
name_one = "SaMER"
name_tow = "Abed"
print(name_one.swapcase())
print(name_tow.swapcase())
print(name_one.lower())
print(name_tow.upper())
print(name_one.isupper())
print(name_tow.islower())
#question  17

print(name_one.startswith('S'))
print(name_tow.endswith('HD'))
#question 18
msg = "I Love Python And Although I Love GSG with Zakaria"
print(f'Number of <Love> is:{msg.count("Love")}')
print(f'Number of <t> is: {msg.count("t")}')
# question 19
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love",1))
#question 20
test1 = "zakzak"
test2 = "zakaria"
test3 = "A war at Tarawa"
test4 = "madam"

string = test1
mid = int(len(string) / 2)
first_str = string[:]
second_str = string[:]

# symmetric
if first_str == second_str:
	print(string, ' is symmetrical')
else:
	print(string, ' is NOT symmetrical')

# palindrome
if first_str == second_str[::-1]:
	print(string, ' is palindrome')
else:
	print(string, ' is NOT a palindrome')




