document.addEventListener('DOMContentLoaded', (event) => {
    // Function to save data to localStorage
    function saveSessionData() {
      // Save text input
      document.querySelectorAll('.question-container input[type="text"]').forEach(input => {
        localStorage.setItem(input.id, input.value);
      });
  
      // Save radio input
      document.querySelectorAll('.question-container input[type="radio"]').forEach(radio => {
        if (radio.checked) {
          localStorage.setItem(radio.name, radio.value);
        }
      });
  
      // Save checkbox input
      document.querySelectorAll('.question-container input[type="checkbox"]').forEach(checkbox => {
        localStorage.setItem(checkbox.id, checkbox.checked);
      });
    }
  
    // Retrieve the saved data when the page loads
    document.querySelectorAll('.question-container input').forEach(input => {
      const savedValue = localStorage.getItem(input.id);
      if (input.type === 'checkbox') {
        input.checked = savedValue === 'true' ? true : false;
      } else if (input.type === 'radio') {
        if (input.value === savedValue) {
          input.checked = true;
        }
      } else {
        input.value = savedValue || '';
      }
    });
  
    // Add event listener to the save button
    const saveButton = document.querySelector('button[name="save"]');
    saveButton.addEventListener('click', saveSessionData);
  });
  