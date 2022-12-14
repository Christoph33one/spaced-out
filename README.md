# Spaced Out. 🚀

👨🏻‍🚀 Spaced Out is a short quiz on space travel. This quick quiz will test your space knowledge on planets, rocket science and space history. Just take your time to answer as best as you can, enjoy and good luck!

# List of contents
<li><a href="#design ">Design</a></li>
<li><a href="#user-experience ">User experience</a></li>
<li><a href="#future-features">Future features</a></li>
<li><a href="#technologies">Technologies</a></li>
<li><a href="#flowchart">Flowchart</a></li>
<li><a href="#testing">Testing</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#acknowledgments">Acknowledgments</a></li>
<li><a href="#credits">Credits</a></li>

---
# Design

- For the design aspect of this game I wanted the user to be involved from the start and to have a command  to enter their name.

- As this is a quiz about space, I wanted to incorporate some ideas which can relate to rockets, so I added a countdown sequence at the very start.

- I have used emojis to give this game more of an interactive feel, I believe images are big part in making a game look and feel fun, which is the whole idea of a game.

- Spaced Out isn't just about answering space questions, but also about giving the user a bit more knowledge into space, space technology and space history. After the user answers a question correct or incorrect, a short piece of information about the question and the correct answer will appear. This is the educational part for the user to learn a bit more about space. 

--- 
# User experience

- From the start of the game, a welcome message and game instructions will appear.

    ![](assets/images/Screenshot%202022-11-29%20at%2023.09.30.png)

- Next the user must enter a name. The user has to choose a name with more than four letters or the game will not start.

    ![](assets/images/user%20name.png)

- Once the user has entered a name and pressed enter, a countdown sequence will count down from 5.

    ![](assets/images/count%20down.png)

- Then the first question will appear with a set of three choices, one of which is the correct answer. 

    ![](assets/images/answer%20info.png)

- The user must aways answer A, B or C. If not then an error message will appear and give the user a chance to submit another answer.

    ![](assets/images/error%20message%20for%20correct%20answer.png)

- After each question has been answered, a message will display if the user got a correct or incorrect answer. If correct, a score of 1 point will be added. The user can then see how many questions they have correct and compare against the list of 10 questions.

    ![](assets/images/adding%20score%20to%20correct%20question.png)

- Once all the questions have been answered, the user will be given a final score of how many they managed to answer correct.

- At the end of the game, the user will be given an option to replay by entering y, which returns to entering a new name, or to quitting the game by entering any key. This takes the user back to the very start.

    ![](assets/images/end%20of%20game%20score.png)
---
# Future features
- Adding more levels to the game, the higher the level, the harder the questions.

- A count down timer to answer all qustions before the game ends.

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
 
 - For the planing and management of this project, I used a workflow constructor called Lucid Spark. Mapping out the game function has helped keeping the build process up to date with what each function is achieving and giving clear instructions on the next task. 
 https://lucid.app

    ![](assets/images/new%20flowchart.png)
---

# Testing

- For the testing purposes of this game, I used the internal PEP8 validation which is a build in validator in Gitpod.

    ![](assets/images/pep8%20validator.png)

- The project has been tested on both Google Chrome and Safari in which the game funcions efficiently.

--- 

# Bugs & error handling 

- In the build process of this game I ran multiple error checks throughout to keep constant updates on handling and documenting errors. 
---
- ERROR - White spaces
- SOLUTION - Using the backspace key to clear all white spaces within the mark up.
---
- ERROR - Wrong indentation with a For Loop in the main function.
- SOLUTION - I used a Python Formator to check that when creating a For Loop, the indentation matches the formator and clears the error.
    https://www.w3schools.com/python/gloss_python_indentation.asp
---
- ERROR - Adding an incorrect argument into the show_next_question function. 
- SOLUTION - I wanted to show the user each question from a dictionary by retrieving a key value. In doing so, I created a For Loop to iterate through the dictationary of keys and their values. 
When calling the show_next_question function in the main function, I had trouble working out the correct value I wanted to pass as an argument. After reviewing my code and with some online help, I managed to pass the correct value (argument) to the called function to show the user a question.
---
- ERROR - ADDING A COUNT DOWN TIMER
- SOLUTION - When creating a count down timer, I did not import time. As a result, the functionality of the timer would give an error. Once I had used (import time), the timer function worked as expected.
---
- ERROR - An error in the build log for when deploying this project to Heruko.
- SOLUTION - Once going over the documention in Heruko, I realised that I had to add a requiremts.txt as a file in my workspace. Once this file was in place, I then had to enter the following command in the terminal of my work space. 
( pip freeze > requirements.txt ) 
After running this command, I had to git add, commit and push my project before deploying with Heruko once more.

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

- Build packs let you select a choice of different technologys which you may be using to build a project. For my project I selected Python and Node JS.

- Node JS build pack is to run the template which I have used to build my repository in Github, supplied with code Institute. The Python build pack is to tell Heruko what language was used and what will be deploy.

- If you are using an external source for data or an API, please add the key and port in the Config var section. (Please read the instructions given!)

- At the top of the page, Open deployment from the same tool bar as to settings. Scroll down to the deployment method and select GitHub. From here you will be asked to authorise that Heruko will link to your GitHub repository. 
    ![](assets/images/deployment%20method%20heruko.png)

- Next you should notice that Heruko has now linked to GitHub to retrieve data.

- From the bottom of the deployment page, please select what branch (main) you will be using. Click deploy branch and wait for the deployment to take place. Heruko will start showing a build log, this log is part of the deployment process and will also show any errors if your project is not deployed correctly. Once deployed, your app will open in a new browser window.
    ![](assets/images/deployment%20heruko.png)

- Click to view the deployed app. 
    ![](assets/images/deployed%20app%20heruko.png)
--- 

# Acknowledgments 
- To get the game questions and answers I used a Google search to see what options I had. I found a great and easy site to copy from.
https://quizglobal.com/quizplay/quizplayqanda/Space%20Quiz%20Questions%20and%20Answers

- When writing my Python mark up in Github, I used W3 Schools and Python starter to help me write some of the correct syntax and methods used in this project.
https://www.w3schools.com/python/
https://www.python.org/about/gettingstarted/

- With the help of my mentor, I used a good template to plan out what needed to be achieved first and what could be added in later updates. This was a very effective way to achieve main objectives first.

# Credits
- I would like to say a thank you to Code Institute for giving me the tools to build my 3rd milestone project and also my first project using Pyhton.

- A big thank you to my mentor for keeping me on track with the build stages and giving me valuable advise within key areas.

- The Slack community has been a great help when I needed it the most, so a thank you to all that answered my qustions and guided me in the process to build the project.


