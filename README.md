### Build the Docker Image
docker build -t flask-ocr-app .

### Run the Docker Container
docker run -d -p 8000:8000 flask-ocr-app
