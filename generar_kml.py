import xml.etree.ElementTree as ET
from xml.dom import minidom

MERCADILLOS = [
    {
        "nombre": "Mercadillo de Ruzafa",
        "dia": "Lunes",
        "horario": "09:00 - 14:00",
        "lat": 39.462150,
        "lon": -0.373100,
        "calles": "C/ Barón de Cortes, C/ Padre Perera, C/ Dr. Serrano, C/ Carlos Cervera, C/ Clero",
        "coords_perimetro": [
            (-0.37380, 39.46250), (-0.37250, 39.46280),
            (-0.37190, 39.46200), (-0.37310, 39.46170), (-0.37380, 39.46250)
        ]
    },
    {
        "nombre": "Mercadillo de Algirós",
        "dia": "Lunes",
        "horario": "09:00 - 14:00",
        "lat": 39.472800,
        "lon": -0.351900,
        "calles": "C/ Actor Llorens, C/ Rugat, C/ La Pobla de Farnals, Plaza San Felipe Neri",
        "coords_perimetro": [
            (-0.35260, 39.47320), (-0.35120, 39.47350),
            (-0.35080, 39.47240), (-0.35220, 39.47210), (-0.35260, 39.47320)
        ]
    },
    {
        "nombre": "Mercadillo de Jerusalén / Convento",
        "dia": "Martes",
        "horario": "09:00 - 14:00",
        "lat": 39.464900,
        "lon": -0.379200,
        "calles": "C/ Convento Jerusalén, C/ Julio Antonio, C/ Ermita, C/ Estrella",
        "coords_perimetro": [
            (-0.37980, 39.46530), (-0.37860, 39.46550),
            (-0.37820, 39.46450), (-0.37950, 39.46430), (-0.37980, 39.46530)
        ]
    },
    {
        "nombre": "Mercadillo de Nazaret",
        "dia": "Martes",
        "horario": "09:00 - 14:00",
        "lat": 39.450800,
        "lon": -0.334600,
        "calles": "C/ Alta del Mar",
        "coords_perimetro": [
            (-0.33520, 39.45120), (-0.33400, 39.45130),
            (-0.33400, 39.45040), (-0.33520, 39.45030), (-0.33520, 39.45120)
        ]
    },
    {
        "nombre": "Mercadillo de Avenida del Cid",
        "dia": "Miércoles",
        "horario": "09:00 - 14:00",
        "lat": 39.468400,
        "lon": -0.399500,
        "calles": "C/ José Maestre, C/ Dels Jurats, C/ Miguel Paredes, Plaza del Mercado",
        "coords_perimetro": [
            (-0.40030, 39.46890), (-0.39880, 39.46910),
            (-0.39850, 39.46790), (-0.40000, 39.46770), (-0.40030, 39.46890)
        ]
    },
    {
        "nombre": "Mercadillo del Cabañal",
        "dia": "Jueves",
        "horario": "09:00 - 14:00",
        "lat": 39.469500,
        "lon": -0.330400,
        "calles": "C/ Escalante, Av. Mediterráneo, Plaza Cruz del Cañamelar, C/ Justo Vilar",
        "coords_perimetro": [
            (-0.33120, 39.47010), (-0.32960, 39.47030),
            (-0.32920, 39.46890), (-0.33080, 39.46870), (-0.33120, 39.47010)
        ]
    },
    {
        "nombre": "Mercadillo de Torrefiel",
        "dia": "Jueves",
        "horario": "09:00 - 14:00",
        "lat": 39.492800,
        "lon": -0.373900,
        "calles": "C/ Alemany, C/ Monte Carmelo, C/ Santo Domingo Savio, C/ Jacomart",
        "coords_perimetro": [
            (-0.37460, 39.49340), (-0.37320, 39.49360),
            (-0.37280, 39.49220), (-0.37420, 39.49200), (-0.37460, 39.49340)
        ]
    },
    {
        "nombre": "Mercadillo de Benimaclet",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.485800,
        "lon": -0.358900,
        "calles": "C/ Sant Esperit, C/ Juan Giner, C/ Utiel, C/ Murta, Plaza de Benimaclet",
        "coords_perimetro": [
            (-0.35960, 39.48640), (-0.35820, 39.48660),
            (-0.35780, 39.48520), (-0.35920, 39.48500), (-0.35960, 39.48640)
        ]
    },
    {
        "nombre": "Mercadillo de La Malvarrosa",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.480200,
        "lon": -0.326800,
        "calles": "C/ Berenguer de Montoliu, C/ Lanzarote",
        "coords_perimetro": [
            (-0.32750, 39.48080), (-0.32610, 39.48100),
            (-0.32580, 39.47960), (-0.32720, 39.47940), (-0.32750, 39.48080)
        ]
    },
    {
        "nombre": "Mercadillo de Monteolivete",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.458300,
        "lon": -0.362800,
        "calles": "C/ Pedro Aleixandre, C/ Alcalde Reig, C/ Escultor José Capuz",
        "coords_perimetro": [
            (-0.36350, 39.45890), (-0.36210, 39.45910),
            (-0.36170, 39.45770), (-0.36310, 39.45750), (-0.36350, 39.45890)
        ]
    },
    {
        "nombre": "Mercadillo de Benicalap",
        "dia": "Sábado",
        "horario": "09:00 - 14:00",
        "lat": 39.494200,
        "lon": -0.388900,
        "calles": "C/ Miguel Servet, C/ Sierra Martés, C/ Mirasol, C/ Lauri Volpi",
        "coords_perimetro": [
            (-0.38970, 39.49480), (-0.38810, 39.49500),
            (-0.38780, 39.49360), (-0.38940, 39.49340), (-0.38970, 39.49480)
        ]
    },
    {
        "nombre": "Mercadillo de Jesús-Patraix",
        "dia": "Sábado",
        "horario": "09:00 - 14:00",
        "lat": 39.457400,
        "lon": -0.387100,
        "calles": "C/ Beato Nicolás Factor, Plaza Jesús, C/ Conca, C/ Pío XI",
        "coords_perimetro": [
            (-0.38790, 39.45800), (-0.38650, 39.45820),
            (-0.38610, 39.45680), (-0.38750, 39.45660), (-0.38790, 39.45800)
        ]
    },
    {
        "nombre": "Rastro de Valencia",
        "dia": "Domingo",
        "horario": "08:00 - 14:00",
        "lat": 39.472200,
        "lon": -0.338900,
        "calles": "Zona Beteró / Av. Tarongers - Serrería",
        "coords_perimetro": [
            (-0.33980, 39.47300), (-0.33800, 39.47320),
            (-0.33760, 39.47140), (-0.33940, 39.47120), (-0.33980, 39.47300)
        ]
    }
]

