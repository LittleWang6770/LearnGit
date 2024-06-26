# 定义一个函数来检查一个数是否为质数
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# 使用for循环遍历100以内的所有数字
for number in range(2, 101):
    if is_prime(number):
        print(number)
