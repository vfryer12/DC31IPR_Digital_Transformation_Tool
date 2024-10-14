from flask import Flask, render_template, redirect, url_for, session
import secrets

def create_app():
    app = Flask(__name__)
    app.secret_key = secrets.token_hex(16)

    # Import and register blueprints
    from controllers.login_controller import login_bp
    from controllers.registration_controller import registration_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(registration_bp)
    

    @app.route('/')
    def index():
        if 'username' in session:
            # User's profile page
            return render_template('HomePage.html')
        else:
            return redirect(url_for('login.login'))
        
    
    @app.route('/registration')
    def registration_page():
        return render_template('RegistrationPage.html')

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

    @app.route('/AssessmentHeaderTemplate')
    def assessment_header_template():
        return render_template('AssessmentHeaderTemplate.html')

    @app.route('/AssessmentFooterTemplate')
    def assessment_footer_template():
        return render_template('AssessmentFooterTemplate.html')

    return app