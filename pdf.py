from fpdf import FPDF
from datetime import datetime

arreglo = [     {'fecha': datetime.now().strftime('%d-%m-%Y %H:%M:%S')},
                {'conversacion': ['User: Hola',
                         'Bot: Hola, ¿en qué puedo ayudarte?',
                          'User: Ayudame', 
                          'Bot: Puedo apoyarte con lo siguiente, solo selecciona una opción:', 
                          'User: solicitarInfoSitioWeb', 
                          'Bot: Perfecto, podemos ayudarte a crear un sitio web exitoso que a su vez cuente con un diseño atractivo, intuitivo y responsivo. Creemos una página web a la medida de tu negocio. Pueden ser informativas, tiendas virtuales o aplicaciones más complejas. Si cuentas con una página web y necesitas asesoría para cambiar de hospedaje, tenemos paquetes que se adaptan a tus necesidades. Podemos ayudarte a mejorar la presencia en línea de tu sitio web con campañas publicitarias y usando técnicas para captar la atención de clientes potenciales. \n Para más información visita nuestro [sitio web](https://uxdigital.com.mx/pagina-web/)', 
                          'Bot: ¿Hay algo más que pueda hacer por ti?', 
                          'User: Si', 
                          'Bot: Puedo apoyarte con lo siguiente, solo selecciona una opción:', 
                          'User: solicitarAtencionPersonal', 
                          'Bot: Por favor proporcionanos tu nombre:', 
                          'User: Mi nombre es José Luis', 'User: Mi nombre es José Luis', 
                          'Bot: Ahora tu número telefónico:', 
                          'User: 7712795866']}
        ]

fecha = arreglo[0]['fecha']
title = 'Conversación'+' fecha: '+fecha

class PDF(FPDF):
    def header(self):
        self.image('logo.png', 12, 5, 25)
        self.set_font('helvetica', 'B', 18) # font
        title_w = self.get_string_width(title) + 6 # Calculate width of title and position
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # colors of frame, background, and text
        self.set_draw_color(220, 50, 50) # border = blue
        self.set_text_color(0, 80, 180) # text = red
        self.set_line_width(1.5) # Thickness of frame (border)
        self.cell(title_w, 15, title, border=1, ln=1, align='C') # Title
        self.ln(20) # Line break

    def footer(self): # Page footer
        self.set_y(-15)  # Set position of the footer
        self.set_font('Times', 'I', 9.5) # set font
        self.set_text_color(169,169,169) # Set font color grey
        self.cell(0, 10, f'Página {self.page_no()}', align='C') # Page number

    def body(self):
        self.add_page()
        self.set_y(50)
        self.set_font('helvetica', 'B', 10)
        contador = 0
        conversacion = arreglo[1]['conversacion']
        for i in conversacion:
                if i == conversacion[contador-1]:
                        pass
                else:
                        if i.count('User:') > 0:
                                self.set_x(15)
                                pdf.set_fill_color(145, 222, 159)
                                pdf.cell(self.get_string_width(i) + 10, 10, i.replace('User:', '- Usuario:'), ln=1, align='L', fill=True)
                        else:
                                self.set_x(85)
                                title_w = self.get_string_width(i)
                                pdf.set_fill_color(136, 173, 245)
                                pdf.set_fill_color(136, 173, 245)
                                if len(i) > 80:
                                        pdf.multi_cell(115, 5, i.replace('nuestro [sitio web]','').replace('(','').replace(')','').replace('Bot','- Bot'), ln=1, align='J', fill=True)
                                        self.ln(5)
                                else:
                                        pdf.multi_cell(title_w + 6, 10, i.replace('nuestro [sitio web]','').replace('(','').replace(')','').replace('Bot','- Bot'), ln=1, align='R', fill=True)
                contador+=1

pdf = PDF('P', 'mm', 'Letter') # Create a PDF object
pdf.alias_nb_pages() # get total page numbers
pdf.set_auto_page_break(auto = True, margin = 15) # Set auto page break
pdf.body()
pdf.output('test.pdf')