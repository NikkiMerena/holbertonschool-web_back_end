import signUpUser from './4-user-promise';
// Importing the signUpUser function from './4-user-promise' module

import uploadPhoto from './5-photo-reject';
// Importing the uploadPhoto function from './5-photo-reject' module

export default async function handleProfileSignup(firstName, lastName, fileName) {
  // Function to handle profile signup

  const status = [];
  // Create an empty array to store the status of each step in the signup process

  await signUpUser(firstName, lastName)
    // Wait for the signUpUser promise to resolve or reject
    .then(async (data) => {
      // Attach a callback function to be executed when the signUpUser promise resolves
      // The resolved data is passed as 'data'

      status.push({ status: 'fulfilled', value: data });
      // Pushanobjectintothe'status'arrayindicatingthatsignUpUser promise was fulfilled successfully

      await uploadPhoto(fileName);
      // Wait for the uploadPhoto promise to resolve or reject
    })
    .catch((err) => {
      // Attach a callback function to be executed when an error occurs in any of the promises
      // The error object is passed as 'err'

      status.push({ status: 'rejected', value: err.toString() });
      // Pushanobjectintothe'status'arrayindicatingthattherewasarejectionw/theerrormessageconvertedtostring
    });
    
  return status;
  // Return the 'status' array containing the status of each step in the signup process
}
