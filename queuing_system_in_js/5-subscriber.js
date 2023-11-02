// Import the required library
import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient({
  host: '127.0.0.1', // Redis server host (localhost)
  port: 6379,        // Redis server port
});

// Handle the connection events
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the "holberton school channel"
subscriber.subscribe('holberton school channel');

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  console.log(message);

  // Check if the message is "KILL_SERVER"
  if (message === 'KILL_SERVER') {
    // Unsubscribe and quit the subscriber
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
