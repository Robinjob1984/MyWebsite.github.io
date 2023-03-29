#!/usr/bin/env python3
print("Soccer League week")
print("==================")
print()
num_of_home_wins = 0
num_of_visiting_wins = 0
num_of_matchs = 0
num_of_home_goals = 0
num_of_visiting_goals = 0
num_of_home_conceded = 0
num_of_visiting_conceded = 0
num_of_winning_goals = 0
team_goals_high = 0
team_goals_high_type = 0
goals_high = 0

while True:
    num_of_matchs += 1
    print('Number of matchs: {}'.format(num_of_matchs))
    x = input("Enter Home Team Name: ")
    if x == 'done':
        break
    home_team = x
    home_score = int(input("Enter Team Home Score: "))
    visiting_team = input("Enter Visiting Team Name: ")
    visiting_score = int(input("Enter Visiting Team Score: "))
    
    
    num_of_home_goals += home_score
    num_of_visiting_goals += visiting_score
    num_of_home_conceded += visiting_score
    num_of_visiting_conceded += home_score
    if home_score > visiting_score:
        num_of_home_wins += 1
        num_of_winning_goals += home_score
    elif home_score < visiting_score:
        num_of_visiting_wins += 1
        num_of_visiting_goals += visiting_score

       
    if goals_high < home_score:
            team_goals_high = home_team
            team_goals_high_type = 'HOME TEAM'
    else:
        num_of_visiting_wins += 1
        num_of_winning_goals += vis_score
        if goals_high < vis_score:
            team_goals_high = visisting_team
            team_goals_high_type = 'VISITING TEAM'
            
print('Number of matchs: {}'.format(num_of_matchs))            
print('Number of wins by the home teams: {}'.format(num_of_home_wins))            
print('Number of wins by the visiting teams: {}'.format(num_of_visiting_wins))
print('Total number of goals scored by visiting teams: {}'.format(num_of_visiting_goals))

avg_home_goals = round(num_of_home_goals / num_of_matchs)
avg_visiting_goals = round(num_of_visiting_goals / num_of_matchs)

print('Total number of average goals scored by home teams: {}'.format(avg_home_goals))
print('Total number of average goals scored by visiting teams: {}'.format(avg_visiting_goals))

print('Total number of goals conceded by home teams: {}'.format(num_of_home_conceded))
print('Total number of goals conceded by visiting teams: {}'.format(num_of_visiting_conceded))

avg_home_conceded = round(num_of_home_conceded / num_of_matchs)
avg_visiting_conceded = round(num_of_visiting_conceded / num_of_matchs)

print('Total number of average goals conceded by home teams: {}'.format(avg_home_conceded))
print('Total number of average goals conceded by visiting teams: {}'.format(avg_visiting_conceded))
print('Total and average goal differential for the home teams: {}'.format(num_of_home_goals - avg_home_goals))

avg_winning_goals = round(num_of_winning_goals / num_of_matchs)
print('Total and average goal differential for the winning teams: {}'.format(num_of_winning_goals - avg_winning_goals))
print('Team with largest number of goals scored: {} - {}'.format(team_goals_high_type, team_goals_high))
