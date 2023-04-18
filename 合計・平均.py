print("合計値と平均値を求めます\n注:'End'で入力終了")

number =  0
tensu = []

while True:
    s = input('{}番の点数:'.format(number + 1))
    if s == 'End':
        break
    tensu.append(int(s))
    number += 1

total = sum(tensu)

print("合計は{}です".format(total))
print("平均は{}です".format(total / number))
