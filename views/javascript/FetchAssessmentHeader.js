document.addEventListener('DOMContentLoaded', function() {
    fetch('templates/AssessmentHeaderTemplate.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-placeholder').innerHTML = data;
        });
});