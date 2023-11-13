# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
# Do this before adding the entire application to leverage Docker cache
COPY ./webservice/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /app
ADD . /app

# Set the working directory in the container to /app/webservice
WORKDIR /app/webservice

# Copy the model file into the Docker image
COPY ./checkpoint.pth.tar /app/webservice/checkpoint.pth.tar

# Copy the webpage directory into the Docker image
COPY ./webpage /app/webpage

# Copy the subclasses.json file into the Docker image
COPY ./webservice/subclasses.json ./subclasses.json

# Copy the ml_ai.gif file into the Docker image
COPY ./webpage/static/images/ml_ai.gif /app/webpage/static/images/ml_ai.gif

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]

# docker build -t lsml2test .
# docker run -p 5000:5000 lsml2test
# docker run -it lsml2test /bin/bash