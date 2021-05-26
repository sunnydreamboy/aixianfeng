from django.test import TestCase

# Create your tests here.
import copy
# def gp(l):
#     l1 = []
#     for i in range(0,len(l)-1):
#         for j in range(i+1,len(l)):
#             a = l[j]-l[i]
#             l1.append(a)
#     l1.sort()
#     print(l1[-1])


def bettle(l:list):
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            l[i],l[i+1] = l[i+1],l[i]
    data = l[-1]
    print(data)
    print(l.index(data))

bettle([5,2,6,1,9,7])


