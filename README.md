# hs-tournament-lineup-optimizer
Given matchup winrates, we answer the question, "What's the optimal tournament lineup?"

## INITIAL VERSION (BAN CHOOSER) MOSCOW
MUST HAVE
    * user can view the recommended optimal ban and win percentage for a Conquest format given the lineups and win rates
    * user can fill in matchups.xlsx with meta decks and win rates
    * user can input their lineup of 4 decks and an opponent's lineup of 4 decks via the CLI

SHOULD HAVE

COULD HAVE
    * program also supports Last Hero Standing

WONT HAVE
    * lineup recommendation
    * deck game order recommendation

## FUTURE VERSION PLANS
INPUTS:
    * meta deck frequency (via matchups.xlsx)
    * meta deck matchup data (via matchups.xlsx)
    * number of decks to bring
    * ban or no ban?
    * last hero standing or conquest?
OUTPUT:
    * highest winrate lineup + ban
