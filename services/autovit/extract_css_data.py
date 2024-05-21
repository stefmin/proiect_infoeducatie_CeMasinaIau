from selectolax.parser import HTMLParser

def extract_text(html,sel):
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None