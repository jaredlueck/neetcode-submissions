class TimeMap:

    def __init__(self):
        self.time_map = dict()

    def binary_search(self, values, timestamp):
        l, r = 0, len(values)-1
        index = -1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                index = m
                l = m + 1
            else:
                r = m - 1               
        return index

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.time_map:
            self.time_map[key] = [(value, timestamp)]
        else:
            self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.time_map:
            return ""
        print(self.time_map[key])
        index = self.binary_search(self.time_map[key], timestamp)
        if index < 0 or index > len(self.time_map[key]):
            return ""
        return self.time_map[key][index][0]

        
