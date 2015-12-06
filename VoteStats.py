from WeightedAverage import WeightedAverage


class VoteStats:
    def __init__(self, vote_stats):
        self.vote_stats = vote_stats
        self.average = WeightedAverage()
        weight = 1
        for votes in vote_stats:
            if votes > 0:
                self.average.add_value(weight, votes)

    def vote(self, rating):
        self.average = self.average.add_value(rating)

    def show_stats(self):
        print("some time later: " + self.count() + " ")

    def count(self):
        return self.average.count

    def rank(self):
        return self.average.rank

    def __str__(self):
        return "Rank: {0}, votes:{1}".format(self.rank(), self.count())
