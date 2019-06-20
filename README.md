# Deploy Python App using ECS Fargate

## Use Docker to Deploy Flask
- Clone this project
- Move to project directory 
- Run this to build the image:
```
docker build -t flask-demo-app .
```
- Now we need to run the container from image. Run this command:
```
docker run -it -p 5000:5000 flask-demo-app:latest
```
- You should be able to open the flask app in browser using:
```
http://localhost:5000
```
