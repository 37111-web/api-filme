from flask import Flask                                  # DE flask IMPORTAR Flask: classe principal usada para criar a aplicação web
from db import db                                        # DE db IMPORTAR db: instância do SQLAlchemy que gerencia a conexão com o banco
from routes.filmes_routes import filmes_routes             # DE routes.filmes_routes IMPORTAR filmes_routes: conjunto de rotas do módulo filmes

app = Flask(__name__)                                    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///filmes.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
db.init_app(app)                                         

app.register_blueprint(filmes_routes)                     

if __name__ == '__main__':                               
    with app.app_context():                             
        db.create_all()                                  
    app.run(debug=True)                                  
