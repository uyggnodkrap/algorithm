"""
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0

    while truck_weights:
        answer += 1
        next_truck = bridge.popleft()
        bridge_weight -= next_truck

        if bridge_weight + truck_weights[0] > weight:
            bridge.append(0)

        else:
            truck = truck_weights.popleft()
            bridge.append(truck)
            bridge_weight += truck

    while bridge_weight > 0:
        answer += 1
        next_truck = bridge.popleft()
        bridge_weight -= next_truck

    return answer
