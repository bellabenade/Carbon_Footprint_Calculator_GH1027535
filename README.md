Gabriella Benade
GH1027535

Carbon Footprint Calculator
19/12/2024

Purpose:
To create a carbon footprint calculator, as an intern, for a chemical supply company, CHEMistry Co.
The aim of this project is to make the clients of the company aware of their effect on the environment (especially considering that they utilize chemical in some way or another.
CHEMistry wants so motivate clients to decrease their footprint, by offering a generous discount to clients that can drop their current carbon footprint by 10% within the next year.
By offering a reward to willing customers, CHEMistry Co. can get clients to take the environment into consideration.

How to run the Python code:
1) Included in the project:
    * Multiple python scripts
    * An SQLite database
    * An image
    * Requirements document.
  
2) The github link https://github.com/bellabenade/Carbon_Footprint_Calculator_GH1027535.git will allow one to get the repository of the project on the creator's profile.
   Multiple commits have been made to show the progress on the project.

3) Please refer to the requirements.txt document. Ensure that all the required libraries are installed on your program, so that there is no problem running the code on your own computer.

4) The script named carbon_footprint_calculator.py is the main Python file and is the only one that would be required to run. You can run the code by entering the following into your terminal:
     streamlit run carbon_footprint_calculator.py
   No other scripts need to be run, altered or changed.
   The other Python scripts were created to store functions that is called when running streamlit on your browser. Changes to these scripts would affect the working of the streamlit website.

6) If the user wants to see the database, then a simple database browser can be installed (https://sqlitebrowser.org/), or the code in the script data_tables.py can be run to create the database tables that is saved in the databse.

How the website works:
1) First, a login page will appear.
2) You can either create your own username and password, or you can login as one of the already existing clients. Here is a profile that you can inspect:
   Username: Company_A
   Password: 3456
3) The website's home page will open welcoming the user to the website. There are tabs at the top of the page, where the user can navigate through the website.
   Clicking on the Add/ Change info will open a form where users can submit monthly data, that the python code then processes to calculate the carbon footprint of the users and visualise the current state of the company, in terms of carbon emmissions.
   Clicking on the Carbon Footprint Report will display all the relevant information, graphs and recommendations to the users.
   


