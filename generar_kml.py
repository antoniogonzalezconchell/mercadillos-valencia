import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

# 1. BASE DE DATOS DE MERCADILLOS EXTRAORDINARIOS DE VALENCIA
# Incluye ubicación aproximada (lat/lon) y las calles afectadas del perímetro
MERCADILLOS_VALENCIA = [
    {
        "nombre": "Mercadillo de Ruzafa",
        "dias_semana": [0],  # 0 = Lunes
        "horario": "09:00 - 14:00",
        "lat": 39.4628,
        "lon": -0.3725,
        "calles": ["C/ Barón de Cortes", "C/ Padre Perera", "C/ Dr. Serrano", "C/ Carlos Cervera", "C/ Clero"]
    },
    {
        "nombre": "Mercadillo de Algirós",
        "dias_semana": [0],  # Lunes
        "horario": "09:00 - 14:00",
        "lat": 39.4722,
        "lon": -0.3514,
        "calles": ["C/ Actor Llorens", "C/ Rugat", "C/ La Pobla de Farnals", "Plaza San Felipe Neri"]
    },
    {
        "nombre": "Mercadillo de Jerusalén / Convento",
        "dias_semana": [1],  # 1 = Martes
        "horario": "09:00 - 14:00",
        "lat": 39.4645,
        "lon": -0.3789,
        "calles": ["C/ Convento Jerusalén", "C/ Julio Antonio", "C/ Ermita", "C/ Estrella"]
    },
    {
        "nombre": "Mercadillo de Nazaret",
        "dias_semana": [1],  # Martes
        "horario": "09:00 - 14:00",
        "lat": 39.4503,
        "lon": -0.3341,
        "calles": ["C/ Alta del Mar"]
    },
    {
        "nombre": "Mercadillo de Avenida del Cid",
        "dias_semana": [2],  # 2 = Miércoles
        "horario": "09:00 - 14:00",
        "lat": 39.4691,
        "lon": -0.3985,
        "calles": ["C/ José Maestre", "C/ Dels Jurats", "C/ Miguel Paredes", "Plaza del Mercado"]
    },
    {
        "nombre": "Mercadillo del Cabañal",
        "dias_semana": [3],  # 3 = Jueves
        "horario": "09:00 - 14:00",
        "lat": 39.4688,
        "lon": -0.3298,
        "calles": ["C/ Escalante", "Av. Mediterráneo", "Plaza Cruz del Cañamelar", "C/ Justo Vilar"]
    },
    {
        "nombre": "Mercadillo de Torrefiel",
        "dias_semana": [3],  # Jueves
        "horario": "09:00 - 14:00",
        "lat": 39.4921,
        "lon": -0.3732,
        "calles": ["C/ Alemany", "C/ Monte Carmelo", "C/ Santo Domingo Savio", "C/ Jacomart"]
    },
    {
        "nombre": "Mercadillo de Benimaclet",
        "dias_semana": [4],  # 4 = Viernes
        "horario": "09:00 - 14:00",
        "lat": 39.4851,
        "lon": -0.3582,
        "calles": ["C/ Sant Esperit", "C/ Juan Giner", "C/ Utiel", "C/ Murta", "Plaza de Benimaclet"]
    },
    {
        "nombre": "Mercadillo de La Malvarrosa",
        "dias_semana": [4],  # Viernes
        "horario": "09:00 - 14:00",
        "lat": 39.4795,
        "lon": -0.3261,
        "calles": ["C/ Berenguer de Montoliu", "C/ Lanzarote"]
    },
    {
        "nombre": "Mercadillo de Benicalap",
        "dias_semana": [5],  # 5 = Sábado
        "horario": "09:00 - 14:00",
        "lat": 39.4935,
        "lon": -0.3881,
        "calles": ["C/ Miguel Servet", "C/ Sierra Martés", "C/ Mirasol", "C/ Lauri Volpi"]
    },
    {
        "nombre": "Mercadillo de Jesús-Patraix",
        "dias_semana": [5],  # Sábado
        "horario": "09:00 - 14:00",
        "lat": 39.4582,
        "lon": -0.3862,
        "calles": ["C/ Beato Nicolás Factor", "Plaza Jesús", "C/ Conca", "C/ Pío XI"]
    },
    {
        "nombre": "Rastro de Valencia",
        "dias_semana": [6],  # 6 = Domingo
        "horario": "08:00 - 14:00",
        "lat": 39.4715,
        "lon": -0.3381,
        "calles": ["Zona Beteró / Av. Tarongers - Serrería"]
    }
]

