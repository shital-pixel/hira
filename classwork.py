# writr a program to detect double spaces in a string.
text = input ("enter a string ")
if " " in text:
    print("double space detected")
else:
    print("No double space found")



# write a program to format the following letter using escape sequence character
#letter ="Dear Students, This python course is going well . Thank you"
letter = "Dear Students,\nThis python course is going well.\nThank you"
print(letter)

#write a program to detect double space in a string
text = input ("enter a string ")
if " " in text:
    print("double space detected")
else:
    print("No double space found")



#replace the double space from problem 3 with single spaces

text=input("enter a string")
fixed_text=text.replace(" "," ")
print("fixed string:",fixed_text)
