document.addEventListener('DOMContentLoaded', function() {
    fetch('templates/AssessmentFooterTemplate.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-placeholder').innerHTML = data;
        });
});