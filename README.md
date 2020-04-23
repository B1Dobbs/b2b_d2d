The Business 2 Business designed for D2D - Spring 2020 SEV

## Navigation of Github Repository

Functionality of each branch is determined by branch name
- **master:** the main release branch<br>
- **development:** the branch used for integration and testing before merging to master
- **\<issueID>_\<issueTitle>:** naming scheme for feature branches
- **<issueTitle>** naming scheme for feature branches


## Setting Up Environment

Run the following commands in the terminal to setup the server

1. git clone https://github.com/B1Dobbs/b2b_d2d.git<br/>
2. cd b2b_d2d<br/>
3. pip install -r requirements.txt<br/>
4. python manage.py makemigrations b2b_app<br/>
5. python manage.py migrate<br/>
6. python manage.py createsuperuser<br/>


## Testing the Application

python manage.py runserver
Open the webpage at the localhost
Click “Add Company” and fill out the page.
Click on the company and add a user.
Once the user is added, log out of the admin page and log in using the new credentials you have created
To test the tool, input data into the search fields and run a search.
Once the page has finished loading, click any of the website names to see the search results.
Use the reporting link to visit a page which generates usage reports for the company.
Use the icon on the top right to visit the user’s profile, edit information, or log out.

#### Folder Structure
```
b2b_d2d \
  |---api_app \	        - Application for the API
  |---b2b \             - Settings for the whole project
  |---b2b_app\		- Application for B2B Interface
    |---static 		- Folder for css
    |---templates \	- Folder for templates
    	|---company \ 	- CRUD templates for a company
	|---user \ 	- CRUD templates for user
    |---checkmate_test.py - Simple test to test checkmate
  |---templates \ 	- Templates for django.auth
```
