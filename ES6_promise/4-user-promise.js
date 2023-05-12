export default function signUpUser(firstName, lastName) {
  // Function to sign up a user

  return Promise.resolve({ firstName, lastName });
  // Creates Promise that resolves immed. w/ an object containing the provided firstName & lastName
}  
