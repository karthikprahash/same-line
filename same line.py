# same-line
i,m=list(map(int,input().split()))
j,n=list(map(int,input().split()))
k,b=list(map(int,input().split()))
if i==m or j==n or k==b or i==j==k or m==n==b:
    print('yes')
else:
    print('no')
