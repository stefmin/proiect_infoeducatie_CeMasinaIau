import services.autovit.raw_data as autovit_raw_data
import services.autovit.lista_auto as lista_containere_autovit

def parcurgere_pagini_site(base_url):
    nr_pagina = 1
    links_from_all_pages = []

    while True:
        result_page = autovit_raw_data.extract(base_url, nr_pagina)
        if result_page == None:
            break
        else:
            # vector cu link de la masinie din pagina
            links_from_all_pages.extend(lista_containere_autovit.parse_pagina_auto(result_page))
        # adaug pagina la setul de pagini
        nr_pagina += 1
    
    return links_from_all_pages