1. Pobierz listę plików z katalogu `materials/karty-postaci/botcmenagerie/assets`.
2. Dla każdego pliku z tej listy użyj nazwy bez rozszerzenia jako klucza do wyszukania obiektu w plikach JSON w katalogu `materials/karty-postaci/botcmenagerie` i jego podkatalogach.
3. Dopasowanie powinno działać tak: usuń wszystkie znaki podkreślenia z nazwy pliku i porównaj wynik z wartością pola `id` w obiekcie, ignorując wielkość liter.
4. Jeśli znajdziesz obiekt o dopasowanym `id`, podmień jego pole `image` na tablicę zawierającą jeden string z URL. URL musi mieć postać:
   `https://raw.githubusercontent.com/czaurus/BOTC-materials---Krew-na-wiezy-zegarowej/refs/heads/master/materials/karty-postaci/botcmenagerie/assets/{oryginalna_nazwa_pliku}.{rozszerzenie_pliku}`
5. Użyj w URL dokładnej oryginalnej nazwy pliku i jego rozszerzenia, bez modyfikowania tych wartości.
6. Nie zmieniaj innych pól JSON ani obiektów, które nie mają dopasowanego `id`.
7. Wypisz (poinformuj Operatora) ile plików i jakie nie znalazły żadnego dopasowania