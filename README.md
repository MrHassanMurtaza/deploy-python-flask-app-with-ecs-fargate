# Deploy Python App using ECS Fargate

### Use Docker to Deploy Flask App
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

### Use ECS Fargate to Deploy Flask App
- Create Repository in Elastic Container Registry (ECR):

```aws ecr create-repository --repository-name demo-flask-app```
- Get a command you can use for logging in to the ECR repository you’ve just created:

```aws ecr get-login --region $YOUR_REGION --no-include-email```
- Let's put our local docker image to ECR (ACCOUNTID is your account id and REGIONNAME is your region):

```docker tag flask-demo-app:latest ACCOUNTID.dkr.ecr.REGIONNAME.amazonaws.com```


