jenkins_setup:
	# docker run -d --name jenkins \
	#   -p 8080:8080 -p 50000:50000 \
	#   -v jenkins_home:/var/jenkins_home \
	#   jenkins/jenkins:lts
	# docker run -d --name jenkins \
	#   -p 8080:8080 -p 50000:50000 \
	#   -m 4g --cpus=2 \
	#   -v /fastdisk:/var/jenkins_home \
	#   jenkins/jenkins:lts
	docker-compose up -d
	docker start jenkins
	docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
	# http://localhost:8080
	docker stop jenkins
	docker rm jenkins
	docker volume rm jenkins_home # to remove admin variable name


