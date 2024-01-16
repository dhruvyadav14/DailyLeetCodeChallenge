from ast import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #keep a winner map, where the key is the winning player and the value is a list of players they have beaten
        #to me this looks like a graph problem
        #keep track of list of players. loop through matches, add to this list if the player is not already in it
        #in the same loop, add to the lostOnceList. get the loser, add to this list if hes not in it. if he is, dont add him

        allPlayers = set()
        losersCount = {}
        for winner, loser in matches:
            allPlayers.update({winner, loser})
            losersCount[loser] = losersCount.get(loser, 0) + 1
        
        allLosers = {player for player in losersCount.keys()}

        lostOnce = list(sorted({player for player, value in losersCount.items() if value ==1}))
        neverLost = list(sorted(allPlayers-allLosers))
        return [neverLost,lostOnce]