# https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html

from fpdf import FPDF
from data_tables import data_tables
from database import cf_calculation, energy_bar_chart, waste_bar_chart, travel_bar_chart, \
    pie_chart



class PDF_Creation(FPDF):

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

def create_pdf(year):
    cf = str(cf_calculation())

    pdf = PDF_Creation()
    pdf.add_page()

    pdf.subtitle('YOUR CARBON FOOTPRINT SUMMARY')
    pdf.subtitle('Monthly Overview:')
    pdf.body(f'Your carbon footprint is : {cf} kg/year')

    pie = pie_chart()
    pie.write_image("pie_chart.png")
    pdf.insert_image("pie_chart_png", 'Your Carbon Footprint Breakdown for the Month')

    pdf.subtitle('Your Energy Consumption:')
    energy_bar = energy_bar_chart(year)
    energy_bar.write_image('energy.png')
    pdf.insert_image('energy.png', 'Energy Consumption of Chosen Year')

    pdf.subtitle('Your Waste Management:')
    waste_bar = waste_bar_chart(year)
    waste_bar.write_image('waste.png')
    pdf.insert_image('waste.png', 'Waste Management of Chosen Year')

    pdf.subtitle('Your Travel Consumption of Chosen Year:')
    travel_bar = travel_bar_chart(year)
    travel_bar.write_image('travel.png')
    pdf.insert_image('travel.png', 'Travel Consumption of Chosen Year')

    pdf.subtitle('Your Data:')
    Monthly_data_df1, monthly_diff, total_change_html, energy_consumption, waste_generation, travel_consumption, carbon_footprint = data_tables(year)
    Monthly_data_df1.write_image('client_data.png')
    total_change_html.write_image('total_change.png')
    monthly_diff.write_image('monthly_diff.png')
    pdf.insert_image('client_data.png', 'Provided Data')
    pdf.insert_image('monthly_diff.png', 'Monthly Difference in Consumption')
    pdf.insert_image('total_change.png', 'Change in Consumption Over the Last Year')

    pdf.body('Please refer to the website for updated recommendations! We will let you know as we think of better ways to help you! :)')
    pdf.subtitle('THANK YOU FOR YOUR SUPPORT IN OUR ENDEAVOR TO SAVE THE PLANET!')

    return pdf
