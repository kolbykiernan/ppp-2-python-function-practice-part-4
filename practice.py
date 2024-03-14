def max_num(x=0 ,y=0, z=0):
   return max([x, y, z])
print(max_num(25, 75, 100))


def mult_list(my_list):
   result = 1
   for numbers in my_list:
       result *= numbers
   return result


numbers = [1, 2, 3, 4, 5]
print(mult_list(numbers))


def rev_string(string):
   return string[::-1]
string =  "hello"
print(rev_string(string))




def num_within(x, y, z):
   return y <= x and z >= x
print(num_within(3,2,4))
print(num_within(13,2,4))


def pascal(n):
   triangle = []
   for i in range(n):
       row = [1] * (i+1)
       for j in range(1, i):
           row [j] = triangle[i-1][j-1] + triangle[i-1][j]
       triangle.append(row)
   for row in triangle:
       print (''.join(map(str, row)).center(n*3))
pascal(5)



