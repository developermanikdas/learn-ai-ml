#1 Is Palindrome

text = input("Enter a string to check Palindrome: ")

start = 0
end = len(text)-1
is_palindrome = True

while start < end:
    if text[start] != text[end]:
        is_palindrome = False
    start+=1
    end-=1       

print(is_palindrome)    