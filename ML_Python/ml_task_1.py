# Task 1 : collatz conjecture

def collatz(x):
    if(x%2==0):
        x=x/2
    else:
        x=3*x+1
    return int(x)

nums=[]

i = eval(input("Enter a number: "))
nums.append(i)

for i in nums:
    if(i==1):
        break
    nums.append(collatz(i))

print('Collatz conjecture:', *nums, sep = ' ') 
print(f'no. of iterations: {len(nums)-1}')
