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
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'ssdocs') {
                        docker.image("ssdocs/myproject:${env.BUILD_NUMBER}").push()
                    }
                }
            }
        }
    }
}