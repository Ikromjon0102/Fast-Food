# def generate_numbers(length):
#     numbers = ["0","9"]
#     while length > 1:
#         temp = []
#         for i in numbers:
#             temp.append(i+"0")
#             temp.append(i+"9")
#         numbers = temp
#         length -= 1
#     return tuple(map(int,numbers))
# print(generate_numbers(1))

loop = int(input())
for i in range(loop):
  n = int(input())
  numbers = ["0","9"]
  step = 1
  while True:
      a = []
      if int(numbers[step]) % n == 0:
          print(int(numbers[step]))
          break
      else:
          for i in numbers[-2:]:
              a.append(i+"0")
              a.append(i+"9")
          numbers = a
          step += 1