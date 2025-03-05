window.addEventListener('load', function() {
    const numberLabelsContainer = document.querySelector('#question-one .number-labels');
    const rangeInput = document.querySelector('#question-one input[type=range]');

    // Calculate the width of the range input instead of the container
    const rangeWidth = rangeInput.offsetWidth;
    const labelWidth = 18;

    for (let i = 0; i <= 10; i++) {
        let label = document.createElement('span');
        label.textContent = i;
        
        // Calculate the offset for each label to center it, considering the label width
        const offset = (labelWidth / 2) / (rangeWidth / 100);
        const position = (i * 10) - offset;

        // Set the top style, clamping values between 0% and 100%
        label.style.top = `clamp(-100%, -${position}%, -200%)`;

        numberLabelsContainer.appendChild(label);
    }
});


document.getElementById('question-two-dropdown').addEventListener('change', function() {
    var otherText = document.getElementById('other-text');
    if(this.value === 'other') {
        otherText.style.display = 'inline-block';
    } else {
        otherText.style.display = 'none';
        document.getElementById('list-output').innerHTML = '';
    }
});

document.getElementById('other-text').addEventListener('keypress', function(event) {
    if(event.key === 'Enter') {
        event.preventDefault();
        var listOutput = document.getElementById('list-output');
        // Clear the list before adding new item to ensure only one item is in the list
        listOutput.innerHTML = '';
        var listItem = document.createElement('div');
        listItem.className = 'list-item';
        listItem.textContent = this.value;
        
        var removeBtn = document.createElement('span');
        removeBtn.textContent = 'X';
        removeBtn.className = 'remove-item';
        removeBtn.onclick = function() {
            listOutput.innerHTML = '';
        };
        
        listItem.appendChild(removeBtn);
        listOutput.appendChild(listItem);
        this.value = ''; // Clear the input field after adding to the list
    }
});


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button[onclick="history.back();"]').addEventListener('click', function() {
        history.back();
    });
});

document.getElementById('next-button').addEventListener('click', function() {
    var otherText = document.getElementById('other-text');
    if(document.getElementById('question-two-dropdown').value === 'other' && !otherText.value.trim()) {
        alert('Please specify the role in the text box.');
    } else {
        window.location = 'PageTwoDigitalSkills.html';
    }
});

document.getElementById('save-button').addEventListener('click', function(event) {
    var otherText = document.getElementById('other-text');
    if(document.getElementById('question-two-dropdown').value === 'other' && !otherText.value.trim()) {
        event.preventDefault();
        alert('Please specify the role in the text box before saving.');
    }
});