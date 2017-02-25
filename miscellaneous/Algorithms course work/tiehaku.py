# -*- coding: utf-8 -*-
from sys import argv
from time import time
"""variation of dijkstras shortest path algorithm that searches route between cities that caries heaviest loads
comments in finnish for the finnish teacher"""
# lukee kartta tiedoston 
def read_roads(name):
	
	# phase määrää lukeeko ohjelma ensinmäisä riviä vai tie rivejä. roads kertoo monta tietä on lukematta ja kun tiet loppuvat, ohjelma tietää olevansä viimeisellä rivillä josta saadaan määränpää
	phase = 0
	tiedosto = open(name)
	tulos = tiedosto.readlines()
	for line in tulos:
		line = line.rstrip()
		if phase == 0:#						ottaa talteen tie lukumäärän ja kaupunkien lukumäärän
			cities, roads = line.split(" ")
			phase += 1
			cities = int(cities)
			roads = int(roads)
			lroads = []
			for i in range(roads):
				lroads.append([])
		elif phase == 1 and roads > 0:
			temp = line.split(" ")
			temp = [int(i) for i in temp]
			lroads[roads-1] = temp# 			luo listan mistä löytyy jokainen tie alku- ja loppupisteineen sekä tien paino
			roads -= 1
		else:
			finish = int(line)
			

	lcities = []
	cities = range(cities)
	for i in cities:
		lcities.append(i+1)
	return lcities, lroads, finish#		funktio palauttaa tie- ja kaupunki-listat sekä määränpään

#luo kaupunki-objectin johon sisällytetään kaikki kyseiseen kaupunkiin liittyvät tiedot
class city:
	def __init__(self, name):#		alustaa kaupungin
		self.name = name
		self.nexto = {}#			Kaupungin naapurit
		self.weight = 0#			painoraja jonka kaupunkiin voi tuoda. 0 tarkoittaa että kaupungille ei ole vielä reittiä eli ei tiedetä painorajaa
		self.next = 0#			kertoo mihin naapuriin täytyy mennä seuraavana. Määritellään myöhemmin
		self.path = 0#			kertoo mistä kaupungista tähän kaupunkiin on tultu
		self.used = False#		kertoo onko kaupungissa käyty

	#seuraavat funktiot palauttavat tietoja kaupungista tai määrittelevät niitä
	def set_weight(self, weight):
		self.weight = weight
	def get_name(self):
		return self.name
	def get_weight(self):
		return self.weight
	def set_nexto(self, next, limit):
		self.nexto[next] = limit
	def set_used(self):
		self.used = True
		
#Kartta-objekti johon tallennetaan kaikki kaupungit kirjastoon
class map:
	def __init__(self):
		self.city_dir = {}
	def __iter__(self):
		return iter(self.city_dir.values())
	def add_city(self, name):
		town = city(name)
		self.city_dir[name] = town
	def add_road(self, start, end, weight):
		self.city_dir[start].set_nexto(self.city_dir[end], weight)
		self.city_dir[end].set_nexto(self.city_dir[start], weight)
		
	def get_city(self, name):
		return self.city_dir[name]
		
