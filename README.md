## Task Assignment
Wentao Mao: Complete the game framework, implement the function of dealing cards and self-selecting the number of computer players, and implement the judgment of ordinary colour number cards under the simple ui interface.<br /><br />
Hao Li: implemented the effect of colour function cards and black card function cards, and implemented the function of reshuffling discarded cards into the deck after it has been dealt.<br /><br />
The above two people have independently implemented different uno programs with simple ui, and have jointly developed the logic part of the game in the main project<br /><br />
Changjiang Huang: independently designed the complex ui for the entire game and assisted in the development of the start and checkout screens.He designed the pictures and added the background music.<br /><br />
Zongzhe Li: completed the development of the game start screen and the game checkout screen<br /><br />
Matthew Shelley: completed the background design and card design for the game interface<br /><br />
## FileInfo
LabelModule.py
This module is to set font text properties

StartMenuModule.py
This module is the homepage of the game, where you can select the corresponding number of AI players according to the number of ducks

GameModule.py
This module realize the main logic of the game running and control the running speed

UserInterface.py
This module is responsible for game interface screen rendering and event triggering

DashBoardModule.py
This module is the game end interface, displaying the scoreboard, you can choose whether to continue the game or exit

main.py
The main entrance of the game running

## How the program work?<br />
The main.py would run an infinite loop. <br />
In the loop:
1. It would call startMenu.run() which would return the number of computer players that the user chosed.<br />
2. Then, the number of computer players would be passed into the Game's constructor.<br />
3. Then, game.run() which run a loop for the game kernal would be called after the game is initialized. In this run(), the game would call UserInterface.waitUserInput() and UserInterface.waitUserChooseColour and UserInterface.renderOutput whenever needed. The two waiting function would keep refreshing the pygame screen and return the user's decision, the render function would render the screen.<br />
4. Once the the game kernal noticed that there is a winner, it would return a data to main.py.<br />
5. Then, main.py would pass this data into the DashBoard's Constructor. This dashBoard.run() would be called to render the infomation of the game result and wait for the user's choice of whether play a new round or quit the game. The choice would be return to main.py. If return false, the infinite loop in main.py would stop, the pygame screen would close. Otherwise, the infinite loop would go back to the '1.'<br />

## ReferenceList：

1. LabelModule.py 
copied from Dr Daniel Karapetyan's example

2. Fonts

times new roman bold italic.ttf
This font is downloaded from the website: https://freefontsfamily.com

farmbright.ttf
This font is downloaded from the website: https://font.chinaz.com

3. Image

duck.png duck1.png duck2.png duck3.png duck4.png
These images are downloaded from the website: www.flaticon.com

4. Audio

90SecondsOfFunk.mp3
This music is downloaded from the website: https://audionautix.com/
