export default function loadBalancer(chinaDownload, USDownload) {
  // Function to perform load balancing between China and US downloads

  return Promise.race([chinaDownload, USDownload]);
  // Returns a new Promise that resolves or rejects as soon as one of the promises
  // in the iterable resolves or rejects
  // The promises being compared are 'chinaDownload' and 'USDownload'
} 
