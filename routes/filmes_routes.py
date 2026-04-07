from flask import Blueprint, request                  
                                                      
from controllers.filmes_controllers import create_filmes, get_filmes
                                                      

filmes_routes = Blueprint('filmes_routes', __name__)    
                                                      

@filmes_routes.route('/Filmes', methods=['GET'])
def filmes_get():
    return get_filmes()

@filmes_routes.route('/Filmes', methods=['POST'])       
def filmes_post():                                    
    filmes_data = request.json                         
    return create_filmes(request.json)                 
