#Given an array such as S = [7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4], determine if it can be partitioned into k=5 subsets.
#algorithms: crent bucket array have k positions, each position represents a bucket, and initially they hold sum(S)//k value,
#.           recursively/backtrackingly substract nums from each bucket, if it can be partition equally into k buckets, 
#            we should get all values appeared to be 0 after recursion/backtracking. 

def checkLeftSum(sumLeft,k):
  #check if all buckets has been filled or not
  for i in range(k):
    if sumLeft[i]!=0:
      return False
  return True 

"""
this functions is to substract num from bucket_arr, and returns result as True if the original array can be separted into k subsets
1.Input: Array:S, Index: n (at S), arr: buckets_array, K: number of partitions
2.Output: Boolean 
"""
def subsetSum(S, n, sumLeft, arr, k):
   #base case
    if checkLeftSum(sumLeft, k):
      return True
  
    if n<0:
      return False 
    
    #return variable
    result = False
    #go through each bucket, if ith bucket still have capacity to include more elements, we will hold return value as False
    #until we finished all buckets, it turns to be True
    for i in range(k):
        if not result and (sumLeft[i] - S[n]) >= 0:
            arr[n] = i + 1 #we update bucket array to store which bucket we used for nth number in the S array
            sumLeft[i] = sumLeft[i] - S[n]
            result = subsetSum(S, n - 1, sumLeft, arr, k)
            sumLeft[i] = sumLeft[i] + S[n]
    return result

def partition(S, k):
    n =len(S)
    # Write your code here...
    if len(S)<k:
      return False
    total =sum(S)
    if total%k!=0:
      return False 
    buckets =[None] * n
    sumleft =[total//k]*k #each bucket aiming to get sum of total//k and we have k buckets
  
    return subsetSum(S,len(S)-1,sumleft,buckets,k)
partition([7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4],5)
