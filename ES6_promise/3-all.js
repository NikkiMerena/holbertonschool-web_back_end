import { uploadPhoto, createUser } from './utils';
// Importing the `uploadPhoto` & `createUser` functions from the './utils' module.

export default function handleProfileSignup() {
  // Function to handle profile signup

  return Promise.all([uploadPhoto(), createUser()])
  // Creates a Promise that resolves when all the promises in the iterable have resolved.
  // The promises `uploadPhoto()` & `createUser()` are executed concurrently.

    .then((values) => {
    // Attach a callback function to be executed when the Promise.all resolves successfully.
    // The resolved values of the promises are passed as an array to the callback function.

      console.log(`${values[0].body} ${values[1].firstName} ${values[1].lastName}`);
      // Log a message to the console using the body of the first resolved promise value
      // and the firstName and lastName properties of the second resolved promise value.
    })

    .catch(() => {
    // Attach a callback function to be executed when an error occurs in any of the promises.
    // The callback function logs the message 'Signup system offline' to the console.

      console.log('Signup system offline');
    });
}

// End of handleProfileSignup function
