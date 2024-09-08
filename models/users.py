from controllers import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    userpassword = db.Column(db.LargeBinary, nullable=False)
    useremail = db.Column(db.String(50), unique=True, nullable=False)

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def add_user(username, userpassword, useremail):
        new_user = User(username=username, userpassword=userpassword, useremail=useremail)
        db.session.add(new_user)
        db.session.commit()