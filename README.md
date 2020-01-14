# Rest API for reading a CSV file containing some data from Olympic Events
## Basic CRUD Api using Django, Django-rest-framework


**The project is deployed in a Free instance of Heroku.com Link:** 
[secret-bayou-30347](http://secret-bayou-30347.herokuapp.com/api/)

***What is used in this project?***
- Python 3.7
- Django 2.2
- Djangorestframework 3.11
- Postgres

### How the database is strucured: ###

The database is structured with the following models:
1. UploadCSV *Model used to Start reading CSV file and store its path in BD and itself in media folder*
2. Noc *Model used to store data from ~~National Olimpic Commitee~~*
3. Team *Model used to store data from teams*
4. Game *Model used to store data from games*
5. City *Model used to store data from cities*
6. Sport *Model used to store data from sports*
7. Event *Model used to store data from events*
8. Athlete *Model used to store data from athletes*
9. AthleteEvent *Model used to store data from athlete events*

### Instructions on how to use this API ###
#### Content-Type: application/json ####

- /api/read-csv/ *Method: POST* **Read CSV File called _athlete_events.csv_ and store its data in database**

- /api/nocs/ *Methods: GET/POST* **List all Noc objects/Create a new Noc object**
- /api/nocs/*id*/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete a Noc object**

- /api/teams/ *Methods: GET/POST* **List all Team objects/Create a new Team object**
- /api/teams/*id*/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete a Team object**

- /api/sports/ *Methods: GET/POST* **List all Sport objects/Create a new Sport object**
- /api/sports/*id*/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete a Sport object**

- /api/cities/ *Methods: GET/POST* **List all City objects/Create a new City object**
- /api/cities/*id*/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete a City object**

- /api/games/ *Methods: GET/POST* **List all Game objects/Create a new Game object**
- /api/games/*id*/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete a Game object**

- /api/events/ *Methods: GET/POST* **List all Event objects/Create a new Event object**
- /api/events/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete an Event object**

- /api/athletes/ *Methods: GET/POST* **List all athletes objects/Create a new Athlete objects**
- /api/athletes/?*querystring=*/ *Methods: GET* **Filter by querystring: [ 'sex','team','age','aboveage','belowage','height','aboveheight','belowheight','weight','aboveweight','belowweight', 'sport' ] all Athlete objects**
- /api/athletes/*id*/ *Methods: GET/PUT/PATCH/DELETE/* **Retrieve/Update/Delete an Athlete object**

- /api/athlete-events/ *Methods: GET/POST* **List all AthleteEvent object/Create a new AthleteEvent object**
- /api/athletes-events/?*querystring=* *Methods: GET/PUT/PATCH/DELETE/* **Filter by querystring: [ 'athlete','event','medal' ] all AthleteEvent objects**
- /api/athlete-events/*id*/ *Methods: GET/PUT/PATCH/DELETE* **Retrieve/Update/Delete an AthleteEvent object**
