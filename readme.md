
# Ouiz -  Milestone project 3 Code Institute



## Summary:

 The purpose of the project is to build a full-stack site where user can 
 play quiz, tracked his score and admin can easily modify data base add new 
 questions, delete old ones and to delete users.
 This site allows user to play short quiz with general knowledge and track 
 his score history

### Project has the following sections:  

- Home page contains image and navigation bar with access to login, register, admin

- Login page contains username field, pasword filed and login button


- Register page contains fields: first name, last name, username, email, password, confirm password and register button

- Admin page contains sections: home, user, questions, quiz taken



## Structure and design: 

### Fonts:

- For projects was used font Roboto from Google Fonts

### Colors:

- Dark grey color was used for navigation bar to fit with image on home page

- Red color was chosen for hover element above of navigation bar

### Images:

- Welcome image was downloaded from [WallpaperAccess](https://wallpaperaccess.com/quiz)


### Wireframes:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/Home%20page%20wireframe.JPG)

- [Login Page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/login%20page%20wireframe.JPG)

- [Register Page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/register%20page%20wireframe.JPG)

- [Admin](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/admin%20page%20wireframe.JPG)


## UX stories:
 
 ### As admin I want to:

 - easy access change database questionsa, to add  new one question  and to delete user
 
 ### As user I want to:

 - easy to register

 - easy to login

 - to play general knowledge quiz

 - to track my previous score


 ## Technology used:

 - HTML5

 - CSS

 - Python

 - Google Fonts
 
 - Bootstrap 

 - Flask-mongoengine to add package to enable comunication with  MongoDB database

 - Flask-WTF standard flask package for WTF forms

 - Flask-Admin-package to enable admin view - to dispaly models and to enable manipulation with data on the website instead rellying on some other GUI tool.
 


 ## Tools used:

- Visual code studio

- Git pod

- Github used for repository hosting service 

- [Herouku](https://dashboard.heroku.com/apps) used to deploy web application

- [MongoDB](https://www.mongodb.com/) used as database storage 

- [W3C Validator](https://validator.w3.org/) used to validite HTML code 

- [W3C CSS Validation Service Jigsaw](https://jigsaw.w3.org/css-validator/) to validate CSS code 

- [PEP8 online Validator](http://pep8online.com/) to validate 

- Python code

- Moquaps used to make wireframes

## Testing:

Application was tested on Chrome and Firefix browsers.

Functionality tested:

- that hover element changing color on navigation bar

- that every link is opening right template 

- that user registration is functional

- that login is functional

- that quiz is functional

- that admin can delete users

- that admin can add new or to remove old questions

- that password matched

- that password has enough length

- that username has enough lenght

### Code Validation:

- HTML code was validated using W3C Markup Validation Service, no errors found html [html base validator](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/base%20html%20validator.JPG)

- CSS code was validated using W3C CSS Validation Service Jigsaw, no errors were found [CSS validator](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/css%20validator.JPG)

- Python  code was validated using PEP8 online checker, no errors found [main python](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/main%20py%20validator.JPG)

- Jinja templetes were unable to valdidate : 

[index](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/index%20html%20validator.JPG)

[login](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/login%20html%20validator.JPG)

[quiz complete](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/quiz%20complete%20html%20validator.JPG)

[quiz](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/templates/quiz.html)

[quiz overview](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/templates/quiz_overview.html)

[register](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/templates/register.html)



## Deployment:

- Project has been deployed at Github and Herouku


## Further Development:

- Plans for further development are to add more questions to database, to add more quizzes
and to add area to show tables with scores.

## Conclusion:

- This project was build only for educational purpose and won`t be in commercial use.
