pipeline {
  agent any
      
    stage('Build Stage') {
      steps {
        echo '********* Build Stage Started **********'
        bat 'pip install flask'
        bat 'pyinstaller myapp.py'
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
