import pandas as pd
import os

def read_files(file_paths):
    dataframes = {}
    for key, path in file_paths.items():
        dataframes[key] = pd.read_csv(path, encoding='ISO-8859-1')
    return dataframes

def explore_files(df):
    valores_nulos = df.isna().sum()
    print("Valores atípicos", valores_nulos)
    return df

def concat_data(dfs):
    combined_df = pd.concat(dfs)
    return combined_df

def load_processed_data(df, output_path):
    
    if not os.path.exists(os.path.dirname(output_path)):
        os.makedirs(os.path.dirname(output_path))

    df.to_csv(output_path, index=False)


file_paths ={
    'africa' : r'raw\\Production_Crops_E_Africa.csv',
    'america' : r'raw\\Production_Crops_E_Americas.csv',
    'asia' : r'raw\\Production_Crops_E_Asia.csv',
    'europa' : r'raw\\Production_Crops_E_Europe.csv',
    'oceania' : r'raw\\Production_Crops_E_Oceania.csv'    
}

dataframes = read_files(file_paths)

transformed_dataframes = {name: explore_files(
    df) for name, df in dataframes.items()}

dataframes_with_keys = [
    df.assign(source_file=key) for key, df in transformed_dataframes.items()
]

df_combined = concat_data(dataframes_with_keys)
print(df_combined)

load_processed_data(df_combined, "processed_data/combined_data.csv")