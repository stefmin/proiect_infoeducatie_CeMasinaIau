import pandas as pd

def export_to_excel(date_toate_masinile, marca_selectata):
    df = pd.DataFrame(date_toate_masinile)
    excel_file = pd.ExcelFile('masini.xlsx')
    sheet_names=excel_file.sheet_names
    replace=0
    with pd.ExcelWriter('masini.xlsx', engine='openpyxl', mode='a') as writer: 
        workBook = writer.book
        try:
            workBook.remove(workBook[f'{marca_selectata}'])
        except:
            print("Worksheet does not exist")
        finally:
            df.to_excel(writer, sheet_name=f'{marca_selectata}')

def import_from_excel(valoare_ceruta, marca_selectata):
    df = pd.read_excel('masini.xlsx', f'{marca_selectata}')
    lista_valori = df[f'{valoare_ceruta}'].values.tolist()
    return lista_valori
