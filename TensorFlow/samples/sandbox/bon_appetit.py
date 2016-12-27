# -*- coding: utf-8 -*-
# for the quiz https://www.hackerrank.com/challenges/bon-appetit

# アンナにチャージする額を求める
def bon_appetit(cost_list, not_eat_index):
    """
    :type cost_list: list
    """
    cost_list.pop(not_eat_index)
    return sum(cost_list) / 2

print bon_appetit([3,10,2,9], 1)