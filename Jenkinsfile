pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("ssdocs/myproject:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Push to Docker Hub') {
            environment {
                DOCKERHUB_CREDENTIALS = credentials('docker')
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker') {
                        docker.image("ssdocs/myproject:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
        stage('Delete the docker image from local machine') {
                steps {
                    script {
                        sh "docker rmi --force registry.hub.docker.com/ssdocs/myproject:${env.BUILD_NUMBER}"
                        sh "docker rmi --force ssdocs/myproject:${env.BUILD_NUMBER}"
                }
                    }
                }
            }
    }

