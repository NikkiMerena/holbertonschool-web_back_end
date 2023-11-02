// Import the required libraries
import kue from 'kue';

// Create an array of jobs data
const jobsData = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  // ... add more job data here ...
];

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs from the "push_notification_code_2" queue
queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;

  // Simulate job progress updates
  let progress = 0;
  const interval = setInterval(() => {
    progress += 10;
    job.progress(progress, 100);
    if (progress === 100) {
      clearInterval(interval);
    }
  }, 100);

  // Simulate job completion after a delay
  setTimeout(() => {
    clearInterval(interval);
    // Indicate that the job is done
    done();
  }, 2000);

  // Log job completion and progress
  job.on('complete', () => {
    console.log(`Notification job ${job.id} completed`);
  });

  job.on('progress', (progress) => {
    console.log(`Notification job ${job.id} ${progress}% complete`);
  });

  // Log job failure
  job.on('failed', (error) => {
    console.log(`Notification job ${job.id} failed: ${error}`);
  });

  // Call the sendNotification function with job data
  console.log(`Notification job created: ${job.id}`);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
});

// Create jobs for each item in the jobsData array
for (const data of jobsData) {
  const job = queue.create('push_notification_code_2', data);

  // Handle job creation success
  job.save((err) => {
    if (!err) {
      // Log the job ID after successful creation
      console.log(`Notification job created: ${job.id}`);
    }
  });
}
