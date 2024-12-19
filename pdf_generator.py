# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
import io
import plotly.express as pe
import streamlit as st
from fpdf import FPDF
import plotly.io as pio
from database import cf_calculation, energy_bar_chart, waste_bar_chart, travel_bar_chart, \
    pie_chart, connection_creation
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
import pdfkit


class PDF_Creation(FPDF):

    # def title(self, title):
    #     self.set_font('Arial', 'B', 20)
    #     self.cell(0, 10, title, 0, 4, 'L')
    #     self.ln(5)

    def subtitle(self, title):
        self.set_font('Arial', 'I', 12)
        self.cell(0, 10, title, 0, 5, 'L')
        self.ln(5)

    def body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def insert_image(self, image_path, title):
        self.add_page()
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'C')
        self.ln(10)
        self.image(image_path, x=10, y=None, w=190)


# Create a PDF document
# def save_images(year):
#     pie = pie_chart()
#     pio.write_image(pie, 'pie_chart.png')
#
#     energy_bar = energy_bar_chart(year)
#     pio.write_image(energy_bar, 'energy.png')
#
#     waste_bar = waste_bar_chart(year)
#     pio.write_image(waste_bar, 'waste.png')
#
#     travel_bar = travel_bar_chart(year)
#     pio.write_image(travel_bar, 'travel.png')
#
#     cf_bar = carbon_footprint_bar_chart(year)
#     pio.write_image(cf_bar, 'cf_bar.png')

def pdf_pie_chart():
    connection = connection_creation()
    cursor = connection.cursor()
    cursor.execute(f'''SELECT energy, waste, travel
                    FROM calculated
                    WHERE username = '{st.session_state.username}'
                    ORDER BY year DESC, month DESC
                    LIMIT 1''')
    values1 = cursor.fetchall()
    connection.close()

    val1_table = pd.DataFrame(values1, columns=['energy', 'waste', 'travel'])
    val1_table_values = val1_table[['energy', 'waste', 'travel']].sum()

    fig = go.Figure(data=[go.Pie(labels=['Energy', 'Waste', 'Travel'],
                                 values=[val1_table_values['energy'], val1_table_values['waste'], val1_table_values['travel']],
                                 hole=.3)])

    fig.write_image("pie_chart.png")

    return "pie_chart.png"


def create_pdf(pie_chart_path):
    cf = str(cf_calculation())

    pdf = PDF_Creation()
    pdf.add_page()

    pdf.subtitle('YOUR CARBON FOOTPRINT REPORT')
    pdf.subtitle('Monthly Overview:')
    pdf.body(f'Your carbon footprint is : {cf}')



    # pie = pie_chart()
    # pie.write_image("pie_chart.png")
    # pdf.image("pie_chart_png", x=50, y=100, w=150)
    # pie_char.write_image('pie_chart.png')
    # pdf.insert_image(image_path = 'pie_chart.png', title = 'Pie Chart: Breakdown of your current carbon footprint')

    # pdf_path = 'carbon_footprint_report'
    # pdf.output(pdf_path)

    # with open(pdf_path, 'rb') as f:
    #     pdf_data = f.read()

    return pdf

# def create_pdf2():
#     # Create a Plotly Express pie chart
#     fig = pe.pie(values=[20, 30, 50], names=['A', 'B', 'C'])
#
#     # Save the figure to a bytes buffer using kaleido
#     img_bytes = fig.to_image(format="png")
#
#     # Create a new PDF document
#     pdf_buffer = io.BytesIO()
#     c = canvas.Canvas(pdf_buffer, pagesize=letter)
#
#     # Add text or any additional content to the PDF
#     c.drawString(100, 750, "Plotly Express Pie Chart PDF Example")
#
#     # Load the pie chart image from the bytes
#     pie_chart_img = Image.open(io.BytesIO(img_bytes))
#
#     img_temp_path = "/tmp/pie_chart_image.png"
#     pie_chart_img.save(img_temp_path)
#
#     # Draw the image onto the PDF
#     c.drawImage(img_temp_path, 100, 400, width=400, height=300)
#
#     # Finalize the PDF document
#     c.showPage()
#     c.save()
#
#     # Return to the beginning of the buffer
#     pdf_buffer.seek(0)
#
#     return pdf_buffer

# def create_pdf():
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt = "Hello World", ln=True, align="C")
#     return pdf
#
# def get_pdf_bytes():
#     pdf = create_pdf()
#     pdf_output = io.BytesIO()
#     pdf.output(pdf_output)
#     pdf_output.seek(0)
#     return pdf_output

def gen_pdf():
    pdf_file = 'streamlit_content.pdf'
    pdfkit.from_url('http://localhost:8501', pdf_file)
    return pdf_file

    # if st.button('Generate PDF'):
    #     pdf_file = save_streamlit_as_pdf()
    #     st.success(f'PDF generated: {pdf_file}')
    #
    #     # Convert PDF to HTML (this requires pdf2htmlEX to be installed)
    #     html_file = 'streamlit_content.html'
    #     os.system(f'pdf2htmlEX {pdf_file} {html_file}')
    #     st.success(f'HTML file generated: {html_file}')
    #
    #     with open(html_file, 'r') as f:
    #         st.download_button('Download HTML', f, file_name='streamlit_content.html')



