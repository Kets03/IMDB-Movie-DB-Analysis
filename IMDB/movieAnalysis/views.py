from django.shortcuts import render
import pandas as pd
# Create your views here.
def IMDB_analysis(request):
    df = pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv')
    revenue_per_year = df.groupby('Year')['Revenue (Millions)'].sum().to_dict()
    analysis = {
        'avg_runtime': df['Runtime (Minutes)'].mean(),
        'avg_rating': df['Rating'].mean(),
        'avg_votes': df['Votes'].mean(),
        'avg_revenue': df['Revenue (Millions)'].mean(),
        'revenue_per_year': revenue_per_year
    }
    return render(request, 'movie_analysis.html', {'analysis': analysis})