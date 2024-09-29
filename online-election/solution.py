import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1

        for p in persons:
            count[p] = count.get(p,0) + 1
            if count[p] >= count.get(lead,0): lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]
    

topVotedCandidate = TopVotedCandidate([0, 1, 1, 0, 0, 1, 7], [0, 5, 10, 15, 20, 25])

print(topVotedCandidate.q(25))

