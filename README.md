# Gamedream - A portfolio project.

Welcome to my code institute website readme. This is for my milestone 3 project. For this, I have decided to create a game wishlisting service to allow for storing games and then wishlisting them; complete with their prices, name and description. I have done this because the goal for this project was to create a python website which was able to utilize either a relational database or a non-relational database in order to provide CRUD functionality to a user through relating at least 2 tables in said database.

!["The first thing users see when loading the site"](read_me/placeholder_screen.png)

## Table of Contents

1. [Planning & Development](#planning--development)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Languages](#languages)
6. [Media Queries](#media-queries)
7. [Software](#software)
8. [Code](#code)
9. [Credits](#credits)

# Planning & Development #

### Business Strategy

When I was considering what kind of website I was going to build, I had recieved many ideas from my weekly tutor, like quizzes and reviews. However I decided upon creating a wishlist service for two reasons. The first was because of my own personal interest in video games and the fun of being able to work with something I enjoy in an educational setting. The second reason was because I thought it would interesting to explore more of flask and what it has to offer outside of the code institute walkthroughs, as I had come to find the most fufilment working with flask as opposed to everything else on the course thus far.

### Target Audience

When I conducted my marketing research for this project I was astounded to learn that there was zero search results for wishlists. Not a single one. I was suprised because this was a very common feature on many websites and I was also expecting similar results like santa's wishlist etc. The fact that there was no results in this category lets me know that wishlisting is a service that is expected to be a part of a larger website rather than it's own dedicated service both due to convinience and the potential to link directly to the wanted items on the site for quick access and real time updates e.g. sales. This can be seen in other gaming services with wishlisting features like Steam and GOG

![There were no results on AdTargeting using the keyword "Wishlist"](read_me/target_audience.png)

### User Needs

#### User Stories

1. Be able to securely create an account, log in and log out.
2. Create a game title with all the details they would want.
2. Create a game wishlist with all the details they would want.

### Site Objectives

* Create a UI that is easy to read with non-conflicting colors.
* Ensure that the site complies to responsive design theory.
* Allow users to create titles with full CRUD functionality.
* Allow users to create wishlists with full CRUD functionality.
* Ensure that users can log in securely.
* Prevent other users from altering or deleteing titles and wishlists they have not created.
* Make sure that the site is accessible to screenreaders
* Create a good design flow so that users are lead from page to page easily.


### Wireframe

These are the wireframes I created to help me plan out the design of my website. The designs were not final but there were a massive help in creating the project.

![The base template used by all pages.](read_me/wireframes/base_template.png)

![Account creation screen](read_me/wireframes/account_creation.png)

![The login screen](read_me/wireframes/login_screen.png)

![Where users can create titles](read_me/wireframes/title_creation.png)

![Where users can create wishlists](read_me/wireframes/wishlist_creator.png)

![The page that lets users view created titles](read_me/wireframes/titles.png)

![The page that lets users view created titles](read_me/wireframes/wishlist.png)

### Color Scheme

![This was the palette I chose to use for my site.](read_me/gamedream_palette.png)

I chose the above color scheme because I was already quite fond of how the site was looking with the default colors. I opted to change the colors for ones that were still the same colors, just in different more muted hues so that they would pop naturally out from the background.

### Typography

![This was the font I chose to use for my site.](read_me/my_font.png)

When I was deciding on a font to use I was not really concern with finding something bombastic or overly stylized. Like the color scheme I wanted something that was still similar to the standard but was still distinct enough to be eyecatching. I decided on Nunito because I thought it had a pleasing design and would also still be clear enough to be readable on smaller devices.

# Features #

### General

Alot of the features on my website revolve around ensures that the user is able to have CRUD functionality. The ability to Create, Read, Update and Delete any and all records they create for the database. This is to ensure users have complete control over what they can input into the site and also to comply with good database practises. For this I will be going page by page since there is alot going on for each feature and I wish to be as comprehensive as I can.

### Home page

![The first page users see when opening the site](read_me/site_images/home.png)

The above image is the first thing that a user will see when accessing my site. A line of text will welcome the user to the site and inform them that they need to create an account and log onto the site before any titles and wishlists can be created. At the top of the screen you can see the header and along the bottom you can see the footer. These both react to whether the user is logged in or not and as such will display certain features depending on this. They are responsive as the screen width changes and the header is a bright white to stand out from the black background. The footer text is black for similar reasons.

### Account Creation

![The page where users can create their accounts.](read_me/site_images/account_creation.png)

The information in the above image is example text. Upon creating an account, the password will be hashed in order to ensure complete security. The login details here get assigned to a database called User which saves it to be used with flask-login.

### Log in Screen

![This is where the user can log onto the site.](read_me/site_images/log_in.png)

The user uses this screen to log onto the site. Using flask-login, the provided details are compared to what is currently stored in the user data table and if there is a match the user is then logged on and given the variable of current_user. With this the user is authenticated and can then go on to create their own titles and wishlists at their leisure.

### Profile

![The user profile where they can see who is logged on.](read_me/site_images/profile.png)

The profile is a simple page made for the sole purpose to displaying the username of the current user so that they may check who is currently logged on as well as to ensure that current_user was working as intended.

### Titles

![The screen where users are able to view titles they have created as well as titles created by other users.](read_me/site_images/titles.png)

Here is where users can see the titles that have been made by all the users of the site. They are arranged in order of what was most recently made and display all the information assigned to them during their creation including names, price and publisher. This is also where users are able to create, edit and delete titles using the buttons provided. The same functionallity to create titles is present in the footer for users who wish to jump into creation one knowing what has already been made. Users can only edit and delete titles they have only made. Attempting to edit/delete titles they do not own will lead to an authentication error.

![A user trying to change a title/wishlist not made by themself will give an authetication error](read_me/site_images/authorization_checker.png)

### Wishlists

![The screen where users are able to view wishlists they have created as well as wishlists created by other users.](read_me/site_images/wishlists.png)
![This displays what information is stored within the wishlist accordion](read_me/site_images/wishlist_accordion.png)

Here is where users can do much the same for wishlists as they can titles. They can create them, edit them and delete them provided they are the original creators. This is check (as is with id's) by comparing an author_id assigned to them upon creation that is set to be equal to the current_user that made it. When attempting to edit/delete a title, a check is ran which compares the author_id to the id of the current logged in user. If the id's match then the user gains access to the edit form and the delete button. Wishlists are ordered oldest to newest and are built using bootstrap accordions which auto update with information present in the wishlist table.

![The modal involved in preventing deletion of titles/wishlists.](read_me/site_images/deletion_checker.png)

The delete button for both titles and wishlists is hidden behind a modal that when triggered will ask the user if they are sure they wish to delete whatever information they wish to delete from the databse. Upon clicking the Delete button again, the item is removed permanently from the database and will need to be recreated if the user has still accidentally deleted it.

### Tile creation.


# Testing #

{}

## Validator Testing

### W3C Validator

{}

# Deployment #

To deploy my site I used heroku. This was done by using the following steps.

1. Generating a requirements.txt file containing the python dependencies needed for the project.
2. Create a Procfile to contain the command for starting up the website.
3. Create a new variable in __init__.py called DATABASE_URL to allow the project to read an external database.
4. Log on to Heroku.com and create a new app, while also giving it a unique name and setting the region to europe.
5. In the settings section, create a config var on the heroku app and assign it the url given by Code Institute.
6. Add to the config var all the details contained in env.py except DEVELOPMENT and DB_URL.
7. Go onto the deploy section, and use Connect to Github as the deployment method.
8. Select your github repo from the list and use Manual Deploy to deploy the branch of choice.
9. Use the run command feature and type python3 into the console to get the python interpreter.
10. Run Terminal.py to build the database for the site.
11. Click run app and enjoy! Be sure to ensure that the site works as it should and that DEBUG is set to false.

# Languages #

* For the development of this website I utilized HTML, CSS, JS and Python in order to create it. 

* Bootstrap 5.3.3 was used to create the accordion and for it's grid system in laying out site features.

# Media Queries #

Media Queries were used exclusively in the role of increasing the responsiveness of web pages by...

# Software #

VS Code was used to create the website. It was the tool for typing out HTML, CSS, JS and Python code along with pushing site updates to the Github repository. Gitpod was used to provide backend and virtual environment support for the use of python without which the site would not function.

Balsamiq was used to create the wireframes saw earlier in this readme.

The microsoft snipping tool was used to take the relevant screenshots.

# Code #

* https://stackoverflow.com/questions/44051379/css-how-to-pin-footer-to-bottom-of-the-page
* https://getbootstrap.com/docs/5.3/examples/footers/
* https://getbootstrap.com/docs/5.3/examples/headers

# Credits #

Code Institute for the opportunity to learn and hone the craft of developing websites.

My loving and supportive family for supporting me in this endeavor.