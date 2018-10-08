def is_palindrome(n):

    ns = str(n)
    l = len(ns)
   
    point = l // 2
    if(l % 2 == 0):
        if ns[:point] == ns[point:]:
            return True
        else:
            return False
    else:
        if ns[:point] == ns[:point:-1]:
            return True
        else:
            return False

output = filter(is_palindrome,range(1,200))
print('1~200:',list(output))

