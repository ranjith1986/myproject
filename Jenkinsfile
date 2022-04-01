pipeline {
  agent any
  stages{ 
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat 'python myapp.py'
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
