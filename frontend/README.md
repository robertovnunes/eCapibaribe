# ecapibaribe Front-end Angular

This is the Front-end base project in Angular for the Software and Systems Engineering discipline, offered by the Informatics Center (CIn) of the Federal University of Pernambuco (UFPE).

## Table of Contents

1. [Getting Started](##getting-started)
2. [Running the tests](#running-the-tests)
3. [Scripts](#scripts)
4. [Dependencies](#dependencies)
5. [Architecture](#architecture)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you'll need to have the following software installed on your system:

- Node.js
- npm (Node Package Manager)

### Installing

Clone the repository and install the dependencies by running the following command in the project directory:

```
npm install
```

### First time running ?

Run the follow scripts

```
chmod +x .husky/pre-commit
chmod +x .husky/pre-push
```

```
npm run
```

### Running the App

To start the app, run the following command:

```
npm start
```

This command will run the Angular app.

## Running the tests

There are two types of tests configured in the base project: unit tests using [Jest](https://jestjs.io/docs/getting-started) and E2E acceptance tests using [Cypress](https://docs.cypress.io/guides/overview/why-cypress) with [Cucumber](https://github.com/badeball/cypress-cucumber-preprocessor).

To run unit tests individually, you can easily use the VScode extension [Jest Run It](https://marketplace.visualstudio.com/items?itemName=vespa-dev-works.jestRunIt). If you want to run all the unit tests suite, you can run: 

```
npm test
```

To run unit tests in **watch mode**

```
npm run test:watch
```

To run E2E acceptance tests, you need to have the app running. Therefore, make sure to initiate the app before running the tests.

To run E2E tests in **interactive mode**

```
npm run cy:open-e2e
```

To run E2E tests in **headless mode**

```
npm run cy:run-e2e
```

## Scripts

The following scripts are available in the `package.json` file:

- `start`: Runs the app in development mode.
- `build`: Compiles the TypeScript code.
- `test`: Runs the Jest tests for the project.
- `prettier`: Formats the code using Prettier.
- `lint`: Lints the code using ESLint.

## Dependencies

The following dependencies are used in the project:

- [Angular CLI](https://github.com/angular/angular-cli) v16.1.3: Angular is a JavaScript library for building user interfaces.
- [Angular Material](https://material.angular.io/) v16.1.3: Material Design components for Angular.


## Architecture

To understand and learn more details about the structure of the project, click [here](./docs/architecture-pattern.md) to be redirected to the README that contains this information.
