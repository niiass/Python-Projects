# THE CARD GAME

## Game Rules

This is a fast-paced card game for three players, where luck and a bit of strategy determine the winner. Each player is dealt five cards, and their goal is to surpass their opponents in points (see below).

> * At the start of the game, after the cards are dealt, each player has the option to replace one of their cards with a random card from the undealt deck. This way, a seemingly losing hand might not end in defeat after all!
> * The cards to be dealt come from 4 standard decks of cards; therefore, during the game, only 4 identical cards can exist at any given time.
> * When a player loses or decides to replace a card, the used card is returned to the deck.
> * Players count and compare their points (see the point distribution below).
> * If a winner cannot be determined by points (a tie), the suits are compared (♥️ Hearts, ♠️ Spades, ♦️ Diamonds, ♣️ Clubs).
> * If there is still a tie (which is very rare), the winner is determined by the number of cards with the same rank/value (🂢 numbers, 🂾 Kings, 🂽 Queens, 🂫 Jacks, 🂡 Aces).

### Player Points Calculation: 
> * 🂢 Cards 2 through 10 - Points are equal to the card's number (e.g., 3 of Clubs is worth 3 points).
> *  🂫 Jack - 11 points 
> *  🂽 Queen - 12 points 
> *  🂾 King - 13 points
> *  🂡 Ace - 20 points

----
## Program Design

We utilized elements of both Functional Programming (FP) and Object-Oriented Programming (OOP) to achieve the desired functionality.

The program is distributed in 4 files: **"winner.py"**, **"manager.py"**, **"dealer.py"**, **"main.py"**.

----
## How Our Program Works

* main.py - This is where the entire game "loop" starts and ends.

* manager.py - Contains two classes: Card and Player, which are necessary for subsequent operations.

* dealer.py - Handles user name input and card dealing functionality. It stores standard card suits and ranks (**\_\_SUITS\_\_ , \_\_RANKS\_\_**) and the available deck (**four_decks**) 

* winner.py - Manages the process of the game, starting from score calculation and ending with determining the winner and loser.
----
## The Most Challenging Parts

1. Implementing the winner logic
2. Collaborating with others on the same code

-------
# Appendix/Conclusion

## Libraries and Imports Used

1. random - Used for selecting a "random" element from an array
2. time - Used to pause for a few seconds in the console (for visual effects)
3. collections - Used to count identical card suits and values
```python
import random
import time
from collections import Counter
```
## Team Members

Nia Gogilidze - https://github.com/niiass

Besik Meskhia - https://github.com/Besika40k

Lika Bazghadze - https://github.com/likabazgh