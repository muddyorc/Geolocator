tourist_spot('Brasil', 'Cristo Redentor', 'paisagem').
tourist_spot('Brasil', 'Museu Oscar Niemeyer', 'historico').
tourist_spot('Brasil', 'Teatro Amazonas', 'historico').
tourist_spot('Brasil', 'Gruta do Lago Azul', 'paisagem').
tourist_spot('Brasil', 'Escadaria Selaron', 'historico').
tourist_spot('Franca', 'Torre Eiffel', 'historico').
tourist_spot('Franca', 'Mont Saint-Michel', 'paisagem').
tourist_spot('Japao', 'Monte Fuji', 'paisagem').
tourist_spot('Japao', 'Palacio Imperial do Japao', 'historico').
tourist_spot('Japao', 'Osaka', 'historico').
tourist_spot('Russia', 'Mae Patria', 'historico').
tourist_spot('Russia', 'Catedral de Sao Basilio', 'historico').
tourist_spot('Russia', 'Moscovo', 'historico').
tourist_spot('Estados Unidos', 'Estatua da Liberdade', 'historico').
tourist_spot('Estados Unidos', 'Times Square', 'historico').
tourist_spot('Estados Unidos', 'Monte Rushmore', 'historico').
tourist_spot('Estados Unidos', 'Sinal de Hollywood', 'historico').
tourist_spot('China', 'Muralha da China', 'historico').
tourist_spot('China', 'Exercito de terracota', 'historico').
tourist_spot('China', 'Vale Jiuzhaigou', 'paisagem').
tourist_spot('China', 'Templo do Buda de Jade', 'historico').
tourist_spot('Australia', 'Zoologico de Taronga', 'paisagem').
tourist_spot('Australia', 'Museu Australiano', 'historico').
tourist_spot('Mexico', 'Chichen Itza', 'historico').
tourist_spot('Mexico', 'Teotihuacan', 'historico').
tourist_spot('Mexico', 'Ilha das Mulheres', 'paisagem').
tourist_spot('India', 'Templo de Lotus', 'historico').

recommend_tourist_spot(Country, Type, TouristSpot) :-
    tourist_spot(Country, TouristSpot, Type).


