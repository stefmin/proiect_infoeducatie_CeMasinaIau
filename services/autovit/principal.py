import services.autovit.raw_data as autovit_raw_data
import services.autovit.lista_auto as lista_containere_autovit
from services.autovit.data_from_containers import date_linkuri_masini
import services.autovit.analysis.import_export as impexp
from services.autovit.analysis.grafice import start_grafice

def main():
    date_toate_masinile = date_linkuri_masini("https://www.autovit.ro/autoturisme/anunt/cadillac-xt6-ID7HiDX2.html")
    return 0

def mainy():
   val="pret"
   impexp.import_from_excel(val,'bentley')
   return 0

def incarcare_date_masina_selectata(base_url_autovit, marca_selectata):
    #base_url_autovit = "https://www.autovit.ro/autoturisme/bentley"
    links_masini_autovit = parcurgere_pagini_site(base_url_autovit)
    #links_masini_autovit=[]
    #links_masini_autovit.append("https://www.autovit.ro/autoturisme/anunt/cadillac-xt6-ID7HiDX2.html")
    date_toate_masinile = date_linkuri_masini(links_masini_autovit)
    impexp.export_to_excel(date_toate_masinile, marca_selectata)
    #start_grafice(marca_selectata)


def mainx():
    base_url_autovit = "https://www.autovit.ro/autoturisme/bentley"
    links_masini_autovit = parcurgere_pagini_site(base_url_autovit)
    #print(links_masini_autovit)
    date_toate_masinile = date_linkuri_masini(links_masini_autovit)
    #print(date_toate_masinile)
    impexp.export_to_excel(date_toate_masinile,'bentley')
    #pagina=["https://www.autovit.ro/autoturisme/anunt/opel-meriva-1-4-ecoflex-start-stop-active-ID7HiES5.html"]
    #date_toate_masinile = date_linkuri_masini(pagina)
    #parcurgere_o_pagina(base_url_autovit)
    return 0


def parcurgere_o_pagina(url):
    pagina_parsata = autovit_raw_data.extract(url, 3)
    print(lista_containere_autovit.parse_pagina_auto(pagina_parsata))


def parcurgere_pagini_site(base_url):
    nr_pagina = 1
    links_from_all_pages = []

    while True:
        result_page = autovit_raw_data.extract(base_url, nr_pagina)
        if result_page == None:
            break
        else:
            # vector cu link de la masinie din pagina
            # links_from_all_pages = extend.#functie
            links_from_all_pages.extend(lista_containere_autovit.parse_pagina_auto(result_page))
        # adaug pagina la setul de pagini
        nr_pagina += 1
    
    return links_from_all_pages

if __name__ == "__main__":
   main()
