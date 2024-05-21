from selectolax.parser import HTMLParser


def parse_pagina_auto(page_content):
    results = []
    htmlpage = HTMLParser(page_content)
    container_masina = htmlpage.css("article.ooa-yca59n")
    for item in container_masina:
        try:
            link_masina = item.css_first("h1.e1i3khom9").css_first("a").attributes["href"]
        except AttributeError:
            link_masina = None

        if link_masina != None:
            results.append(link_masina)
        
    return results
