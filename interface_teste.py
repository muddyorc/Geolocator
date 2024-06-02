import customtkinter as ctk
from tkinter import StringVar, Listbox
from tkintermapview import TkinterMapView
from pyswip import Prolog
import webbrowser

prolog = Prolog()
prolog.consult("recommendation.pl")

tourist_spot_urls = {
    'Cristo Redentor': 'https://www.tremdocorcovado.rio/',
    'Museu Oscar Niemeyer': 'https://www.museuoscarniemeyer.org.br/',
    'Teatro Amazonas': 'https://cultura.am.gov.br/espacos-culturais/teatros/teatro-amazonas/',
    'Gruta do Lago Azul': 'https://grutadolagoazul.com.br/',
    'Escadaria Selaron': 'https://freewalkertours.com/pt-br/escadaria-selaron/',
    'Torre Eiffel': 'https://www.toureiffel.paris/pt',
    'Mont Saint-Michel': 'https://www.booking.com/city/fr/le-mont-saint-michel.html?aid=383259;label=le-mont-saint-michel-416MNQFp0p4NZaWWTRIgHgS394345926608:pl:ta:p1:p2:ac:ap:neg:fi:tikwd-48850471:lp1001556:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YRlijhKLEMjJLyONwTyX95c;ws=',
    'Monte Fuji': 'https://www.japan.travel/pt/fuji-guide/mt-fuji-climbing-guide/',
    'Palacio Imperial do Japao': 'https://www.japan.travel/pt/spot/2121/',
    'Osaka': 'https://www.japan.travel/pt/destinations/kansai/osaka/',
    'Mae Patria': 'https://br.rbth.com/estilo-de-vida/82741-como-por-dentro-estatua-mae-patria-fotos',
    'Catedral de Sao Basilio': 'https://www.tripadvisor.com.br/Attraction_Review-g298484-d300367-Reviews-Saint_Basil_s_Cathedral-Moscow_Central_Russia.html',
    'Moscovo': 'https://www.tripadvisor.com.br/Attractions-g298484-Activities-Moscow_Central_Russia.html',
    'Estatua da Liberdade': 'https://www.civitatis.com/br/nova-york/tour-estatua-liberdade/',
    'Times Square': 'https://www.timessquarenyc.org/',
    'Monte Rushmore': 'https://www.tripadvisor.com.br/Attraction_Review-g54774-d2279516-Reviews-Mount_Rushmore_Tours-Rapid_City_South_Dakota.html',
    'Sinal de Hollywood': 'https://www.getyourguide.com/pt-br/letreiro-de-hollywood-l3912/',
    'Muralha da China': 'https://www.civitatis.com/br/pequim/excursao-grande-muralha-china/',
    'Exercito de terracota': 'https://www.viator.com/pt-BR/tours/Xian/Terracotta-Warriors-Day-Tour/d326-63239P8',
    'Vale Jiuzhaigou': 'https://www.viator.com/pt-BR/tours/Jiuzhaigou-County/Private-Day-Tour-to-Jiuzhaigou-Park/d51585-15971P1',
    'Templo do Buda de Jade': 'https://www.tudosobreshanghai.com/templo-buda-jade',
    'Zoologico de Taronga': 'https://taronga.org.au/sydney-zoo',
    'Museu Australiano': 'https://australian.museum/event/highlight-tours/',
    'Chichen Itza': 'https://www.chichenitza.com/pt',
    'Teotihuacan': 'https://www.tripadvisor.com.br/Attractions-g499421-Activities-c42-San_Juan_Teotihuacan_Central_Mexico_and_Gulf_Coast.html',
    'Ilha das Mulheres': 'https://seusingressos.com.br/p/cancun-tour-premium-ilha-mulheres/',
    'Templo de Lotus': 'https://www.getyourguide.com/pt-br/templo-de-lotus-l11956/'
}

def open_url(event):
    selected_spot = tourist_spot_listbox.get(tourist_spot_listbox.curselection())
    url = tourist_spot_urls.get(selected_spot)
    if url:
        webbrowser.open(url)

