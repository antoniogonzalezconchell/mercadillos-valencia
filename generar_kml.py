import urllib.request
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom

# URL API Datos Abiertos Ayuntamiento de Valencia (Mercados extraordinarios)
API_VALENCIA_URL = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/mercats-ambulants-mercados-ambulantes/records?limit=100"

# Mercadillos adicionales / comprobación manual por si no están mapeados en la API
MERCADILLOS_EXTRA = [
    {
        "nombre": "Mercadillo de Monteolivete",
        "dia": "Viernes",
        "horario": "09:00 - 14:00",
        "lat": 39.4589,
        "lon": -0.3621,
        "calles": "C/ Pedro Aleixandre, C/ Alcalde Reig"
    }
]

def obtener_datos_ayuntamiento():
    try:
        req = urllib.request.Request(API_VALENCIA_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('results', [])
    except Exception as e:
        print(f"Error consultando API consistorio: {e}")
        return []

def generar_kml():
    registros_api = obtener_datos_ayuntamiento()
    
    kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, 'Document')
    
    ET.SubElement(document, 'name').text = "Mercadillos Valencia (Oficial API)"
    
    # Definición de Estilo: Icono de cesta/tienda azul/rojo
    style = ET.SubElement(document, 'Style', id="iconoMercadillo")
    icon_style = ET.SubElement(style, 'IconStyle')
    ET.SubElement(icon_style, 'scale').text = "1.2"
    icon = ET.SubElement(icon_style, 'Icon')
    # Icono oficial de Google Maps para Shopping/Market
    ET.SubElement(icon, 'href').text = "http://maps.google.com/mapfiles/kml/shapes/shopping.png"

    # 1. Procesar registros API oficial
    for r in registros_api:
        # Extraer campos de la API
        nombre = r.get('nombre', r.get('descripcio', 'Mercadillo Ambulante'))
        geo = r.get('geo_point_2d', {})
        lat = geo.get('lat')
        lon = geo.get('lon')
        calles = r.get('ubicacion', 'Consultar señalización local')
        dia = r.get('dia_semana', 'Consultar cartelera')

        if lat and lon:
            pm = ET.SubElement(document, 'Placemark')
            ET.SubElement(pm, 'name').text = f"🛒 {nombre}"
            ET.SubElement(pm, 'styleUrl').text = "#iconoMercadillo"
            
            desc = (
                f"<![CDATA["
                f"<b>Ubicación:</b> {calles}<br/>"
                f"<b>Día de montaje:</b> {dia}<br/>"
                f"<b>Horario prohibición aparcar:</b> 06:00 - 15:00 h<br/>"
                f"<i>Fuente: Open Data Ayto. de Valencia</i>"
                f"]]>"
            )
            ET.SubElement(pm, 'description').text = desc
            
            point = ET.SubElement(pm, 'Point')
            ET.SubElement(point, 'coordinates').text = f"{lon},{lat},0"

    # 2. Procesar adicionales (ej. Monteolivete)
    for m in MERCADILLOS_EXTRA:
        pm = ET.SubElement(document, 'Placemark')
        ET.SubElement(pm, 'name').text = f"🛒 {m['nombre']}"
        ET.SubElement(pm, 'styleUrl').text = "#iconoMercadillo"
        desc = (
            f"<![CDATA["
            f"<b>Ubicación:</b> {m['calles']}<br/>"
            f"<b>Día de montaje:</b> Todos los {m['dia']}s<br/>"
            f"<b>Horario prohibición aparcar:</b> 06:00 - 15:00 h"
            f"]]>"
        )
        ET.SubElement(pm, 'description').text = desc
        point = ET.SubElement(pm, 'Point')
        ET.SubElement(point, 'coordinates').text = f"{m['lon']},{m['lat']},0"

    # Formatear y guardar XML
    xml_str = minidom.parseString(ET.tostring(kml, encoding='utf-8')).toprettyxml(indent="  ")
    with open("mercadillos_valencia.kml", "w", encoding="utf-8") as f:
        f.write(xml_str)

    print("✅ KML actualizado con datos oficiales e iconos personalizados.")

if __name__ == "__main__":
    generar_kml()
   
