class WeightedAverage:
    def __init__(self, rank=None, count=0):
        if count < 0:
            raise ValueError("bad count")
        if count > 0:
            if rank < 1 or rank > 5:
                raise ValueError("bad weight")
            self.count = count
            self.rank = rank
        else:
            self.count = 0
            self.rank = 0

    def add_value(self, rank, count=1):
        if count < 0:
            raise ValueError("bad count")
        if rank < 1 or rank > 5:
            raise ValueError("bad weight")
        if count > 0:
            self.count += 1
            self.rank = self.rank * (self.count - count)/self.count + (rank * count)/self.count
        return self

    def __str__(self):
        return "Rank: {0}, Number of votes: {1}".format(self.rank, self.count)


if __name__ == '__main__':
    ave = WeightedAverage(0, 0)
    print(ave)
    ave.add_value(5)
    print(ave)
    ave.add_value(5)
    print(ave)
    ave.add_value(5)
    print(ave)