const rtlSdr = require('rtl-sdr');

const deviceIndex = 0; // Index of your RTL-SDR device
const frequencyHz = 100.5e6; // Example frequency to tune to
const sampleRateHz = 2.4e6; // Sample rate (Hz)

rtlSdr.open(deviceIndex, (err, device) => {
    if (err) {
        console.error('Error opening device:', err);
        return;
    }

    rtlSdr.setCenterFreq(device, frequencyHz, (err) => {
        if (err) {
            console.error('Error setting frequency:', err);
            rtlSdr.close(device);
            return;
        }

        rtlSdr.setSampleRate(device, sampleRateHz, (err) => {
            if (err) {
                console.error('Error setting sample rate:', err);
                rtlSdr.close(device);
                return;
            }

            const buffer = Buffer.alloc(1024 * 16); // Buffer for samples
            rtlSdr.readSync(device, buffer, buffer.length, (err, bytesRead) => {
                if (err) {
                    console.error('Error reading samples:', err);
                } else {
                    console.log('Received', bytesRead, 'bytes');
                    // Process the received samples here
                }

                rtlSdr.close(device);
            });
        });
    });
});
