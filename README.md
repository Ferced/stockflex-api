# cornalito-api

![Github last commit](https://img.shields.io/github/last-commit/ferced/cornalito-api)



# About the project
 
This is the api made for cornalito.


### Built With

* [Python](https://python.org)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Redis](https://redis.io/)
* [Mongodb](https://www.mongodb.com)


# Usage

### Prerequisites

We will be using docker and docker-compose.

* [Docker](https://docs.docker.com/get-docker/)
* [Docker-compose](https://docs.docker.com/compose/install/)


### Installation

1. Clone the repo
  ```sh
  git clone https://github.com/ferced/cornalito-api.git
  ```
2. cd Into the repository folder
  ```sh
  cd reverse-proxy-meli
  ```
### Run with Docker

3. Run docker-compose
  ```sh
  docker-compose up
  ```
### Or you can run it manually with Makefile

3. Install libraries into the virtualenv
  ```sh
   make install
   ```
4. Run program
  ```sh
   make run
   ```
   
### Run tests

1. Run tests with makefile
  ```sh
  make tests
  ```
