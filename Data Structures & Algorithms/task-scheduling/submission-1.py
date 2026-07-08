class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        # heap ordered by amount of each task. We ideally want to pick a task that has
        # multiple occurances so that we can execute other tasks in between
        heap = [(-cnt, float('-inf'), task) for [task, cnt] in counts.items()]
        heapq.heapify(heap)
        print(heap)
        clock = 0

        while heap:
            # pop until we find a task we can complete
            tmp = []
            while heap and clock - heap[0][1] <= n:
                tmp.append(heapq.heappop(heap))
            if heap:
                (cnt, time, task) = heapq.heappop(heap)
                # we can complete this task. If there are more 
                if abs(cnt) > 1:
                    tmp.append((cnt+1, clock, task))
            for t in tmp:
                heapq.heappush(heap, t)
            clock += 1
        return clock


        