import customtkinter as ctk
from tkinter import StringVar, Listbox
from tkintermapview import TkinterMapView
from pyswip import Prolog
import webbrowser

prolog = Prolog()
prolog.consult("recommendation.pl")

urls_pontos_turisticos = {
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

nomes_sem_acentuacao = {
    "Brasil": "Brasil",
    "França": "Franca",
    "Japão": "Japao",
    "China": "China",
    "Rússia": "Russia",
    "Estados Unidos": "Estados Unidos",
    "Índia": "India",
    "Austrália": "Australia",
    "México": "Mexico"
}

coordenadas_paises = {
    'Brasil': (-10.3333, -53.2),
    'França': (46.6034, 1.8883),
    'Japão': (36.2048, 138.2529),
    'China': (35.8617, 104.1954),
    'Rússia': (61.5240, 105.3188),
    'Estados Unidos': (37.0902, -95.7129),
    'Índia': (20.5937, 78.9629),
    'Austrália': (-25.2744, 133.7751),
    'México': (23.6345, -102.5528)
}

coordenadas_pontos_turisticos = {
    'Cristo Redentor': (-22.9519, -43.2105),
    'Museu Oscar Niemeyer': (-25.4106, -49.2646),
    'Teatro Amazonas': (-3.1302, -60.0233),
    'Gruta do Lago Azul': (-21.4805, -56.3733),
    'Escadaria Selaron': (-22.9156, -43.1792),
    'Torre Eiffel': (48.8584, 2.2945),
    'Mont Saint-Michel': (48.6361, -1.5115),
    'Monte Fuji': (35.3606, 138.7274),
    'Palacio Imperial do Japao': (35.682839, 139.759455),
    'Osaka': (34.6937, 135.5023),
    'Mae Patria': (48.7425, 44.5378),
    'Catedral de Sao Basilio': (55.7525, 37.6231),
    'Moscovo': (55.7558, 37.6173),
    'Estatua da Liberdade': (40.6892, -74.0445),
    'Times Square': (40.7580, -73.9855),
    'Monte Rushmore': (43.8791, -103.4591),
    'Sinal de Hollywood': (34.1341, -118.3215),
    'Muralha da China': (40.4319, 116.5704),
    'Exercito de terracota': (34.3853, 109.2786),
    'Vale Jiuzhaigou': (33.2520, 104.2386),
    'Templo do Buda de Jade': (31.2317, 121.4415),
    'Zoologico de Taronga': (-33.8422, 151.2410),
    'Museu Australiano': (-33.8748, 151.2131),
    'Chichen Itza': (20.6843, -88.5678),
    'Teotihuacan': (19.6925, -98.8433),
    'Ilha das Mulheres': (21.2329, -86.7314),
    'Templo de Lotus': (28.5535, 77.2588)
}

def abrir_url(event):
    ponto_turistico_selecionado = lista_pontos_turisticos.get(lista_pontos_turisticos.curselection())
    url = urls_pontos_turisticos.get(ponto_turistico_selecionado)
    if url:
        webbrowser.open(url)

def atualizar_mapa():
    pais = variavel_pais.get()
    tipo_ponto = variavel_tipo.get()
    
    pais_sem_acentuacao = nomes_sem_acentuacao.get(pais, pais)
    
    consulta = f"recomendar_local_turistico('{pais_sem_acentuacao}', '{tipo_ponto}', PontoTuristico)"
    pontos_turisticos = list(prolog.query(consulta))
    
    latitude, longitude = coordenadas_paises.get(pais, (0, 0))
    mapa.set_position(latitude, longitude)
    mapa.delete_all_marker()
    lista_pontos_turisticos.delete(0, 'end')
    
    for ponto in pontos_turisticos:
        nome_ponto = ponto['PontoTuristico']
        coords = coordenadas_pontos_turisticos.get(nome_ponto)
        if coords:
            mapa.set_marker(*coords, text=nome_ponto)
            lista_pontos_turisticos.insert('end', nome_ponto)

def tela_cheia(janela):
    janela.attributes("-fullscreen", True)

app = ctk.CTk()
tela_cheia(app)
app.title("Recomendações de Pontos Turísticos")

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill='both', expand=True)

titulo = ctk.CTkLabel(master=frame, text="Geolocator", font=("Helvetica", 24))
titulo.pack(pady=20)

frame_combobox = ctk.CTkFrame(master=frame)
frame_combobox.pack(pady=10)

variavel_pais = StringVar(value="Selecione um País")
variavel_tipo = StringVar(value="Selecione um Tipo")

combobox_pais = ctk.CTkComboBox(master=frame_combobox, variable=variavel_pais, values=list(nomes_sem_acentuacao.keys()))
combobox_pais.pack(side='left', padx=10)

combobox_tipo = ctk.CTkComboBox(master=frame_combobox, variable=variavel_tipo, values=["Paisagem", "Historico"])
combobox_tipo.pack(side='left', padx=10)

botao_pesquisar = ctk.CTkButton(master=frame_combobox, text="Pesquisar", command=atualizar_mapa)
botao_pesquisar.pack(side='left', padx=10)

frame_conteudo = ctk.CTkFrame(master=frame)
frame_conteudo.pack(pady=20, padx=10, fill='both', expand=True)

frame_mapa = ctk.CTkFrame(master=frame_conteudo)
frame_mapa.pack(side='left', pady=20, padx=10, fill='both', expand=True)

mapa = TkinterMapView(frame_mapa, width=400, height=600, corner_radius=0)
mapa.pack(fill="both", expand=True)
mapa.set_zoom(1)

lista_pontos_turisticos = Listbox(
    master=frame_conteudo, 
    width=50, 
    height=35, 
    background="#2b2b2b", 
    foreground="white", 
    font=("Helvetica", 12), 
    bd=0,  
    highlightthickness=0  
)
lista_pontos_turisticos.pack(side='left', pady=20, padx=10, fill='both', expand=False)
lista_pontos_turisticos.bind('<<ListboxSelect>>', abrir_url)

app.mainloop()
