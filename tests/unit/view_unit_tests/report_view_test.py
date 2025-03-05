import pytest
from bs4 import BeautifulSoup
from app import create_app


@pytest.fixture
def client():
    
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_report_page_structure(client):
    mock_data = {
        "total_score": 85,
        "overall_feedback": "Good progress, but there's room for improvement in some areas.",
        "section_feedback": {
            "Digital Strategy": "Strong vision but needs better implementation.",
            "Digital Skills": "Adequate, but training is needed in advanced tools.",
            "Technology Adoption": "Lacks integration of modern tools.",
            "Market Trends": "Good awareness, but implementation is slow.",
            "Digital Marketing": "Great strategies but inconsistent execution.",
        },
        "knn_sections": [
            {"section": "Technology Adoption", "distance": 5.3},
            {"section": "Digital Skills", "distance": 3.8},
        ],
        "user_scores": {
            "Digital Strategy": 80,
            "Digital Skills": 75,
            "Technology Adoption": 60,
            "Market Trends": 85,
            "Digital Marketing": 90,
        },
        "recommended_solutions": {
            "Digital Strategy": ["Define clearer goals.", "Improve cross-department communication."],
            "Technology Adoption": ["Invest in cloud-based solutions.", "Provide technical training."],
        },
    }

    # Inject mock data into the test using the template rendering
    with client.application.app_context():
        from flask import render_template

        # Render the page with the mock data
        html = render_template('ReportPage.html', **mock_data)

    # Parse the rendered HTML for testing
    soup = BeautifulSoup(html, 'html.parser')

    # Validate structure
    assert soup.title.string == "Report Page"
    assert soup.find('div', {'id': 'header-placeholder'}) is not None
    assert soup.find('div', {'id': 'footer-placeholder'}) is not None
    assert "Good progress" in soup.text