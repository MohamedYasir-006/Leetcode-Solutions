class Solution:
    def networkDelayTime(self, times, n, k):

        graph = {i: [] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))

        distances = {i: float('inf') for i in range(1, n + 1)}

        distances[k] = 0

        pq = [(0, k)]

        while pq:

            dist, node = heapq.heappop(pq)

            if dist > distances[node]:
                continue

            for neighbour, weight in graph[node]:

                new_dist = dist + weight

                if new_dist < distances[neighbour]:

                    distances[neighbour] = new_dist

                    heapq.heappush(pq, (new_dist, neighbour))

        result = max(distances.values())

        return result if result != float('inf') else -1