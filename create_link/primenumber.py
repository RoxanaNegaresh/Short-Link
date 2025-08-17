# for n in range(1, 1000):
#     for i in range(2, n):
#         if n % i == 0:
#             print(n, 'is not prime')
#             break
#     else:
#         print(n, 'is prime')

counter = 0
text = 'asdfkasdfjasdfiasdf'
for char in text:
    if char == 'i' or char == 'j':
        counter += 1
print(counter)