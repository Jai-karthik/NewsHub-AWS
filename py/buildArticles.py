# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:38:06 2020

@author: Karthik
"""
import datetime
from dateutil import tz
import pytz


def tzToIST(date):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('Asia/Calcutta')
    d = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    d = d.replace(tzinfo=from_zone)
    d = d.astimezone(to_zone)
    d = d.strftime("%b %d, %Y %H:%M")
    return d+' IST'

def buildArticles(articles):
    
    articleSource = ""
    articleTime = ""
    articleImage = ""
    articleURL = ""
    articleTitle = ""
    articleDescription = ""
    newArticleHTML = "" 
    index = 0
    
    articleHTML = """		<div class="card mb-3" style="max-width: 2000px;">
                    		  <div class="row no-gutters">
                    			<div class="col-md-4#pos1#">
                    			<img src="#ArticleimgSrc#" alt="Article Image" height="250" width="100%" style="border-style:outset ;border-radius:0.45rem">
                    			</div>
                    			<div class="col-md-8#pos2#">
                    			  <div class="card-body">
                    				<p class="card-text"><small class="text-muted">#ArticleSource_Time#  </small></p>
                    				<h5 class="card-title"><a href="#ArticleURL#" target="_blank" rel="noopener noreferrer" class="stretched-link" style="color:black;">#ArticleTitle# </a></h5>
                    				<p class="card-text">#ArticleDescription#<a href="#ArticleURL#" target="_blank" rel="noopener noreferrer" class="stretched-link"> [See more...]</a></p>
                    			  </div>
                    			</div>
                            </div>
                         </div>
            
            """
    
    for article in articles:
        try:
            
            articleSource = article['source']['name']
            articleTime = tzToIST(article['publishedAt'])
            articleImage = article['urlToImage']
            articleURL = article['url']
            articleTitle = article['title']
            articleDescription = article['description']
            tempHTML = articleHTML
            tempHTML = tempHTML.replace("#ArticleimgSrc#", articleImage)
            tempHTML = tempHTML.replace("#ArticleSource_Time#", articleSource+' · '+ articleTime)
            tempHTML = tempHTML.replace("#ArticleURL#", articleURL)
            tempHTML = tempHTML.replace("#ArticleTitle#", articleTitle)
            tempHTML = tempHTML.replace("#ArticleDescription#", articleDescription)
            index= index+1
            if index%2 == 0:
                tempHTML = tempHTML.replace("#pos1#", " order-md-2")
                tempHTML = tempHTML.replace("#pos2#", " order-md-1")
            else:
                tempHTML = tempHTML.replace("#pos1#", "")
                tempHTML = tempHTML.replace("#pos2#", "") 
                
            
            
            newArticleHTML = newArticleHTML + tempHTML
        except:
            continue
        
    return newArticleHTML

currentTime = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
lastRefresh = currentTime.strftime("%H:%M") + ' IST'
nextRefresh = (currentTime + datetime.timedelta(minutes = 15)).strftime("%H:%M") + ' IST'


indiaHeadline = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Headlines</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Headlines</h5>
			<p><a class="btn btn-secondary" href="worldheadlines.html" role="button">View details »</a></p>
          </div>"""

worldHeadline = """
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Headlines</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
		  <div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Headlines</h5>
			<p><a class="btn btn-secondary" href="index.html" role="button">View details »</a></p>
          </div>"""

covidIndia = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/covid.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Covid India Dashboard</h5>
			<p><a class="btn btn-secondary" href="http://covid19india.org" role="button" target="_blank">View details »</a></p>
          </div>
<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Covid India</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Covid World</h5>
			<p><a class="btn btn-secondary" href="worldcovid.html" role="button">View details »</a></p>
          </div>
           """

covidWorld = """ <div class="col-lg-4">
            <img class="rounded-circle" src="./images/covid.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Covid India Dashboard</h5>
			<p><a class="btn btn-secondary" href="http://covid19india.org" role="button" target="_blank">View details »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Covid World</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          
		  <div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Covid India</h5>
			<p><a class="btn btn-secondary" href="covid.html" role="button" role="button">View details »</a></p>
          </div>"""
          
businessIndia = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Business</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Business</h5>
			<p><a class="btn btn-secondary" href="worldbusiness.html" role="button">View details »</a></p>
          </div>"""
businessWorld = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Businiess</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
	<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Businiess</h5>
			<p><a class="btn btn-secondary" href="business.html" role="button">View details »</a></p>
          </div>
          """

entertainmentIndia = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Entertainment</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Entertainment</h5>
			<p><a class="btn btn-secondary" href="worldentertainment.html" role="button">View details »</a></p>
          </div>"""
entertainmentWorld = """ <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Entertainment</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
			<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Entertainment</h5>
			<p><a class="btn btn-secondary" href="entertainment.html" role="button">View details »</a></p>
          </div>
         """
          
science = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/science.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Science</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/health.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Health</h5>
			<p><a class="btn btn-secondary" href="health.html" role="button">View details »</a></p>
          </div>
           <div class="col-lg-4">
            <img class="rounded-circle" src="./images/technology.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Technology</h5>
			<p><a class="btn btn-secondary" href="technology.html" role="button" >View details »</a></p>
          </div>"""
health = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/science.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Science</h5>
			<p><a class="btn btn-secondary" href="science.html" role="button" role="button">View details »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/health.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Health</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
           <div class="col-lg-4">
            <img class="rounded-circle" src="./images/technology.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Technology</h5>
			<p><a class="btn btn-secondary" href="technology.html" role="button" >View details »</a></p>
          </div>"""
technology = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/science.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Science</h5>
			<p><a class="btn btn-secondary" href="science.html" role="button" role="button">View details »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/health.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Health</h5>
			<p><a class="btn btn-secondary" href="health.html" role="button">View details »</a></p>
          </div>
           <div class="col-lg-4">
            <img class="rounded-circle" src="./images/technology.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Technology</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>"""
          
sportsIndia = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Sports</h5>
			<p><a class="btn btn-secondary" href="sports.html" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Sports</h5>
			<p><a class="btn btn-secondary" href="worldsports.html" role="button">View details »</a></p>
          </div>
           <div class="col-lg-4">
            <img class="rounded-circle" src="./images/cricket.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Cricket</h5>
			<p><a class="btn btn-secondary" href="cricket.html" role="button" >View details »</a></p>
          </div>"""
sportsWorld = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Sports</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Sports</h5>
			<p><a class="btn btn-secondary" href="sports.html" role="button" role="button">View details »</a></p>
          </div>
          
           <div class="col-lg-4">
            <img class="rounded-circle" src="./images/cricket.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Cricket</h5>
			<p><a class="btn btn-secondary" href="cricket.html" role="button" >View details »</a></p>
          </div>"""
sportsCricket = """<div class="col-lg-4">
            <img class="rounded-circle" src="./images/cricket.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">Cricket</h5>
			<p><a class="btn btn-secondary" href="#" role="button" style="background-color:green;">Scroll down »</a></p>
          </div>
		<div class="col-lg-4">
            <img class="rounded-circle" src="./images/india-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">India Sports</h5>
			<p><a class="btn btn-secondary" href="sports.html" role="button" role="button">View details »</a></p>
          </div>
          <div class="col-lg-4">
            <img class="rounded-circle" src="./images/world-news.gif" alt="Generic placeholder image" width="100" height="100">
            <h5 style="color:black;">World Sports</h5>
			<p><a class="btn btn-secondary" href="worldsports.html" role="button">View details »</a></p>
          </div>
           """