def generar_kml():
    kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, 'Document')
    ET.SubElement(document, 'name').text = "Mercadillos Valencia - Zonas y Perímetros"

    # Definir estilos para los polígonos (áreas delimitadas de color rojo semitransparente)
    style_poly = ET.SubElement(document, 'Style', id="estiloPerimetro")
    poly_style = ET.SubElement(style_poly, 'PolyStyle')
    ET.SubElement(poly_style, 'color').text = "550000FF"  # Rojo translúcido (formato AABBGGRR)
    line_style = ET.SubElement(style_poly, 'LineStyle')
    ET.SubElement(line_style, 'color').text = "FF0000FF"  # Rojo opaco para el borde
    ET.SubElement(line_style, 'width').text = "3"

    for m in MERCADILLOS:
        # 1. Capa de Polígono (Perímetro delimitador en el mapa)
        pm_poly = ET.SubElement(document, 'Placemark')
        ET.SubElement(pm_poly, 'name').text = f"Perímetro {m['nombre']}"
        ET.SubElement(pm_poly, 'styleUrl').text = "#estiloPerimetro"
        
        polygon = ET.SubElement(pm_poly, 'Polygon')
        outer = ET.SubElement(polygon, 'outerBoundaryIs')
        linear_ring = ET.SubElement(outer, 'LinearRing')
        coords_str = " ".join([f"{lon},{lat},0" for lon, lat in m['coords_perimetro']])
        ET.SubElement(linear_ring, 'coordinates').text = coords_str

        # 2. Capa de Chincheta (Con toda la información detallada)
        pm_point = ET.SubElement(document, 'Placemark')
        ET.SubElement(pm_point, 'name').text = f"🛒 {m['nombre']} ({m['dia']})"
        
        desc = (
            f"<![CDATA["
            f"<div style='font-family: Arial, sans-serif; font-size: 13px;'>"
            f"<b>⚠️ PREVENCIÓN GRÚA / APARCAMIENTO</b><br/>"
            f"<b>Día:</b> Todos los {m['dia']}s de 06:00 a 15:00 h<br/>"
            f"<b>Horario de venta:</b> {m['horario']}<br/><br/>"
            f"<b>📍 Calles con restricción de estacionamiento:</b><br/>"
            f"<span style='color: #c0392b; background-color: #f9ebe8; padding: 3px; display: block; margin-top: 4px;'>{m['calles']}</span>"
            f"</div>"
            f"]]>"
        )
        ET.SubElement(pm_point, 'description').text = desc
        
        point = ET.SubElement(pm_point, 'Point')
        ET.SubElement(point, 'coordinates').text = f"{m['lon']},{m['lat']},0"

    xml_str = minidom.parseString(ET.tostring(kml, encoding='utf-8')).toprettyxml(indent="  ")
    with open("mercadillos_valencia.kml", "w", encoding="utf-8") as f:
        f.write(xml_str)

if __name__ == "__main__":
    generar_kml()
