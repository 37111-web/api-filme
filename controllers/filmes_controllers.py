from models.filmes_models import filmes   
from db import db                        
from flask import make_response

def get_filmes():
    filmes = filmes.query.all()  
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de filmes.',
            'dados': [filmes.json() for filmes in filmes]  
        }, ensure_ascii=False, sort_keys=False)  
    )
    response.headers['Content-Type'] = 'application/json'  
    return response

def get_filmes_by_id(filmes_id):
    filmes = filmes.query.get(filmes_id)  

    if filmes: 
        response = make_response(
            json.dumps({
                'mensagem': 'filmes encontrado.',
                'dados': filmes.json()  
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
    else:
        
        response = make_response(
            json.dumps({'mensagem': 'filmes não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  
        )
        response.headers['Content-Type'] = 'application/json'  
        return response
        
def create_filmes(filmes_data):           
    novo_filmes = filmes(  
                       
        titulo=filmes_data['titulo'],     
        genero=filmes_data['genero'],       
        ano=filmes_data['ano'],
        duracao=filmes_data['duracao'],
        diretor=filmes_data['diretor']                                
    )
    db.session.add(novo_filmes)          
    db.session.commit()                  
    response = make_response(            
        json.dumps({                      
            'mensagem': 'filmes cadastrado com sucesso.',  
            'filmes': novo_filmes.json()   
        }, sort_keys=False)               
    )
    response.headers['content-Type'] = 'application/json'  
    return response                      

