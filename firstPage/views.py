from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import math
# Create your views here.

from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin-faaraan:test123@cluster0-fcqod.mongodb.net/retryWrites=true&w=majority")
db = client['ott_movie_tv1']
collectionD = db['ottTable']
# collectionD=pd.read_csv('final_ott_data.csv')


def index(request):
    temp={}
    temp['cylinders']='Inception'

    print(temp['cylinders'])

    context={'temp':temp}
    return render(request,'index.html',context)


def rel(request):
    if request.method == 'POST':
        temp={}
        temp['cylinders']=request.POST.get('cylinderVal')
        val=temp['cylinders']
        temp['cylinders']=temp['cylinders'].upper()
        temp['cylinders']=temp['cylinders'].replace(' ', '')

    countOfrow=collectionD.find_one({'title1':temp['cylinders']},{'Title':1,"Netflix":1,'Hulu':1,'Prime Video':1,'Disney+':1,'IMDb':1,'Directors':1,'Year':1,
    'Runtime':1,'Age':1,'_id':0,'zee5':1,'link':1,'Type':1})

    print("ye error hai",countOfrow)
    if countOfrow==None:
        title= "This movie  is not available on any of the OTT platforms that we support or please check if the spelling is wrong."
        error=1
        context={'title':title,'temp':temp['cylinders'],'error':error,'val':val}
        return render(request,'rel.html',context)

    title=countOfrow['Title']
    netflix=countOfrow['Netflix']
    hulu=countOfrow['Hulu']
    prime_video=countOfrow['Prime Video']
    disney=countOfrow['Disney+']
    zee5=countOfrow['zee5']
    imdb=countOfrow['IMDb']
    link=countOfrow['link']
    Type=countOfrow['Type']

    #
    # if netflix==1:
    #     def getMovies(title):
    #         axios.get("http://api.tvmaze.com/singlesearch/shows?q="+ title)
    #         .then((response) => {
    #           console.log(response);
    #           let movies = response.data;
    #            link=movies.officialSite
    #             $('#movies').html(output);
    #           })
    #           .catch((err) => {
    #             console.log(err);
    #           });
    #


    #director
    dir=str(countOfrow['Directors'])
    if dir=='nan':
        director='Not Availabel !'
    else:
        director=countOfrow['Directors']
    #year
    year=countOfrow['Year']

    #runtime
    # if math.isnan(countOfrow['Runtime']):
    #     runtime='Not Availabel !'
    # else:
    runtime=countOfrow['Runtime']
        # runtime=str(runtime)+' mins'
    #age
    age=countOfrow['Age']


    context={'title':title,'netflix':netflix,'hulu':hulu,'prime_video':prime_video,'disney':disney,'imdb':imdb,
    'director':director,'year':int(year),'runtime':runtime,
    'age':age,'temp':temp['cylinders'],'val':val,'link':link,'zee5':zee5,'Type':Type}

    return render(request,'rel.html',context)


def viewDatabase(request):
    countOfrow=collectionD.find().count()
    context={'countOfrow':countOfrow}
    return render(request,'viewDB.html',context)
