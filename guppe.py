import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/digitalinnovationone/live-coding-evitando-o-7x1-com-python-e-sql/main/data.csv')
df.head()

import random

class Team:
    BEST_SCORE = 1837.6  # BRAsil
    
  # TODO: Definir um construtor com os atributos adequados (tendo em vista o conteúdo de uma célula do CSV)
    def __init__(self, cellData):
        teamData = cellData.split("|")
        self.name= teamData[0]
        self.score = float(teamData[1])
    def motivate(self):
        self.lastMotivation = random.uniform(70, (self.score * 100) / Team.BEST_SCORE)
    # TODO: Criar uma lógica para atribuir a motivação ao time.
        return self.lastMotivation


bestTeamsByGroup = {}
for label, content in df.items():
    team1 = Team(content[0])
    team2 = Team(content[1])
    team3 = Team(content[2])
    team4 = Team(content[3])
    
    bestTeamsByGroup[label] = sorted([team1, team2, team3, team4], key=Team.motivate, reverse=True)

for grupo, motivatedTeams in bestTeamsByGroup.items():
  print(f"Grupo {grupo}: ", end="")
  for team in motivatedTeams:
    print(f"{team.name} ({team.lastMotivation})"")

bestTeamsByGroup["A"][0]
team2A = bestTeamsByGroup["A"][1]
team1B = bestTeamsByGroup["B"][0]
team2B = bestTeamsByGroup["B"][1]
team1C = bestTeamsByGroup["C"][0]
team2C = bestTeamsByGroup["C"][1]
team1D = bestTeamsByGroup["D"][0]
team2D = bestTeamsByGroup["D"][1]
team1E = bestTeamsByGroup["E"][0]
team2E = bestTeamsByGroup["E"][1]
team1F = bestTeamsByGroup["F"][0]
team2F = bestTeamsByGroup["F"][1]
team1G = bestTeamsByGroup["G"][0]
team2G = bestTeamsByGroup["G"][1]
team1H = bestTeamsByGroup["H"][0]
team2H = bestTeamsByGroup["H"][1]

quarter1 = team1A if team1A.motivate() > team2B.motivate() else team2B
quarter2 = team1C if team1C.motivate() > team2D.motivate() else team2D
quarter3 = team1E if team1E.motivate() > team2F.motivate() else team2F
quarter4 = team1G if team1G.motivate() > team2H.motivate() else team2H
quarter5 = team1B if team1B.motivate() > team2A.motivate() else team2A
quarter6 = team1D if team1D.motivate() > team2C.motivate() else team2C
quarter7 = team1F if team1F.motivate() > team2E.motivate() else team2E
quarter8 = team1H if team1H.motivate() > team2G.motivate() else team2G

print(f"{team1A.name} ({team1A.lastMotivation:.2f}) x {team2B.name} ({team2B.lastMotivation:.2f})")
print(f"{team1C.name} ({team1C.lastMotivation:.2f}) x {team2D.name} ({team2D.lastMotivation:.2f})")
print(f"{team1E.name} ({team1E.lastMotivation:.2f}) x {team2F.name} ({team2F.lastMotivation:.2f})")
print(f"{team1G.name} ({team1G.lastMotivation:.2f}) x {team2H.name} ({team2H.lastMotivation:.2f})")
print(f"{team1B.name} ({team1B.lastMotivation:.2f}) x {team2A.name} ({team2A.lastMotivation:.2f})")
print(f"{team1D.name} ({team1D.lastMotivation:.2f}) x {team2C.name} ({team2C.lastMotivation:.2f})")
print(f"{team1F.name} ({team1F.lastMotivation:.2f}) x {team2E.name} ({team2E.lastMotivation:.2f})")
print(f"{team1H.name} ({team1H.lastMotivation:.2f}) x {team2G.name} ({team2G.lastMotivation:.2f})")


# TODO: Simular os confrontos das Quartas de Final (randomizando novamente suas respectivas motivações).
#       Além disso, também definir os classificados para as semifinais em novas vaiáveis:
semi1 = quarter1 if quarter1.motivate() > quarter2.motivate() else quarter2
semi2 = quarter3 if quarter3.motivate() > quarter4.motivate() else quarter4
semi3 = quarter5 if quarter5.motivate() > quarter6.motivate() else quarter6
semi4 = quarter7 if quarter7.motivate() > quarter8.motivate() else quarter8

# TODO: Imprimir os "resultados" dos confrontos realizados nas Quartas de Final:
print(f"{quarter1.name} ({quarter1.lastMotivation:.2f}) x {quarter2.name} ({quarter2.lastMotivation:.2f})")
print(f"{quarter3.name} ({quarter3.lastMotivation:.2f}) x {quarter4.name} ({quarter4.lastMotivation:.2f})")
print(f"{quarter5.name} ({quarter5.lastMotivation:.2f}) x {quarter6.name} ({quarter6.lastMotivation:.2f})")
print(f"{quarter7.name} ({quarter7.lastMotivation:.2f}) x {quarter8.name} ({quarter8.lastMotivation:.2f})")


# TODO: Simular os confrontos das Semifinais (randomizando novamente suas respectivas motivações).
#       Além disso, também definir os classificados para a final e disputa de 3º e 4º em novas vaiáveis:
final1 = semi1 if semi1.motivate() > semi2.motivate() else semi2
terceiro1 = semi1 if semi1.lastMotivation < semi2.lastMotivation else semi2

final2 = None
terceiro2 = None
if semi3.motivate() > semi4.motivate():
  final2 = semi3
  terceiro2 = semi4
else:
  final2 = semi4
  terceiro2 = semi3

# TODO: Imprimir os "resultados" dos confrontos realizados nas Semifinais:
print(f"{semi1.name} ({semi1.lastMotivation:.2f}) x {semi2.name} ({semi2.lastMotivation:.2f})")
print(f"{semi3.name} ({semi3.lastMotivation:.2f}) x {semi4.name} ({semi4.lastMotivation:.2f})")


winner = final1 if final1.motivate() > final2.motivate() else final2
second = final1 if final1.lastMotivation < final2.lastMotivation else final2
third = terceiro1 if terceiro1.motivate() > terceiro2.motivate() else terceiro2
fourth = terceiro1 if terceiro1.lastMotivation < terceiro2.lastMotivation else terceiro2

print(f"1º: {winner.name} ({winner.lastMotivation:.2f})")
print(f"2º: {second.name} ({second.lastMotivation:.2f})")
print(f"3º: {third.name} ({third.lastMotivation:.2f})")
print(f"4º: {fourth.name} ({fourth.lastMotivation:.2f})")