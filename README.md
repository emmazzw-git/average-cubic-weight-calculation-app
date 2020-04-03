# Average Cubic Weight Calculation Application
This command line application provides a calculation of Kogan's Air Conditioners' average cubic weight. The app can be run in docker container and the output will be shown in the command line, such as, 

```
The average cubic weight is 41.6133846875
```
The app is written in python3.

## Development
### Why Docker?
This app was designed to run as many processes as possible within Docker containers to ensure behavioural consistency, this includes using docker in your development environment. Using `docker run` will execute commands inside docker container .


### Getting Started
1. Install [Docker Desktop](https://www.docker.com/get-started)

2. Build the app image using docker:

```bash
    docker build -t cubic-weight-calc-app . 
```

3. Check the latest docker build,

```bash
    docker images
```

The images list,

```
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
cubic-weight-calc-app   latest              93288f7ca081        2 minutes ago       941MB
...
```


4. Run application locally using docker:

```bash
    docker run cubic-weight-calc-app
```
The result of the calculation will show in the command line.


## Testing
### Unit Testing
To be implemented with `pytest`

### Unit Testing Coverage
To be implemented with `Coverage.py`
 
### Running Code Linting
`flake8` to be installed and run

### Running Code Security Scan
`bandit` to be intalled and run

## Language Used
*python*

