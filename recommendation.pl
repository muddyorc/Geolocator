turista_local('Brasil', 'Cristo Redentor', 'Paisagem').
turista_local('Brasil', 'Museu Oscar Niemeyer', 'Historico').
turista_local('Brasil', 'Teatro Amazonas', 'Historico').
turista_local('Brasil', 'Gruta do Lago Azul', 'Paisagem').
turista_local('Brasil', 'Escadaria Selaron', 'Historico').
turista_local('Franca', 'Torre Eiffel', 'Historico').
turista_local('Franca', 'Mont Saint-Michel', 'Paisagem').
turista_local('Japao', 'Monte Fuji', 'Paisagem').
turista_local('Japao', 'Palacio Imperial do Japao', 'Historico').
turista_local('Japão', 'Osaka', 'Historico').
turista_local('Russia', 'Mae Patria', 'Historico').
turista_local('Russia', 'Catedral de Sao Basilio', 'Historico').
turista_local('Russia', 'Moscovo', 'Historico').
turista_local('Estados Unidos', 'Estatua da Liberdade', 'Paisagem').
turista_local('Estados Unidos', 'Times Square', 'Historico').
turista_local('Estados Unidos', 'Monte Rushmore', 'Historico').
turista_local('Estados Unidos', 'Sinal de Hollywood', 'Historico').
turista_local('China', 'Muralha da China', 'Historico').
turista_local('China', 'Exercito de terracota', 'Historico').
turista_local('China', 'Vale Jiuzhaigou', 'Paisagem').
turista_local('China', 'Templo do Buda de Jade', 'Historico').
turista_local('Australia', 'Zoologico de Taronga', 'Paisagem').
turista_local('Australia', 'Museu Australiano', 'Historico').
turista_local('Mexico', 'Chichen Itza', 'Historico').
turista_local('Mexico', 'Teotihuacan', 'Historico').
turista_local('Mexico', 'Ilha das Mulheres', 'Paisagem').
turista_local('India', 'Templo de Lotus', 'Historico').

recomendar_local_turistico(Pais, Tipo, LocalTuristico) :-
    turista_local(Pais, LocalTuristico, Tipo).
