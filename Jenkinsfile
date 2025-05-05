pipeline {
    agent {
        docker {
            image 'docker:20.10.16-dind'
            args '--privileged -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        IMAGE_NAME = 'ankoayfeno/chronoci:latest'
    }

    stages {
        stage('Login DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWD')]) {
                    sh 'echo "$DOCKER_PASSWD" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                sh '''
                    docker build --no-cache -f website/Dockerfile -t $IMAGE_NAME website/
                    docker push $IMAGE_NAME
                '''
            }
        }
    }
}
