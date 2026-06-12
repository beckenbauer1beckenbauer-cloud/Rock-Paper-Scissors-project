import RPS_game
from RPS import player
from RPS_game import play, mrugesh, abbey, quincy, kris

print("=" * 50)
print("  LAUNCHING ROCK PAPER SCISSORS AI TOURNAMENT  ")
print("=" * 50)

# Testing our AI player against the 4 baseline freeCodeCamp bots
print("\n[Match 1] Playing against Quincy (1000 games)...")
play(player, quincy, 1000, verbose=False)

print("\n[Match 2] Playing against Abbey (1000 games)...")
play(player, abbey, 1000, verbose=False)

print("\n[Match 3] Playing against Kris (1000 games)...")
play(player, kris, 1000, verbose=False)

print("\n[Match 4] Playing against Mrugesh (1000 games)...")
play(player, mrugesh, 1000, verbose=False)

print("\n" + "=" * 50)
print("Tournament Completed. Check accuracy percentages above!")
print("=" * 50)
