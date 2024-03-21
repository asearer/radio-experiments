const axios = require('axios');

// Function to fetch ISS data
async function fetchISSData() {
  try {
    const response = await axios.get('http://api.open-notify.org/iss-now.json');
    return response.data;
  } catch (error) {
    console.error('Error fetching ISS data:', error);
    return null;
  }
}

// Function to fetch radio signals from the ISS
async function fetchRadioSignals(latitude, longitude) {
  try {
    const response = await axios.get(`http://api.open-notify.org/iss-pass.json?lat=${latitude}&lon=${longitude}`);
    return response.data.response;
  } catch (error) {
    console.error('Error fetching radio signals:', error);
    return null;
  }
}

// Main function to run the application
async function main() {
  console.log('Fetching ISS data...');
  const issData = await fetchISSData();

  if (!issData) {
    console.log('ISS data not found.');
    return;
  }

  console.log('ISS current position:');
  console.log('Latitude:', issData.iss_position.latitude);
  console.log('Longitude:', issData.iss_position.longitude);

  // Replace these values with your actual location coordinates
  const latitude = 40.7128; // Example latitude (New York City)
  const longitude = -74.0060; // Example longitude (New York City)

  console.log('\nFetching radio signals from ISS...');
  const radioSignals = await fetchRadioSignals(latitude, longitude);

  if (!radioSignals) {
    console.log('Radio signals not found.');
    return;
  }

  console.log('\nNext passes over your location:');
  radioSignals.forEach(pass => {
    const passTime = new Date(pass.risetime * 1000);
    console.log(`- Duration: ${pass.duration} seconds, Rise Time: ${passTime}`);
  });
}

// Run the application
main();
