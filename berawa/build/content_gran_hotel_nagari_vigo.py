# Contenido de la demo Gran Hotel Nagari (Vigo) (es/en/fr/de). Hechos de granhotelnagari.com leidos el 02/11/2026 (ver berawa/sources.json). Sin valoraciones; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Loft Room y Executive Room','Gold Suite Alameda y Silver Master Suite'],'en':['Loft Room and Executive Room','Gold Suite Alameda and Silver Master Suite'],'fr':['Loft Room et Executive Room','Gold Suite Alameda et Silver Master Suite'],'de':['Loft Room und Executive Room','Gold Suite Alameda und Silver Master Suite']}
RD={
'es':['Diseño elegante, ecléctico y vanguardista, con bañera de hidromasaje; la Executive suma zona de lectura y escritorio.','La Gold Suite mira a la centenaria arboleda de la Alameda; la Silver Master Suite tiene jacuzzi, salón independiente, chimenea y vistas al mar.'],
'en':['Elegant, eclectic and avant-garde design with a whirlpool bath; the Executive adds a reading area and desk.','The Gold Suite overlooks the century-old trees of the Alameda; the Silver Master Suite has a jacuzzi, separate lounge, fireplace and sea views.'],
'fr':['Design élégant, éclectique et avant-gardiste, avec baignoire hydromassante ; l’Executive ajoute un coin lecture et un bureau.','La Gold Suite donne sur les arbres centenaires de l’Alameda ; la Silver Master Suite a un jacuzzi, un salon séparé, une cheminée et vue sur la mer.'],
'de':['Elegantes, eklektisches und avantgardistisches Design mit Whirlpool-Badewanne; das Executive bietet zusätzlich Leseecke und Schreibtisch.','Die Gold Suite blickt auf die hundertjährigen Bäume der Alameda; die Silver Master Suite hat Jacuzzi, separaten Salon, Kamin und Meerblick.']}
ART={
'hero':('waves',3601,['#0f1c26','#c9a46a','#efd9ae','#3c5a6e','#2a4252','#15242e']),
'intro':('columns',3602,['#f1eee8','#f9f7f2','#7a6440','#52432a','#2a2216']),
'r1':('columns',3611,['#eeeae2','#c9a46a','#7a6440','#52432a','#2a2216']),
'r2':('waves',3612,['#0f1c26','#d2ae74','#f2dfb8','#46667a','#30485a','#1a2a36']),
'g1':('skyline',3621,['#0f1c26','#c9a46a','#efd9ae','#3c5a6e','#2a4252','#15242e']),
'g2':('waves',3622,['#ebeef0','#f4f1ea','#b89660','#6e8a9a','#4e6a7a','#304a58']),
'g3':('arches',3623,['#f0ede6','#f9f7f1','#7e6844','#54452c','#2a2216']),
'g4':('skyline',3624,['#0f1c26','#d2ae74','#f2dfb8','#46667a','#30485a','#1a2a36'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Gran Hotel Nagari · Boutique & Spa cinco estrellas en Vigo',see_rooms='Ver las habitaciones',hero_k='Vigo · Praza de Compostela, 21',hero_t='El espíritu cosmopolita en el corazón de Vigo',hero_s='Un cinco estrellas en un edificio histórico, con spa y skyline sobre la ría.',
 intro_t='Inspirador, vanguardista, sofisticado',intro_p1='El Gran Hotel Nagari Boutique & Spa se inauguró en 2010 en un edificio histórico del arquitecto Manuel Gómez Román, que conserva su imponente fachada catalogada.',
 intro_p2='Dentro, líneas clásicas y orientales se funden con el vanguardismo más moderno; 750 m² se dedican a la salud y el bienestar.',
 stats=['Cinco estrellas','72 habitaciones','750 m² de spa','Gimnasio de 7:00 a 00:00'],nav_rooms='Habitaciones',rooms_t='Las habitaciones',rooms_s='Todas con bañera de hidromasaje, Smart TV, cafetera y minibar con café y agua de cortesía, wifi de alta velocidad gratuito, aire acondicionado, albornoz y zapatillas.',
 svcs=['Nagari Health & Spa','Piscina climatizada Skyline','Restaurante Alameda XXI','Manhattan Lounge Bar','Room service','Parking en el propio edificio'],
 around_s='En la Praza de Compostela, junto a la Alameda de Vigo, con salidas en barco a las Islas Cíes.',
 loc_p='Praza de Compostela, 21 · 36201 Vigo (Pontevedra). Espacio libre de humo.',
 chips=['¿Qué habitaciones tenéis?','¿Puedo ir al spa sin alojarme?','¿A qué hora es el desayuno?','¿Cómo reservo?']),
'en':dict(title='Gran Hotel Nagari · Five-star Boutique & Spa in Vigo',see_rooms='See the rooms',hero_k='Vigo · Praza de Compostela, 21',hero_t='The cosmopolitan spirit in the heart of Vigo',hero_s='A five-star hotel in a historic building, with a spa and skyline over the estuary.',
 intro_t='Inspiring, avant-garde, sophisticated',intro_p1='Gran Hotel Nagari Boutique & Spa opened in 2010 in a historic building by architect Manuel Gómez Román, which keeps its imposing listed façade.',
 intro_p2='Inside, classic and oriental lines blend with the most modern avant-garde; 750 m² are devoted to health and wellbeing.',
 stats=['Five stars','72 rooms','750 m² spa','Gym 7:00 to 00:00'],nav_rooms='Rooms',rooms_t='The rooms',rooms_s='All with whirlpool bath, Smart TV, coffee maker and minibar with complimentary coffee and water, free high-speed wifi, air conditioning, bathrobe and slippers.',
 svcs=['Nagari Health & Spa','Heated Skyline pool','Alameda XXI restaurant','Manhattan Lounge Bar','Room service','Parking in the building'],
 around_s='On Praza de Compostela, next to Vigo’s Alameda, with boat trips to the Cíes Islands.',
 loc_p='Praza de Compostela, 21 · 36201 Vigo (Pontevedra). Smoke-free hotel.',
 chips=['Which rooms do you have?','Can I use the spa without staying?','What time is breakfast?','How do I book?']),
'fr':dict(title='Gran Hotel Nagari · Boutique & Spa cinq étoiles à Vigo',see_rooms='Voir les chambres',hero_k='Vigo · Praza de Compostela, 21',hero_t='L’esprit cosmopolite au cœur de Vigo',hero_s='Un cinq étoiles dans un bâtiment historique, avec spa et skyline sur la ria.',
 intro_t='Inspirant, avant-gardiste, sophistiqué',intro_p1='Le Gran Hotel Nagari Boutique & Spa a ouvert en 2010 dans un bâtiment historique de l’architecte Manuel Gómez Román, qui conserve son imposante façade classée.',
 intro_p2='À l’intérieur, lignes classiques et orientales se mêlent à l’avant-garde la plus moderne ; 750 m² sont consacrés à la santé et au bien-être.',
 stats=['Cinq étoiles','72 chambres','750 m² de spa','Salle de sport de 7h00 à 00h00'],nav_rooms='Chambres',rooms_t='Les chambres',rooms_s='Toutes avec baignoire hydromassante, Smart TV, cafetière et minibar avec café et eau offerts, wifi haut débit gratuit, climatisation, peignoir et chaussons.',
 svcs=['Nagari Health & Spa','Piscine chauffée Skyline','Restaurant Alameda XXI','Manhattan Lounge Bar','Service en chambre','Parking dans le bâtiment'],
 around_s='Sur la Praza de Compostela, près de l’Alameda de Vigo, avec des sorties en bateau vers les îles Cíes.',
 loc_p='Praza de Compostela, 21 · 36201 Vigo (Pontevedra). Hôtel non-fumeur.',
 chips=['Quelles chambres avez-vous ?','Puis-je aller au spa sans séjourner ?','À quelle heure est le petit-déjeuner ?','Comment réserver ?']),
'de':dict(title='Gran Hotel Nagari · Fünf-Sterne-Boutique & Spa in Vigo',see_rooms='Zimmer ansehen',hero_k='Vigo · Praza de Compostela, 21',hero_t='Kosmopolitischer Geist im Herzen von Vigo',hero_s='Ein Fünf-Sterne-Hotel in einem historischen Gebäude, mit Spa und Skyline über der Ría.',
 intro_t='Inspirierend, avantgardistisch, raffiniert',intro_p1='Das Gran Hotel Nagari Boutique & Spa öffnete 2010 in einem historischen Gebäude des Architekten Manuel Gómez Román, das seine imposante denkmalgeschützte Fassade bewahrt.',
 intro_p2='Innen verbinden sich klassische und orientalische Linien mit modernster Avantgarde; 750 m² sind Gesundheit und Wohlbefinden gewidmet.',
 stats=['Fünf Sterne','72 Zimmer','750 m² Spa','Fitnessraum 7:00 bis 00:00'],nav_rooms='Zimmer',rooms_t='Die Zimmer',rooms_s='Alle mit Whirlpool-Badewanne, Smart-TV, Kaffeemaschine und Minibar mit Kaffee und Wasser gratis, kostenlosem Highspeed-WLAN, Klimaanlage, Bademantel und Hausschuhen.',
 svcs=['Nagari Health & Spa','Beheizter Skyline-Pool','Restaurant Alameda XXI','Manhattan Lounge Bar','Zimmerservice','Parkplatz im Gebäude'],
 around_s='An der Praza de Compostela, neben der Alameda von Vigo, mit Bootsfahrten zu den Cíes-Inseln.',
 loc_p='Praza de Compostela, 21 · 36201 Vigo (Pontevedra). Rauchfreies Hotel.',
 chips=['Welche Zimmer gibt es?','Kann ich das Spa ohne Übernachtung nutzen?','Wann gibt es Frühstück?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RE='https://granhotelnagari.com/reservas/';RN='https://granhotelnagari.com/en/reservas-en/'
BOOK=dict(mode='engine',url=dict(es=RE,en=RN,fr=RN,de=RN))
D=dict(name='Gran Hotel Nagari',ac='#14222c',ac2='#7a6440',ac2_a11y='#5e4c30',book=BOOK,around=['Alameda de Vigo','Islas Cíes'],foot=FOOT,
 address='Praza de Compostela, 21 · 36201 Vigo (Pontevedra)',phones=['+34 986 21 11 11'],emails=['info@granhotelnagari.com'],maps='Gran Hotel Nagari, Praza de Compostela 21, 36201 Vigo',t=T)
META=dict(repo='demo-gran-hotel-nagari-vigo',name='Gran Hotel Nagari',legal_name='ONIX VIGO S.L. (aviso legal de su web)',registry_ids=['B36575272'],
 url='https://granhotelnagari.com/',domain='granhotelnagari.com',municipality='Vigo',province='Pontevedra',sector='hotel boutique y spa de cinco estrellas en el centro de Vigo',
 read_at='2026-11-02T07:00:00+01:00',created_at='2026-11-02T06:59:00+01:00',built_at='2026-11-02T07:15:00+01:00',audit_date='2026-11-02T06:48:27+01:00',
 rating=dict(value=4.5,coincide=['web','dir'],date='2026-10-29',url='https://www.google.com/maps/place/Gran+Hotel+Nagari/@42.2396951,-8.7214113,17z/data=!4m9!3m8!1s0xd2f6241eea267b1:0x16aa2a784e662c95!5m2!4m1!1i2!8m2!3d42.2396951!4d-8.7214113!16s%2Fg%2F1vfwf46m'),
 book=dict(mode='engine',url=RE,note='pagina de reservas real de su web con el motor Mirai (granhotelnagari.com/reservas/ y /en/reservas-en/), HTTP 200 comprobado el 02/11/2026; su web no tiene version alemana ni francesa de la pagina de reservas, fr y de usan la inglesa.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Cuántas habitaciones tiene?','K01'),('¿Tenéis suites?','K02'),('¿Puedo ir al spa sin alojarme?','K03'),('¿Hay piscina?','K04'),('¿A qué hora es el desayuno?','K05'),('¿Hay gimnasio?','K06'),('¿Hay parking?','K07'),('¿Pueden alojarse menores?','K08'),('¿Se puede fumar?','K09'),('¿Dónde está el hotel?','K10'),('¿Cómo reservo?','K11'),('¿Podéis confirmarme disponibilidad para mañana?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis campo de golf?',None)],
'en':[('Which rooms do you have?','K01'),('How many rooms does it have?','K01'),('Do you have suites?','K02'),('Can I use the spa without staying?','K03'),('Is there a pool?','K04'),('What time is breakfast?','K05'),('Is there a gym?','K06'),('Is there parking?','K07'),('Can minors stay?','K08'),('Can I smoke?','K09'),('Where is the hotel?','K10'),('How do I book?','K11'),('Can you confirm availability for tomorrow?','K11'),('How much is a night?',None),('Do you have a golf course?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Combien de chambres a-t-il ?','K01'),('Avez-vous des suites ?','K02'),('Puis-je aller au spa sans séjourner ?','K03'),('Y a-t-il une piscine ?','K04'),('À quelle heure est le petit-déjeuner ?','K05'),('Y a-t-il une salle de sport ?','K06'),('Y a-t-il un parking ?','K07'),('Les mineurs peuvent-ils séjourner ?','K08'),('Peut-on fumer ?','K09'),('Où se trouve l’hôtel ?','K10'),('Comment réserver ?','K11'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous un terrain de golf ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wie viele Zimmer hat das Hotel?','K01'),('Haben Sie Suiten?','K02'),('Kann ich das Spa ohne Übernachtung nutzen?','K03'),('Gibt es einen Pool?','K04'),('Wann gibt es Frühstück?','K05'),('Gibt es einen Fitnessraum?','K06'),('Gibt es Parkplätze?','K07'),('Dürfen Minderjährige übernachten?','K08'),('Darf man rauchen?','K09'),('Wo liegt das Hotel?','K10'),('Wie kann ich buchen?','K11'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K11'),('Was kostet eine Nacht?',None),('Haben Sie einen Golfplatz?',None)]}
