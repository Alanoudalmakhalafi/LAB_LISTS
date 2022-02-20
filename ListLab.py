### Q1
# def sum(items):
#     lst = 0
#     for item in items:
#         lst += item
#     return lst

# lst1= [1,2,3]
# print(sum(lst1))

### Q2
# def maxNum(lst):
#     max = lst[0]
#     for i in lst:
#         if max < i:
#             max = i
#     return max      
# print(maxNum([8,5,7,3]))  

### Q3
# lst = []
# for i in range(1200,2000,125):
#     if i%2 != 0:
#         lst.append(i)
# print(lst)

# x = [i for i in range(1200,2000,125) if i%2 != 0 ]
# print(x)

## TUPLES
### Q1
# t = (1,2,3,3,3)
# for item in t:
#     if t.count(item)>1: 
#         print(t.index(item))
        
        
### Q2
t = (1,2,3,3,3)
t1 = list(t)
for item in t1:
    if t1.count(item)>1:
         t1.remove(item)
print(t1)   
