// Import the required libraries
import kue from 'kue';

// Create an array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a function to send notifications
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress from 0 to 100
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job if the phone number is blacklisted
    const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(error);
  } else {
    // Track job progress to 50%
    job.progress(50, 100);

    // Log sending notification
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Simulate job completion after a delay
    setTimeout(() => {
      // Indicate that the job is done
      done();
    }, 2000);
  }
}

// Create a Kue queue
const queue = kue.createQueue({
  prefix: 'q',
  redis: {
    host: '127.0.0.1',
    port: 6379,
  },
});

// Set concurrency for the queue to process two jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message, job, done);
});

// Log when the queue starts processing jobs
queue.on('job complete', (job) => {
  console.log(`Notification job #${job.id} completed`);
});

queue.on('job failed', (job, error) => {
  console.log(`Notification job #${job.id} failed: ${error.message}`);
});

// Log when the queue is ready
queue.on('ready', () => {
  console.log('Queue is ready to process jobs');
});
