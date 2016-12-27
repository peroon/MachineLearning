# -*- coding: utf-8 -*-
# for the quiz of https://www.hackerrank.com/challenges/acm-icpc-team/
n = 4
m = 5
topic = ['10101', '11100', '11010', '00101']

# answer
# 5
# 2

def acm_icpc_team(topic):
    length = len(topic)
    max_one_num = 0 # 1の数
    max_one_count = 0

    for i in xrange(length):
        for j in xrange(length):
            if i < j:
                s0 = "0b" + topic[i]
                s1 = "0b" + topic[j]
                # 二進数扱いして数値にする
                b0 = int(s0, 2)
                b1 = int(s1, 2)

                # 二進数で論理和をとる
                or_value =  b0 | b1
                #or_value =  b0 or b1

                # 文字列に戻す # 例 0b11011
                s = bin(or_value)
                count = s.count("1")
                if count > max_one_num:
                    max_one_num = count
                    max_one_count = 1
                #トップタイ
                elif count == max_one_num:
                    max_one_count += 1
    return (max_one_num, max_one_count)

ret = acm_icpc_team(topic)
print ret[0]
print ret[1]