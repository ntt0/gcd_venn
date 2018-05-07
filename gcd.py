#          _____                   _____                   _____          
#         /\    \                 /\    \                 /\    \         
#        /::\    \               /::\    \               /::\    \        
#       /::::\    \             /::::\    \             /::::\    \       
#      /::::::\    \           /::::::\    \           /::::::\    \      
#     /:::/\:::\    \         /:::/\:::\    \         /:::/\:::\    \     
#    /:::/  \:::\    \       /:::/  \:::\    \       /:::/  \:::\    \    
#   /:::/    \:::\    \     /:::/    \:::\    \     /:::/    \:::\    \   
#  /:::/    / \:::\    \   /:::/    / \:::\    \   /:::/    / \:::\    \  
# /:::/    /   \:::\ ___\ /:::/    /   \:::\    \ /:::/    /   \:::\ ___\ 
#/:::/____/  ___\:::|    /:::/____/     \:::\____/:::/____/     \:::|    |
#\:::\    \ /\  /:::|____\:::\    \      \::/    \:::\    \     /:::|____|
# \:::\    /::\ \::/    / \:::\    \      \/____/ \:::\    \   /:::/    / 
#  \:::\   \:::\ \/____/   \:::\    \              \:::\    \ /:::/    /  
#   \:::\   \:::\____\      \:::\    \              \:::\    /:::/    /   
#    \:::\  /:::/    /       \:::\    \              \:::\  /:::/    /    
#     \:::\/:::/    /         \:::\    \              \:::\/:::/    /     
#      \::::::/    /           \:::\    \              \::::::/    /      
#       \::::/    /             \:::\____\              \::::/    /       
#        \::/____/               \::/    /               \::/____/        
#                                 \/____/                 ~~              

import collections

##funct def
def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

##runtime                                                          
while True:
  print("Enter comma separated numbers to find greatest common divisor for")
  print("   example input: 36,42,8")
  print("or enter q to quit.")

  usr_in=raw_input(": ")

  if usr_in=="q":
    break
  else:
    a=[]
    i=0
    nums = map(int, usr_in.split(','))
    for num in nums: 
      s=primes(num)
      a.append(collections.Counter(s))
      i+=1
    
    intersect=a[i-1]
    while True:
      i-=1
      intersect=intersect & a[i]
      if i==0:
        break

    venn=list(intersect.elements())
    t=1
    if len(venn)==0:
      print("gcd = 1")
    else:
      for x in venn:
        t*=x
      print("gcd = {}".format(t))



    