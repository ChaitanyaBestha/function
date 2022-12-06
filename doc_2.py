# def maximum(x, y):
#  if x > y:
#   return x
#  elif x == y:
#   return 'The numbers are equal'
#  else:
#   return y
# print(maximum(2, 3))

def maximum(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
print(maximum(23,45,67))                