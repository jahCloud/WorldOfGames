pipeline {
    agent any

    stages {

        stage('Cloning Git') {
            steps {
                echo 'Cloning Git..'
                git 'https://github.com/jahCloud/WorldOfGames'
            }
        }

        stage('Building Image') {
            steps {
                echo 'Building Image..'
                bat 'docker build -t world_of_games'
            }
        }

        stage('Running Container') {
            steps {
                echo 'Running Container..'
                bat 'docker-compose up -d'
            }
        }

        stage('Testing Application') {
            steps {
                echo 'Testing Application..'
                bat 'pip install selenium'
                bat 'python tests/e2e.py'
            }
        }
    }

    post {
        always {
            echo 'Finalizing..'
            bat 'docker login -u mika -p *******'
            bat 'docker-compose push'
            bat 'docker-compose down --rmi all'
        }
    }

}
