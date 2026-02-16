

# def F(x,y,z,w):
#     return ((w <= y)<= x) or not z
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 res = F(x,y,z,w)
#                 if not res:
#                     print(x,y,z,w,res)

from functools import lru_cache
@lru_cache(None)
def F(n):
    if n > 10000:
        return 1
    if n > 1:
        return (n+1) * F(n-1)
for n in range(1,2024):
    F(n) 






print((F(2024)-3*F(2023))/F(2022))





#

# def F1(x,y,z,w):
#     return (x <= y) or ((not w) == z)
# def F2(x,y,z,w):
#     return (x <= y) == (w and (not z))

# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 res1 = F1(x, y, z ,w)
#                 res2 = F2(x, y, z, w)
#                 if res1 == res2:
#                     print(x,y,z,w,res1, res2)

























# from turtle import *
# tracer(0)
# screensize(10000,10000)
# r = 16
# for i in range(2):
#     down()
#     for i in range(2):
#         forward(8*r)
#         right(90)
#         forward(8*r)
#         right(90)
#     up()

#     forward(6*r)
#     right(90)
#     forward(6*r)
#     left(90)

# right(180)
# forward(4*r)

# down()

# for i in range(4):
#     forward(8*r)
#     right(270)
    

# up()
# for x in range(-50,50):
#     for y in range(-50,50):
#         goto(x*r, y*r)
#         dot(3,'red')
    
# exitonclick()
    
    
# print(3*(8*2 + 8*2))
#
#
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #from turtle import *
        #tracer(0)
        #screensize(10000,10000)
        #r = 20
        #for i in range(2):
                #forward(r*5)
                #right(90)
                #forward(r*8)
                #right(90)
        #up()
        #forward(r*2)
        #right(90)
        #forward(r*3)
        #left(90)
        #down()
        #for i in range(2):
            #forward(r*4)
            #right(90)
            #forward(r*9)
            #right(90)


        #up()
        #for x in range(-50, 50):
            #for y in range(-50, 50):
                #goto(x*r, y*r)
                #dot(3, 'red')
        #exitonclick()