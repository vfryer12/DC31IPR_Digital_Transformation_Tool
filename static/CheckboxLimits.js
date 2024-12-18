document.addEventListener('DOMContentLoaded', function () {

  //Page One
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

  //Page Two
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

  //Page Three
  // Restrict up to 3 answers for page three question one
  enforceMaxSelection('#page-three-question-one', 3, 'You can only select up to three options for Question One.');
  // Restrict selection for page three question two (exactly one required answer)
  enforceSingleSelection('#page-three-question-two', 'You must select exactly one option for Question Two.');
  // Restrict up to 3 answers for page three question three
  enforceMaxSelection('#page-three-question-three', 3, 'You can only select up to three options for Question Three.');
  // Restrict up to 3 answers for page three question four
  enforceMaxSelection('#page-three-question-four', 3, 'You can only select up to three options for Question Four.');
  // Restrict up to 3 answers for page three question five
  enforceMaxSelection('#page-three-question-five', 3, 'You can only select up to three options for Question Five.');
  // Restrict up to 3 answers for page three question six
  enforceMaxSelection('#page-three-question-six', 3, 'You can only select up to three options for Question Six.');
  // Restrict up to 3 answers for page three question seven
  enforceMaxSelection('#page-three-question-seven', 3, 'You can only select up to three options for Question Seven.');
  // Restrict up to 3 answers for page three question eight
  enforceMaxSelection('#page-three-question-eight', 3, 'You can only select up to three options for Question Eight.');
  // Restrict up to 3 answers for page three question nine
  enforceMaxSelection('#page-three-question-nine', 3, 'You can only select up to three options for Question Nine.');
  // Restrict up to 3 answers for page three question ten
  enforceMaxSelection('#page-three-question-ten', 3, 'You can only select up to three options for Question Ten.');

  //Page Four
  // Restrict up to 3 answers for page four question One
  enforceMaxSelection('#page-four-question-one', 3, 'You can only select up to three options for Question One.');
  // Restrict selection for page four question one (exactly one required answer)
  enforceSingleSelection('#page-four-question-two', 'You must select exactly one option for Question Two.');
  // Restrict up to 3 answers for page four question three
  enforceMaxSelection('#page-four-question-three', 3, 'You can only select up to three options for Question Three.');
  // Restrict up to 3 answers for page four question four
  enforceSingleSelection('#page-four-question-four', 'You must select exactly one option for Question Four.');
  // Restrict up to 3 answers for page four question five
  enforceSingleSelection('#page-four-question-five', 'You must select exactly one option for Question Five.');
  // Restrict up to 3 answers for page four question six
  enforceMaxSelection('#page-four-question-six', 3, 'You must select exactly one option for Question Six.');
  // Restrict up to 3 answers for page four question seven
  enforceMaxSelection('#page-four-question-seven', 3, 'You must select exactly one option for Question Seven.');
  // Restrict up to 3 answers for page four question eight
  enforceSingleSelection('#page-four-question-eight', 'You must select exactly one option for Question Eight.');
  // Restrict up to 3 answers for page four question nine
  enforceSingleSelection('#page-four-question-nine', 'You must select exactly one option for Question Nine.');
  // Restrict up to 3 answers for page four question ten
  enforceSingleSelection('#page-four-question-ten', 'You must select exactly one option for Question Ten.');

  //Page Five
  // Restrict up to 3 answers for page five question One
  enforceMaxSelection('#page-five-question-one', 3, 'You can only select up to three options for Question One.');
  // Restrict up to 3 answers for page five question two
  enforceMaxSelection('#page-five-question-two', 3, 'You can only select up to three options for Question Two.');
  // Restrict up to 3 answers for page five question three
  enforceMaxSelection('#page-five-question-three', 3, 'You can only select up to three options for Question Three.');
  // Restrict up to 3 answers for page five question four
  enforceSingleSelection('#page-five-question-four', 'You must select exactly one option for Question Four.');
  // Restrict up to 3 answers for page five question five
  enforceSingleSelection('#page-five-question-five', 'You must select exactly one option for Question Five.');
  // Restrict up to 3 answers for page five question six
  enforceMaxSelection('#page-five-question-six', 3, 'You can only select up to three options for Question Six.');
  // Restrict up to 3 answers for page five question seven
  enforceMaxSelection('#page-five-question-seven', 3, 'You can only select up to three options for Question Seven.');
  // Restrict up to 3 answers for page five question eight
  enforceSingleSelection('#page-five-question-eight', 'You must select exactly one option for Question Eight.');
  // Restrict up to 3 answers for page five question nine
  enforceSingleSelection('#page-five-question-nine', 'You must select exactly one option for Question Nine.');
  // Restrict up to 3 answers for page five question ten
  enforceSingleSelection('#page-five-question-ten', 'You must select exactly one option for Question Ten.');
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
