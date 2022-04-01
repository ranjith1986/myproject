pipeline {
  agent any
  stages{ 
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        sh 'python myapp.py'
        echo '********* Build Stage Finished **********'
        }
    }
    stage('Testing Stage') {
      steps {
        echo '********* Test Stage Started **********'
        sh 'python py.test'
        echo '********* Test Stage Finished **********'
      }   
    }
  }

}
