import pickle
import pandas as pd
import numpy  as np

class Preparation( object ):
    def __init__( self ):
        self.home_path = ''
        self.scaler = pickle.load( open( self.home_path + 'parameter/scaler.pkl', 'rb' ) )
    
    def data_cleaning( self, df_raw ):
        df1 = df_raw.fillna( 0 )
        return df1
    
    def feature_engineering( self, df2 ):
        # Liquidez Corrente
        df2['Liquidez Corrente'] = df2[['Ativo Circulante', 'Passivo Circulante']].apply( lambda x: 0 if x['Passivo Circulante'] == 0 
                                                                        else x['Ativo Circulante'] / x['Passivo Circulante'], axis=1 )
        # LPA
        df2['LPA'] = df2['Lucro/Prejuízo do Período'] / df2['quantity'] 

        # P/L
        df2['P/L'] = df2[['Adj Close', 'LPA']].apply( lambda x: 0 if x['LPA'] == 0 else x['Adj Close'] / x['LPA'], axis=1 )

        # VPA
        df2['VPA'] = df2['Patrimônio Líquido'] / df2['quantity']

        # P/VP 
        df2['P/VP'] = df2[['Adj Close', 'VPA']].apply( lambda x: 0 if x['VPA'] == 0 else x['Adj Close'] / x['VPA'], axis=1 )

        # EBIT - NAO TEM!!
        df2['EBIT'] = df2['Receita Líquida de Vendas e/ou Serviços'] - df2['Custo de Bens e/ou Serviços Vendidos'] - ( df2['Despesas Com Vendas'] + df2['Despesas Gerais e Administrativas'] )

        # EV/EBIT - NAO TEM!!!!
        df2['EV/EBIT'] = df2[['Adj Close', 'quantity', 'Empréstimos e Financiamentos_1', 'Ativo Circulante', 'EBIT']].apply( lambda x: 0 
                                                            if x['EBIT'] == 0 else ( ( x['Adj Close'] * x['quantity'] ) 
                                                                                    + ( x['Empréstimos e Financiamentos_1'] 
                                                                                    - x['Ativo Circulante'] ) ) 
                                                                                    / x['EBIT'] , axis=1 )
        # NOPLAT - NAO TEM!!!!
        df2['NOPLAT'] = df2['EBIT'] - df2['IR Diferido']

        # ROIC - NAO TEM!!!!
        df2['ROIC'] = df2[['NOPLAT', 'Investimentos']].apply( lambda x: 0 if x['Investimentos'] == 0 
                                                                          else x['NOPLAT'] / x['Investimentos'], axis=1 )

        # ROE
        df2['ROE'] = df2[['Reservas de Lucros', 'Patrimônio Líquido']].apply( lambda x: 0 
                                                        if x['Patrimônio Líquido'] == 0 
                                                        else x['Reservas de Lucros'] / x['Patrimônio Líquido'], axis=1 )

        # Pay-Out
        df2['Pay-Out'] = df2[['Dividendos e JCP a Pagar', 'Lucro/Prejuízo do Período']].apply( lambda x: 0 
                                           if x['Lucro/Prejuízo do Período'] == 0 
                                           else ( x['Dividendos e JCP a Pagar'] / x['Lucro/Prejuízo do Período'] ) * 100, axis=1 )

        # Dividend Yield
        df2['Dividend Yield'] = ( ( df2['Dividendos e JCP a Pagar'] / df2['quantity'] ) / df2['Adj Close'] ) * 100

        # Marg. Ebit - NAO TEM!!!!
        df2['MargEbit'] = df2[['EBIT', 'Receita Líquida de Vendas e/ou Serviços']].apply( lambda x: 0 
                                                                if x['Receita Líquida de Vendas e/ou Serviços'] == 0 
                                                                else x['EBIT'] / x['Receita Líquida de Vendas e/ou Serviços'], axis=1 )

        # Marg. Liquida 
        df2['MargLiquida'] = df2[['Lucro/Prejuízo do Período', 'Receita Líquida de Vendas e/ou Serviços']].apply( lambda x: 0 
                                          if x['Receita Líquida de Vendas e/ou Serviços'] == 0 
                                          else x['Lucro/Prejuízo do Período'] / x['Receita Líquida de Vendas e/ou Serviços'], axis=1 )

        # P/Ebit 
        df2['P/Ebit'] = df2[['Adj Close', 'EBIT']].apply( lambda x: 0 if x['EBIT'] == 0 else x['Adj Close'] / x['EBIT'], axis=1 )

        # PSR
        df2['PSR'] = df2[['Adj Close', 'Receita Líquida de Vendas e/ou Serviços', 'quantity']].apply( lambda x: 0 
                                        if x['Receita Líquida de Vendas e/ou Serviços'] == 0 
                                        else x['Adj Close'] / ( x['Receita Líquida de Vendas e/ou Serviços'] / x['quantity'] ), axis=1 )

        # P/Ativos
        df2['P/Ativos'] = df2[['Adj Close', 'Ativo Total', 'quantity']].apply( lambda x: 0 if x['Ativo Total'] == 0 
                                                                    else x['Adj Close'] / ( x['Ativo Total'] / x['quantity'] ), axis=1 )

        # Giro do Ativo Total
        df2.loc[:, 'GA'] = df2[['Receita Líquida de Vendas e/ou Serviços', 'Ativo Total']].apply( lambda x: 0 if x['Ativo Total'] == 0
                                                          else x['Receita Líquida de Vendas e/ou Serviços'] / x['Ativo Total'], axis=1 )

        # ROA - Retorno do Ativo Total
        df2.loc[:, 'ROA'] = df2[['Lucro/Prejuízo do Período', 'Ativo Total']].apply( lambda x: 0 if x['Ativo Total'] == 0
                                                                         else  x['Lucro/Prejuízo do Período'] / x['Ativo Total'], axis=1 )
        return df2
    
    def data_filtering( self, df3 ):
        df3 = df3.loc[ ( df3['Company'] != 'MMAQ3' ) & ( df3['Company'] != 'MMAQ4' ) &
               ( df3['Company'] != 'VSPT3' ) & ( df3['Adj Close'] > 0 ) ]   
        
        df3 = df3.drop( ['Perc', 'quantity', 'Adj Close', 'Class'], axis=1 )
        
        return df3
    
    def transform_to_percentage_changes( self, df4 ):

        for column in df4:
            if column == 'Company':
                continue

            conditions = [
                ( df4[column].shift( 1 ) == 0 ) & ( df4[column] > 0 ),
                ( df4[column].shift( 1 ) == 0 ) & ( df4[column] < 0 ),
                ( df4[column].shift( 1 ) == 0 ) & ( df4[column] == 0 )
            ]

            values = [1, -1, 0]

            df4[column] = np.select( conditions, values, default=df4[column].diff() / df4[column].abs().shift() )

        return df4.drop( df4.index[0], axis=0 )
    
    def data_preparation( self, df5 ):
        df5.drop( 'Company', axis=1, inplace=True )
        
        # scaling
        df5 = pd.DataFrame( self.scaler.transform( df5 ), index=df5.index, columns=df5.columns )
        
        # feature selection
        cols_selected = ['Ativo Total',
                         'Caixa e Equivalentes de Caixa',
                         'Imobilizado',
                         'Passivo Total',
                         'Patrimônio Líquido',
                         'Lucros/Prejuízos Acumulados',
                         'Financeiras',
                         'P/L',
                         'VPA',
                         'P/VP',
                         'MargEbit',
                         'P/Ativos']

        return df5[ cols_selected ]
    
    def get_prediction( self, model, original_data, test_data ):
        # prediction
        pred = model.predict( test_data )
        
        original_data.drop( 0, axis=0, inplace=True )
        
        # join pred into the original data
        original_data['prediction'] = pred
        
        return original_data.to_json( orient='records' )