NOMBRES_DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 2. GESTIÓN DE FECHAS Y DÍAS PRÓXIMOS
def obtener_proxima_fecha(dia_semana_target):
    """Calcula la fecha exacta del próximo día de la semana indicado."""
    hoy = datetime.date.today()
    dias_hasta_evento = (dia_semana_target - hoy.weekday()) % 7
    if dias_hasta_evento == 0:
        dias_hasta_evento = 0  # Es hoy
    return hoy + datetime.timedelta(days=dias_hasta_evento)

# 3. GENERACIÓN DEL ARCHIVO KML
def generar_kml_mercadillos(lista_mercadillos, archivo_salida="mercadillos_valencia.kml"):
    """Crea un documento KML estructurado para Google Maps."""
    kml = ET.Element('kml', xmlns="http://www.opengis.net/kml/2.2")
    document = ET.SubElement(kml, 'Document')
    
    # Nombre del mapa en Google Maps
    nombre_mapa = ET.SubElement(document, 'name')
    nombre_mapa.text = "Mercadillos Semanales de Valencia - Avisos de Aparcamiento"
    
    descripcion_mapa = ET.SubElement(document, 'description')
    descripcion_mapa.text = "Ubicaciones oficiales, días de montaje y calles afectadas para evitar multas de grúa."

    # Definir estilos de icono (Pin Rojo)
    style = ET.SubElement(document, 'Style', id="iconoMercadillo")
    icon_style = ET.SubElement(style, 'IconStyle')
    scale = ET.SubElement(icon_style, 'scale')
    scale.text = "1.1"
    icon = ET.SubElement(icon_style, 'Icon')
    href = ET.SubElement(icon, 'href')
    href.text = "http://maps.google.com/mapfiles/kml/paddle/red-circle.png"

    # Insertar los marcadores
    for mercadillo in lista_mercadillos:
        proximo_dia = obtener_proxima_fecha(mercadillo["dias_semana"][0])
        nombre_dia = NOMBRES_DIAS[mercadillo["dias_semana"][0]]
        calles_str = "<br/>• ".join(mercadillo["calles"])
        
        pm = ET.SubElement(document, 'Placemark')
        
        name = ET.SubElement(pm, 'name')
        name.text = f"{mercadillo['nombre']} ({nombre_dia})"
        
        style_url = ET.SubElement(pm, 'styleUrl')
        style_url.text = "#iconoMercadillo"
        
        description = ET.SubElement(pm, 'description')
        description.text = (
            f"<![CDATA["
            f"<b>Día habitual:</b> Todos los {nombre_dia}s<br/>"
            f"<b>Horario prohibición aparcar:</b> 06:00 - 15:00 h<br/>"
            f"<b>Horario venta:</b> {mercadillo['horario']}<br/>"
            f"<b>Próxima edición:</b> {proximo_dia.strftime('%d/%m/%Y')}<br/><br/>"
            f"<b>Calles afectadas:</b><br/>• {calles_str}"
            f"]]>"
        )
        
        point = ET.SubElement(pm, 'Point')
        coordinates = ET.SubElement(point, 'coordinates')
        # Formato KML: Longitud, Latitud, Altitud
        coordinates.text = f"{mercadillo['lon']},{mercadillo['lat']},0"

    # Formatear XML de forma limpia
    xml_str = minidom.parseString(ET.tostring(kml, encoding='utf-8')).toprettyxml(indent="  ")
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        f.write(xml_str)
        
    print(f"✅ Archivo KML generado con éxito: '{archivo_salida}'")

if __name__ == "__main__":
    generar_kml_mercadillos(MERCADILLOS_VALENCIA)
