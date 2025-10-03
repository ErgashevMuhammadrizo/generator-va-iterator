# 1. Generator funksiya (yield)



# 1 dan 5 gacha bo'lgan sonlarni generatsiya qiluvchi generator funksiya

def gen_numbers():
    for i in range(1, 6):
        yield i

# Foydalanish
for num in gen_numbers():
    print(num)


# 2. juft sonlari  generator funksiya


def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

for x in even_numbers(10):
    print(x)
