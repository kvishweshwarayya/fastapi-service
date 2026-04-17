# fastapi-service
fastapi based web application.

## How to use?
  1. clone the git repository
     `git clone https://github.com/kvishweshwarayya/fastapi-service.git`
  
  2. go inside the repo and build docker images with the help of given Dockerfile
     `docker build -t <your org>/fastapi-service:<version> .`
     
     eg.
     `docker build -t kvishweshwar/fastapi-service:0.1.0 .`
  
  3. Now, run the docker container on local machine and access web ui.
     As fastapi-service is exposed on port 8080; use `http://127.0.0.1:8080/`.
  
  4. Now, consider sample user 'octocat' to see gists of octocat user on browser.
     So, your resultant accessing url will be `http://127.0.0.1:8080/octocat`.

  5. Once you confirm that application is working as expected, you can test application using pytest.
     In root of project, I have created 'test_user_gists.py' file. Just run it with the help of pytest.
     
     eg.
     pytest test_user_gists.py
  
     This will execute test case and provide status.


## mywork
If you would like to use my image then, you can find the same on docker hub:
`docker pull kvishweshwar/fastapi-service-with-routers:0.1.0`

Note: make sure that you logged in to hub.docker.com.

