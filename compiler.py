if __name__ == '__main__':
 print("Enter the line of code: ")
code= ''
temp= 0
while temp<4:
    code.format(input())
    if (input()==';'):
        break
    temp += 1;
a=code.count('<')
b=code.count('>')
c=code.count('{')
d=code.count('}')
e=code.count('(')
f=code.count(')')
g=code.count('[')
h=code.count(']')
if(a == b and c == d and e == f and g == h):
     print("the brackets have been nested correctly")
else:
     print("please check the brackets nesting and try again")
        