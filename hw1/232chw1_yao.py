"""
Class: Stat232C
Project 1: Bayesian inference
Name: Mingjia Yao
Date: April 2020

"""
import copy
def getPosterior(priorOfA, priorOfB, likelihood):
    marginalOfA=copy.copy(priorOfA)
    marginalOfB=copy.copy(priorOfB)
    pdata=0
    for key in likelihood:
        ai=key[0]
        bi=key[1]
        pjoint=priorOfA[ai]*priorOfB[bi]
        pdata=pdata+likelihood[key]*pjoint
    for aj in marginalOfA:
        pajdata=0
        for joint in likelihood:
            if aj in joint:
                ai=joint[0]
                bi=joint[1]
                pjoint=priorOfA[ai]*priorOfB[bi]
                pajdata=pajdata+likelihood[joint]*pjoint
        marginalOfA[aj]=pajdata/pdata
    for bj in marginalOfB:
        pbjdata=0
        for joint in likelihood:
            if bj in joint:
                ai=joint[0]
                bi=joint[1]
                pjoint=priorOfA[ai]*priorOfB[bi]
                pbjdata=pbjdata+likelihood[joint]*pjoint
        marginalOfB[bj]=pbjdata/pdata
    return([marginalOfA, marginalOfB])



def main():
    exampleOnePriorofA = {'a0': .5, 'a1': .5}
    exampleOnePriorofB = {'b0': .25, 'b1': .75}
    exampleOneLikelihood = {('a0', 'b0'): 0.42, ('a0', 'b1'): 0.12, ('a1', 'b0'): 0.07, ('a1', 'b1'): 0.02}
    print(getPosterior(exampleOnePriorofA, exampleOnePriorofB, exampleOneLikelihood))

    exampleTwoPriorofA = {'red': 1/10 , 'blue': 4/10, 'green': 2/10, 'purple': 3/10}
    exampleTwoPriorofB = {'x': 1/5, 'y': 2/5, 'z': 2/5}
    exampleTwoLikelihood = {('red', 'x'): 0.2, ('red', 'y'): 0.3, ('red', 'z'): 0.4, ('blue', 'x'): 0.08, ('blue', 'y'): 0.12, ('blue', 'z'): 0.16, ('green', 'x'): 0.24, ('green', 'y'): 0.36, ('green', 'z'): 0.48, ('purple', 'x'): 0.32, ('purple', 'y'): 0.48, ('purple', 'z'): 0.64}
    print(getPosterior(exampleTwoPriorofA, exampleTwoPriorofB, exampleTwoLikelihood))




if __name__ == '__main__':
    main()
