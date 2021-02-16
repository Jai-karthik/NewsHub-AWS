# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:41:05 2020

@author: Karthik
"""
import requests
import codecs
import buildArticles

def updatePages(req, page_title, active_tag_text, page_name, article_navigation):
    response = requests.get(req)    
    #responseJSON = json.loads(response.content)
    responseJSON = response.json()
    articlesList = responseJSON['articles'] 
        
    finalArticleHTML = buildArticles.buildArticles(articlesList)
    
    
    index_template=open("/home/ec2-user/lockdown/template.txt","r").read()
    index_template=index_template.replace("#ArticleDetails#",finalArticleHTML)
    index_template=index_template.replace(active_tag_text, active_tag_text.replace("nav-link", "nav-link active"))
    index_template=index_template.replace("#PageTitle#", page_title)
    index_template=index_template.replace("#ArticleNavigation#", article_navigation)
    index_template=index_template.replace("#LastRefresh#", buildArticles.lastRefresh)
    index_template=index_template.replace("#NextRefresh#", buildArticles.nextRefresh)
    index_template=index_template.replace("Â", "")
    index_template=index_template
                                          
    
                                        
    output_index=codecs.open("/home/ec2-user/lockdown/"+page_name+".html","w", "utf-8")
    output_index.write(index_template)
        


#update Pages
#update Business Pages

updatePages("https://newsapi.org/v2/top-headlines?category=general&country=in&apiKey=f2abfaecb4e34e9896f35b95a8570789",
            "Top Headlines",
            "",
            "index",
            buildArticles.indiaHeadline)

updatePages("https://newsapi.org/v2/top-headlines?category=general&apiKey=200ae994998d4f60ac5d2f44a9a2b375",
            "World Headlines",
            "",
            "worldheadlines",
            buildArticles.worldHeadline)

updatePages("https://newsapi.org/v2/top-headlines?q=covid&country=in&sortBy=publishedAt&pageSize=100&apiKey=f2abfaecb4e34e9896f35b95a8570789",
            "Covid-19 India",
            '<a class="nav-link" href="covid.html">Covid-19</a>',
            "covid",
            buildArticles.covidIndia)

updatePages("https://newsapi.org/v2/everything?q=(covid OR corona)&sortBy=publishedAt&pageSize=100&apiKey=200ae994998d4f60ac5d2f44a9a2b375",
            "Covid-19 World",
            '<a class="nav-link" href="covid.html">Covid-19</a>',
            "worldcovid",
            buildArticles.covidWorld)

updatePages("https://newsapi.org/v2/top-headlines?category=business&country=in&sortBy=publishedAt&pageSize=100&apiKey=f2abfaecb4e34e9896f35b95a8570789",
            "Business",
            '<a class="nav-link" href="business.html">Business</a>',
            "business",
            buildArticles.businessIndia)

updatePages("https://newsapi.org/v2/top-headlines?category=business&sortBy=publishedAt&pageSize=100&apiKey=200ae994998d4f60ac5d2f44a9a2b375",
            "Business",
            '<a class="nav-link" href="business.html">Business</a>',
            "worldbusiness",
            buildArticles.businessWorld)

updatePages("https://newsapi.org/v2/top-headlines?category=entertainment&country=in&sortBy=publishedAt&pageSize=100&apiKey=f2abfaecb4e34e9896f35b95a8570789",
            "Entertainment",
            '<a class="nav-link" href="entertainment.html">Entertainment</a>',
            "entertainment",
             buildArticles.entertainmentIndia)

updatePages("https://newsapi.org/v2/top-headlines?category=entertainment&sortBy=publishedAt&pageSize=100&apiKey=200ae994998d4f60ac5d2f44a9a2b375",
            "Entertainment",
            '<a class="nav-link" href="entertainmentWorld.html">Entertainment</a>',
            "worldentertainment",
             buildArticles.entertainmentWorld)

updatePages("https://newsapi.org/v2/top-headlines?country=in&category=health&sortBy=publishedAt&pageSize=100&apiKey=ddd9aef8fe5348c9a26bfe10af5a8435",
            "Health",
            '<a class="nav-link" href="science.html">Sci-Tech & Health</a>',
            "health",
            buildArticles.health)

updatePages("https://newsapi.org/v2/top-headlines?country=in&category=science&sortBy=publishedAt&pageSize=100&apiKey=ddd9aef8fe5348c9a26bfe10af5a8435",
            "Science",
            '<a class="nav-link" href="science.html">Sci-Tech & Health</a>',
            "science",
            buildArticles.science)


updatePages("https://newsapi.org/v2/top-headlines?country=in&category=technology&sortBy=publishedAt&pageSize=100&apiKey=ddd9aef8fe5348c9a26bfe10af5a8435",
            "Technology",
            '<a class="nav-link" href="science.html">Sci-Tech & Health</a>',
            "technology",
            buildArticles.technology)

updatePages("https://newsapi.org/v2/top-headlines?country=in&category=sports&sortBy=publishedAt&pageSize=100&apiKey=f2abfaecb4e34e9896f35b95a8570789",
            "Sports",
            '<a class="nav-link" href="sports.html">Sports</a>',
            "sports",
            buildArticles.sportsIndia)

updatePages("https://newsapi.org/v2/top-headlines?category=sports&sortBy=publishedAt&pageSize=100&apiKey=200ae994998d4f60ac5d2f44a9a2b375",
            "Sports",
            '<a class="nav-link" href="sports.html">Sports</a>',
            "worldsports",
            buildArticles.sportsWorld)

updatePages("https://newsapi.org/v2/everything?q=(cricket OR t20 OR ODI)&sortBy=publishedAt&pageSize=100&apiKey=ddd9aef8fe5348c9a26bfe10af5a8435",
            "Cricket",
            '<a class="nav-link" href="sports.html">Sports</a>',
            "cricket",
            buildArticles.sportsCricket)

print("Updated Successfully!")
