from dao import UserDAO

class UserRepository:
    def __init__(self):
        self.userDao = UserDAO()

    def buscar_todos_usuarios_json(self):
        users = UserDAO.buscar_todos_usuarios()
        listinha = []
        for user in users:
            listinha.append(user.toJson())
        return listinha
    
    def buscar_todos_usuarios(self):
        return UserDAO.buscar_todos_usuarios()
    
    def add_usuario(self, nome, email):
        retorno = UserDAO.add_usuario("Dudinha", "dudinha@dudu.com")
        if retorno:
            return "Adicionado com sucesso! :)" 
        return "Erro ao adicionar! :("
    
    
        
# toda vez que se cria um repositório é necessário criar um dao 