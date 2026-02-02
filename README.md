# uplaince-ai-assignment
Rock, paper, scissors game AI judge

Prompt for the game

Goal: Build a computer game called "Rock, Paper, Scissors, Bomb" featuring a window and clickable buttons.

Game Rules:

Standard Moves: Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
The Bomb: Bomb beats Rock, Paper, and Scissors.
One-Time Use: Both you and the computer can only use the Bomb move once during the match. Once it's played, it can't be used again for the rest of that match.
How It Should Work:

Buttons: The screen needs big, clear buttons for Rock, Paper, Scissors, and Bomb. They'll be your controls.
Bomb Status: There should be an on-screen message displaying if your Bomb is "Ready" or "Empty" so you always know if you can use it.
Bomb Button Lock: When you press Bomb, that button should immediately stop working for you for the rest of the match - no accidental double clicks allowed.
Computer's Bomb: The computer picks moves randomly, but it should stick to the same Bomb rule: only one Bomb per match, and if it's used, it's out.
Results Message: After each round, show a message that simply says: "bot won", "user won", or "its a draw match".
Play Again Option: After every turn, give me the option to play another round.


Why the prompt is written this way!

The prompt is designed so the computer picks up on three things you typically won't find in standard games:

1. Managing Resources (The 'One-Bomb' Rule)
Most games let you use moves as much as you want. By telling the AI to "Disable the button" and only let the bomb be used once, it has to keep track of what's happened. Skip that instruction and it'll just forget you already used the bomb last round.

2. Clear-Cut Input and Output (The 'Judge' Voice)
When we insist on phrases like "bot won", "user won", or "it's a draw match", the game comes off sharper and more reliable. This keeps the computer from going off-topic with long explanations, which helps the interface look crisp.

3. Behavior-Based Rules vs. Coding Jargon
The prompt talks about what the player sees, not the nitty-gritty code. That's intentional: It lets the AI figure out the best way to write the code on its own.

It keeps the user experience front and center - like making sure the button really does become unclickable at the right moment.




What failure cases you considered

1. the UI was not satisfactory


improvements

better UI
