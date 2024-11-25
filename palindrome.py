def is_palindrome(s):
    
    s = ''.join(s.split()).lower()
   
    return s == s[::-1]


test_string = "A man a plan a canal Panama"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')