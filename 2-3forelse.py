nums=[1,2,3,4,5]
for i in nums:
    if i%5==0:
        print(i)
        break
else:
    print("No element is divisible by 5")