N=int(input(""))
if N<100000:
    S=list(map(int,input().split()))
    for i in range(len(S)):
         for j in range(len(S)):
              for k in range(len(S)):
                  if i<j<k:
                      if S[i]+S[j]==S[k]:
                          print(S[i],S[j],S[k])
