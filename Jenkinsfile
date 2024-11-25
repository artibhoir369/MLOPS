pipeline {
    agent any

    environment {
        // Set your environment variables here
        IMAGE_NAME = 'model-serving'
        IMAGE_TAG = 'latest'
        KIND_CLUSTER_NAME = 'kind-cluster'
        REGISTRY = 'docker.io'
        DEPLOYMENT_YAML = 'model-serving-deployment.yaml'
        TEST_SCRIPT = 'test_model.py'
        TRAIN_SCRIPT = 'train_model.py'
        DOCKERFILE = 'Dockerfile'
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone your repository containing model files
                git branch: 'main', url: 'https://github.com/artibhoir369/MLOPS.git'
            }
        }
        
        stage('Train Model') {
            steps {
                // Run model training (if needed)
                script {
                    sh "python ${TRAIN_SCRIPT}"
                }
            }
        }


        stage('Build Docker Image') {
            steps {
                // Build the Docker image from the Dockerfile
                script {
                    sh "docker build -t ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG} -f ${DOCKERFILE} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                // Push the image to Docker registry
                script {
                    // Use withCredentials to securely pass the Docker registry credentials
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        // Log in to Docker registry using the credentials
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin ${REGISTRY}"
                        sh "docker push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

        stage('Deploy to Kubernetes (kind)') {
            steps {
                // Deploy your model in the Kubernetes cluster (kind)
                script {
                    sh "kubectl apply -f ${DEPLOYMENT_YAML}"
                }
            }
        }

        stage('Test Model') {
            steps {
                // Run tests on the deployed model
                script {
                    sh "python ${TEST_SCRIPT}"
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
    }
}
