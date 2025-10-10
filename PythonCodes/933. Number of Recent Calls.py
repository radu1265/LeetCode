class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        while self.counter:
            if self.counter[0] < t - 3000:
                self.counter.pop(0)
            else: 
                break
        self.counter.append(t)
        return len(self.counter)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
