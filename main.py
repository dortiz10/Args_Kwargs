def my_sum(*args):
  print(args)
print(my_sum(3,4,5))
#args are for entering as many arguments as possible
# def a_sum (*args):
#   for num in args:
#     print(num)

# print(a_sum(1))
# print(a_sum(1,3))
# print(a_sum(1,3,4,5,6))

list = [3,4,5,6,7,8,9,10,11,12,13,14,15]
def sum_number(list):
  # sum = 0
  # for num in list:
  #   sum += num
  # return sum
  return sum(list)

print(sum_number(list))

#args 
def a_sum(*args):
  # total = 0
  # for num in args:
  #   total += num
  return sum (args)

print(a_sum(4,56,77,88,9,45,76))