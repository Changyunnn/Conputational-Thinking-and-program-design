# -*- coding: utf-8 -*-
"""week10_a105050273.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Og5h9OvJChwDi7qBOko8AWB1ECYvmaWb
"""

A = int(input('請輸入上衣數量？'))
B = int(input('請輸入褲子數量？'))
C = int(input('請輸入背心數量？'))

總金額 = A*300 + B*350 + C*400
print('訂購服裝的總金額為', 總金額)

a = int(input("請輸入購買罐數?"))
一打 =(a//12)
不足一打 =(a % 12)
總金額 =(一打*200 + 不足一打*20)
print("總金額為", 總金額)

第一次期中考成績 = int(input("請輸入第一次期中考成績"))
第二次期中考成績 = int(input("請輸入第二次期中考成績"))
期末考成績 = int(input("請輸入期末考成績"))
總分數 = 第一次期中考成績 + 第二次期中考成績 + 期末考成績
print("總分數為",總分數)
平均分數 = (第一次期中考成績 + 第二次期中考成績 + 期末考成績)//3
print("平均分數為",平均分數)

座號=int(input("請輸入您的座號?")) #文字轉數字
組別=(座號-1)//5 + 1
print("組別為",組別)