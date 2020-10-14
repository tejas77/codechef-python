t = int(input())
player_one = 0
player_two = 0
leader = 0
lead = 0

for _ in range(t):
    score_one, score_two = map(int, input().split())
    player_one = player_one + score_one
    player_two = player_two + score_two
    lead_temp = player_one - player_two
    if player_one > player_two and lead_temp > lead:
        leader = 1
        lead = lead_temp if lead_temp > lead else lead
    elif player_one < player_two and -lead_temp > lead:
        leader = 2
        lead = -lead_temp if - lead_temp > lead else lead

print(f'{leader} {lead}')
