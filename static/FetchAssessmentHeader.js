document.addEventListener('DOMContentLoaded', function() {
    fetch('/AssessmentHeaderTemplate')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-placeholder').innerHTML = data;
        });
});