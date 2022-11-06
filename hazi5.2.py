word = input("Adjon meg egy szót: ")

def isPalindrome(s):
    return s == s[::-1]

palindrome = isPalindrome(word)

if palindrome:
    print("A szó palindrom.")
else:
    print("A szó nem palindrom.")