#inbuilt iterators
nums=[1,2,3,4,5]
it = iter(nums)
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print()
print(next(it))
print()
for i in nums:
    print(i)
print()   
#user defined iterators
class topten():
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values = topten()
print(values.__next__())
print(values.__next__())
print()
print(next(values))
print()

for i in values:
    print(i)
    
print()

def toptensqr():
    n=1
    while n<=10:
        sq=n*n
        yield sq#yield returns an iterator
        n=n+1
values1 =toptensqr()
print(values1)
print(values1.__next__())
print(values1.__next__())
print(next(values1))
for j in values1:
    print(j)