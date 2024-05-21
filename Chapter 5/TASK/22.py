import math

def merge(P, left, mid, right):
    sorted = [None] * (right - left + 1)
    k, i, j = 0, left, mid + 1
    while i <= mid and j <= right:
        if P[i][1] <= P[j][1]:
            sorted[k] = P[i]
            i += 1
        else:
            sorted[k] = P[j]
            j += 1
        k += 1
    while i <= mid:
        sorted[k] = P[i]
        i += 1
        k += 1
    while j <= right:
        sorted[k] = P[j]
        j += 1
        k += 1
    for k in range(right - left + 1):
        P[left + k] = sorted[k]

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(P):
    min_dist = float('inf')
    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(P[i], P[j])
            if d < min_dist:
                min_dist = d
    return min_dist

def strip_closest(Pm, d):
    min_dist = d
    size = len(Pm)
    for i in range(size):
        for j in range(i + 1, size):
            if (Pm[j][1] - Pm[i][1]) < min_dist:
                d = dist(Pm[i], Pm[j])
                if d < min_dist:
                    min_dist = d
    return min_dist

def closest_pair_dist(P, n):
    if n <= 3:
        P.sort(key=lambda pt: pt[1])
        return closest_pair(P)
    mid = n // 2
    mid_x = P[mid][0]
    dl = closest_pair_dist(P[:mid], mid)
    dr = closest_pair_dist(P[mid:], n - mid)
    d = min(dl, dr)
    merge(P, 0, mid - 1, n - 1)

    Pm = []
    for i in range(n):
        if abs(P[i][0] - mid_x) < d:
            Pm.append(P[i])
    ds = strip_closest(Pm, d)
    return min(d, ds)

p = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
p.sort(key=lambda point: point[0])
print("가장 가까운 두 점의 거리:", closest_pair_dist(p, len(p)))