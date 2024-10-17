from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright
from services.autovit.extract_css_data import extract_text

def date_linkuri_masini(links_masini_autovit):
    # CONST_NR_AUTO_EXTRASE=4
    date_toate_masinile=[]
    i=0
    for link in links_masini_autovit:
        date_o_masina={}
        # print(link)
        i=i+1
        # if i>CONST_NR_AUTO_EXTRASE:
        #     break
        with sync_playwright() as pw:
            browser=pw.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(link, wait_until="networkidle")
            raw_page=page.content()
            parsed_page=HTMLParser(raw_page)
            sectiuni_auto=parsed_page.css("div.ooa-10m47vf.eizxi835")
            a = page.locator('"Accept"')
            b = page.locator('"Specificații tehnice"')
            c = page.locator('"Stare și istoric"')
            if (b.count() == 0 or c.count() == 0):
                    continue
            else:
                date_o_masina['pret']=extract_text(parsed_page.css_first("div.ooa-18a76w7.evnmei42"), "h3")
                date_o_masina['moneda']=extract_text(parsed_page.css_first("div.ooa-18a76w7.evnmei42"), "p")
                # Dealer sau persoana fizica
                date_o_masina['tip_vanzator']=extract_text(parsed_page.css_first("div.ooa-yd8sa2.ern8z620"), "p.ooa-1v45bqa.er34gjf0")
                a.click()
                b.click()
                sectiuni_auto=reincarca_date_pagina_auto(page)
                date_o_masina=get_date_vehicul(sectiuni_auto,date_o_masina)
                c.click()
                sectiuni_auto=reincarca_date_pagina_auto(page)
                date_o_masina=get_date_vehicul(sectiuni_auto,date_o_masina)
                if(date_o_masina["pret"]!=None):
                    date_toate_masinile.append(date_o_masina)
    return date_toate_masinile


def reincarca_date_pagina_auto(page):
    raw_page=page.content()
    parsed_page=HTMLParser(raw_page)
    sectiuni_auto=parsed_page.css("div.ooa-arbkbm.eizxi834")    
    return sectiuni_auto

def get_date_vehicul(sectiuni_auto,date_o_masina):
    # Id-ul ce identifica inregistrarile cu datele masinii
    id_extract="p.eizxi838"
    for item in sectiuni_auto:
    #identificare proprietati vehicul
        tip_camp_item=extract_text(item, "p.eizxi837")
        match tip_camp_item:
            case "Model":
                date_o_masina['model']=extract_text(item, id_extract)
            case "Versiune":
                date_o_masina['versiune']=extract_text(item, id_extract)
            case "Anul producției":
                date_o_masina['an_productie']=extract_text(item, id_extract)
            case "Km":
                date_o_masina['kilometraj']=extract_text(item, id_extract)
            case "Combustibil":
                date_o_masina['combustibil']=extract_text(item, id_extract)
            case "Putere":
                date_o_masina['putere']=extract_text(item, id_extract)
            case "Capacitate cilindrica":
                date_o_masina['capacitate_cilindrica']=extract_text(item, id_extract)
            case "Cutie de viteze":
                date_o_masina['cutie_viteze']=extract_text(item, id_extract)
            case "Consum Urban":
                date_o_masina['consum_urban']=extract_text(item, id_extract)
            case "Culoare":
                date_o_masina['culoare']=extract_text(item, id_extract)
            case "Numar locuri":
                date_o_masina['numar_locuri']=extract_text(item, id_extract)
    return date_o_masina

