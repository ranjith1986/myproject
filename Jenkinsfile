pipeline {
  agent any
  assoc .py=Python.File
  ftype Python.File="C:/Users/86ran/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.10/"
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
