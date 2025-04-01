class MovingAverage(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.sum = 0
        self.nums = []
        self.start = 0
        self.end = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.nums) == 0:
            self.nums.append(val)
            self.sum += val
            return self.sum / 1
        else:
            self.nums.append(val)
            self.end +=1
            self.sum += val
            window_size = (self.end - self.start) + 1.0
            if window_size > self.size:
                self.sum -= self.nums[self.start]
                self.start += 1
                return self.sum / float(self.size)
            else:
                return self.sum / window_size
            



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)