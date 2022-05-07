# 📌 문제

[1260번: DFS와 BFS](https://www.acmicpc.net/problem/1260)

## 🔎 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

## 🔎 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

## 🔎 출력

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## 📋 예제 입력

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

```
1000 1 1000
999 1000
```

## 📋 예제 출력

```
1 2 4 3
1 2 3 4
```

```
3 1 2 5 4
3 1 4 2 5
```

```
1000 999
1000 999
```

## 🔎 접근

1. 입력받은 데이터로 양방향 그래프를 만든다. 
2. BFS, DFS를 수행한다. 
    1. 수행 과정 중 방문할 수 있는 정점이 여러개인 경우는 정점 번호가 작은 것 부터 탐색할 수 있도록 queue, stack에 추가한다. 
3. 각각의 원소를 출력한다. 

```python
import sys
from collections import deque

def dfs(graph, v):
    stack = deque([])
    visited = []

    stack.append(v)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node in graph:
                x = list(set(graph[node]) - set(visited))
                x.sort(reverse = True)
                stack.extend(x)
    
    return ' '.join(map(str, visited))

def bfs(graph, v):
    queue = deque([])
    visited = []
    queue.append(v)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph:
                x = list(set(graph[node]) - set(visited))
                x.sort()
                queue.extend(x)

    return ' '.join(map(str, visited))

n, m, v = map(int, sys.stdin.readline().rstrip().split(' '))
graph = {i+1: [] for i in range(n)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, v))
print(bfs(graph, v))

```

**결과**

| 메모리 | 시간 |
| --- | --- |
| 32416KB | 88ms |

## 📎결론

- 단순한 BFS, DFS 문제이다. 다만, 출력조건을 잘 생각해야 한다. 원소를 방문한 순서대로 한 줄에 출력해야지. 방문한 원소가 있는 리스트를 통째로 출력하는 문제는 아니다.
- 또한 노드 탐색에 조건이 있어서 이를 해결해야 하는 과정을 놓칠 뻔 했다. 아마 BFS, DFS 문제를 외우다시피 풀어서 그런 것 같다. 함수 작성 중 조건만 추가하면 되므로 쉽게 생각하자