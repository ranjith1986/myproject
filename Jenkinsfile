pipeline {
  agent any
  environment{
  PATH="C:/Users/86ran/AppData/Local/Programs/Python/Python310/;C:/WINDOWS/SYSTEM32;C:/Users/86ran/AppData/Local/Programs/Python/Python310/Lib/site-packages"
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
        bat 'python py.test'
        echo '********* Test Stage Finished **********'
      }   
    }
  }

}
