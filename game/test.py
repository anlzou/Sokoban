'''
 * @author  anlzou
 * @date  2020/5/9 16:03
 * @version xx
 * @description xx
'''

from map import mapRead as r
from map import mapWrite as w

n = 1
while n > 0:
    n = input("输入一个数：")
    n = int(n)
    w.mapWrite(n)
    r.mapRead()

