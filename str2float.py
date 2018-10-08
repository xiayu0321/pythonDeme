from functools import reduce
Digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

def str2float(s):
    def fc(x,y):
        return x * 10 + y
    def char2num(s):
        return Digits[s]

    pointIndex = s.find('.')

    if pointIndex != -1:
        sx = 10 ** (len(s) - pointIndex - 1)

        s = s[:pointIndex] + s[pointIndex+1:]
        print(s)
        return reduce(fc,map(char2num,s))/sx
    else:
        return reduce(fc,map(char2num,s))

print(str2float('123.456'))
