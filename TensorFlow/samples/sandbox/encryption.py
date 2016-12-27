# -*- coding: utf-8 -*-
# for the quiz https://www.hackerrank.com/challenges/encryption
import math

# 箱形に暗号化する
def encryption(s):
    sqrt_val = math.sqrt(len(s))
    rows_len = int(math.floor(sqrt_val))
    columns_len = int(math.floor(sqrt_val))
    # 収まらなければ拡張
    if rows_len * columns_len < len(s):
        columns_len += 1
    # 収まらなければ拡張
    if rows_len * columns_len < len(s):
        rows_len += 1
    #箱がピッタリ埋まるようにスペース挿入
    s = s.ljust(rows_len * columns_len, ' ')

    encrypted_text = []
    # スライスでいれていく
    for i in range(0, len(s), columns_len):
        encrypted_text.append(s[i:i+columns_len])
    #print encrypted_text
    # あとは縦に読んで出力をつくる
    output_text = []
    for i in range(columns_len):
        text = ""
        for j in range(rows_len):
            #値があるならとって連結
            text += encrypted_text[j][i]
        output_text.append(text)
    output_text = map(str.strip, output_text)
    return ' '.join(output_text)

sample_input = "haveaniceday"
print encryption(sample_input)

sample_input = "feedthedog"
print encryption(sample_input)

sample_input = "chillout"
print encryption(sample_input)
# answer "clu hlt io"