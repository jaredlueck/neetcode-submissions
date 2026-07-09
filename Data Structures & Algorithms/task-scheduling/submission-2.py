class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        # heap ordered by amount of each task. We ideally want to pick a task that has
        # multiple occurances so that we can execute other tasks in between
        heap = [val for val in counts.values()]
        heapq.heapify_max(heap)
        print(heap)
        queue = []
        clock = 0

        while heap or queue:
            if queue and clock == queue[0][0]:
                # task is done cooldown so move it to the heap
                heapq.heappush_max(heap, queue.pop(0)[1])
                continue
            if heap:
                # there is a task that can be scheduled on the heap
                cnt = heapq.heappop_max(heap)
                # if there are multiple instances of the same task
                # put it in the queue for cooldown
                if cnt > 1:
                    ready_time = clock + n + 1
                    queue.append((ready_time, cnt-1))
                # otherwise this was the last instance of this task so
                # don't put it on heap or queue
            clock += 1
        return clock


        