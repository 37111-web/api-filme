from db import db                       # DE db IMPORTAR db: importa a instância do SQLAlchemy que gerencia o banco de dados

class filmes(db.Model):                   # Define a classe filme como um titulo do SQLAlchemy (herda de db.Model)
    __tablename__ = 'filmes'              # Nome da tabela no banco de dados será "filmes"

    id = db.Column(db.Integer, primary_key=True)          # Coluna "id": número inteiro, chave primária (identificador único)
    titulo = db.Column(db.String(80), nullable=False)     # Coluna "titulo": texto com limite de 80 caracteres, não pode ser nula
    genero = db.Column(db.String(80), nullable=False)
    ano = db.Column(db.Integer, nullable=False)    
    duracao = db.Column(db.Integer, nullable=False)
    diretor = db.Column(db.String(80), nullable=False)           # Coluna "duracao": número inteiro, não pode ser nulo

    def json(self):                                        # Define o método json() que retorna os dados do filme como dicionário
        return {
            'id': self.id,            
            'titulo': self.titulo,   
            'genero': self.genero,  
            'ano': self.ano,    
            'duracao': self.duracao,
            'diretor': self.diretor                                            
        }
