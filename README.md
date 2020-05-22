# py-learn

Tutorial for learning basic Python for Windows

## Install required software

* [Download and install Python3](https://www.python.org/downloads/windows/)
* [Download and install VSCode](https://code.visualstudio.com/Download)
* [Download and install Git](https://gitforwindows.org/)
  * select `VSCode` as the default editor, leave other options as default
* Start VSCode or restart if already open to load Git integration
* Click the `graph` icon on the left-hand navigation bar
* Click the `clone repository` button that appears
* Enter [https://github.com/limscoder/py-learn](https://github.com/limscoder/py-learn) as the repository to clone

## Install code dependencies

* Select `terminal->new terminal` from the VSCode menu bar to open a terminal within VSCode
* Run the following commands in the terminal
  * `> python .\bin\get-pip.py`
  * `> python -m pip install -U matplotlib`

## Running the app

* Click the `document` icon on the left-hand navigation bar
* Open the `src/main.py` file and install Python extension when prompted
  * you may need to restart VSCode after installing the Python extension
* Select the `run->run without debugging` option from the VSCode menu bar
* You can also run the application from the terminal
  * `> python .\src\main.py`

## Saving changes

* Create an account on [github.com](https://github.com/)
* Configure git user (in terminal)
  * `> git config --global user.name "Your Name"
  * `> git config --global user.email "{email-you-used-for-github}"
* Browse to [https://github.com/limscoder/py-learn](https://github.com/limscoder/py-learn)
* Click the `fork` button in the upper right hand corner to copy the repository to your personal account
* Add your fork (in terminal)
  * `> git remote add forked https://github.com/{github-username}/py-learn.git`
* Save your changes (in terminal)
  * `> git add .`
  * `> git commit -m "describe what you changed"`
* Upload your changes to github (in terminal)
  * `> git push forked HEAD:master`
