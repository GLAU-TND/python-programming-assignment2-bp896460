'''
Assignment 6
Bottle Necks
Problem

'''
def min_visible_bottles (arr,n):
     a = dict()
     ans = 0
     for i in range (n):
          a[arr[i]] = a.get(arr[i],0)+1
          ans = max(ans,a[arr[i]])

     print("Minimum number of","Visible Bottles are :",ans)
n = int(input())
arr = input().split()
min_visible_bottles (arr,n)
