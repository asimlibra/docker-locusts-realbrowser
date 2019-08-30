As standalone:
* docker run -p 8089:8089 *docker image*

As Master:
* docker run -e LOCUST_MODE=master *docker image*

As Slave: 
* docker run -e LOCUST_MODE=slave   -e MASTER_HOST=*master node ip* *docker-image*
