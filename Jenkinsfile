pipeline {
  agent any

  stages{ 
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat 'myapp.py'
        echo '********* Build Stage Finished **********'
        }
    }
    stage('Testing Stage') {
      steps {
        echo '********* Test Stage Started **********'
        bat 'py.test'
        echo '********* Test Stage Finished **********'
      }   
    }
  }

}
