// document.addEventListener('DOMContentLoaded', function() {
//     var checkboxes = document.querySelectorAll('#question-five .checkbox-group input[type="checkbox"]');
//     checkboxes.forEach(function(checkbox) {
//       checkbox.addEventListener('change', function() {
//         var checkedCheckboxes = document.querySelectorAll('#question-five .checkbox-group input[type="checkbox"]:checked');
//         if (checkedCheckboxes.length > 3) {
//           alert('You can only select up to three options.');
//           checkbox.checked = false;
//         }
//       });
//     });
//   });

//   document.addEventListener('DOMContentLoaded', function() {
//     var checkboxes = document.querySelectorAll('#question-four .checkbox-group input[type="checkbox"]');
//     checkboxes.forEach(function(checkbox) {
//       checkbox.addEventListener('change', function() {
//         var checkedCheckboxes = document.querySelectorAll('#question-four .checkbox-group input[type="checkbox"]:checked');
//         if (checkedCheckboxes.length > 1) {
//           alert('You can only select one options.');
//           checkbox.checked = false;
//         }
//       });
//     });
//   });

// document.addEventListener('DOMContentLoaded', function() {
//   // Question Four Logic
//   var questionFourCheckboxes = document.querySelectorAll('#question-four .checkbox-group input[type="checkbox"]');
//   questionFourCheckboxes.forEach(function(checkbox) {
//       checkbox.addEventListener('change', function() {
//           questionFourCheckboxes.forEach(function(box) {
//               if (box !== checkbox) box.checked = false; // Deselect other checkboxes
//           });
//       });
//   });

//   // Question Five Logic
//   var questionFiveCheckboxes = document.querySelectorAll('#question-five .checkbox-group input[type="checkbox"]');
//   questionFiveCheckboxes.forEach(function(checkbox) {
//       checkbox.addEventListener('change', function() {
//           var checkedCheckboxes = document.querySelectorAll('#question-five .checkbox-group input[type="checkbox"]:checked');
//           if (checkedCheckboxes.length > 3) {
//               alert('You can only select up to three options.');
//               checkbox.checked = false;
//           }
//       });
//   });
// });

  

document.addEventListener('DOMContentLoaded', function () {
  // Restrict selection for question one (exactly one required answer)
  enforceSingleSelection('#question-one', 'You must select exactly one option for Question One.');

  // Restrict selection for question two (exactly one required answer)
  enforceSingleSelection('#question-two', 'You must select exactly one option for Question Two.');

  // Restrict selection for question three (exactly one required answer)
  enforceSingleSelection('#question-three', 'You must select exactly one option for Question Three.');

  // Restrict selection for question four (exactly one required answer)
  enforceSingleSelection('#question-four', 'You must select exactly one option for Question Four.');

  // Restrict up to 3 answers for question five
  enforceMaxSelection('#question-five', 3, 'You can only select up to three options for Question Five.');

  // Restrict up to 3 answers for question six
  enforceMaxSelection('#question-six', 3, 'You can only select up to three options for Question Six.');

  // Restrict up to 3 answers for question seven
  enforceMaxSelection('#question-seven', 3, 'You can only select up to three options for Question Seven.');

  // Restrict selection for question eight (exactly one required answer)
  enforceSingleSelection('#question-eight', 'You must select exactly one option for Question Eight.');

  // Restrict up to 2 answers for question nine
  enforceMaxSelection('#question-nine', 2, 'You can only select up to two options for Question Nine.');

  // Restrict selection for question ten (exactly one required answer)
  enforceSingleSelection('#question-ten', 'You must select exactly one option for Question Ten.');
});

/**
 * Enforces that only one checkbox is selected for a given question.
 * @param {string} questionSelector - The selector for the question's checkbox group.
 * @param {string} errorMessage - The error message to display if the rule is violated.
 */
function enforceSingleSelection(questionSelector, errorMessage) {
  var checkboxes = document.querySelectorAll(`${questionSelector} .checkbox-group input[type="checkbox"]`);
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      var checkedCheckboxes = document.querySelectorAll(`${questionSelector} .checkbox-group input[type="checkbox"]:checked`);
      if (checkedCheckboxes.length > 1) {
        alert(errorMessage);
        checkbox.checked = false;
      }
    });
  });
}

/**
 * Enforces that a maximum number of checkboxes are selected for a given question.
 * @param {string} questionSelector - The selector for the question's checkbox group.
 * @param {number} maxSelections - The maximum number of checkboxes allowed.
 * @param {string} errorMessage - The error message to display if the rule is violated.
 */
function enforceMaxSelection(questionSelector, maxSelections, errorMessage) {
  var checkboxes = document.querySelectorAll(`${questionSelector} .checkbox-group input[type="checkbox"]`);
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener('change', function () {
      var checkedCheckboxes = document.querySelectorAll(`${questionSelector} .checkbox-group input[type="checkbox"]:checked`);
      if (checkedCheckboxes.length > maxSelections) {
        alert(errorMessage);
        checkbox.checked = false;
      }
    });
  });
}
