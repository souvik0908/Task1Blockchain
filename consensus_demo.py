import random

# PoW
miner = {"A": random.randint(1, 100), "B": random.randint(1, 100)}
pow_winner = max(miner, key=miner.get)
print(f"PoW Winner: {pow_winner}, Power: {miner[pow_winner]}")

# PoS
staker = {"X": random.randint(1, 1000), "Y": random.randint(1, 1000)}
pos_winner = max(staker, key=staker.get)
print(f"PoS Winner: {pos_winner}, Stake: {staker[pos_winner]}")

# DPoS
votes = {"D1": 3, "D2": 5, "D3": 2}
dpos_winner = max(votes, key=votes.get)
print(f"DPoS Delegate: {dpos_winner}, Votes: {votes[dpos_winner]}")
