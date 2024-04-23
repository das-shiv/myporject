# Using the python alpine base image from dockerhub
FROM python:alpine


# Setting the working directory
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to the container's working directory
COPY . /app/

# Expose port 8000 to allow communication to the server
EXPOSE 8000

# Starting the django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

