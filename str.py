# string capitalize 1
str_1="tharun ajith kumar"
print(str_1.capitalize())
print(str_1)
print("==========================")
#string title 2
str_2="tharun ajith kumar"
print(str_2.title())
print(str_2)
print("==========================")
#string istitle 3
str_3="Tharun  @123Ajith Kumar"
print(str_3.istitle())
str_4="Tharun ajith kumar"
print(str_4.istitle())
print("==========================")
#str center 4
str_5="python is for data science"
print(str_5.center(50,"*"))

print("==========================")
#str count 5
str_6="monty monty for python"
print(str_6.count('m',5,20))
print(str_6.count('o'))
print("==========================")
#str endwith 6
str_7="Python is a programming language that lets you work quickly and integrate systems more effectively.@"
#not a necessary of start and end
print(str_7.endswith('n',5,10))
print(str_7.endswith('@',5,100))
print(str_7.endswith('@'))
print(str_7.endswith('y'))
