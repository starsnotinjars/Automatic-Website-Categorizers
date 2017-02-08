# -*- coding: utf-8 -*-
import re
import sys


pin1 = open('output.txt','r')
lines1 = pin1.readlines();

pin2 = open('ads2.txt','r')
lines2 = pin2.readlines();
keys_ads=[]
for line in lines2:
	values2 = re.split(',', line);
	#print (values2)
	for i in range(0,len(values2)):
		word=list(values2[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values2[i]=''.join(word)
		keys_ads.append(values2[i])
# print (keys_ads)

pin3 = open('commerce2.txt','r')
lines3 = pin3.readlines();
keys_commerce=[]
for line in lines3:
	values3 = re.split(',', line);
	#print (values3)
	for i in range(0,len(values3)):
		word=list(values3[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values3[i]=''.join(word)
		keys_commerce.append(values3[i])

pin4 = open('search2.txt','r')
lines4 = pin4.readlines();
keys_search=[]
for line in lines4:
	values4 = re.split(',', line);
	#print (values4)
	for i in range(0,len(values4)):
		word=list(values4[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values4[i]=''.join(word)
		keys_search.append(values4[i])

pin5 = open('adult2.txt','r')
lines5 = pin5.readlines();
keys_adult=[]
for line in lines5:
	values5 = re.split(',', line);
	#print (values5)
	for i in range(0,len(values5)):
		word=list(values5[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values5[i]=''.join(word)
		keys_adult.append(values5[i])

pin6 = open('news2.txt','r')
lines6 = pin6.readlines();
keys_news=[]
for line in lines6:
	values6 = re.split(',', line);
	#print (values6)
	for i in range(0,len(values6)):
		word=list(values6[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values6[i]=''.join(word)
		keys_news.append(values6[i])

pin7 = open('service2.txt','r')
lines7 = pin7.readlines();
keys_service=[]
for line in lines7:
	values7 = re.split(',', line);
	#print (values7)
	for i in range(0,len(values7)):
		word=list(values7[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values7[i]=''.join(word)
		keys_service.append(values7[i])

pin8 = open('platform2.txt','r')
lines8 = pin8.readlines();
keys_platform=[]
for line in lines8:
	values8 = re.split(',', line);
	#print (values8)
	for i in range(0,len(values8)):
		word=list(values8[i])
		if word[len(word)-1]=='$':
			word[len(word)-1]=','
			values8[i]=''.join(word)
		keys_platform.append(values8[i])

counts_ads=[]

counts_commerce=[]

counts_search=[]

counts_adult=[]

counts_news=[]

counts_service=[]

counts_platform=[]

for z in range(0, len(keys_ads)):

			counts_ads.append(0)

for z in range(0, len(keys_commerce)):

			counts_commerce.append(0)

for z in range(0, len(keys_search)):

			counts_search.append(0)

for z in range(0, len(keys_adult)):

			counts_adult.append(0)

for z in range(0, len(keys_news)):

			counts_news.append(0)

for z in range(0, len(keys_service)):

			counts_service.append(0)

for z in range(0, len(keys_platform)):

			counts_platform.append(0)

count=0
on=0
on2=0
temp=[]

target = open('output_from_search3.txt', 'w')

for line in lines1:

	values1 = re.split('\s+', line);
#	print (values1)

	if values1[1]=="'query':":

		target.write(str(values1[2]))

		on=1
		count=0

	if on==1 and values1[1]=="'snippet':":

		on=2

	if on==2:

		for i in range(0, len(values1)):

			if values1[i]=="'title':":

				#print ("Temp",temp)
				nothing=1
###############

				for j in range(0, len(keys_ads)):

					for k in range(0, len(temp)):

						if temp[k]==keys_ads[j]:

							counts_ads[j]=counts_ads[j]+1
							target.write(' Ads ')
							nothing=0


###############

###############

				for j in range(0, len(keys_commerce)):

					for k in range(0, len(temp)):

						if temp[k]==keys_commerce[j]:

							counts_commerce[j]=counts_commerce[j]+1
							target.write(' Commerce ')
							nothing=0



###############

###############

				for j in range(0, len(keys_search)):

					for k in range(0, len(temp)):

						if temp[k]==keys_search[j]:

							counts_search[j]=counts_search[j]+1
							target.write(' Search ')
							nothing=0



###############

###############

				for j in range(0, len(keys_adult)):

					for k in range(0, len(temp)):

						if temp[k]==keys_adult[j]:

							counts_adult[j]=counts_adult[j]+1
							target.write(' Adult ')
							nothing=0



###############

###############

				for j in range(0, len(keys_news)):

					for k in range(0, len(temp)):

						if temp[k]==keys_news[j]:

							counts_news[j]=counts_news[j]+1
							target.write(' News')
							nothing=0



###############

###############

				for j in range(0, len(keys_service)):

					for k in range(0, len(temp)):

						if temp[k]==keys_service[j]:

							counts_service[j]=counts_service[j]+1
							target.write(' Service')
							nothing=0



###############

###############

				for j in range(0, len(keys_platform)):

					for k in range(0, len(temp)):

						if temp[k]==keys_platform[j]:

							counts_platform[j]=counts_platform[j]+1
							target.write(' Platform')
							nothing=0

				if nothing==1:
					target.write(' Nothing')

###############
				target.write("\n")
				on=0
				on2=0
				temp=[]
				break;

			if values1[i]!="'title':":

				# print (values1[i])
				temp.append(values1[i])

###############



###########################################################








