![Image describing the resposiveness](static/media/Responsive.PNG)

Looking to post your travel blog? You've come to the right place! Travel Blog is a place where you can view how other people have travelled around the world and shared their experiences.You also have the freedom of sharing and commenting on the other people experiences. And,do you have experiences that you'd like to share as well? Great news! You can create your own free account and add an unlimited number of travelling experiences and share it with the world.This website is also responsive

# UX
## User Stories
Navigation: As a user I can view a navbar from every page so that I can navigate easily between pages

Sign up: 
As a user I can create a new account so that I can access all the features for signed up users

Sign in: 
As a user I can sign in to the app so that I can access functionality for logged in users

View most recent posts: 
As a user I can view all the most recent posts

Edit post: 
As a post owner I can edit my post title and description so that I can make corrections or update my post after it was created

Post a comment: 
As a logged in user I can add comments to a post so that I can share my thoughts about the post

View comments: 
As a user I can read comments on posts so that I can read what other users think about the posts

## Wireframe: 
Mockups were designed using Adobe XD
![Alt text](static/media/Mockup1.PNG)
![Alt text](static/media/Mockup2.PNG)
![Alt text](static/media/Mockup3.PNG)
![Alt text](static/media/Mockup4.PNG)
## Existing Features
### Register Account
Anybody can register for free and create their own unique account.![SignUp](static/media/SignUp.PNG)

### Log In to Account
Users can easily log out of their account with the click of a button.![Alt text](static/media/Signin.PNG)

### Log Out of Account
Users can easily log out of their account with the click of a button.
### CRUD functionality
![CRUD functionality](static/media/CRUD.PNG)

### [CRUD]Read functionality
Travelling Posts can be viewed by going on the Manage Posts button on the navigation bar and clicking on View button on the individual post

### Add a post
[CRUD] Create or 'add' a new travelling experience by clicking on the Add New button. 

### Update a Travelling Experience
[CRUD] Update or 'edit' their own travelling experience on this page.

### Delete a Travelling Experience
[CRUD] Delete or 'remove' a  travelling experience by clicking on the Delete button. 

### Detailed view of each post can also be viewed!
![Detail of individual post](static/media/PostDetail.PNG)


## Technologies Used
HTML,
CSS, 
Javascript,
Heroku,
Python,
Django,
ElephantSQL

## Agile Method:
The agile Methodology was used and different user stories were created using Kanban board and implemented for the project.
![A Kanban project image](static/media/Kanban%20project.PNG)

### Model for project
Here is the model I used
![Model](static/media/Model.PNG)

## Validators

#### W3C HTML Validator -
I used This HTML validator to ensure my code was legal.
The only warnings were when the validator failed to recognise the Django template tags.
The Django templates were checked found by going through View Page Source on the deployed website where we got rendered html and then was taken to the W3C validator and then the errors were checked no so no errors in these templates only warnings found

#### W3C CSS Validator - 
No errors found


#### JShint: 
There were initially following undefined variables as shown here
![Jshint validation](static/media/Jshint%20validation%201.png)
It was fixed in the following way
![Jshint validation](static/media/Jshint%20validation%202.png)



#### PEP8 Online: 
No errors found

## Testing of user stories
## User Stories
 
Navigation Test: As a user I can view a navbar from every page so that I can navigate easily between pages

Result: Pass, A navigation bar was found

Sign up Test: 
As a user I can create a new account so that I can access all the features for signed up users

Result: Pass, A sign up page was found


Sign in Test: 
As a user I can sign in to the app so that I can access functionality for logged in users

Result: Pass, A sign in page was found


View most recent posts Test: 
As a user I can view all the most recent posts

Result: Pass, A view button under "Manage Posts"on each individual post was found 


Edit post Test: 
As a post owner I can edit my post title and description so that I can make corrections or update my post after it was created

Result: Pass, An Edit button under "Manage Posts"on each individual post was found


Post a comment Test: 
As a logged in user I can add comments to a post so that I can share my thoughts about the post

Result: Pass, A comment box was found on each of the post detail view through which you can add the comments


View comments v: 
As a user I can read comments on posts so that I can read what other users think about the posts

Result: Pass, A comment section was found on each of the post detail view  where the posted comments can be found

![Accessibilty test](static/media/Accessibilty.PNG)

## Javascript and Python testing
Unit tests were written for both Python and Js 

Python: Unit tests were written to test the url of different views 

Javascript: Unit tests were written to test the next travel destionation page On Tripcostcalculator page. 

Result:These tests were successful.

## Setup and Deployment


### Making a Local Clone
Log in to GitHub and locate the GitHub Repository
Under the repository name, click "Clone or download".
To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
Open Git Bash
Change the current working directory to the location where you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 3.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
Press Enter. Your local clone will be created.
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
Running it from the github

After cloning the repo please run the following command to include all the neccesary apps in requirement.txt

pip install -r requirements.txt

and include the env.py file which should look like this and the user has to fill in these values

![env.py sample](static/media/env.py%20sample.PNG)
### remote Heroku Deployment:
Create an account at Heroku.

Download CLI here.

Open up CMD (Windows) or Terminal (MacOS) and type the following and follow the instructions that appear.

heroku login
Create a new Heroku app using the following code in your terminal:
heroku create app-name-here
With the Heroku app name you just created, modified the production.py file in the settings folder and update the following:
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '127.0.0.1', 'localhost']
Open the Heroku apps webpage and click the app you created in Step 4.

Navigate to the Settings tab on the top horizontal bar, we will be adding the required environment variables here.

Click the 'Reveal Config Vars' button and add the below variables:
![Heroku parameters](static/media/Heroku%20param.PNG)

You can deploy it using the Deploy option and carry out the build like this
![Heroku Deployment](static/media/Heroku%20Deployment.PNG)


## Acknowledgements and Credits
Mentor and Tutor support
Media Info
Inspired by "I think before I blog walkthrough project"
