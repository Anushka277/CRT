'''
operators - symbols that perform operations on variables and values

Types of operators:
1. Arithmetic Operators: +, -, *, /, %, **, //
2.Assignment Operators: =, +=, -=, *=, /=, %=, //=, **= [(return type is a boolean)]
3. Comparison Operators: ==, !=, >, <, >=, <=
4. Logical Operators: and, or, not [(&&, ||, ! in other languages)]
5. Bitwise Operators: &, |, ^, ~, <<, >> [(>>: right shift, <<: left shift)]
6. Membership Operators: in, not in
7. Identity Operators
8. Relational Operators: ==, !=, >, <, >=, <= [(eg: x += 10 --> x = x + 10)]


'''

x = int(input("Enter a value:"))
print(x<<2)
print(x>>2)
print(~x)

# Membership Operators: in, not in
s=input()
print('on' in s)
print('on' not in s)
# Identity Operators: is, is not
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 is l2)