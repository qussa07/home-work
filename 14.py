"""# 1
f = 283 ** 382 + 9 ** 15 + 2 ** 3
count_B = 0
count_C = 0
while f > 0:
    b = f % 14
    if b == 11:
        count_B += 1
    if b == 12:
        count_C += 1
    f = f // 14
print(abs(count_B - count_C))"""

"""# 2
f = 673 ** 7 + 67 ** 6 + 3 ** 3
count_B = 0
count_C = 0
while f > 0:
    b = f % 12
    if b == 10:
        count_B += b
    if b == 8:
        count_C += b
    f = f // 12
print(count_B - count_C)
"""

"""# 3
f = 7 * 5** 123 + 6 * 5 ** 111 - 5 * 25 ** 50 + 4 * 125 ** 30 - 3 * 5 ** 10
count_B = 0
count_C = 0
while f > 0:
    b = f % 5
    if b == 4:
        count_B += 1
    f = f // 5
print(count_B)"""

"""# 4
print(str(bin(2 ** 24 + 2 ** 14 - 2 ** 5)).count('1'))"""

"""# 5
f = 7 ** 21 + 49 ** 13 - 7 ** 10
count_B = 0
count_C = 0
while f > 0:
    b = f % 7
    if b == 6:
        count_B += 1
    f = f // 7
print(count_B)"""

"""# 6
***"""

"""# 7
f = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
count = 0
while f > 0:
    b = f % 25
    if b == 0:
        count += 1
    f //= 25
print(count)"""

"""# 8
f = 5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3
f1 = 0
k = 0
while f > 0:
    b = f % 5
    f1 += b * 10 ** k
    k += 1
    f //= 5
print(sum([int(i) for i in list(str(f1))]))"""

"""# 9
f = 3 * 7 ** 82 - 4 * 49 ** 21 + 5 * 343 ** 25
f1 = 0
k = 0
while f > 0:
    b = f % 7
    f1 += b * 10 ** k
    k += 1
    f //= 7
print(sum([int(i) for i in list(str(f1))]))"""

"""# 10
summa = 0
for i in range(951):
    o = i
    f = i
    ternary = 0
    fivefold = 0
    k = 0
    if i % 10 != 0 and i != 950:
        while i > 0:
            b = i % 3
            ternary += b * 10 ** k
            k += 1
            i //= 3
        k = 0
        while f > 0:
            b = f % 5
            fivefold += b * 10 ** k
            k += 1
            f //= 5
        if str(fivefold)[-1] == '3' and len(str(ternary)) >= 2 and f"{str(ternary)[-2]}{str(ternary)[-1]}" == '21':
            summa += o / 10
print(summa)"""