# Ouiz -  Milestone project 3 Code Institute



## Summary:

The purpose of the project is to build a full-stack site where users can play the quiz, tracked their scores and admin can easily modify data base, add new questions, delete old ones and to delete users.

This site allows users to play short general knowledge quiz and to track their scores.

### The project has the following sections:  

- Home page contains main image and navigation bar with access to quiz, login, register

- Login page contains username field, password filed and login button

- Register page contains fields: first name, last name, username, email, password confirm password and register button

- Quiz page contains quiz for play after user / admin has been logged in

- Settings page for changing user details and passwords 

- Admin page, only accessible  for Admin


## UX stories:
 
 ### Admin stories:

 - As an admin I would like to be able to add new questions, to add and to delete users

 - As an admin I would like to add users and to delete them

 - As an admin I would like to
 
 ### User stories:

 - As a user I would like to register

 - As a user I would like to login

 - As a user I would like to play general knowledge quiz

 - As a user I would like to track my previous score

## Structure and design: 

### Wireframes:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/Home%20page%20wireframe.JPG)

- [Home page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/home%20page%20wireframe%20mobile.JPG)

- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/login%20page%20wireframe.JPG)

- [Login page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/login%20page%20wireframe%20mobile.JPG)

- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/register%20page%20wireframe.JPG)

- [Register page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/register%20page%20wireframe%20mobile.JPG)

- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/admin%20page%20wireframe.JPG)

- [Admin page mobile](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/wireframes/admin%20page%20mobile%20wireframe.JPG)

### Design and colors:

#### Fonts:

- I used Roboto from, from Google Fonts

#### Color:

 - Navigation bar color [#333](https://htmlcolors.com/hex/333)
 - Primary background color [#F5F5F5](https://www.color-hex.com/color/f5f5f5)
 - Navigation bar links []
 - 

#### Design

- [Home Page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/home_page_image.JPG)

- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/login_page_image.JPG)

- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/quiz_page_image.JPG)

- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/register_page_image.JPG)

- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/settings_page_image.JPG)

- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/admin_page_image.JPG)

### Technology Used:

 - HTML5
 - CSS3
 - [Bootstarp5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
 - [Python](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/requirements.txt)
 - 

 ### Tools Used:

 - Visual code studio
 - Git pod
 - Github for repository hosting service
 - [Heroku](https://dashboard.heroku.com/apps) to deploy web application
 - [MongoDB](https://www.mongodb.com/cloud/atlas/lp/try2-de?utm_content=rlsapostreg&utm_source=google&utm_campaign=gs_emea_rlsamulti_search_brand_dsa_atlas_desktop_rlsa_postreg&utm_term=&utm_medium=cpc_paid_search&utm_ad=b&utm_ad_campaign_id=14412646473&gclid=EAIaIQobChMItZq0nt358gIVDpftCh3FhQRAEAAYASAAEgKGnfD_BwE) for database
 - [PEP8](http://pep8online.com/) online for validation of Python code 
 - [W3C](https://validator.w3.org/) for HTML validation
 - [Jigsaw](https://jigsaw.w3.org/css-validator/) foR CSS validation

 ### Deployment:

#### Project setup:

Github:

- Create a new repository on Git Hub using code institute`s template

- Change repository visibility

- Press green button to open project in git pod

- Create readme.md file and make initial commit

- Make regular commits after project change with quality description using commands: git add -A and git commit -m "message"

- Use git push command in CMD for code commits


Heroku:

- Navigate to [Heroku](https://id.heroku.com/login)

- Register account 

- Press Button New

- Select Create a New App, enter the app name and select region

- Press Resource and connect with database

MongoDB:
- Navigate to [MongoDB](https://account.mongodb.com/account/login?signedOut=true)

- Create account 

- Create data base

Deployment`s final steps:

- After registration of test users, change status of one the user to [admin](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/deployment/admin_MongoDB.JPG)

- Create quiz questions




### Testing

Throughout the development of the project, I carried out testing. I used the Chrome Developer Tools consistently.
The application structure and mobile-first layout was tested on Google Chrome, Firefox and Safari.
The application was tested on the following smartphone devices: iPhone11, Google Pixel 3, Galaxy S7

#### Functional testing:

- That all of the links are open wihout any problems

- That application is mobile responsive

- That user can get logged in

- That quiz can not be run before user is logged in

- That user needs to create account 

- That user name and e-mail must be unique

- That user name and password length must be between 10 and 150 characters 

- That e mail must be in valid form

- 

#### Testing examples:

Google Chrome:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/home_page_chrome.JPG)
- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/login_page_chrome.JPG)
- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/register_page_chrome.JPG)
- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/quiz_page_chrome.JPG)
- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/settings_page_chrome.JPG)
- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/chrome%20desktop/admin_page_chrome.JPG)

Firefox:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/home_page_firefox.JPG)
- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/login_page_firefox.JPG)
- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/register_page_firefox.JPG)
- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/quiz_page_firefox.JPG)
- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/settings_page_firefox.JPG)
- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/firefox%20desktop/admin_page_firefox.JPG)

Safari / mobile phone:

- [Home page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/home_page_mobile.PNG)
- [Login page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/login_page_mobile.PNG)
- [Register page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/register_page_mobile.PNG)
- [Quiz page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/quiz_page_%20mobile.jpg)
- [Settings page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/settings_page_mobile.PNG)
- [Admin page](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/images/test%20images/safari_mobile/admin_page_mobile.PNG)

###Validator tests:

HTML:
- [Home page](https://ms3-mario.herokuapp.com/)------[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/home_page_html_validation.JPG)
- [Quiz page](https://ms3-mario.herokuapp.com/login/)-----[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/quiz_page_html.JPG)
- [Quiz page, user logged](https://ms3-mario.herokuapp.com/quiz/)-----[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/quiz_page_html_user.JPG)
- [Register page](https://ms3-mario.herokuapp.com/register/)-----[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/register_page_html.JPG)]
- [Login page](https://ms3-mario.herokuapp.com/login/)-----[test results][https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/login_page_html.JPG]
- [Settings page, user logged](https://ms3-mario.herokuapp.com/settings/)-----[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/settings_page_html.JPG)
- [Admin page, admin logged](https://ms3-mario.herokuapp.com/admin/)-----[test results](https://github.com/mariodragun/Milestone-3-Code-Institute/blob/master/validator/html%20validator/admin_page_html.JPG)

Python:

