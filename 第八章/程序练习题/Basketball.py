# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 19:57:27 2017

@author: park
"""

def main():
    printIntro()
    a2,a3,b2,b3,n=getInputs()
    scoreA,scoreB=simNGames(n,a2,a3,b2,b3)
    winner=whoiswinner(scoreA,scoreB)
    printSummary(n,scoreA,scoreB,winner)
    
def printIntro():
    print("这个程序模拟两个球队A和B的篮球比赛")
    print("程序运行需要球队A和B的能力值（以0到1之间的小数表示）")
    
def getInputs():
    a2,a3=eval(input("请输入A队的两分球和三分球能力值（0-1）："))
    b2,b3=eval(input("请输入B队的两分球和三分球能力值（0-1）："))
    n=eval(input("请输入模拟比赛的回合数："))
    return a2,a3,b2,b3,n

def simNGames(n,a2,a3,b2,b3):
    scoreA,scoreB=0,0
    servings=["A","B"]
    serving=choice(servings)
    for i in range (n):
        if serving=="A":
            a2or3=[a2,a3,a2]
            a=choice(a2or3)
            if a==a2:  #两分进攻
                if random()<a2:
                    scoreA+=2
                    serving="B"
                else:
                    serving="B"
                print(scoreA,scoreB)
                sleep(1)
            else:       #三分进攻
                if random()<a3:
                    scoreA+=3
                    serving="B"
                else:
                    serving="B"
                print(scoreA,scoreB)
                sleep(1)
        else:
            b2or3=[b2,b3,a2]
            b=choice(b2or3)
            if b==b2:
                if random()<b2:
                    scoreB+=2
                    serving="A"
                else:
                    serving="A"
                print(scoreA,scoreB)
                sleep(1)
            else:
                if random()<b3:
                    scoreB+=3
                    serving="A"
                else:
                    serving="A"
                print(scoreA,scoreB)
                sleep(1)
    return scoreA,scoreB
    
def whoiswinner(scoreA,scoreB):
    if scoreA>scoreB:
        winner="A队"
    elif scoreB>scoreA:
        winner="B队"
    else:
        winner="没有队伍"
    return winner
    


def printSummary(n,scoreA,scoreB,winner):
    print("篮球竞技分析开始，共模拟{}个回合".format(n))
    print("比赛结果为，A队{}分,B队{}分，{}胜利".format(scoreA,scoreB,winner))
    
from time import *
from random import *
main()