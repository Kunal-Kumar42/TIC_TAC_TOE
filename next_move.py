import pandas as pd
import numpy as np

df = pd.read_csv("my_tic_tac_toe_all.csv")

postopos = {
    0:"TL",
    1:"TM",
    2:"TR",
    3:"ML",
    4:"MM",
    5:"MR",
    6:"BL",
    7:"BM",
    8:"BR",
}

revpostopos = {
    "TL":0,
    "TM":1,
    "TR":2,
    "ML":3,
    "MM":4,
    "MR":5,
    "BL":6,
    "BM":7,
    "BR":8,
}

def makeitgood(sign , arr):
    arr1 = []
    for el in arr:
        arr1.append( sign+":"+postopos[el] )
    return arr1

def correctorder(arr1,arr2,curr):
    arr=[]
    if(len(arr1) > len(arr2)):
        idx = len(arr2)
        for el in range(idx):
            arr.append(arr1[el])
            arr.append(arr2[el])
        arr.append(arr1[idx])

    elif(len(arr1) < len(arr2)):
        idx = len(arr1)
        for el in range(idx):
            arr.append(arr2[el])
            arr.append(arr1[el])
        arr.append(arr2[idx])
    else:
        idx = len(arr1)
        if(curr == 0):
            for el in range(idx):
                arr.append(arr1[el])
                arr.append(arr2[el])
        else :
            for el in range(idx):
                arr.append(arr2[el])
                arr.append(arr1[el])


    return arr


def predict(df , x_filled_pos : list[int] , o_filled_pos : list[int] , sign :  chr ) -> chr:

    x_filled_pos = makeitgood('X',x_filled_pos)
    o_filled_pos = makeitgood('O',o_filled_pos)
    curr=None
    if(sign=='X'): curr = 0
    else: curr=1
    arr = correctorder(x_filled_pos,o_filled_pos,curr)

    #trimming
    for (el,no) in zip(arr,range(len(arr))):
        df = df[df["move"+str(no+1)] == el]

    #removing unwanted
    df = df.drop(df.columns[np.arange(len(arr))] , axis=1)
    df = df[ (df["result"] == sign) | (df["result"] == "Draw")]
    # getting result
    try:
        k =  df[df.columns[0]].max().split(":")[1]
        return revpostopos[k]
    except:
        return '-'

print(predict(df , [6,1,5,8],[2,0,4] , 'O'))