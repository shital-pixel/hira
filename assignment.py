# 1. Indexing and Slicing
#    Given the string s = "PythonPractice", what are the outputs of:
#    - s[1]
#    - s[-3:]
#    - s[2:7]
s = "pythonPractice"
print(s[1])
print(s[-3:])
print(s[2:7])



# 2. Reverse a String
#    Write a one-liner to reverse the string "developer" using slicing.
st= "developer"
print(st[::-1])



# 3. Count Vowels
#    Write a function that counts the number of vowels in a given string.
def vowel_letters(st):
    vowels ="aeiouAEIOU"
    count =0
    for char in st:
        if char in vowels:
            count +=1
    return count

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels(st))


# 4. Check for Palindrome
#    Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

# def palindrome_function(text):
#     cleaned = text.replace(" ", "").lower()
#     reversed = cleaned[::-1]


#     if cleaned == reversed:
#         return True
#     else:
#         return False
# print(palindrome_function("Madam"))               




# 5. Clean and Format String
#    Given text = "   hello world! welcome to Python.   ", write code to:
#    - Remove leading/trailing spaces
#    - Capitalize each word
#    - Replace the word "Python" with "Programming"

text1="   hello world! welcome to Python.   "
removed=text1.strip()
capital=removed.title()
replaced=capital.replace("Python","Programming")
print(replaced)


# 6. Find Longest Word
#    Write a function that takes a sentence and returns the longest word in it.
def longest_word(sentence):
    words = sentence.split()  # Split sentence into words
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
print(longest_word("What is yout nameeeeeee"))

# 7. String Operators
#    Given s1 = "Py" and s2 = "thon", what are the results of:
#    - s1 + s2
#    - s1 * 3
#    - "y" in s1

s1 = "py"
s2= "thon"

sum = s1 + s2
mul = s1 * 3
result="y" in s1

print(sum)
print(mul)
print(result)




#  8. Remove Duplicate Characters
#    Write a function that removes all duplicate characters from a string but keeps the first occurrence.
def remove_duplicates(s):
    result = ""
    seen = set()

    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result


print(remove_duplicates("programming"))  




# 9. Check for Anagram
#    Write a function that returns True if two strings are anagrams of each other.

def is_anagram(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    
    return sorted(str1) == sorted(str2)


print(is_anagram("evil", "vile"))  

#
#



# 10. Word Frequency Counter
#     Write a function that takes a sentence and returns a dictionary of word frequencies.
def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

word_frequency_result = word_frequency("this is an apple and this is a orange")
print(word_frequency_result)