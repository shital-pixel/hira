# Takes a secret word as input (without spaces).
# Then encodes the word using a custom cipher:
# Replace all vowels with *
# Reverse the entires string
# Then shift each letter 2 places ahead in the alphabet (wrap around if needed,e.g,y->a,z->b)
# Finally print the resulting encoded word.

def encode_word(word):
    vowels = "aeiouAEIOU"
  
    replaced = ''.join('+' if ch in vowels else ch for ch in word)
   
    reversed_str = replaced[::-1]
    
    result = []
    for ch in reversed_str:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            shifted = chr(base + (ord(ch) - base + 2) % 26)
            result.append(shifted)
        else:
            result.append(ch)
    
    encoded_word = ''.join(result)
    print(encoded_word)


secret_word = input("Enter the secret word (no spaces): ")
encode_word(secret_word)