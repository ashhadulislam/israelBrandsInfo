import requests
from bs4 import BeautifulSoup
import json
import pickle

def scrape_web():

	
	src_link="https://boycott.thewitness.news"
	URL = "https://boycott.thewitness.news/categories"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")

	category_elements = soup.find_all("a", class_="m-e615b15f mantine-Card-root m-1b7284a3 mantine-Paper-root")

	categ_urls=[]
	categ_names=[]
	for categ_elem in category_elements:
	    print(categ_elem)
	    categ_url = categ_elem["href"]
	    if "https:" not in categ_url:
	        print(src_link+categ_url)
	        categ_urls.append(src_link+categ_url)
	        categ_names.append(categ_url.split('/')[-1])
	    

	dic_data={}
	for i in range(len(categ_urls)):
	    categ_url=categ_urls[i]
	    categ_name=categ_names[i]
	    print(categ_name)
	    dic_data[categ_name]={}
	    page = requests.get(categ_url)
	    soup = BeautifulSoup(page.content, "html.parser")
	    dic_data[categ_name]["logo_urls"]=[]    
	    dic_data[categ_name]["names"]=[]
	    dic_data[categ_name]["why_urls"]=[]   
	    divs_interest=soup.find_all("div", class_="m-e615b15f mantine-Card-root m-1b7284a3 mantine-Paper-root")
	    
	    
	    for div_interest in divs_interest:
	        # get logo link
	        logo_link=div_interest.find_all("img",class_="m-11f8ac07 mantine-Avatar-image")
	#         print(logo_link[0]["src"])
	        dic_data[categ_name]["logo_urls"].append(logo_link[0]["src"])
	        
	        # get company Name
	        company_name=div_interest.find_all("p",class_="mantine-focus-auto m-b6d8b162 mantine-Text-root")[0].text
	#         print(company_name)
	        dic_data[categ_name]["names"].append(company_name)
	        
	        
	        # get why url
	        why_url=div_interest.find_all("a",class_="mantine-focus-auto mantine-active m-77c9d27d mantine-Button-root m-87cf2631 mantine-UnstyledButton-root")[0]['href']
	        dic_data[categ_name]["why_urls"].append(src_link+why_url)
	    
	    
	    
	    
	dic_companywise={}

	for category in dic_data:
	    print(category)
	    names=dic_data[category]["names"]
	    logo_urls=dic_data[category]["logo_urls"]
	    why_urls=dic_data[category]["why_urls"]    
	    for i in range(len(names)):
	        name=names[i]
	        why_url=why_urls[i]
	        dic_companywise[name]={}
	        page = requests.get(why_url)
	        soup = BeautifulSoup(page.content, "html.parser")
	        scripts = soup.find_all('script')
	        desc_object = json.loads(scripts[-1].contents[0])
	        dic_companywise[name]['description']=desc_object['props']['pageProps']['listing']['description']
	        dic_companywise[name]['reason']=desc_object['props']['pageProps']['listing']['reason']
	        dic_companywise[name]['howToBoycott']=" ".join(desc_object['props']['pageProps']['listing']['howToBoycott'])
	        dic_companywise[name]['alternatives']=" ".join(desc_object['props']['pageProps']['listing']['alternatives'])
	        dic_companywise[name]['source']=desc_object['props']['pageProps']['listing']['source']
	        dic_companywise[name]['logo']=desc_object['props']['pageProps']['listing']['logo']
	        



	   
	filehandler = open("dic_data.obj","wb")
	pickle.dump(dic_data,filehandler)
	filehandler.close()



	filehandler = open("dic_companywise.obj","wb")
	pickle.dump(dic_companywise,filehandler)
	filehandler.close()

