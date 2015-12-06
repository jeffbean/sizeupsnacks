from weightedaverage import WeightedAverage
import math

class VoteStats:
    def __init__(self, votes_by_star, average, count):
        if votes_by_star:
            self.votes_by_star = votes_by_star
            self.average = WeightedAverage()
            weight = 1
            for votes in votes_by_star:
                if votes > 0:
                    self.average.add_value(weight, votes)
                weight += 1
        else:
            self.votes_by_star = [0, 0, 0, 0, 0]
            if count > 0 and average > 0:
                if average > 5:
                    raise ValueError("average in not in range [0, 5]")
                rounded_average = math.ceil(average)
                self.votes_by_star[rounded_average - 1] = count
                self.average = WeightedAverage(rounded_average, count)
            else:
                self.average = WeightedAverage()

    def vote(self, rating):
        self.average = self.average.add_value(rating)
        self.votes_by_star[rating - 1] += 1

    def show_stats(self):
        print("some time later: " + self.count() + " ")

    def count(self):
        return self.average.count

    def rank(self):
        return self.average.rank

    def percent(self, index):
        vote_count = int(self.votes_by_star[index])
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
