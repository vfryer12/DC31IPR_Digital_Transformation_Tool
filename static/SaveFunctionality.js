

document.addEventListener('DOMContentLoaded', function() {
    restoreForm();

    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault();
        saveForm();
    });

    // Save data when the save button is clicked
    document.getElementById('save-button').addEventListener('click', function() {
        saveForm();
    });
});

function saveForm() {
    var formData = {};
    document.querySelectorAll('input, select').forEach(function(input) {
        if ((input.type === 'checkbox' || input.type === 'radio') && input.checked) {
            formData[input.id] = input.value;
        } else if (input.type === 'range') {
            formData[input.id] = input.value;
        } else if (input.type !== 'checkbox' && input.type !== 'radio') {
            formData[input.id] = input.value;
        }
    });

    localStorage.setItem(window.location.pathname, JSON.stringify(formData));
    alert('Form data saved!');
}

function restoreForm() {
    var formData = JSON.parse(localStorage.getItem(window.location.pathname));

    if (formData) {
        for (var id in formData) {
            var input = document.getElementById(id);
            if (input) {
                if ((input.type === 'checkbox' || input.type === 'radio') && input.value === formData[id]) {
                    input.checked = true;
                } else if (input.type === 'range') {
                    input.value = formData[id];
                } else {
                    input.value = formData[id];
                }
            }
        }
    }
}
