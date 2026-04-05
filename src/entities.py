class BandMember:
    def __init__(self, name, instrument, health):
        self.name = name
        self.instrument = instrument
        self.hp = health
        self.max_hp = health
        # Each member brings 2 unique signature cards to the deck
        self.signature_cards = [] 

class Stage:
    def __init__(self):
        self.members = []
        self.shared_deck = []
        self.shared_energy = 3
        
    def add_member(self, member):
        self.members.append(member)
        # When a member joins, their cards are shuffled into the main deck
        self.shared_deck.extend(member.signature_cards)
