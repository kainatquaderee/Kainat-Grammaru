// Example: Replace text in all textareas on the page
document.querySelectorAll('textarea').forEach(textarea => {
  textarea.addEventListener('input', () => {
    const inputText = textarea.value;
    chrome.runtime.sendMessage({ action: 'processText', text: inputText }, (response) => {
      if (response.modifiedText) {
        textarea.value = response.modifiedText;
      }
    });
  });
});
