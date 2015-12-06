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
        self.vote_stats[rating - 1] += 1

    def show_stats(self):
        print("some time later: " + self.count() + " ")

    def count(self):
        return self.average.count

    def rank(self):
        return self.average.rank

    def percent(self, index):
        vote_count = int(self.vote_stats[index])
        if vote_count <= 0:
            print("no votes")
            return 0
        return float(vote_count) / self.count() * 100.

    def __str__(self):
        return 'Rank: {0:.1f}, votes:{1} {0:.1f} out of 5 stars: 5 star {2:.0f}% 4 star {3:.0f}% 3 star {4:.0f}% 2 star {5:.0f}% 1 star {6:.0f}%'.format(
            self.rank(), self.count(), self.percent(4), self.percent(3), self.percent(2), self.percent(1), self.percent(0))


if __name__ == '__main__':
    votes = VoteStats([0, 0, 0, 0, 0])
    print(votes)
    votes.vote(5)
    print(votes)
    votes.vote(5)
    print(votes)
    votes.vote(5)
    print(votes)
    votes.vote(4)
    print(votes)
    votes.vote(4)
    print(votes)
    votes.vote(4)
    print(votes)
