import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trends = TrendReq()

def interest(kwList):
    
    print("\n\n\n\t\t*** Interest for Keywords ["+ ' , '.join(kwList) +"] by Region ***\n")
    trends.build_payload(kw_list=kwList)
    try:
        data = trends.interest_by_region()
    except:
        print("Please check your connection and try again!")
    else:
        data = data[(data != 0).all(1)]  # to remove rows with value of zero
        df = data.head()
        print(df)
        if input("\nShow the chart?(y/n)  ")=="y":
            showPlot(df,kwList)
    
def showPlot(df, kwList):
    df.reset_index().plot(x="geoName", y=kwList, figsize=(20,12), kind="bar")
    plt.show()

def trendingSeacrches(country):
    
    print("\n\n\n\t\t*** Trending Searches in "+ country.title() +" ***\n")
    data = trends.trending_searches(pn=country)
    print(data.head(10))

def suggestions(k):

    print("\n\n\n\t\t*** '"+ k +"' Keyword Suggestions ***\n")
    keywords = trends.suggestions(keyword=k)
    data = pd.DataFrame(keywords)
    print(data.head())

x = "Interest for Keywords by Region"
y = "Trending Searches in a Specific Country"
z = "Keyword Suggestions"

i = int(input("API Methods :\n1- "+ x +"\n2- "+ y +"\n3- "+ z +"\n\nPlease choose a method. Write its number: "))

if i == 1 :
    kwList = input("Please enter keywords (separate with ','): ").split(',')
    interest(kwList)
elif i == 2 :
    country = input("Please specify a country: ")
    trendingSeacrches(country)
elif i == 3 :
    keyword = input("Please enter the keyword: ")
    suggestions(keyword)


print("\n\n\t\tGood Luck!")