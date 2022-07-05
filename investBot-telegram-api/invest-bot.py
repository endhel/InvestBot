import os
import pandas   as pd
import json
import requests
from   flask    import Flask, request, Response
                
def send_message( chat_id, text ):
    url = 'https://api.telegram.org/bot{}/'.format( TOKEN )
    url = url + 'sendMessage?chat_id={}'.format( chat_id )
    
    r = requests.post( url, json={ 'text': text } )
    print( 'Status code {}'.format( r.status_code ) )
    
    return None
    

def load_dataset( paper_code ):
    # Importing 
    df1 = pd.read_csv( 'Fundamentals.csv' )

    # loading test dataset
    test_dataset = df1.loc[df1['Company'] == paper_code, :][-2:]
    
    if not test_dataset.empty:

        # Reading the dataset of the number of papers available
        df_qnt = pd.read_csv( 'quantity.csv' )

        # merge
        test_dataset = pd.merge( test_dataset, df_qnt, how='inner', on=['Company'] )

        # change data type
        test_dataset['quantity'] = test_dataset['quantity'].astype( 'int64' )

        # convert DataFrame to json
        data = json.dumps( test_dataset.to_dict( orient='records' ) )
        
    else:
        data = 'error'
        
    return data

def predict( data ):

    # API call
    url = 'https://investbot-model.herokuapp.com/investbot/predict'
    header = {'Content-type': 'application/json' }
    data = data

    r = requests.post( url, data = data, headers = header )
    print( f'Status Code {r.status_code}' )

    result = pd.DataFrame( r.json(), columns=r.json()[0].keys() )
    
    return result

def parse_message( message ):
    try:
        chat_id = message['message']['chat']['id']
        paper_code = message['message']['text']
    except:
        return '', ''
    
    paper_code = paper_code.replace( '/', '' )
    
    return chat_id, paper_code

# API initialize
app = Flask( __name__ )

@app.route( '/', methods=['GET', 'POST'] )
def index():
    if request.method == 'POST':
        message = request.get_json()
        
        chat_id, paper_code = parse_message( message )
        # loading data
        data = load_dataset( paper_code )
        
        if data != 'error':
            # prediction
            result = predict( data )
            
            # send message
            if result.loc[0, 'prediction']:
                msg = 'O papel {} irá render 3% ou mais até o próximo trimestre!'.format( result.loc[0, "Company"] )
            else:
                msg = 'O papel {} não irá render 3% ou mais até o próximo trimestre!'.format( result.loc[0, "Company"] )
            
            send_message( chat_id, msg )
            return Response( 'OK', status=200 )
                
        else:
            send_message( chat_id, 'Código de Ação Inválido!' )
            return Response( 'OK', status=200 )
    
    else:
        return '<h1> InvestBot </h1>'

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( host='0.0.0.0', port=port )
