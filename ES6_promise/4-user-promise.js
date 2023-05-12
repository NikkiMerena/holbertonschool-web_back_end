export default function signUpUser(firstName, lastName) {
  // Function to sign up a user

  return Promise.resolve({ firstName, lastName });
  // Creates a Promise that resolves immediately w/ an object containing the provided firstName & lastName
}

// End of signUpUser function  