def update_map():
    country = country_var.get()
    spot_type = type_var.get()
    
    query = f"recommend_tourist_spot('{country}', '{spot_type}', TouristSpot)"
    print(f"Consulta Prolog: {query}")
    tourist_spots = list(prolog.query(query))
    print(f"Resultados Prolog: {tourist_spots}")
    
    if country == 'Brasil':
        latitude, longitude = -10.3333, -53.2  
    elif country == 'Franca':
        latitude, longitude = 46.6034, 1.8883  
    elif country == 'Japao':
        latitude, longitude = 36.2048, 138.2529 
    elif country == 'China':
        latitude, longitude = 35.8617, 104.1954  
    elif country == 'Russia':
        latitude, longitude = 61.5240, 105.3188  
    elif country == 'Estados Unidos':
        latitude, longitude = 37.0902, -95.7129  
    elif country == 'India':
        latitude, longitude = 20.5937, 78.9629  
    elif country == 'Australia':
        latitude, longitude = -25.2744, 133.7751  
    elif country == 'Mexico':
        latitude, longitude = 23.6345, -102.5528  
    else:
        latitude, longitude = 0, 0  
    
    map_widget.set_position(latitude, longitude)
    
    
    map_widget.delete_all_marker()
    
    tourist_spot_listbox.delete(0, 'end')
    
    for spot in tourist_spots:
        spot_name = spot['TouristSpot']
        print(f"Adicionando marcador: {spot_name}")
        

        if spot_name == 'Cristo Redentor':
            latitude, longitude = -22.9519, -43.2105
        elif spot_name == 'Museu Oscar Niemeyer':
            latitude, longitude = -25.4106, -49.2646
        elif spot_name == 'Teatro Amazonas':
            latitude, longitude = -3.1302, -60.0233
        elif spot_name == 'Gruta do Lago Azul':
            latitude, longitude = -21.4805, -56.3733
        elif spot_name == 'Escadaria Selaron':
            latitude, longitude = -22.9156, -43.1792
        elif spot_name == 'Torre Eiffel':
            latitude, longitude = 48.8584, 2.2945
        elif spot_name == 'Mont Saint-Michel':
            latitude, longitude = 48.6361, -1.5115
       
        elif spot_name == 'Monte Fuji':
            latitude, longitude = 35.3606, 138.7274  
        elif spot_name == 'Palacio Imperial do Japao':
            latitude, longitude = 35.682839, 139.759455 
        elif spot_name == 'Osaka':
            latitude, longitude = 34.6937, 135.5023  
        elif spot_name == 'Mae Patria':
            latitude, longitude = 48.7425, 44.5378  
        elif spot_name == 'Catedral de Sao Basilio':
            latitude, longitude = 55.7525, 37.6231  
        elif spot_name == 'Moscovo':
            latitude, longitude = 55.7558, 37.6173  
        elif spot_name == 'Estatua da Liberdade':
            latitude, longitude = 40.6892, -74.0445  
        elif spot_name == 'Times Square':
            latitude, longitude = 40.7580, -73.9855 
        elif spot_name == 'Monte Rushmore':
            latitude, longitude = 43.8791, -103.4591 
        elif spot_name == 'Sinal de Hollywood':
            latitude, longitude = 34.1341, -118.3215  
            latitude, longitude = 40.4319, 116.5704  
        elif spot_name == 'Exercito de terracota':
            latitude, longitude = 34.3853, 109.2786  
        elif spot_name == 'Vale Jiuzhaigou':
            latitude, longitude = 33.2520, 104.2386  
        elif spot_name == 'Templo do Buda de Jade':
            latitude, longitude = 31.2317, 121.4415  
        elif spot_name == 'Zoologico de Taronga':
            latitude, longitude = -33.8422, 151.2410  
        elif spot_name == 'Museu Australiano':
            latitude, longitude = -33.8748, 151.2131  
        elif spot_name == 'Chichen Itza':
            latitude, longitude = 20.6843, -88.5678 
        elif spot_name == 'Teotihuacan':
            latitude, longitude = 19.6925, -98.8433  
        elif spot_name == 'Ilha das Mulheres':
            latitude, longitude = 21.2329, -86.7314  
        elif spot_name == 'Templo de Lotus':
            latitude, longitude = 28.5535, 77.2588
        else:
            continue
        
        map_widget.set_marker(latitude, longitude, text=spot_name)
        
        tourist_spot_listbox.insert('end', spot_name)

def set_fullscreen(window):
    window.attributes("-fullscreen", True)

app = ctk.CTk()

set_fullscreen(app)

app.title("Recomendações de Pontos Turísticos")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill='both', expand=True)

titulo = ctk.CTkLabel(master=frame, text="Geolocator", font=("Helvetica", 24))
titulo.pack(pady=20)

frame_combobox = ctk.CTkFrame(master=frame)
frame_combobox.pack(pady=10)

country_var = StringVar(value="Selecione um país")
type_var = StringVar(value="Selecione um tipo")

country_combobox = ctk.CTkComboBox(master=frame_combobox, variable=country_var, values=["Brasil", "Franca", "Japao", "China", "Russia", "Estados Unidos", "India", "Australia", "Mexico"])
country_combobox.pack(side='left', padx=10)

type_combobox = ctk.CTkComboBox(master=frame_combobox, variable=type_var, values=["paisagem", "historico"])
type_combobox.pack(side='left', padx=10)

search_button = ctk.CTkButton(master=frame_combobox, text="Pesquisar", command=update_map)
search_button.pack(side='left', padx=10)

frame_content = ctk.CTkFrame(master=frame)
frame_content.pack(pady=20, padx=10, fill='both', expand=True)

frame_mapa = ctk.CTkFrame(master=frame_content)
frame_mapa.pack(side='left', pady=20, padx=10, fill='both', expand=True)

map_widget = TkinterMapView(frame_mapa, width=400, height=600, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_zoom(1)

background_color = "#2b2b2b"  

tourist_spot_listbox = Listbox(
    master=frame_content, 
    width=50, 
    height=35, 
    background=background_color, 
    foreground="white", 
    font=("Helvetica", 12), 
    bd=0,  
    highlightthickness=0  
)
tourist_spot_listbox.pack(side='left', pady=20, padx=10, fill='both', expand=False)


tourist_spot_listbox.bind('<<ListboxSelect>>', open_url)


app.mainloop()
