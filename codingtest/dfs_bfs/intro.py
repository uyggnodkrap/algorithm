# stack 구현
def stack():
    stack = []
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()
    return stack

# queue 구현
def queue_using_deque():
    from collections import deque
    queue = deque([])

    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    return list(queue)

# 재귀함수
def factorial_using_recursive(x):
    if x <= 1:
        return 1
    else:
        return x * (factorial_using_recursive(x - 1))

# 인접 행렬
def adjacency_matrix():
    INF = 9999999
    graph = [[0, 7, 5],
             [7, 0, INF],
             [5, INF, 0]]
    return graph

# 인접 리스트
def adjacency_list():
    graph = [[] for _ in range(3)]

    # 노드 0과 연결된 노드 정보 (노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    # 노드 1과 연결된 노드 정보 (노드, 거리)
    graph[1].append((0, 7))

    # 노드 2과 연결된 노드 정보 (노드, 거리)
    graph[2].append((0, 5))
    return graph


print(stack())
print(queue_using_deque())
print(factorial_using_recursive(5))
print(adjacency_matrix())
print(adjacency_list())


def dfs(g, v, visited):
    # 현재 노드를 방문 처리 하기
    visited[v] = True

    print(v, end=' ')
    for i in graph[v]:
        # 해당 노드에 방문하지 않았다면
        if not visited[i]:

            # 재귀적으로 방문하기
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    from collections import deque
    queue = deque([start])

    # 현재 노드 방문 처리
    visited[start] = True
    while queue:
        # 원소를 하나 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            # 해당 노드를 방문하지 않았다면
            if not visited[i]:
                # 해당 노드를 큐에 삽입
                queue.append(i)

                visited[i] = True


graph = [ 
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5, ],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9
dfs(graph, 1, visit)

visit = [False] * 9
bfs(graph, 1, visit)
