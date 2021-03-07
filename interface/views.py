from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json


# Create your views here.


def indexPage(request):
	
	dat = pd.read_excel('C:/Users/xxaa/Documents/DS1Large.xlsx')
	dat = dat.astype(float, errors ='ignore')
	dataSet = dat[['Country','Population']].replace('..', np.nan).dropna()
	dataSet1 = dat[['Population','Area']].replace('..',np.nan).dropna()
	
	varA = dataSet.Country.tolist()
	varB = dataSet.Population.tolist()
	
	varC = dataSet1.Population.tolist()
	varD = dataSet1.Area.tolist()

	aa = np.array([varC]).mean()
	ab = np.array([varD]).mean()


	context = {'varA':varA, 'varB':varB, 'varC':varC, 'varD':varD, 'aa':aa,'ab':ab}
	return render(request, 'index.html', context)





def testPage(request):


	data = pd.read_excel('C:/Users/xxaa/Documents/DS1Large.xlsx')
	data = data.astype(float, errors ='ignore')
	dataSet3 = data[['Population','Area']].replace('..',np.nan).dropna()
	dataSet2 = data[['Country','Population','Area']].replace('..',np.nan).dropna()

	V1 = dataSet2.Country.tolist()
	V2 = dataSet2.Population.tolist()
	V3 = dataSet3.Area.tolist()
	V4 = dataSet3.Population.tolist()

	aa = np.array([V2]).mean()
	

	s = pd.Series([1, 2, 3])
	fig, ax = plt.subplots()
	s.plot.bar()
	fig.savefig('my_plot.png')

	pls = [['xx','yy']]
	for i in range(0, len(V2)):
		pls.append([V3[i],V2[i]])

	content = {'pls': pls, 'V1':V1, 'V2':V2, 'aa':aa}
	return render(request, 'test.html', content)


def basePage(request):
	data = pd.read_excel('C:/Users/xxaa/Documents/DS1Large.xlsx')
	data = data.astype(float, errors ='ignore')
	dataSet2 = data[['Country','Population']].replace('..',np.nan).dropna()

	V1 = dataSet2.Country.tolist()
	V2 = dataSet2.Population.tolist()

	pls =[]
	for i in range(0, len(V1)):
		pls.append([V1[i],V2[i]])

	consent = {'pls': pls, 'V1':V1, 'V2':V2}
	return render(request,'base.html', consent)

def chartPage(request):
	#data = pd.read_excel('C:/Users/xxaa/Documents/DS1Large.xlsx')
	#data = data.astype(float, errors ='ignore')
	#data = data[['Country','Population']].replace('..',np.nan).dropna()
	#x = data.Country
	#y = data.Population
	
	#data.to_csv('dataset11.csv')
	#data = pd.read_csv('dataset11.csv')
	x = ['British','Indian','German','Chinese']
	y = [5,6,3,4]
	#convent = {'data' : data, 'x': xy, 'y' : yx }
	return render(request,'chart.html', {'x': x , 'y': y})
