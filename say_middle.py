# 백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다. 백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다. 만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

# 예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면, 동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다. 백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5
import heapq
import sys

small_heap = []
big_heap = []

init = int(sys.stdin.readline())

for _ in range(init):

    num = int(sys.stdin.readline())
    if len(small_heap) == len(big_heap):
        heapq.heappush(big_heap,num)
    else:
        heapq.heappush(small_heap,-num)
    if len(small_heap) != 0 and -small_heap[0]> big_heap[0]:
        a = heapq.heappop(small_heap)
        b = heapq.heappop(big_heap)
        heapq.heappush(small_heap, -b)
        heapq.heappush(big_heap, -a)    
    if len(small_heap) == len(big_heap):
        print(-small_heap[0])
    else:
        print(big_heap[0])