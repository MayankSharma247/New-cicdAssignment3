pipeline {
    agent any

    environment {
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        RESOURCE_GROUP = 'mayank8875518_pipeline'
        FUNCTION_APP_NAME = 'functionpipeline8875518'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests with pytest...'
                sh '''
                    . venv/bin/activate
                    pytest HttpExample/
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Zipping and deploying to Azure...'
                sh '''
                    zip -r function.zip *
                    az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                    az functionapp deployment source config-zip \
                        --resource-group $RESOURCE_GROUP \
                        --name $FUNCTION_APP_NAME \
                        --src function.zip
                '''
            }
        }
    }
}

