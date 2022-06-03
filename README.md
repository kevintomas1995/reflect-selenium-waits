# Waiting until elements are interactable in Selenium

## Available scripts for demo-app

Cd into the demo-app directory with `cd demo-app`

Inside the directory, you can run:

### `npm install`

Installs all the dependencies needed for starting the demo-app

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npx cypress run --browser chrome --headed`

Launches the test runner in a new Chrome browser window.\
See the section about the [command line](https://docs.cypress.io/guides/guides/command-line#What-you-ll-learn) for more information.


## Available scripts for selenium-scripts

Cd into the demo-app directory with `cd selenium-scripts`

Inside the directory, you can run:

### `pip install selenium`

Installs the latest version of selenium package

### `python/python3 test.py`

Launches the Selenium tests. Please be aware, that you need to first start the demo-app with `npm start` in order to successfully pass the tests. 