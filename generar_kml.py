import xml.etree.ElementTree as ET
from xml.dom import minidom

MERCADILLOS = [
    {
        "nombre": "Mercadillo de Ruzafa",
        "dia": "Lunes",
        "horario": "09:00 - 14:00",
        "lat": 39.462750,
        "lon": -0.372320,
        "calles": "C/ Barón de Cortes, C/ Padre Perera, C/ Dr. Serrano, C/ Carlos Cervera, C/ Clero"
    },
    {
        "nombre": "Mercadillo de Algirós",
        "dia": "Lunes",
        "horario": "09:00 - 14:00",
        "lat": 39.472110,
        "lon": -0.351280,
        "calles": "C/ Actor Llorens, C/ Rugat, C/ La Pobla de Farnals, Plaza San Felipe Neri"
    },
    {
        "nombre": "Mercadillo de Jerusalén / Convento",
        "dia": "Martes",
        "horario": "09:00 - 14:00",
        "lat": 39.464410,
        "lon": -0.378750,
        "calles": "C/ Convento Jerusalén, C/ Julio Antonio, C/ Ermita, C/ Estrella"
    },
    {
        "nombre": "Mercadillo de Nazaret",
        "dia": "Martes",
        "horario": "09:00 - 14:00",
        "lat": 39.450190,
        "lon": -0.333950,
        "calles": "C/ Alta del Mar"
    },
    {
        "nombre": "Mercadillo de Avenida del Cid",
        "dia": "Miércoles",
        "horario": "09:00 - 14:00",
        "lat": 39.468980,
        "lon": -0.398320,
        "calles": "C/ José Maestre, C/ Dels Jurats, C/ Miguel Paredes, Plaza del Mercado"
    },
    {
        "nombre": "Mercadillo del Cabañal",
        "dia": "Jueves",
        "horario": "09:00 - 14:00",
        "lat": 39.468650,
        "lon": -0.329610,
        "calles": "C/ Escalante, Av. Mediterráneo, Plaza Cruz del Cañamelar, C/ Justo Vilar"
    },
    {
        "nombre": "Mercadillo de Torrefiel",
        "dia": "Jueves",
        "horario": "09:00 - 14:00",
        "lat": 39.491950,
        "lon": -0.373010,
        "calles": "C/ Alemany, C/ Monte Carmelo, C/ Santo Domingo Savio, C/ Jacomart"
    },
    {
        "nombre": "Mercadillo de Benimaclet",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.484920,
        "lon": -0.358010,
        "calles": "C/ Sant Esperit, C/ Juan Giner, C/ Utiel, C/ Murta, Plaza de Benimaclet"
    },
    {
        "nombre": "Mercadillo de La Malvarrosa",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.479380,
        "lon": -0.325940,
        "calles": "C/ Berenguer de Montoliu, C/ Lanzarote"
    },
    {
        "nombre": "Mercadillo de Monteolivete",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.458750,
        "lon": -0.361950,
        "calles": "C/ Pedro Aleixandre, C/ Alcalde Reig, C/ Escultor José Capuz"
    },
    {
        "nombre": "Mercadillo de Benicalap",
        "dia": "Sábado",
        "horario": "09:00 - 14:00",
        "lat": 39.493320,
        "lon": -0.387910,
        "calles": "C/ Miguel Servet, C/ Sierra Martés, C/ Mirasol, C/ Lauri Volpi"
    },
    {
        "nombre": "Mercadillo de Jesús-Patraix",
        "dia": "Sábado",
        "horario": "09:00 - 14:00",
        "lat": 39.458020,
        "lon": -0.386010,
        "calles": "C/ Beato Nicolás Factor, Plaza Jesús, C/ Conca, C/ Pío XI"
    },
    {
        "nombre": "Rastro de Valencia",
        "dia": "Domingo",
        "horario": "08:00 - 14:00",
        "lat": 39.471350,
        "lon": -0.337920,
        "calles": "Zona Beteró / Av. Tarongers - Serrería"
    }
]

def generar_kml():
    kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, 'Document')
    ET.SubElement(document, 'name').text = "Mercadillos Valencia - Zonas de Afectación"

    for m in MERCADILLOS:
        pm = ET.SubElement(document, 'Placemark')
        ET.SubElement(pm, 'name').text = f"🛒 {m['nombre']} ({m['dia']})"
        
        # Descripción enriquecida resaltando claramente las calles de corte y prevención de grúa
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
        ET.SubElement(pm, 'description').text = desc
        
        point = ET.SubElement(pm, 'Point')
        ET.SubElement(point, 'coordinates').text = f"{m['lon']},{m['lat']},0"

    xml_str = minidom.parseString(ET.tostring(kml, encoding='utf-8')).toprettyxml(indent="  ")
    with open("mercadillos_valencia.kml", "w", encoding="utf-8") as f:
        f.write(xml_str)

if __name__ == "__main__":
    generar_kml()
