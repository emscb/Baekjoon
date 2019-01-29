def isPalindrome(string):
    return string[::-1] == string

A = input()
a = isPalindrome(A)
if a:
    print(1)
else:
    print(0)

# Done
