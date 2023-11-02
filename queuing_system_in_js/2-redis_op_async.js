// Import the required library
import redis from 'redis';
import { promisify } from 'util'; // Import the promisify function

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

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Async function to display the school value from Redis
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (error) {
    console.error(`Error: ${error}`);
  }
}

// Call the functions and perform operations
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
