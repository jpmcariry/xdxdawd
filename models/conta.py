from sql_alchemy import banco

class ContaModel(banco.Model):
    __tablename__ = 'usuarios'
    user_id = banco.Column(banco.Integer, primary_key=True)
    user_ip = banco.Column(banco.String(20))
    user_resoluction= banco.Column(banco.String(9))
    status = banco.Column(banco.Integer)

    def __init__(self, user_ip, user_resoluction, status):
        self.user_ip = user_ip
        self.user_resoluction = user_resoluction
        self.status = status

    def json(self):
        return {
            'user_ip': self.user_ip,
            'user_resoluction': self.user_resoluction,
            'status': self.status
        }

    @classmethod
    def seach(cls, user_ip):
        user = cls.query.filter_by(user_ip=user_ip).first()
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()

    def update_user(self, status):
        self.status = status

class UsernameModel(banco.Model):
    __tablename__ = 'username'
    user_id = banco.Column(banco.Integer, primary_key=True)
    user_ip = banco.Column(banco.String(20))
    user_name = banco.Column(banco.String(25))

    def __init__(self, user_ip, user_name):
        self.user_ip = user_ip
        self.user_name = user_name
    def json(self):
        return {
            'user_ip': self.user_ip,
            'user_name': self.user_resoluction
        }

    @classmethod
    def seach(cls, user_name):
        user = cls.query.filter_by(user_name=user_name).first()
        if user:
            return user
        return None
    def save_user(self):
        banco.session.add(self)
        banco.session.commit()