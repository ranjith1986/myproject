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
    
    stage('Scan with Probely') {
            steps {
                probelyScan targetId: '4B5nxovDynbf', credentialsId: 'Probely-API', waitForScan: true, stopIfFailed: true, failThreshold: 'medium'
            }
         }
    
    stage('Deploy'){
      steps{
        echo '********* Deployment   Started **************'
        timeout(time : 1, unit : 'MINUTES'){
        bat '''python myapp.py'''
        }
      echo '********* Deployment Finished ***********'
       }
    }
    
  }

}
