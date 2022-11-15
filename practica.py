# consume los datos del archivo de inversiones
# almacena en un dataframe el NOM_EMS, la superficie y el TIPUSSOL
# giráfico de dspersión de los importes de inversiones por TIPUSSOL
# gráfico de barras de la inversión media de los 10 primeros NOM_ENS
# grafico circular de las inversiones de 10 TIPUSSOL
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

def consumirInversiones():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df = datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL','CODI_TIPUSSOL']]
    #print(df)
    df.CODI_TIPUSSOL.plot.hist()
    plt.show()
consumirInversiones()

