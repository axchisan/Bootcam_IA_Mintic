#importa la libreria de pandas
import pandas as pd # type: ignore

#define la ruta del archivo csv de los datos
#si el archivo esta en el mismo directorio que el script, no es necesario especificar la ruta completa
path =  'Online_Retail.csv'

#Lee el archivo csv usando la funcion read_csv de pandas
#se especifica la codificacion 'latin1' (también conocida como 'ISO-8859-1') para manejar caracteres 
retail_data = pd.read_csv(path, encoding='latin1')

#muestra el tipo de la variable 'retail_data' para confirmar que es un DataFrame 
#Un dataframe es una estructura de datos bidimensional, similar a una tabla, que se utiliza para almacenar datos en pandas

print(type(retail_data))
#Imprime todo el contenido del DataFrame 'retail_data' para ver los datos que fueron leidos del archivo csv

print(retail_data)