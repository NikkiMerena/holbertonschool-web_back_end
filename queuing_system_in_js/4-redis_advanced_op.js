// Import the required library
import redis from 'redis';

// Create a Redis client
const client = redis.createClient({
  host: '127.0.0.1', // Redis server host (localhost)
  port: 6379,        // Redis server port
});

// Handle the connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to create and store a hash in Redis
function createHash() {
  client.hset(
    'HolbertonSchools', // Key of the hash
    {
      Portland: 50,
      Seattle: 80,
      'New York': 20,
      Bogota: 20,
      Cali: 40,
      Paris: 2,
    },
    (err, reply) => {
      if (err) {
        console.error(`Error: ${err}`);
      } else {
        console.log(`Reply: ${reply}`);
      }
    }
  );
}

// Function to display the hash stored in Redis
function displayHash() {
  client.hgetall('HolbertonSchools', (err, reply) => {
    if (err) {
      console.error(`Error: ${err}`);
    } else {
      console.log(reply);
    }
  });
}

// Call the functions to perform operations
createHash();
displayHash();
