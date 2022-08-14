def count(s, c) :
     
    # Count variable
    res = 0
     
    for i in range(len(s)) :
         
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res
        
     
# Driver code
str= input('given string:\n')
c = input('The character to be count: \n')
print(count(str, c))

