# ansible-roles-demo

This project create 3 microservices.
 - Front end service handling web request
 - prime service (checks if input data is prime or composite)
 - converter service (convert input year into age in months)
 
 Each of these services run is separare docker containers.
 
 Useful docker commands
  - docker-build -t myflask:1.0.1 .
  - docker run --name myflask-container -p 80:5000 -d myflask:1.0.1

  - docker run --name docker-nginx -p 5000:80 nginx -d

  - docker exec -it 2b8933dc1b27 bash
  - docker rm $(docker ps -aq)
  - docker rmi $(docker images -aq)
  - docker system prune -a -f

  - cker container inspect 00fec897e560

  -  usermod -aG docker $USER
  - do chown $USER /var/run/docker.sock

  # To enforce the build again
  - docker-compose up --build -d
   
  # Repo's for reference
  - https://github.com/nathanforester/DockerComposeTutorial.git
  - https://github.com/nathanforester/API2.git
