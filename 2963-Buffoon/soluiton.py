n = int(input())
votes = []

for i in range(n):
    vote = int(input())
    votes.append(vote)

carlos_vote = votes[0]

max_vote = max(votes)

if carlos_vote == max_vote:
    print('S')
else:
    print('N')