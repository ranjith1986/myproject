pipeline {
  agent any
  environment{
  PATH="C:/Users/86ran/AppData/Local/Programs/Python/Python310/;C:/WINDOWS/SYSTEM32;C:/Users/86ran/AppData/Local/Programs/Python/Python310/Scripts"
  }
  stages{ 
    stage('This is Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat '''pip install flask'''
        echo '********* Build Stage Finished **********'
        }
    }
    stage('This is Testing Stage') {
      steps {
        echo '********* Test Stage Started **********'
        bat '''pytest'''
        echo '********* Test Stage Finished **********'
      }   
    }
  }

}
