pipeline {
    agent {
        label 'jnode'
    }

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Enter the branch name to deploy')
    }

    environment {
        DOCKER_IMAGE_NAME = 'counter'
        GITHUB_REPO_URL = 'git@github.com:edislab2023/counterpy.git'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: "*/${params.BRANCH_NAME}"]], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: "${env.GITHUB_REPO_URL}"]]])
                }
            }
        }
        stage('Remove Existing Container') {
            steps {
                script {
                    // Remove the existing Docker container if it exists
                    sh 'docker rm -f $(docker ps -aqf "name=counter*") || true'
                }
            }
        }

        stage('Build and Deploy') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${env.DOCKER_IMAGE_NAME}:${params.BRANCH_NAME} ."
                    
                    // Run the Docker container, exposing port 80 to the host network
                    sh "docker run -d --name ${env.DOCKER_IMAGE_NAME}-${params.BRANCH_NAME} -p 80:80 --network host ${env.DOCKER_IMAGE_NAME}:${params.BRANCH_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
