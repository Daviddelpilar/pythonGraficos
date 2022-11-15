import pandas as pd
import matplotlib.pyplot as plt

def consumirHistograma():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX']] #convertir datos en dataframe
    #print(df)
    df.RM.plot.hist()
    plt.show()

#consumirHistograma()

def consumirDispersion():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] #convertir datos en dataframe
    #print(df)
    df.plot.scatter(x='CRIM',y='MEDV',alpha=0.3)
    plt.show()

#consumirDispersion()

def consumirBarras():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] #convertir datos en dataframe
    #print(df)
    valor_por_ciudad = df.groupby("TOWN")["MEDV"].mean()
    valor_por_ciudad.head(5).plot.barh()
    plt.show()

#consumirBarras()

def consumirCajas():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] #convertir datos en dataframe
    #print(df)
    #df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
    df.head(10).boxplot(column="MEDV", by="CRIM",figsize=(8, 6))
    plt.show()

#consumirCajas()

def consumirCircular():
    datos=pd.read_csv('casasboston.csv')
    #print(datos)
    df=datos[['RM','CRIM','TOWN','TAX','MEDV']] #convertir datos en dataframe
    #print(df)
    #df["VALOR_CUANTILES"] = pd.qcut(df.VALOR_MEDIANO, 5)
    df.CRIM.head(10).value_counts().plot.pie()
    plt.show()

consumirCircular()
