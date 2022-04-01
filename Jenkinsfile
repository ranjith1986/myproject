pipeline {
  agent any
  environment{
  PATH="C:/Users/86ran/AppData/Local/Programs/Python/Python310/;C:/WINDOWS/SYSTEM32;C:/Users/86ran/AppData/Local/Programs/Python/Python310/Scripts"
  }
  stages{ 
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat '''pip install flask'''
        echo '********* Build Stage Finished **********'
        }
    }
    stage('Testing Stage') {
      steps {
        echo '********* Test Stage Started **********'
        bat '''python test_myapp.py'''
        echo '********* Test Stage Finished **********'
      }   
    }
  }

}
