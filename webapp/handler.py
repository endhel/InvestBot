import os
import pickle
import pandas              as pd
from   flask               import Flask, request, Response
from   investBot.InvestBot import Preparation

# loading model
model = pickle.load( open( 'model/tuned_model.pkl', 'rb' ) )

# initialize API
app = Flask( __name__ )

@app.route( '/investbot/predict', methods=['POST'] )
def invest_bot():
    test_json = request.get_json()
    
    if test_json: # there is data
        test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
        
        # Instatiate
        pipeline = Preparation()

        # data cleaning
        df1 = pipeline.data_cleaning( test_raw )

        # feature engineering
        df2 = pipeline.feature_engineering( df1 )
        
        # data_filtering
        df3 = pipeline.data_filtering( df2 )

        # transform to percentage changes
        df4 = pipeline.transform_to_percentage_changes( df3 )

        # data preparation
        df5 = pipeline.data_preparation( df4 )

        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df5 )

        return df_response
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )
    
if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( host='0.0.0.0', port=port )