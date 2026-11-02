# Challenge #10
# 
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
# If the town judge exists, then:
# 
# - The town judge trusts nobody.
# - Everybody (except for the town judge) trusts the town judge.
# - There is exactly one person that satisfies properties 1 and 2.
# 
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.
# If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
# 
# Input Format:
# 1. The first line contains an integer m representing the size of the trust array (number of trust pairs).
# 2. The second line contains an integer n representing the number of people in the town.
# 3. The next m lines contain two integers ai and bi.

import sys

def find_town_judge():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    n = int(input_data[1])
    
    # Array to track net trust score: (indegree - outdegree)
    # Since person labels are 1-indexed (1 to n), we use a size of n + 1
    trust_scores = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        ai = int(input_data[idx])
        bi = int(input_data[idx+1])
        idx += 2
        
        trust_scores[ai] -= 1  # Person 'ai' trusts someone (outdegree increases -> decreases net score)
        trust_scores[bi] += 1  # Person 'bi' is trusted by someone (indegree increases -> increases net score)
        
    # The town judge must be trusted by everyone else (n - 1 people) and trust nobody (0 people)
    # Therefore, their net trust score must be exactly n - 1
    for person in range(1, n + 1):
        if trust_scores[person] == n - 1:
            print(person)
            return
            
    # If no person satisfies the conditions, print -1
    print(-1)

if __name__ == '__main__':
    find_town_judge()
