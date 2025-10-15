class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        voting = True
        winner = ''

        while voting:
            if 'R' not in senate:
                voting = False
                winner = 'Dire'
            elif 'D' not in senate:
                voting = False
                winner = 'Radiant'
            else:
                voter = senate.pop(0)
                if voter == 'R':
                    senate.remove('D')
                else: senate.remove('R')
                senate.append(voter)
        return winner
