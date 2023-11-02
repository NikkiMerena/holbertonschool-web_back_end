# Queuing System in JS - README

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- How to run a Redis server on your machine
- How to run simple operations with the Redis client
- How to use a Redis client with Node JS for basic operations
- How to store hash values in Redis
- How to deal with async operations with Redis
- How to use Kue as a queue system
- How to build a basic Express app interacting with a Redis server
- How to build a basic Express app interacting with a Redis server and queue

## Requirements
- All of your code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All of your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the js extension
- Required Files for the Project:
  - package.json
  - .babelrc
- Don't forget to run `$ npm install` when you have the package.json

## Tasks
### Task 0: Install a Redis instance
- Download, extract, and compile the latest stable Redis version (higher than 5.0.7)
- Start Redis in the background with `src/redis-server`
- Make sure that the server is working with a ping `src/redis-cli ping`
- Using the Redis client, set the value School for the key Holberton
- Kill the server with the process id of the redis-server

### Task 1: Node Redis Client
- Install node_redis using npm
- Write a script named `0-redis_client.js` to connect to the Redis server and handle connection errors

### Task 2: Node Redis Client and Basic Operations
- Copy the code from `0-redis_client.js` to `1-redis_op.js`
- Add two functions: `setNewSchool` and `displaySchoolValue` for basic Redis operations

### Task 3: Node Redis Client and Async Operations
- Copy the code from `1-redis_op.js` to `2-redis_op_async.js`
- Modify the `displaySchoolValue` function to use async/await with promisify

### Task 4: Node Redis Client and Advanced Operations
- Create a file `4-redis_advanced_op.js`
- Use the Redis client to store hash values with `hset` and retrieve them with `hgetall`

### Task 5: Node Redis Client Publisher and Subscriber
- Create a subscriber script `5-subscriber.js` and a publisher script `5-publisher.js` using Redis for message passing

### Task 6: Create the Job Creator
- Create a queue with Kue
- Create jobs with job data and log messages

### Task 7: Create the Job Processor
- Create a queue with Kue
- Process jobs, send notifications, and log messages

### Task 8: Track Progress and Errors with Kue - Create the Job Creator
- Create jobs with job data and log messages with progress tracking

### Task 9: Track Progress and Errors with Kue - Create the Job Processor
- Process jobs, send notifications, and log messages with progress tracking

### Task 10: Writing the Job Creation Function
- Create a function `createPushNotificationsJobs` to create jobs in a queue

### Task 11: Writing the Test for Job Creation
- Write tests for the `createPushNotificationsJobs` function

### Task 12: In Stock?
- Create a web application with Express to manage product stock and reservations using Redis and Kue


