# #4:
# def longestCommonPrefix(strs):
#         result=''
#         for i in range(len(strs)-1):
#             for j in range(1,len(strs)-1):
#                 if strs[0][i] == strs[j][i]: 
#                     if strs[1][i] not in result:
#                         result += strs[1][i]
                
#                 else:
#                     break
        
#         print(result)
    
    
# longestCommonPrefix(["dog","racecar","car"])

#4:
def longestCommonPrefix(strs):
    minel= min(strs)
    maxel= max(strs)
    res=''
    for i in range(min(len(minel),len(maxel))):
        if minel[i] != maxel[i] :
            return res
        res +=minel[i]
    return res
#print(longestCommonPrefix(["flower","flow","flight"]))

#5:

def isValid(s):
    stack=[]
    for i in s:
        if i == '(' or i == '{' or i=='[':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                if i ==')' and stack[-1] =='(':
                    stack.pop()
                elif i=='}' and stack[-1] =='{':
                    stack.pop()
                elif i==']' and stack[-1] =='[':
                    stack.pop()
                else:
                    return False
    
    if stack:
        return False
    return True

#print(isValid('{}'))
# def removeDuplicates(nums):
#         ans = 1
#         for i in range(1, len(nums)):
#             if nums[i] != nums[i - 1]: 
#                 nums[ans] = nums[i] 
#                 ans += 1
#         return ans
#print(removeDuplicates([1,1,2]))


def removeDuplicates(nums) :
    nums=set(nums)
        # newlen=len(newnum)
        # return newlen, list(newnum)
    return list(nums)


#print(removeDuplicates([1,1,2]))


def strStr(haystack, needle):
        #newstr=haystack.split(needle)
        return haystack.find(needle)
#print(strStr('sadbutsad','sad'))
        
def strStr(haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            #print(i, haystack[i: i+len(needle)])
            if haystack[i: i+len(needle)] == needle:
                return i
        return -1

#print(strStr('abc','c'))

# def distinct_target(nums,target):
#     low,high=0,len(nums)-1
#     while (low <= high):
#         mid=(high+low)//2
#         print(mid)
#         if nums[mid] == target :
#             return mid
#         elif nums[mid] > target:
#             high=mid-1
#         else:
#             low=mid+1
#     #return low

# nums,target =[1,3,5,6], 7
# print(distinct_target(nums,target)) 
    
def Search_Insert_Position(nums,target):
    low,high=0,len(nums)-1
    while(low<=high):
        mid=(low+high) //2
        print('mid :',mid)
        print('mid :',low)
        print('mid :',high)
        if nums[mid]==target:
            return mid
        elif target  > nums[mid]:
            low =mid+1
        else:
            high =mid-1
    return low
            
    
    
#print(Search_Insert_Position([1,2,3,4], 0))

def lengthOfLastWord(s):
        s1=s.split(' ')
        print(s1)
        for i in range(len(s1)-1,-1,-1):
            #print(i)
            if s1[i] != '':
                return s1[i]
#print(lengthOfLastWord("   fly me   to   the moon  "))

def plusOne(digits):
    #return list(map(int, str(int("".join([str(x) for x in digits]))+1)))
    return  [ int(j)  for j in    str(int("".join( [str(i) for i in digits]))+1)]
    

    
#print(plusOne([9]))

# def mySqrt(x):
#     low,high,ans=1,x,0
#     while low <= high:
#         mid=(high + low) //2
#         if mid *mid == x:
#             return mid
        
#         elif x > mid * mid:
#             low=mid+1
#             ans=mid
            
#         else:
#             high=mid-1
            
#     return ans
            
    
# print(mySqrt(15))



def mySqrt(x):
    low,high=0,x
    while low +1 < high:
        mid=(high + low) //2
        if mid *mid == x:
            return mid
        
        elif x > mid * mid:
            low=mid
            #ans=mid
            
        else:
            high=mid
            
    if high * high == x:
        return high
    return low
            
    
#print(mySqrt(9))



# def maxProfit(prices) :
#     i=0
#     profit=0
#     min_price=prices[0]
    
#     while i<len(prices):
#         if prices[i] < min_price:
#             min_price=prices[i]
#         else:
#             profit= max(profit, prices[i]-min_price)
#         i+=1
#     return profit

# prices = [7,3,5,1,6,4]
# #prices = [7,6,4,3,1]
# print(maxProfit(prices))



def maxProfit(prices):
    i=0
    profit=0
    min_price=prices[0]
    while i < len(prices):
        if prices[i] < min_price:
            min_price=prices[i]
        else:
            profit= max(profit, prices[i]-min_price)
        
        i+=1
    return profit
    
    
    
prices = [7,3,5,1,6,4]
#print(maxProfit(prices))


def isPalindrome(s) :
    s1=''
    for i in s:
        if i.isalnum():
            s1 += i.lower()
    
    #print(s1)
    
    # if s1 == s1[::-1]:
    #     return True
    # return False
    i=0
    j=len(s1)-1
    while i<j:
        if s1[i] != s1[j]:
            return False
        i +=1
        j-=1
    return True

            
    

s = "A man, a plan, a canal: Panama" 
#s = "race a car"
#s = " "
#print(isPalindrome(s))



def singleNumber( nums):
    dict={}
    for i in nums:
        if i in dict:
            dict[i] =dict.get(i)+1
        else:
            dict[i]=1
    #print(dict)
    for m,n in dict.items():
        if n == 1:
            return m
    
#nums = [2,2,1]
#nums = [4,1,2,1,2]
nums = [1]
print(singleNumber(nums))

    