#                       function in python 
# def hello():
#     print("hello")
#     print("from python")
# hello();

# def sum(a,b):
#     s = a + b
#     return s

# ans = sum(10,5)

# print(ans)

#                         find 3 number average in function

# def cal_avg(a,b,c):
#     sum = a + b + c 
#     return sum/3

# print(cal_avg(2,2,2))

#                        lambda functions

# sum = lambda a,b : a + b
# print(sum(5,6))


#                        write a function for n factorial

def cal_factorial(n):
    fact = 1
    for i in range(1,n+1):
      fact *= i

     
     
    return fact

n = int(input("enter num :"))   

print(cal_factorial(n))