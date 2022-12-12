Wentao Mao: Complete the game framework, implement the function of dealing cards and self-selecting the number of computer players, and implement the judgment of ordinary colour number cards under the simple ui interface.<br /><br />
Hao Li: implemented the effect of colour function cards and black card function cards, and implemented the function of reshuffling discarded cards into the deck after it has been dealt.<br /><br />
The above two people have independently implemented different uno programs with simple ui, and have jointly developed the logic part of the game in the main project<br /><br />
Changjiang Huang: independently designed the complex ui for the entire game and assisted in the development of the start and checkout screens.He designed the pictures and added the background music.<br /><br />
Zongzhe Li: completed the development of the game start screen and the game checkout screen<br /><br />
Matthew Shelley: completed the background design and card design for the game interface<br /><br />
**********************************************************************************************************************************************************
DashBoardModule:This module is the settlement screen and contains a settlement class whose main function is to settle the player's score<br /><br />
GameModule:This module is the one that controls the entire operation of the game<br /><br />
StartMenuModule:This module is the start menu of the game and the player opens the game to see this screen<br /><br />
UserInterface:This module is the game's ui interface, through which players interact during gameplay<br /><br />
main:This module is the game's ui interface, through which players interact during gameplay<br /><br />

How the program work?<br />
The main.py would run a infinite loop. <br />
In the loop:
1. It would call startMenu.run() which would return the number of computer players that the user chosed.<br />
2. Then, the number of computer players would be passed into the Game's constructor.<br />
3. Then, game.run() which run a loop for the game kernal would be called after the game is initialized. In this run(), the game would call UserInterface.waitUserInput() and UserInterface.waitUserChooseColour and UserInterface.renderOutput whenever needed. The two waiting function would keep refreshing the pygame screen and return the user's decision, the render function would render the screen.<br />
4. Once the the game kernal noticed that there is a winner, it would return a data to main.py.<br />
5. Then, main.py would pass this data into the DashBoard's Constructor. This dashBoard.run() would be called to render the infomation of the game result and wait for the user's choice of whether play a new round or quit the game. The choice would be return to main.py. If return false, the infinite loop in main.py would stop, the pygame screen would close. Otherwise, the infinite loop would go back to the '1.'<br />
