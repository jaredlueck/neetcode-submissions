class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}

        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        # heap ordered by amount of each task. We ideally want to pick a task that has
        # multiple occurances so that we can execute other tasks in between
        heap = [(-cnt, -1, task) for [task, cnt] in counts.items()]
        heapq.heapify(heap)
        print(heap)
        clock = 0

        while heap:
            # pop until we find a task we can complete
            tasks = []
            while heap:
                (cnt, time, task) = heapq.heappop(heap)
                print((cnt, time, task))
                rem = clock - time
                # we can complete this task. If there are more 
                # instances of the task remaining we will update the heap
                if time < 0 or rem > n:
                    if abs(cnt) > 1:
                        tasks.append((cnt+1, clock, task))
                    break
                # must wait longet to the task so put it back on the heap
                else:
                    tasks.append((cnt, time, task))
            # put skipped tasks back on the heap
            for task in tasks:
                heapq.heappush(heap, task)
            clock += 1
        
        return clock


        