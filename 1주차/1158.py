from queue import Queue

N,K = map(int,input().split())
ans = list()
q = Queue()

for i in range(1,N+1):
    q.put(i)
    
count = 0
while q.qsize() > 0:
    number  = q.get()
    count += 1
    if count == 3:
        ans.append(number)
        count = 0
    else:
        q.put(number)

print("<",", ".join(map(str,ans)),">")