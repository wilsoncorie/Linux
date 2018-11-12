#Item-Catalog
The Catalog project consists of developing an application that provides a list of items within a variety of categories, as well as provide a user registration and authentication system. 
This project creates an app for Dessert stores. 
The users can add, edit, and delete stores and the menus for each store. 
The two ways the users can log in is by Facebook and Google.
The homepage of the app welcomes users and request login authentication.  


Here are the steps that I used to complete and run the project.

First I downloaded the three tools below. 
Download and install    [Vagrant](https://www.vagrantup.com/)
[VirtualBox](https://www.virtualbox.org)
Clone the fullstack-nanodegree-vm
[VM configuration](https://github.com/udacity/fullstack-nanodegree-vm). 
FSND-Virtual-Machine File folder for project. All documents will be stored in this directory. Save folder to desktop.
Put the file in the FSND-Virtual-Machine folder, vagrant directory 
Download the project from github link https://github.com/wilsoncorie/Full_Stack_Projects
Download the folder from github and save it to `vagrant` directory

Create a Google Account for Authentication
- client-id 
- client-secret

Create a Develops Account on Facebook  https://developers.facebook.com 
- app-id
- app-secret

#How to Populate Database Project
Open the terminal:
Navigate to the Vagrant folder on the local drive 'cd vagrant/catalog'

Type the following commands:
Run command $python lotsofmenus.py
Run command $python database_setup.py
This will populate the database for the site


#How to Run Project
Launch the Vagrant VM (vagrant up)

```
$vagrant up

$vagrant ssh

$cd /vagrant

$cd catalog

$python project.py

open the browser and go to http://localhost:5000
``


Program Description: The project file is the main file that has all of the APIs and the connect and disconnect to Google and Facebook. The html files can be found in the template folder. The static folder contains the css styling for the html pages. The main database for the catalog is restaurantwithusers. This file has to be initiated before the url is visited. 
