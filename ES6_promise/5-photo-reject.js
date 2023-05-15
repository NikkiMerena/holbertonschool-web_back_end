export default function uploadPhoto(fileName) {
  // Function to upload a photo

  return new Promise((resolve, reject) => {
    // Create a new Promise that takes a resolver function with resolve and reject parameters

    reject(Error(`${fileName} cannot be processed`));
    // Reject promise & pass an Error object w/ a mess indicatin fileName can'yS be processed
  });
}
