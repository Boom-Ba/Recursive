#find inversion count using Merge Sort
class Solution:
	#merge two sorted_arr A[start:mid] A[mid+1:end]
  def merge(self,aux, A, start,end,mid):
    i=start
    k =i 
    j =mid+1 
    count= 0
    while i<=mid and j<=end: 
      if A[i] <=A[j]:
        aux[k] = A[i]
        i+=1 
      else:
        aux[k] = A[j]
        count+=(mid-i+1)
        j+=1 
      k+=1
    # copy remaining elements
      while i <= mid:
          aux[k] = A[i]
          k = k + 1
          i = i + 1
      for i in range(start, end + 1):
          A[i] = aux[i]
    return count 
		
  def mergeSort(self,A,aux, start, end):
    if start==end:
      return 0 
    inversedCount =0
    mid =start+(end-start)//2
    inversedCount+= self.mergeSort(A,aux, start,mid)
    inversedCount+= self.mergeSort(A,aux, mid+1,end)
    inversedCount+= self.merge(A,aux,start,end,mid)
    return inversedCount

  def findInversionCount(self, nums):
    # Write your code here...
    aux=nums.copy()
    if not nums:
      return 0
    if len(nums)<2:
      return 0
    return self.mergeSort(nums,aux,0,len(nums)-1)
