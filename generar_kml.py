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
            (-0.37430, 39.46320), (-0.37120, 39.46320),
            (-0.37120, 39.46130), (-0.37430, 39.46130), (-0.37430, 39.46320)
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
            (-0.35330, 39.47410), (-0.34980, 39.47410),
            (-0.34980, 39.47140), (-0.35330, 39.47140), (-0.35330, 39.47410)
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
            (-0.38050, 39.46600), (-0.37750, 39.46600),
            (-0.37750, 39.46380), (-0.38050, 39.46380), (-0.38050, 39.46600)
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
            (-0.33590, 39.45180), (-0.33300, 39.45180),
            (-0.33300, 39.44970), (-0.33590, 39.44970), (-0.33590, 39.45180)
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
            (-0.40150, 39.46980), (-0.39750, 39.46980),
            (-0.39750, 39.46700), (-0.40150, 39.46700), (-0.40150, 39.46980)
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
            (-0.33250, 39.47120), (-0.32850, 39.47120),
            (-0.32850, 39.46780), (-0.33250, 39.46780), (-0.33250, 39.47120)
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
            (-0.37580, 39.49450), (-0.37200, 39.49450),
            (-0.37200, 39.49120), (-0.37580, 39.49120), (-0.37580, 39.49450)
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
            (-0.36080, 39.48750), (-0.35680, 39.48750),
            (-0.35680, 39.48420), (-0.36080, 39.48420), (-0.36080, 39.48750)
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
            (-0.32880, 39.48180), (-0.32480, 39.48180),
            (-0.32480, 39.47880), (-0.32880, 39.47880), (-0.32880, 39.48180)
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
            (-0.36480, 39.45990), (-0.36080, 39.45990),
            (-0.36080, 39.45680), (-0.36480, 39.45680), (-0.36480, 39.45990)
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
            (-0.39080, 39.49590), (-0.38680, 39.49590),
            (-0.38680, 39.49250), (-0.39080, 39.49250), (-0.39080, 39.49590)
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
            (-0.38910, 39.45910), (-0.38510, 39.45910),
            (-0.38510, 39.45580), (-0.38910, 39.45580), (-0.38910, 39.45910)
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
            (-0.34120, 39.47420), (-0.33620, 39.47420),
            (-0.33620, 39.47020), (-0.34120, 39.47020), (-0.34120, 39.47420)
        ]
    }
]

def generar_kml():
    kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, 'Document')
    ET.SubElement(document, 'name').text = "Mercadillos Valencia - Zonas de Afectación Reales"

    # Estilo para los perímetros (áreas rectangulares que engloban perfectamente las calles de afectación)
    style_poly = ET.SubElement(document, 'Style', id="estiloPerimetro")
    poly_style = ET.SubElement(style_poly, 'PolyStyle')
    ET.SubElement(poly_style, 'color').text = "400000FF"  # Rojo translúcido suave
    line_style = ET.SubElement(style_poly, 'LineStyle')
    ET.SubElement(line_style, 'color').text = "FF0000FF"  # Rojo sólido para delimitar el perímetro exacto
    ET.SubElement(line_style, 'width').text = "2"

    for m in MERCADILLOS:
        # 1. Capa de Perímetro delimitador de la zona afectada
        pm_poly = ET.SubElement(document, 'Placemark')
        ET.SubElement(pm_poly, 'name').text = f"Zona afectada: {m['nombre']}"
        ET.SubElement(pm_poly, 'styleUrl').text = "#estiloPerimetro"
        
        polygon = ET.SubElement(pm_poly, 'Polygon')
        outer = ET.SubElement(polygon, 'outerBoundaryIs')
        linear_ring = ET.SubElement(outer, 'LinearRing')
        coords_str = " ".join([f"{lon},{lat},0" for lon, lat in m['coords_perimetro']])
        ET.SubElement(linear_ring, 'coordinates').text = coords_str

        # 2. Capa de Chincheta Informativa
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
