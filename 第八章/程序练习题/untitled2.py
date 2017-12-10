# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:22:08 2017

@author: park
"""

def whoiswinner(scoreA,scoreB):
    if scoreA>scoreB:
        winner="A队"
    elif scoreB>scoreA:
        winner="B队"
    else:
        winner="没有队伍"
    return winner
    


def printSummary(n,winner):
    print("篮球竞技分析开始，共模拟{}个回合".format(n))
    print("比赛结果为，{}胜利".format(winner))
    
    

a,b,n=10,5,100
winner=whoiswinner(a,b)
printSummary(n,winner)