class Player:
    """Represents a player in catan

    Attributes: name, points, bonuses, hand, buildings, soldiers, devcards
    """

    def __init__(self):
        self.name = raw_input("Player Name? ")
        self.points = 0
        self.bonuses = {'longestRoad':False, 'largestArmy': False}
        self.hand = {'ore':0,'lumber':0,'brick':0,'sheep':0,'grain':0}
        self.buildings = []
        self.soldiers = 0
        self.devcards = {}
        self.roads = []
        #self.hist is a dic mapping dice roll to cards a person goes        
        self.hist = {2:{},3:{},4:{},5:{},6:{},8:{},9:{},10:{},11:{},12:{}}

    def __str__(self):
        if len(self.buildings) == 0:
            buildings = "No Buildings"
        return """%s has: \n %d points
Longest Road? %s 
Largest Army? %s 
%d soldiers
""" % (self.name,self.points,'{longestRoad} {largestArmy}'.format(**self.bonuses),buildings,self.soldiers)

    def buildHist(self): # not done
        for building in self.buildings:
            resource = building.resProv

    def takeCards(self, d):
        """ Takes a player and gives them resource cards

        Input: Player object and a dictionary of resource String mapped to number of resources
        """
        for resource in d:
            self.hand[resource] =  (self.hand[resource]) + (d[resource])
      

    def payCards(self,d):
        """ Takes a player and removes the dictionary of resource cards 
        from the players hand

        Input: Player object and a Resource Card String
        """
        for resource in d:
            if self.hand[resource] < d[resource]:
                print "player has insufficient cards" 
                return None           
        for resource in d:         
            self.hand[resource] =  self.hand[resource] - d[resource]
        


    def calcPoints(self):
        """Calculates the number of points for the player

        Input: Player obj

        Returns: int points
        """

        points = 0
        for i in range(0,len(self.buildings)):
            if (self.buildings[i]).isCity():
                points += 2
            else:
                points += 1

        if self.bonuses['longestRoad']:
            points +=2
        if self.bonuses['largestArmy']:
            points +=2
        points += self.bonuses['devPoints']
        self.points = points
        return points

def trade(player1,resources1, player2, resources2):
    """ Commits a trade between two players. May be able to 
    trade something for nothing 

    Input: 2 player objects and two dictionary of resources saying what
    each player is offering 
    """
    for resources in resources1:
        if player1.hand[resources] < resources1[resources]:
            print "Player 1 has insufficient resources"
            return None
    for resources in resources2:
        if player2.hand[resources2] < resources2[resources]:
            print "Player 2 has insufficient resources"
            return None
    player1.payCards(resources1)
    player2.takeCards(resources1)
    player2.payCards(resources2)
    player1.takeCards(resources2)

#    def build(self,)

def main():
    pass 

if __name__ == '__main__':
    main()

