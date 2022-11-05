# Credit Card Fraud Detection
* Deep Learning Project on detecting fraudulent card transactions.

## Steps to run on Windows

* Prerequisites: [Python 3.9](https://www.python.org/downloads/) (ensure Python is added to [PATH](https://medium.com/co-learning-lounge/how-to-download-install-python-on-windows-2021-44a707994013)) + [Git](https://www.markdownguide.org/basic-syntax/) Client 
* Open GIT CMD >> navigate to working directory >> Clone this Github Repo (or download project files from GitHub directly)

      git clone https://github.com/skillcate/credit-card-fraud-detection.git
* Open Windows Powershell >> navigate to new working directory (cloned repo folder)
* Run Project in Flask

  * Using PIP + Virtualenv:
 
        pip install virtualenv                  # install virtual environment        
        virtualenv ENV                          # create virtual environment by the name ENV
        .\ENV\Scripts\activate                  # activate ENV
        pip install -r .\requirements.txt       # install project dependencies
        python app.py                           # run the project
        deactivate                              # close virtual environment once done

        

### Steps to run on Mac

* Prerequisites: [Python 3.9](https://www.python.org/downloads/)
* Open Terminal >> navigate to working directory >> Clone this Github Repo (or download project files from GitHub directly)

        git clone https://github.com/skillcate/credit-card-fraud-detection.git  
* Navigate to project working directory (cloned repo folder)
* Run Project in Flask
  
  * Using PIP + Virtualenv:

        pip install virtualenv                  # install virtual environment
        virtualenv ENV                          # create virtual environment by the name ENV
        source ENV/bin/activate                 # activate ENV
        pip install -r requirements.txt         # install project dependencies
        python app.py                           # run the project
        deactivate                              # close virtual environment once done
        
### Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/skillcate/credit-card-fraud-detection/issues) by including your search query and the expected result.
