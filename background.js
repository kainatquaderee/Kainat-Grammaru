chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'processText') {
    fetch('http://localhost:5000/process', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: request.text }),
    })
      .then((response) => response.json())
      .then((data) => {
        sendResponse({ modifiedText: data.modified_text });
      })
      .catch((error) => {
        console.error('Error:', error);
        sendResponse({ modifiedText: 'Error processing text.' });
      });
    return true; // Keep the message channel open for the response
  }
});
