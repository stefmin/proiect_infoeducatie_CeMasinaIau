import tkinter as tk
import ttkbootstrap as tb
import services.autovit.principal as p
import pandas as pd
from services.autovit.analysis.grafice import start_grafice

def ascunde_butoane():
    update_toggle.forget()
    buton_lanseaza_statistici.forget()

def afiseaza_butoane():
    update_toggle.pack(pady=100)
    buton_lanseaza_statistici.pack(pady=100)

def clicker():
    # statistica = statistica_marca_auto()
    if on_off.get()==0:
        up_page_label.config(text="Asteptati cat timp se incarca datele si graficele")
        #label_asteptare.pack(pady=100)
        marca_selectata = combo_alege_masini.get()
        url_masina_ceruta = f"https://www.autovit.ro/autoturisme/{marca_selectata}"
        p.incarcare_date_masina_selectata(url_masina_ceruta, marca_selectata)
        start_grafice(marca_selectata)
    else:
        marca_selectata = combo_alege_masini.get()
        try:
            df = pd.read_excel('masini.xlsx', f'{marca_selectata}')
        except:
            up_page_label.config(text="Nu exista date deja salvate despre masina")
        start_grafice(marca_selectata)



#creere fereastra
root = tb.Window(themename="cyborg")
root.title("Selectare configuratie statistici pentru masini")
root.geometry("1000x800")

#primul label
up_page_label = tb.Label(root, bootstyle="primary", text="Alege marca de masina pentru care ai vrea sa aflii informatii", 
                         font=("Arial", 18), anchor="center")
up_page_label.pack(fill="both")
#label_asteptare = tb.Label(root, text="Asteptati cat timp se incarca datele si graficele", bootstyle = "inverse-primary")

#meniu alegere masina
marci_masini = ["bentley", "opel", "ford", "audi", "bmw", "cupra", "tesla", "cadillac"]
combo_alege_masini = tb.Combobox(root, bootstyle="info", values=marci_masini, style="")
combo_alege_masini.pack(pady=100)
combo_alege_masini.current(0)

#checkbox daca facem update la informatii sau le luam pe cele deja existente din tabel
on_off = tb.IntVar()
update_toggle = tb.Checkbutton(bootstyle="warning square-toggle",
                                text="Pastreaza datele deja colectate despre masinile din aceasta marca",
                                variable=on_off,
                                onvalue=1,
                                offvalue=0)
update_toggle.pack(pady=100)

#buton pentru lansarea statisticilor
buton_lanseaza_statistici = tb.Button(root, bootstyle="danger", text="creeaza statisticie", command=clicker)
buton_lanseaza_statistici.pack(pady=100)


root.mainloop()