document.addEventListener('DOMContentLoaded', function() {
    var checkboxes = document.querySelectorAll('#question-five .checkbox-group input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
      checkbox.addEventListener('change', function() {
        var checkedCheckboxes = document.querySelectorAll('#question-five .checkbox-group input[type="checkbox"]:checked');
        if (checkedCheckboxes.length > 3) {
          alert('You can only select up to three options.');
          checkbox.checked = false;
        }
      });
    });
  });
  