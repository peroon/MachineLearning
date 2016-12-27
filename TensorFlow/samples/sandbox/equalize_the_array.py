# -*- coding: utf-8 -*-

# 何個消せば全ての要素が同じになるか
def equalize_the_array(arr):
    arr = sorted(arr)

    max_length = 0
    length = 1

    prev_val = None
    for val in arr:
        if prev_val == val:
            length += 1
        else:
            length = 1
        if length > max_length:
            max_length = length
        prev_val = val
    return max_length

# 何個消せば全ての要素が同じになるか2
# count(v)で個数が求まることを利用する
def equalize_the_array2(arr):
    # forのためのset
    val_set = set(arr)
    max_len = 0
    for val in val_set:
        count = arr.count(val)
        if count > max_len:
            max_len = count
    return max_len

a = [3, 3, 2, 1, 3]

print equalize_the_array(a)
print equalize_the_array2(a)