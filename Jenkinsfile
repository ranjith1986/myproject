pipeline {
  agent any
  environment{
  PATH="C:/Users/86ran/AppData/Local/Programs/Python/Python310/;C:/WINDOWS/SYSTEM32;C:/Users/86ran/AppData/Local/Programs/Python/Python310/Scripts"
  }
  stages{ 
    
        stage('Clean working Directory')
    {
      steps{
        echo '********* Cleaning Workspace Stage Started **********'
        bat 'rmdir /s /q dist'
        echo '********* Cleaning Workspace Stage Finished **********'
      }
    }
    
    stage('Build') {
      steps {
        echo '********* Build Stage Started  ***********'
        bat '''pip install flask'''
        bat '''pyinstaller myapp.py'''
        echo '********* Build Stage Finished ***********'
        }
    }
    stage('Testing') {
      steps {
        echo '********* Test Stage Started **********'
        bat '''pytest'''
        echo '********* Test Stage Finished **********'
      }   
    }
    
    stage('Deploy - Production'){
       withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: '86.ranjith@gmail.com', usernameVariable: 'ranjith1986', passwordVariable: 'Pass@mar22']]) {
       bat 'git push https://${ranjith1986}:${Pass@mar22}@git.heroku.com/ranjithtestapp.git HEAD:refs/heads/master')
       }
    }
    
  }

}
