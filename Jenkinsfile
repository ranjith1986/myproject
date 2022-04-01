pipeline {
  agent any
  environment{
  PATH="C:/Users/86ran/AppData/Local/Programs/Python/Python310/"
  }
  stages{ 
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        sh '''python myapp.py'''
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
