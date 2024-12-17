# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
import streamlit as st
from fpdf import FPDF
import plotly.io as pio
from database import cf_calculation, energy_bar_chart, waste_bar_chart, travel_bar_chart, \
    pie_chart


class PDF_Creation(FPDF):

    def title(self, title):
        self.set_font('Arial', 'B', 20)
        self.cell(0, 10, title, 0, 4, 'L')
        self.ln(5)

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

def create_pdf():
    cf = str(cf_calculation())
    # save_images(year)

    pdf = PDF_Creation()
    pdf.add_page()

    pdf.title('YOUR CARBON FOOTPRINT REPORT')
    pdf.subtitle('Monthly Overview:')
    # pdf.body(f'Your carbon footprint is : {cf}')

    # pdf.insert_image(image_path = 'pie_chart.png', title = 'Pie Chart: Breakdown of your current carbon footprint')

    pdf_path = 'carbon_footprint_report'
    pdf.output(pdf_path)

    with open(pdf_path, 'rb') as f:
        pdf_data = f.read()

    return pdf_data
