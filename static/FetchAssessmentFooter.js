document.addEventListener('DOMContentLoaded', function() {
    fetch('/AssessmentFooterTemplate')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-placeholder').innerHTML = data;
        });
});