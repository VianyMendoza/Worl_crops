import pandas as pd
import os

#Leer archivos
def read_files(file_paths):
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = pd.read_csv(path, encoding='windows-1252')
    return dataframes

#Identificar nulos
def explore_files(df):
    valores_nulos = df.isna().sum()
    print("Valores atípicos", valores_nulos)
    return df

#Concatenar archivos
def concat_data(dfs):
    combined_df = pd.concat(dfs)
    return combined_df

#Ajustar archivo, reenombrar continentes
def transform_data(df):
    continentes = {
        'africa' : 'África',
        'america' : 'Ámerica',
        'asia' : 'Asia',
        'europa' : 'Europa',
        'oceania' : 'Oceanía'
    }
    df['continente'] = df['continente'].map(continentes)

    columns_to_remove = [col for col in df.columns if col.endswith('F')]
    df = df.drop(columns=columns_to_remove)

    df.fillna(0, inplace=True)

    return df


#Cargar archivo
def load_processed_data(df, output_path):
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    df.to_csv(output_path, index=False, encoding='windows-1252')

#Rutas a los archivos
file_paths ={
    'africa' : r'raw\\Production_Crops_E_Africa.csv',
    'america' : r'raw\\Production_Crops_E_Americas.csv',
    'asia' : r'raw\\Production_Crops_E_Asia.csv',
    'europa' : r'raw\\Production_Crops_E_Europe.csv',
    'oceania' : r'raw\\Production_Crops_E_Oceania.csv'    
}

#Llama a leer archivos
dataframes = read_files(file_paths)

#Crea diccionario
e_dataframes = {name: explore_files(
    df) for name, df in dataframes.items()}

#Agreaga columna con continente
dataframes_with_keys = [
    df.assign(continente=key) for key, df in e_dataframes.items()
]

#Llama a concatenar df
df_combined = concat_data(dataframes_with_keys)

#Llama a la función par transformar el df final
df_final = transform_data(df_combined)
print(df_final)

#Carga el producto de la transformación
load_processed_data(df_final, "processed_data/combined_data.csv")

###DUDA!! Se puede llamar a el procesamiento de la notebook en este mismo archivo??

