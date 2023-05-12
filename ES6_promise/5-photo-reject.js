export default function uploadPhoto(fileName) {
  // Function to upload a photo

  return new Promise((resolve, reject) => {
    // Create a new Promise that takes a resolver function with resolve and reject parameters

    reject(Error(`${fileName} cannot be processed`));
    // Reject the promise & pass an Error object w/ a message indicating that the given fileName cannot be processed
  });
}  
