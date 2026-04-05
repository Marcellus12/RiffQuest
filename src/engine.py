class ComboEngine:
    def __init__(self):
        self.last_instrument = None
        self.combo_count = 0

    def calculate_effect(self, card, player, enemy):
        final_vol = card.volume
        final_har = card.harmony
        msg = ""

        # SYNERGY LOGIC: 
        # If last card was Drums, and this is Guitar -> Double Damage (The "Riff" Bonus)
        if self.last_instrument == "Drums" and card.instrument == "Guitar":
            final_vol *= 2
            msg = "SYNERGY: Drum Fill boosted the Riff!"

        # If last card was Bass, and this is Drums -> Extra Harmony (The "Groove" Bonus)
        elif self.last_instrument == "Bass" and card.instrument == "Drums":
            final_har += 5
            msg = "SYNERGY: Locked into the Groove! +5 Harmony"

        # Apply results
        enemy.health -= final_vol
        player.block += final_har
        
        # Update tracker
        self.last_instrument = card.instrument
        return msg