#dijkstran algoritmi jota on muunettu niin että se etsii reitin jonka kantovara on suurin lyhimmän reitin sijaan
def	path_find(start, end, map):
	not_visited = [(place.get_weight(), place)for place in map]#		luo listan jossa on jokainen tutkimaton kaupunki painoineen
	Pass = 0#							jos = 0, reitti määränpäähän löytyy, jos 1 niin ei löydy
	while True:
		largest = 0
		examine = None
		for i in not_visited:#			Etsii kaupungin jota tutkitaan seuraavaksi sillä perusteella että mihin kaupunkiin voi viedä suurimman kuorman
			if i[0] > largest:
				largest = i[0]
				examine = i[1]
		if examine == None:#				mikäli ei ole tutkimatonta kaupunkia jonka paino olisi suurempi kuin 0, niin se tarkoittaa että kaikki kaupungit on tutkittu, joihin on reitti aloituskaupungista ja reittiä määränpäähän ei ole
			Pass = 1
			break
			
		examine.set_used()#  			merkkaa tutkittavan kaupungin vierailluksi
		for next in examine.nexto:#		antaa kaupungin naapureille painoarvot teiden mukaan mikäli naapurissa ei ole käyty jo
			if next.used == True:
				pass
			else:
				if examine.nexto[next] < examine.weight and examine.weight != float("inf") or examine.weight == float("inf"):#		jos tien paino on pienempi kun kaupungin paino, naapuri saa painokseen tien painon
					examine.next = examine.nexto[next]
				else:#															jos tien painoraja on kaupungin painoa suurempi, naapuri saa painokseen tutkittavan kaupungin painon
					examine.next = examine.weight		
				if next.weight < examine.next:#									Mikäli naapurilla on jo paino ja se on pienempi kuin tutkittavan kaupungin sille tarjoama paino, naapurin painoksi tulee tutkittavan kaupungin paino
					next.set_weight(examine.next)
					next.path = examine
				else:#															Mikäli naapurin paino on tarjolla olevaa suurempi, on naapuriin olemassa jo reitti joka on tutkittavaa reittiä parempi joten ei tehdä mitään	
					pass
		not_visited = []
		for town in map:
			if town.used == False:
				not_visited.append((town.weight, town))#			luo listan jossa on jokainen kaupunki jota algoritmi ei ole vielä käsitellyt sekä kaupungin paino
			else:
				pass
		if map.get_city(end).used == True:#						lopettaa reittihaun mikäli määränpää kaupunki on tutkittu
			break
		else:
			pass
	return Pass#			funktio palauttaa tiedon siitä löytyikö reitti

#funktio joka antaa reitin, mikäli sellainen on syötteenä annettuun kaupunkiin	
def path (route, city):
	past = city.path
	if past == 0:
		pass
	else:
		name = past.get_name()
		route.append(name)
		path(route, past)
	
if __name__ == "__main__":
	alku = time()
	komento = argv[1]#								lukee karttatiedoston nimen
	nodes, edges, goal = read_roads(komento)#		lukee karttatiedoston
	map = map()#									alustaa kartan
	for node in nodes:#								Alustaa kaikki kaupungit karttaan
		map.add_city(node)
	for road in edges:#								Antaa jokaiselle kaupungille tiedot sen naapureista sekä teiden painot
		map.add_road(road[0], road[1], road[2])
	first = map.get_city(1)
	first.set_weight(float("inf"))#					määrittää aloituskaupungin painon äärettömäksi jotta algoritmi löytäisi aloituskaupungin
	Pass = path_find(1, goal, map)#					tekee reittihaun
	weight = map.get_city(goal)
	weight = weight.get_weight()
	weight = weight-8#								laskee kuinka suuren painon voi viedä määränpäähän
	if Pass == 0 and weight > 0:#					mikäli reitti on olemassa ja painoraja on nollaa suurempi, printtaa painon jonka reittiä pitkin voi kuljettaa
		print(weight)
	elif weight < 0 or Pass == 1:#					mikäli painoraja on nollaa pienempi, ei ole reittiä mitä rekka voi kulkea joten printataan  ettei reittiä ole
		print("no route")
	elif weight == 0:#								mikäli painoraja on nolla, reitti on olemassa mutta sillä ei voi kuljettaa kuormaa
		print("Maximum load = 0 / No route")
	else:#											mikäli pass on yksi, ei ole olemassa reittiä jolla voisi kuljettaa minkäänlaista kuormaa määränpäähän. Ei tehdä mitään koska tässä tilanteessa on jo printattu aiemmin ettei ole tietä
		pass
	loppu = time()
	aika = loppu - alku
	print (aika)