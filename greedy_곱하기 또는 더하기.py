# input : 02984 output :576
# input : 567 output : 210

number = '02984'

result = 0
for i, num in enumerate(number):
  num = int(num)
  if result <= 1 or num <= 1: result += num
  else: result *= num

print(result)