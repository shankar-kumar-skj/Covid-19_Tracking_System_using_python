from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load data from CSV
df = pd.read_csv("C:\\1st_year_internship_SHANKAR\\covid\\venv\\real_covid.csv")  # Use a relative path to the CSV file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']  # Get the country from the form
        summary = covid_case_tracker(df, country)  # Call the function to get summary
        return render_template('index.html', summary=summary)  # Render the template with summary
    else:
        return render_template('index.html')  # Render the template for GET request

def covid_case_tracker(df, country):
    # Filter data for the specified country
    country_data = df[df['country'].str.lower() == country.lower()]

    # Check if there's data for the country
    if country_data.empty:
        return f"No data found for {country}."  # Return a message if no data found

    # Summarize total cases, recoveries, and deaths
    total_cases = country_data['cases'].sum()
    total_recoveries = country_data['recoveries'].sum()
    total_deaths = country_data['deaths'].sum()

    # Create summary dictionary
    summary = {
        'Total Cases': total_cases,
        'Total Recoveries': total_recoveries,
        'Total Deaths': total_deaths
    }

    return summary  # Return the summary

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode