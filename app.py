from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HomePage.html')

# Assessment Page Routes
@app.route('/PageOneDigitalStrategy')
def page_one_digital_strategy():
    return render_template('PageOneDigitalStrategy.html')

@app.route('/PageTwoDigitalSkills')
def page_two_digital_skills():
    return render_template('PageTwoDigitalSkills.html')

@app.route('/PageThreeTechnologyAdoption')
def page_three_technology_adoption():
    return render_template('PageThreeTechnologyAdoption.html')

@app.route('/PageFourMarketTrends')
def page_four_market_trends():
    return render_template('PageFourMarketTrends.html')

@app.route('/PageFiveDigitalMarketing')
def page_five_digital_marketing():
    return render_template('PageFiveDigitalMarketing.html')

# Template Routes
@app.route('/AssessmentHeaderTemplate')
def assessment_header_template():
    return render_template('AssessmentHeaderTemplate.html')

@app.route('/AssessmentFooterTemplate')
def assessment_footer_template():
    return render_template('AssessmentFooterTemplate.html')

if __name__ == "__main__":
    app.run(debug=True)