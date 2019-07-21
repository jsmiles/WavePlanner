# WavePlanner
To help plan your surf trip

# Summary
WavePlanner is a toy app that superficially helps people 
to plan their surf trips. You give certain information 
and it will send some useful information back. It is built in Flask utilising the Python modules specified in 
the requirements.txt file. 

# Input
You need to provide two pieces of information to use 
WavePlanner.
1. Location: Where you are currently located?
2. Spot: Where you want to go surfing?

# Output
After you have input the two pieces of information, five 
pieces of information are returned:
* The current swell in feet at the surf spot specified
* The distance between your location and spot
* The estimated driving duration between your two locations
* The nearest pub to the surf spot specified
* A bonus dog picture

# Data
There are four sources of data utilised in WavePlanner
* [MagicSeaweed API](https://magicseaweed.com/developer/api)
* [Dog CEO API](https://dog.ceo/dog-api/)
* [Open Route Service API](https://openrouteservice.org/)
* [What Pub](https://whatpub.com/)

# Requirements
In order to run a version of WavePlanner locally you will 
need a few things.
* A MagicSeaweed API key. You can get one by emailing 
them directly, see the API documentation above
* An Open Route Service API key. Again, see the documentation on their website. 

# Run locally
After you have your two API keys (and stored them as environment variables), you can run this app 
locally. 
* Create a virutal environment using virtualenv or any equivalent. 
* download the required packages 
* initialise the sqlite database locally [this page](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/) should help, especically the `db.create_all()` command. 
* run your server locally `python app.py`
* Open a browser, open the page (usually <localhost:5000> is the default) and use the app

Note: the major limitation of the app is that the MagicSeaweed API key I have, only allows two surf spots. I choose Croyde and Newquay so the app has been built with that limitaiton in mind. 

# Roadmap
WavePlanner is the definition of a rough and ready project. 
It is not production ready and not intended to be. It was
just a proof of concept. However, some of the many ways it 
could be improved include:
* Extending the functionality to change the date requested
* Offering alternative route options to driving distance and duration. 
* Extending the range of countries offered
* Improving the graphics returned. While the dog picture 
is dynamic the pub, route and swell pictures are static 
files. 

