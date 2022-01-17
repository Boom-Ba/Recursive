#if array can be partitioned into three equal subsets. 
#recursive method
def partition(S):
  # Write your code here...
  if len(S)<3:
    return False
  total =sum(S)
  if total%3!=0:
    return False 
    
  def subsetSum(S,n,a,b,c):
    if a==0 and b==0 and c==0 and n==-1:
      return True
    if n<0:
      return False 
    #created a variable to identify if sum1 can be decreased to 3
    sum1=False 
    if a-S[n]>=0:
      sum1 = subsetSum(S,n-1,a-S[n],b,c)
    sum2=False 
    if not sum1 and b-S[n]>=0:
      sum2 = subsetSum(S,n-1,a,b-S[n],c)	
    sum3=False 
    if not sum1 and not sum2 and c-S[n]>=0:
      sum3 = subsetSum(S,n-1,a,b,c-S[n])	
    # print(sum1,sum2,sum3,n)
    return sum1 or sum2 or sum3 #either of one of them can continue substract the unseen num
  return subsetSum(S,len(S)-1,total//3,total//3,total//3)
partition([7, 3, 2, 1, 5, 4, 8])
