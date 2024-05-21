from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright
from services.autovit.extract_css_data import extract_text

def date_linkuri_masini(links_masini_autovit):
    date_toate_masinile=[]
    for link in links_masini_autovit:
        date_o_masina={}
        with sync_playwright() as pw:
            browser=pw.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(link, wait_until="networkidle")
            raw_page=page.content()
            parsed_page=HTMLParser(raw_page)
            data=parsed_page.css("div.ooa-162vy3d.e18eslyg3")
            if data!=None:
                date_o_masina['pret']=extract_text(parsed_page.css_first("div.ooa-1xhj18k.eqdspoq2"), "h3")
                date_o_masina['moneda']=extract_text(parsed_page.css_first("div.ooa-1xhj18k.eqdspoq2"), "p")
                for item in data:
                    #identificare taguri proprietati vehicul
                    #print(item.html)
                    tip_camp_item=extract_text(item, "p.e18eslyg4")
                    match tip_camp_item:
                        case "Oferit de":
                            date_o_masina['tip_vanzator']=extract_text(item, "p.e16lfxpc0")
                        case "Model":
                            date_o_masina['model']=extract_text(item, "a.e16lfxpc1")
                        case "Versiune":
                            date_o_masina['versiune']=extract_text(item, "a.e16lfxpc1")
                        case "Anul producției":
                            date_o_masina['an_productie']=extract_text(item, "p.e16lfxpc0")
                        case "Km":
                            date_o_masina['kilometraj']=extract_text(item, "p.e16lfxpc0")
                        case "Combustibil":
                            date_o_masina['combustibil']=extract_text(item, "a.e16lfxpc1")
                        case "Putere":
                            date_o_masina['putere']=extract_text(item, "p.e16lfxpc0")
                        case "Capacitate cilindrica":
                            date_o_masina['capacitate_cilindrica']=extract_text(item, "p.e16lfxpc0")
                        case "Cutie de viteze":
                            date_o_masina['cutie_viteze']=extract_text(item, "a.e16lfxpc1")
                        case "Consum Urban":
                            date_o_masina['consum_urban']=extract_text(item, "p.e16lfxpc0")
                        case "Culoare":
                            date_o_masina['culoare']=extract_text(item, "a.e16lfxpc1")
                        case "Numar locuri":
                            date_o_masina['numar_locuri']=extract_text(item, "p.e16lfxpc0")
                if(date_o_masina["pret"]!=None):
                    date_toate_masinile.append(date_o_masina)
    return date_toate_masinile

            




