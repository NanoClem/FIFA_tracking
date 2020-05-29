# FIFA_tracking

This project is meant to save positions of FIFA 19 player's during a match and show them on several vizualisation.  
You can find [here](https://drive.google.com/drive/folders/1wGbBVf5hffwysKyJc9UaqGVEti60Lzil?usp=sharing) a presentation video in french of the project.

## Project goal

This project has two goals.
- The first one is to analyze a FIFA 19 match and detect every player's positions on the minimap located at the very bottom of the screen. It will save the position on a distant database through an API.
- The second use is the vizualisation part : After fetching data from database, it will display them on different vizulisation, as bar chart, heatmap etc...

## Installation
Install required python modules using `pip install -r requirements.txt`.  

## Run Flask api
### Setup .env
The project needs a .env file for configuration, it should contain : 
````bash
DB_URI = your neo4j graph database uri
````  

### Setup flask env
Now to setup the flask env, you'll find a default .flaskenv file to the project root folder with :  
````bash
FLASK_APP = flask_app (don't change it unless you know what you're doing)
FLASK_RUN_PORT = port on which flask is running
FLASK_RUN_HOST = host on which flask is running
FLASK_ENV = development (here debug mode is enabled, change it according to your development stade)
````
All you have to do now is to start flask with `flask run` from project root folder. Go to the base url to see the api documentation.

## Run positions tracking
If you want to run the frames capture and positions tracking, run /core/tracking.py

### Client installation and run
The project needs node.js installed on your computer, download it [here](https://nodejs.org/en/download/).
Once installed, open a terminal to the web folder and run following instructions :
1. `npm install`
2. `npm start`

## Authors
This project was designed and programmed by four students :
[![](https://avatars3.githubusercontent.com/u/43412314?s=60&v=4)](https://github.com/thomascormier) 
[![](https://avatars3.githubusercontent.com/u/22052945?s=60&v=4)](https://github.com/evandadure)
[![](https://avatars2.githubusercontent.com/u/33009785?s=60&v=4)](https://github.com/NanoClem)
[![](https://avatars3.githubusercontent.com/u/18655688?s=60&v=4)](https://github.com/MaxencePRSZ)
