from model import User, db

class UserDAO:
    @staticmethod
    def buscar_todos_usuarios():
        return User.query.all()
    
    @staticmethod
    def add_usuario(nome, email):
        try:
            user = User(nome = nome, email = email)
            db.session.add(user)
            db.session.commit()
            return True
        
        except Exception as e:
            db.session.rollback()
            return False