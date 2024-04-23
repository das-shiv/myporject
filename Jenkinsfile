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
            
            stage('Delete Old Docker Image') {
                steps {
                    script {
                        sh "docker rmi ssdocs/myproject:${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}
