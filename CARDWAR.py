import random

class deck:
    def __init__(self,suit,value):
        self.suits=suit
        self.values=value
        self.udeck=[]
    def createdeck(self):
        print("Creating your deck")
        for suit in self.suits:
            for value in self.values:
                self.udeck.append((suit,value))
        return self.udeck
    def shuflleNsplit(self):
        print("Shuffling and making two decks for both the players")
        random.shuffle(self.udeck)
        midIndex=len(self.udeck)/2
        return (self.udeck[:26],self.udeck[26:])
class hand:
    def __init__(self,cards):
        self.cards= cards
    def __str__(self):
        print(f"There are {len(self.cards)}")
    def addCards(self,cards):
        self.cards.extend(cards)
    def removeCard(self):
        return self.cards.pop()
class player:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def playCard(self):
        play=self.hand.removeCard()
        print(f"{play} card has been played")
        return play
    def checkCards(self):
        n=len(self.hand.cards)
        if n>0:
            return True
        else :
            return False
    def removeWarCards(self):
        warcards=[]
        for x in range(3):
            warcards.append(self.hand.removeCard())
        return warcards
if __name__=="__main__":
    suit=["D","H","C","S"]
    value="2 3 4 5 6 7 8 9 10 J Q K A".split()
    d=deck(suit,value)
    d.createdeck()
    pone,ptwo=d.shuflleNsplit()
    player1=player("computer",hand(pone))
    player_name=input("Enter your name")
    player2=player(player_name,hand(ptwo))
    rounds=0
    war_count=0
    while(player1.checkCards() and player2.checkCards()):
        table_cards=[]
        print("New round has begun")
        rounds += 1
        print(f"{player1.name} has {str(len(player1.hand.cards))} ")
        print(f"{player2.name} has {str(len(player2.hand.cards))} ")

        comp=player1.playCard()
        table_cards.append(comp)
        user=player2.playCard()
        table_cards.append(user)
        

        if comp[1]==user[1]:
            print("YOU'RE AT WAR")
            war_count+=1
            table_cards.extend(player1.removeWarCards())
            table_cards.extend(player2.removeWarCards())
            # draw a new card to decide the winner of this war
            comp=player1.playCard()
            table_cards.append(comp)
            user=player2.playCard()
            table_cards.append(user)

            if value.index(user[1])>value.index(comp[1]):
                player2.hand.addCards(table_cards)
                print(f"{player2.name} has won the round, adding to the hand.....")
            else:
                player1.hand.addCards(table_cards)
                print(f"{player1.name} has won the round, adding to the hand.....")
                
        else:
            if value.index(user[1])>value.index(comp[1]):
                player2.hand.addCards(table_cards)
                print(f"{player2.name} has won the round, adding to the hand.....")
            else:
                player1.hand.addCards(table_cards)
                print(f"{player1.name} has won the round, adding to the hand.....")
    print("Great Game, it lasted: "+str(rounds))
    print("A war occured "+str(war_count)+" times.")




        
        


 








