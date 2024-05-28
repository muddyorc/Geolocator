import customtkinter as ctk
from tkinter import StringVar
from tkintermapview import TkinterMapView
from pyswip import Prolog


# Inicializa o Prolog
prolog = Prolog()
prolog.consult("recommendation.pl")


# Função para obter recomendações de pontos turísticos e atualizar o mapa
def update_map():
    country = country_var.get()
    spot_type = type_var.get()
    
    # Consultar o Prolog para obter pontos turísticos com base nos filtros
    query = f"recommend_tourist_spot('{country}', '{spot_type}', TouristSpot)"
    print(f"Consulta Prolog: {query}")
    tourist_spots = list(prolog.query(query))
    print(f"Resultados Prolog: {tourist_spots}")
    
    # Definir a posição inicial do mapa para o país selecionado
    if country == 'Brasil':
        latitude, longitude = -10.3333, -53.2  # Centralizando no Brasil
    elif country == 'Franca':
        latitude, longitude = 46.6034, 1.8883  # Centralizando na França
    elif country == 'Japao':
        latitude, longitude = 36.2048, 138.2529  # Centralizando no Japão
    elif country == 'China':
        latitude, longitude = 35.8617, 104.1954  # Centralizando na China
    elif country == 'Russia':
        latitude, longitude = 61.5240, 105.3188  # Centralizando na Rússia
    elif country == 'Estados Unidos':
        latitude, longitude = 37.0902, -95.7129  # Centralizando nos Estados Unidos
    elif country == 'India':
        latitude, longitude = 20.5937, 78.9629  # Centralizando na Índia
    elif country == 'Australia':
        latitude, longitude = -25.2744, 133.7751  # Centralizando na Austrália
    elif country == 'Mexico':
        latitude, longitude = 23.6345, -102.5528  # Centralizando no México
    else:
        latitude, longitude = 0, 0  # Posição padrão
    
    map_widget.set_position(latitude, longitude)
    
    # Limpar os marcadores no mapa
    map_widget.delete_all_marker()
    
    # Adicionar marcadores para cada ponto turístico recomendado
    for spot in tourist_spots:
        spot_name = spot['TouristSpot']
        print(f"Adicionando marcador: {spot_name}")
        
        # Coordenadas dos pontos turísticos conhecidos
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
        # Adicione aqui os pontos turísticos dos novos países
        elif spot_name == 'Monte Fuji':
            latitude, longitude = 35.3606, 138.7274  # Coordenadas do Monte Fuji
        elif spot_name == 'Palacio Imperial do Japao':
            latitude, longitude = 35.682839, 139.759455  # Coordenadas do Palácio Imperial do Japão
        elif spot_name == 'Osaka':
            latitude, longitude = 34.6937, 135.5023  # Coordenadas de Osaka
        elif spot_name == 'Mae Patria':
            latitude, longitude = 48.7425, 44.5378  # Coordenadas da Mãe Pátria na Rússia
        elif spot_name == 'Catedral de Sao Basilio':
            latitude, longitude = 55.7525, 37.6231  # Coordenadas da Catedral de São Basílio
        elif spot_name == 'Moscovo':
            latitude, longitude = 55.7558, 37.6173  # Coordenadas de Moscovo
        elif spot_name == 'Estatua da Liberdade':
            latitude, longitude = 40.6892, -74.0445  # Coordenadas da Estátua da Liberdade
        elif spot_name == 'Times Square':
            latitude, longitude = 40.7580, -73.9855  # Coordenadas da Times Square
        elif spot_name == 'Monte Rushmore':
            latitude, longitude = 43.8791, -103.4591  # Coordenadas do Monte Rushmore
        elif spot_name == 'Sinal de Hollywood':
            latitude, longitude = 34.1341, -118.3215  # Coordenadas do Sinal de Hollywood
        elif spot_name == 'Muralha da China':
            latitude, longitude = 40.4319, 116.5704  # Coordenadas da Muralha da China
        elif spot_name == 'Exercito de terracota':
            latitude, longitude = 34.3853, 109.2786  # Coordenadas do Exército de terracota
        elif spot_name == 'Vale Jiuzhaigou':
            latitude, longitude = 33.2520, 104.2386  # Coordenadas do Vale Jiuzhaigou
        elif spot_name == 'Templo do Buda de Jade':
            latitude, longitude = 31.2317, 121.4415  # Coordenadas do Templo do Buda de Jade
        elif spot_name == 'Zoologico de Taronga':
            latitude, longitude = -33.8422, 151.2410  # Coordenadas do Zoológico de Taronga
        elif spot_name == 'Museu Australiano':
            latitude, longitude = -33.8748, 151.2131  # Coordenadas do Museu Australiano
        elif spot_name == 'Chichen Itza':
            latitude, longitude = 20.6843, -88.5678  # Coordenadas de Chichén Itzá
        elif spot_name == 'Teotihuacan':
            latitude, longitude = 19.6925, -98.8433  # Coordenadas de Teotihuacan
        elif spot_name == 'Ilha das Mulheres':
            latitude, longitude = 21.2329, -86.7314  # Coordenadas da Ilha das Mulheres
        elif spot_name == 'Templo de Lotus':
            latitude, longitude = 28.5535, 77.2588
        else:
            # Se o resultado do Prolog estiver vazio ou não corresponder a nenhum ponto conhecido, continue para o próximo ponto turístico
            continue
        
        map_widget.set_marker(latitude, longitude, text=spot_name)

# Função para abrir a janela em tela cheia
def set_fullscreen(window):
    window.attributes("-fullscreen", True)

# Inicialização da aplicação
app = ctk.CTk()

# Configurar a janela para abrir em tela cheia
set_fullscreen(app)

# Definir o título da janela
app.title("Recomendações de Pontos Turísticos")

# Criar um frame para centralizar o conteúdo
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill='both', expand=True)

# Título centralizado na parte superior
titulo = ctk.CTkLabel(master=frame, text="Geolocator", font=("Helvetica", 24))
titulo.pack(pady=20)

# Frame para organizar as comboboxes lado a lado
frame_combobox = ctk.CTkFrame(master=frame)
frame_combobox.pack(pady=10)

# Variáveis para armazenar as opções selecionadas
country_var = StringVar(value="Selecione um país")
type_var = StringVar(value="Selecione um tipo")

# Caixas de seleção (comboboxes) com opções, lado a lado
country_combobox = ctk.CTkComboBox(master=frame_combobox, variable=country_var, values=["Brasil", "Franca", "Japao", "China", "Russia", "Estados Unidos", "India", "Australia", "Mexico"])
country_combobox.pack(side='left', padx=10)

type_combobox = ctk.CTkComboBox(master=frame_combobox, variable=type_var, values=["paisagem", "historico"])
type_combobox.pack(side='left', padx=10)

# Botão de pesquisa
search_button = ctk.CTkButton(master=frame_combobox, text="Pesquisar", command=update_map)
search_button.pack(side='left', padx=10)

# Frame para o mapa
frame_mapa = ctk.CTkFrame(master=frame)
frame_mapa.pack(pady=20, padx=10, fill='both', expand=True)

# Inicialização do mapa
map_widget = TkinterMapView(frame_mapa, width=800, height=600, corner_radius=0)
map_widget.pack(fill="both", expand=True)
map_widget.set_zoom(1)

# Iniciar o loop principal da aplicação
app.mainloop()
