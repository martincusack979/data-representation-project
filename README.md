# Data Representation Project

This repository is submitted in partial fullfillment of a H.Dip in Science in Data Analytics.

**Name: Martin Cusack**

**Student ID: G00239124**
***

## Introduction
***

### How to use this repository

* Install latest version of Anaconda.
* Install the latest version of Visual Studio Code.
* Clone the repository at https://github.com/martincusack979/data-representation-project
* Open the repository in Visual Studio Code.
* Run using Python interpreter 3.9.18.

### This repository contains: 
* A folder entitled **dvds_Database_files** containing all the Python files used in creating the database table entitled "DVDs".
* A HTML file entitled **dvdViewer.html** which contains the interface and AJAX requests required to perform CRUD operations on the "DVDs" webpage.
* A Python file entitled **dvds_server.py** which runs the Flask server created for the project. The server
 serves a RESTful API which can perform CRUD operations on the "DVDs" webpage.
* An **images** folder.
* A **.gitignore** file and a **readme** file.

### Project - Flask server with RESTful API:   

I decided to choose the type A, or simple, project option.  I went with this option mainly because so much of the content in the module was quite new to me 
(I had not taken the "Applied Databases" or "Web Aplications" modules before because I had deferred these and will be taking them in the Spring 2024 semester).  
For this reason, I decided to choose the simpler project option so that I would not be overloaded with too much new material which I was not familiar with.

Using HTML and JavaScript I created a webpage called "DVDs", modelled on the Books example outlined in the course notes.  "DVDs" is a simple table of DVD titles
(see image below) listing an ID number, a title, a director, the year of release and the DVD price. The code is contained in **dvdViewer.html**.

![viewDvds](https://github.com/martincusack979/data-representation-project/blob/main/images/viewDvds.png)

The server **dvds_server.py** was created using the Flask operations server framework in Python.  The server serves a RESTful API which can perform CRUD operations
on the "DVDs" table.

The database table "DVDs" was created using mySQL (downloaded using Wampserver).  The code for the DAO (Database object) is contained in the file dvdsDAO.py in the 
folder **dvds_Database_files**.

![dvdsMySQL](https://github.com/martincusack979/data-representation-project/blob/main/images/dvdsMySQL.png)

## References
***
[1] https://www.w3schools.com/js/js_ajax_intro.asp

[2] https://www.w3schools.com/js/default.asp

[3] https://realpython.com/python-mysql/

[4] (for mySQL database) https://www.wampserver.com/en/

[5] https://www.w3schools.com/jquery/default.asp

[6] https://www.datacamp.com/tutorial/my-sql-tutorial

[7] https://martin-thoma.com/configuration-files-in-python/







