# 2. Generator comferfishon (() ichida)


# 1. 1 dan 5 gacha sonlar kvadratlari
squares = (x**2 for x in range(1, 6))
for s in squares:
    print(s)

# 2. Faqat toq sonlarni olish
odds = (x for x in range(10) if x % 2 != 0)
print(list(odds))
