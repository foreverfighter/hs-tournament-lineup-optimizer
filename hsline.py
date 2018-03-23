#!usr/bin/env python

# user inputs deck matchup winrates in a dictionary, with an tuple as the key and the winrate as the value
# user must specify last hero standing or conquest
# user must specify 3 decks or 4 decks
# INPUT:
#   meta decks
#   deck matchup winrates (in a dictionary, tuple key winrate value)
#   can input deck matchup archetype winrates (eg fatigue warrior vs control 70% wr)
#   format(no. of games/bans)
#   last hero standing or conquest
# OUTPUT:
#   highest winrate lineup + ban

META_DECKS = [
    "Jade Druid",
    "Spiteful Druid",
    "Spell Hunter",
    "Secret Mage",
    "Big Spell Mage",
    "Exodia Paladin",
    "Murloc Paladin",
    "Silver Hand Recruit Paladin",
    "Dragon Priest",
    "Spiteful Dragon Priest",
    "Control Demon Warlock",
    "Cube Warlock",
    "Warlock Zoo",
    "Fatigue Warrior",
]

