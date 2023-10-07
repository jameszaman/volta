# VOLTA

Both the backend and frontend for the volta project is in this repo.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)

## Project Overview

I have way to many projects started and later forgotten. This project will help me to keep track of the projects. I will make a new app that will show all the projects that I am interested in and things that I am doing and want to do with them in the future.

## Getting Started
### Prerequisites
List any prerequisites or system requirements that users need to have installed before they can use your project. For example:

- [Node.js](https://nodejs.org/) (v14 or higher)
- [npm](https://www.npmjs.com/) (v6 or higher) or [Yarn](https://yarnpkg.com/) (v1 or higher)

### Installation

Clone this repository:

```bash
git clone <repository-url>
```
#### Frontend
```bash
cd Frontend
npm install

```
#### Backend
Go To backend Folder and create a new environment for python
```bash
cd backend
python -m venv env
```
Select the environment.

Windows:
```bash
.\env\Scripts\activate
```
Linux:
```bash
source env/bin/activate
```
Install the modules:
```bash
pip install -r requirements.txt
```

### Running the Application

In the `frontend` folder:
#### Frontend
```bash
npm run dev
```

#### Backend
In the `backend` folder:
```bash
python main.py
```
