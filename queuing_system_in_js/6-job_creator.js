// Import the required libraries
import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Define the job data object
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification message.',
};

// Create a job in the push_notification_code queue
const notificationJob = queue.create('push_notification_code', jobData);

// Handle job creation success
notificationJob
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notificationJob.id}`);
    } else {
      console.error('Error creating notification job:', err);
    }
  });

// Handle job completion
notificationJob.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure
notificationJob.on('failed', () => {
  console.log('Notification job failed');
});
