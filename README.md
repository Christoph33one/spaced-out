# Spaced Out. 🚀

👨🏻‍🚀 Spaced Out is a short quiz on space travel. This quick quiz will test your space knowledge on planets, rocket science and space history. Just take your time to answer as best as you can, enjoy and good luck!

# List of contents
<li><a href="#design ">Design</a></li>
<li><a href="#user-experience ">User Experience</a></li>
<li><a href="#future-features">Future features</a></li>
<li><a href="#technologies">Technologies</a></li>
<li><a href="#flowchart">Flowchart</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#deployment">Testing</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
<li><a href="#credits">Credits</a></li>

---
# Design

- For the design aspect of this game I wanted the user to be involved from the start and to have inputs to enter the game.

- As this is a quiz about space, I wanted to incorporate some ideas which can relate to rockets, so I added a countdown sequence at the very start.

- I have used emoji's to give this game more of an inertative feel, I believe images are big part in making a game look and feel fun, which is the whole idea to a game.

- Spaced Out isn't just about answering space questions, but also to the give the user a bit more knowledge into space, space technology and space history.

--- 
# User experience

- From the start of the game, a message will display an welcome message and some brief game instructions.

    ![](assets/images/Screenshot%202022-11-29%20at%2023.09.30.png)

- Next is a user input method to enter a name. The name must be more than 4 letters to enter the game.

    ![](assets/images/user%20name.png)

- Once the user has entered a name and pressed enter, a countdown sequence with count down from 5.

    ![](assets/images/count%20down.png)

- Then the first question will appear with a set of three choices, one of which is the correct answer. 

- User to then enter an answer bofore the next question is shown.

    ![](assets/images/questions%20and%20asnswers.png)

- Once all questions have been answered, the user will be given a final score of how many they managed to answer correct.
ADD A FINAL SCORE PICTURE HERE!!!!!!!

- End of game will give the user an option to replay by entering y, which returns to entering a name. Or to quite, enter n for the game to finish and take the user back to the very start.

ADD END OF GAME PICTURE HERE!!!!!!!!
---
# Future features
- To add more levels to the game, the higher the level, the harder the questions.

- Count down timer to answer all qustions before the game ends.

- Randomise questions.

- Give a leader board for highest score.

--- 

# Technologies 
- All Python mark up was created in a Gitpod workspace.

- Gitpod workspace is then linked to a Github repository. 
https://github.com/

- A hosting cloud platform called Heroku was used to deploy the Github repository, as Heroku is designed to run backend languages such as Python. 
https://id.heroku.com/

- Lucidchart was used for the initial planning by creating a flow chart for the functioning of the game.
https://lucid.app/

--- 

# Flowchart
 
 - For the planing and management of this project, I used a workflow constructor called Lucid Spark. By mapping out the game function, this helped in keeping the build process up to date with what each function is achieving and to give clear instructions on the next task. 
 https://lucid.app

    ![](assets/images/flow%20chart.png)
---

# Testing

- For the testing purposes of this game, I used the internal PEP8 validation which is a build in validator in Gitpod.

 THAKE PICURE OF ERROR TRERMINAL IN WORKSPACE !!!!!!

- The project has been tested on both Google Chrome and Safari in which the game funcions efficiently.

--- 

# Bugs & Error handling 

- In the build process of this game, I ran multiple error checks throughout as to keeping a constant update on fixing and documenting errors. 

- ERROR - White spaces
- SOLUTION - Using the backspace key to clear all white spaces with the mark up

- ERROR - Wrong indentation with a For loop in the main function.
- SOLUTION - I used a Python Formator to check that when creating a for loop, that the indentation matches what to what the formator shows to clear all indentation erros.
    https://www.w3schools.com/python/gloss_python_indentation.asp

- ERROR - Adding an incorrect argument into the show next question function. 
- SOLUTION - I wanted to show the user each question from a key's value. In doing so, I created a for loop to irritate through a dictationary of keys and their values. 
When calling the show next question function in the main function, I had trouble working out the correct value I want to pass as an argument. After reviewing my code and with some online help, I managed to pass the correct value to the called function to show the key's values.

- ERROR - ADDING A COUNT DOWN TIMER
- SOLUTION - When creating a count down timer, I did not import time. As a result, the functionality of the timer would give an error. Once I had used (import time), the timer function worked as expected.

---
# Deployment 

- In keeping with the rules of deployment with Code Institute, I had to deploy this project using Heruko. 

- Go to the following webpage: https://id.heroku.com/login

- Create a Heruko account linked to your email address.
    ![](assets/images/heruko%20log%20in.png)

- Once logged in, create a new app which is placed in the top right corner.
    ![](assets/images/new%20app%20heruko.png)

- Within new app, click settings and scoll to (build packs)
![](assets/images/build%20packs%20heruko.png)

- Build packs let you select a choice of different technology's which you may be using to build a project. For my project I selected Python and Node JS.

- Node JS build pack is to run the template which I have used to build my repository in Github, supplied with code Institute. The Python build pack is to tell Heruko what language was used and what will to deploy.

- If you are using an external source for data or an API, please add the key and port in the Config var section. (Please read the instructions given!)

- At the top of the page, Open deployment from the same tool bar as to settings. Scroll down to the deployment method and select GitHub. From here you will be asked to authorise that Heruko will link to your GitHub repository. 
    ![](assets/images/deployment%20method%20heruko.png)

- Next you should notice that Heruko has now linked to GitHub, to retrieve data.

- From the bottom of the deployment page, please select what branch (main) you will be using. Click deploy branch and wait for the deployment to take place. Heruko will start showing a build log, this log is part of the deployment process and will also show any errors if your project is not deployed correctly. Once deployed, you app will open in a new browser window.
    ![](assets/images/deployment%20heruko.png)

- Click to view the deployed app. 
    ![](assets/images/deployed%20app%20heruko.png)
--- 

# Acknowledgments 
- To get the game questions and answers I used a Google search to see what options I had. I found a great and easy site to copy from.
https://quizglobal.com/quizplay/quizplayqanda/Space%20Quiz%20Questions%20and%20Answers

- When writing my Python mark up in Github, I used W3 Schools and Python starter help me write some of the correct syntax and methods used in this project.
https://www.w3schools.com/python/
https://www.python.org/about/gettingstarted/

- With the help of my mentor, I used a good template to plan out what needed to be achieved first and what could be added in later updates. This is very effective way to achieve the main objective first.

# Credits
- I would like to say a thank you to Code Institute for giving me the tools to build my 3rd milestone project and also my first project using Pyhton.

- A big thank you to my mentor for keeping me on track with the build stages and giving me valuable advise with key areas.

- The Slack community has been a great help when I needed it the most, so a thank you to all that answered my qustions and guided me in the process to build the project.


