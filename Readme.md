 " HELLOOOWWWW THIS IS A BASIC PYTHON CHATBOT " 
HEYA ! Its cleffair here I'm basically following a guy on yt to replicate his chatbot just to learn some basics of python and ML. I'll keep udating my progress aswell as some notes here.

heres the link for the tutorial: https://www.youtube.com/watch?v=t933Gh5fNrc
This project has a very limited set of intent based queries which can be asked to the chatbot. the project will use basic ML/ basic algorithms like gradiant descent to simply classify the intent of the user and respond accordingly.

Current Progress :-

-created virtual env first 
-made intents.json with basic queries ex - 

 {"tag": "greeting",
         "patterns": ["Hi there", "How are you", "Is anyone there?","Hey","Hola", "Hello", "Good day"],
         "responses": ["Hello", "Good to see you again", "Hi there, how can I help?"],
         "context": [""]
 }

-installed libraries :numpy, tensorflow, nltk ( check requirements.txt )
-while understanding different libraries and frameworks i came up with an analogy for diffrenciating between libraries and frameworks: imagine a building/ apartment complex ( this is your codebase ), here you have multiple utilities ( libraries) like lift, water filter, thermostat etc. and then you have the whole elctric circuit/wiring ( framework) that connects everything together and makes the building function as a whole. so basically the framework is the structure that calls the code and libraries are chunks of code with independent use wheras the building is your codebase functioning with both.

created main python file new.py
