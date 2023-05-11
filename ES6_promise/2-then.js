export default function handleResponseFromAPI(promise) {
    // Function to handle the response from the API
    
  return promise
    .then(() => ({ status: 200, body: 'success' }))
    // Attach a callback function to be executed when the promise is resolved.
    // The callback returns an object with status 200 and body 'success'.
  
    .catch(() => Error())
    // Attach a callback function to be executed when the promise is rejected.
    // The callback returns a new Error object.
  
    .finally(() => console.log('Got a response from the API'));
    // Attach a callback function to be executed regardless of whether the promise is resolved or rejected.
    // The callback logs the message 'Got a response from the API' to the console.
}
  
// End of handleResponseFromAPI function
  