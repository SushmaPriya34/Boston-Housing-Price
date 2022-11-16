#base image is taken from the docker hub take any base image (ex:linux) and install python 3.10 on top of it. The docker hub contains all the base images.
FROM python:3.10 
#copy the entire content from my current location to app folder in the base location
COPY . /app
#Make this as my working directory
WORKDIR /app
# Install all the requirements in your app which is on the base location
RUN pip install -r requirements.txt
#In order to run the application inside ther container we have to expose a port to acess the application. The cloud automatically takes the port which is available when $PORT is given
EXPOSE $PORT
#gunicorn helps to run the python application inside heroku. Workers do load balancing among themselves. 0.0.0.0 IP address is the local address in the heroku cloud. app:app means inside app.py file run the flask name app
#bind will bind the $PORT to the local IP address in heroku. gunicorn is required whenever heroku is used for deployment
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

#FCWREC- For cup work reach essential cup