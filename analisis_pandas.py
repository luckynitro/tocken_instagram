import pandas as pd

datos = {'publicacion': ['Publicacion 1', 'Publicacion 2', 'Publicacion 3'],
         'likes': [100, 150, 120],
         'comentarios': [10, 25, 15]}

df = pd.DataFrame(datos)

if __name__ == "__main__":
    print(df)
