document.addEventListener('DOMContentLoaded', function () {
  // Restrict selection for page one question one (exactly one required answer)
  enforceSingleSelection('#question-one', 'You must select exactly one option for Question One.');

  // Restrict selection for page one question two (exactly one required answer)
  enforceSingleSelection('#question-two', 'You must select exactly one option for Question Two.');

  // Restrict selection for page one question three (exactly one required answer)
  enforceSingleSelection('#question-three', 'You must select exactly one option for Question Three.');

  // Restrict selection for page one question four (exactly one required answer)
  enforceSingleSelection('#question-four', 'You must select exactly one option for Question Four.');

  // Restrict up to 3 answers for page one question five
  enforceMaxSelection('#question-five', 3, 'You can only select up to three options for Question Five.');

  // Restrict up to 3 answers for page one question six
  enforceMaxSelection('#question-six', 3, 'You can only select up to three options for Question Six.');

  // Restrict up to 3 answers for page one question seven
  enforceMaxSelection('#question-seven', 3, 'You can only select up to three options for Question Seven.');

  // Restrict selection for page one question eight (exactly one required answer)
  enforceSingleSelection('#question-eight', 'You must select exactly one option for Question Eight.');

  // Restrict up to 2 answers for page one question nine
  enforceMaxSelection('#question-nine', 2, 'You can only select up to two options for Question Nine.');

  // Restrict selection for page one question ten (exactly one required answer)
  enforceSingleSelection('#question-ten', 'You must select exactly one option for Question Ten.');

  // Restrict up to 3 answers for page two question one
  enforceMaxSelection('#page-two-question-one', 3, 'You can only select up to three options for Question One.');

  // Restrict up to 3 answers for page two question two
  enforceMaxSelection('#page-two-question-two', 3, 'You can only select up to three options for Question Two.');

  // Restrict up to 3 answers for page two question three
  enforceMaxSelection('#page-two-question-three', 3, 'You can only select up to three options for Question Three.');

  // Restrict up to 3 answers for page two question four
  enforceMaxSelection('#page-two-question-four', 3, 'You can only select up to three options for Question Four.');

  // Restrict up to 3 answers for page two question five
  enforceMaxSelection('#page-two-question-five', 3, 'You can only select up to three options for Question Five.');

  // Restrict up to 3 answers for page two question six
  enforceMaxSelection('#page-two-question-six', 3, 'You can only select up to three options for Question Six.');

  // Restrict up to 3 answers for page two question seven
  enforceMaxSelection('#page-two-question-seven', 3, 'You can only select up to three options for Question Seven.');

  // Restrict up to 3 answers for page two question eight
  enforceMaxSelection('#page-two-question-eight', 3, 'You can only select up to three options for Question Eight.');

  // Restrict up to 3 answers for page two question nine
  enforceMaxSelection('#page-two-question-nine', 3, 'You can only select up to three options for Question Nine.');

  // Restrict up to 3 answers for page two question ten
  enforceMaxSelection('#page-two-question-ten', 3, 'You can only select up to three options for Question Ten.');
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
