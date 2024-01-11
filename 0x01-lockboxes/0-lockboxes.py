#!/usr/bin/python3
'''algorithm for locked boxes'''

from collections import deque


def canUnlockAll(boxes):
    '''algorithm for locked boxes'''

    if not boxes or not boxes[0]:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True

    queue = deque([0])

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
