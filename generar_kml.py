import urllib.request
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Lista completa de mercadillos extraordinarios de Valencia con Monteolivete incluido
MERCADILLOS = [
    {
        "nombre": "Mercadillo de Ruzafa",
        "dia": "Lunes",
        "horario": "09:00 - 14:00",
        "lat": 39.4628,
        "lon": -0.3725,
        "calles": "C/ Barón de Cortes, C/ Padre Perera, C/ Dr. Serrano, C/ Carlos Cervera, C/ Clero"
    },
    {
        "nombre": "Mercadillo de Algirós",
        "dia": "Lunes",
        "horario": "09:00 - 14:00",
        "lat": 39.4722,
        "lon": -0.3514,
        "calles": "C/ Actor Llorens, C/ Rugat, C/ La Pobla de Farnals, Plaza San Felipe Neri"
    },
    {
        "nombre": "Mercadillo de Jerusalén / Convento",
        "dia": "Martes",
        "horario": "09:00 - 14:00",
        "lat": 39.4645,
        "lon": -0.3789,
        "calles": "C/ Convento Jerusalén, C/ Julio Antonio, C/ Ermita, C/ Estrella"
    },
    {
        "nombre": "Mercadillo de Nazaret",
        "dia": "Martes",
        "horario": "09:00 - 14:00",
        "lat": 39.4503,
        "lon": -0.3341,
        "calles": "C/ Alta del Mar"
    },
    {
        "nombre": "Mercadillo de Avenida del Cid",
        "dia": "Miércoles",
        "horario": "09:00 - 14:00",
        "lat": 39.4691,
        "lon": -0.3985,
        "calles": "C/ José Maestre, C/ Dels Jurats, C/ Miguel Paredes, Plaza del Mercado"
    },
    {
        "nombre": "Mercadillo del Cabañal",
        "dia": "Jueves",
        "horario": "09:00 - 14:00",
        "lat": 39.4688,
        "lon": -0.3298,
        "calles": "C/ Escalante, Av. Mediterráneo, Plaza Cruz del Cañamelar, C/ Justo Vilar"
    },
    {
        "nombre": "Mercadillo de Torrefiel",
        "dia": "Jueves",
        "horario": "09:00 - 14:00",
        "lat": 39.4921,
        "lon": -0.3732,
        "calles": "C/ Alemany, C/ Monte Carmelo, C/ Santo Domingo Savio, C/ Jacomart"
    },
    {
        "nombre": "Mercadillo de Benimaclet",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.4851,
        "lon": -0.3582,
        "calles": "C/ Sant Esperit, C/ Juan Giner, C/ Utiel, C/ Murta, Plaza de Benimaclet"
    },
    {
        "nombre": "Mercadillo de La Malvarrosa",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.4795,
        "lon": -0.3261,
        "calles": "C/ Berenguer de Montoliu, C/ Lanzarote"
    },
    {
        "nombre": "Mercadillo de Monteolivete",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.4589,
        "lon": -0.3621,
        "calles": "C/ Pedro Aleixandre, C/ Alcalde Reig, C/ Escultor José Capuz"
    },
    {
        "nombre": "Mercadillo de Benicalap",
        "dia": "Sábado",
        "horario": "09:00 - 14:00",
        "lat": 39.4935,
        "lon": -0.3881,
        "calles": "C/ Miguel Servet, C/ Sierra Martés, C/ Mirasol, C/ Lauri Volpi"
    },
    {
        "nombre": "Mercadillo de Jesús-Patraix",
        "dia": "Sábado",
        "horario": "09:00 - 14:00",
        "lat": 39.4582,
        "lon": -0.3862,
        "calles": "C/ Beato Nicolás Factor, Plaza Jesús, C/ Conca, C/ Pío XI"
    },
    {
        "nombre": "Rastro de Valencia",
        "dia": "Domingo",
        "horario": "08:00 - 14:00",
        "lat": 39.4715,
        "lon": -0.3381,
        "calles": "Zona Beteró / Av. Tarongers - Serrería"
    }
]

def generar_kml():
    kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, 'Document')
    
    ET.SubElement(document, 'name').text = "Mercadillos Valencia"
    
    # Estilo de icono (Cesta de compras de Google Maps)
    style = ET.SubElement(document, 'Style', id="iconoMercadillo")
    icon_style = ET.SubElement(style, 'IconStyle')
    ET.SubElement(icon_style, 'scale').text = "1.2"
    icon = ET.SubElement(icon_style, 'Icon')
    ET.SubElement(icon, 'href').text = "http://maps.google.com/mapfiles/kml/shapes/shopping.png"

    for m in MERCADILLOS:
        pm = ET.SubElement(document, 'Placemark')
        ET.SubElement(pm, 'name').text = f"🛒 {m['nombre']} ({m['dia']})"
        ET.SubElement(pm, 'styleUrl').text = "#iconoMercadillo"
        
        desc = (
            f"<![CDATA["
            f"<b>Día habitual:</b> Todos los {m['dia']}s<br/>"
            f"<b>Horario prohibición aparcar:</b> 06:00 - 15:00 h<br/>"
            f"<b>Horario venta:</b> {m['horario']}<br/><br/>"
            f"<b>Calles afectadas:</b><br/>{m['calles']}"
            f"]]>"
        )
        ET.SubElement(pm, 'description').text = desc
        
        point = ET.SubElement(pm, 'Point')
        ET.SubElement(point, 'coordinates').text = f"{m['lon']},{m['lat']},0"

    # Formatear XML de forma limpia
    xml_str = minidom.parseString(ET.tostring(kml, encoding='utf-8')).toprettyxml(indent="  ")
    
    with open("mercadillos_valencia.kml", "w", encoding="utf-8") as f:
        f.write(xml_str)

    print("✅ KML generado correctamente.")

if __name__ == "__main__":
    generar_kml()
