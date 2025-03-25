document.getElementById('processButton').addEventListener('click', () => {
  const inputText = document.getElementById('inputText').value;
  if (inputText.trim() === '') {
    alert('Please enter some text.');
    return;
  }

  chrome.runtime.sendMessage(
    { action: 'processText', text: inputText },
    (response) => {
      document.getElementById('outputText').textContent = response.modifiedText;
    }
  );
});
