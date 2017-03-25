#!/usr/bin/env python

import os, pwd
import urllib.request,html.parser
from urllib.error import URLError
from bs4 import BeautifulSoup as BS
import requests,argparse

def main():
    cur_dir = os.getcwd()
    parser = argparse.ArgumentParser(description="This is a command line tool for downloading manga.")
    parser.add_argument('-m' , '--manga', type=str, required=True)
    parser.add_argument('-p' , '--path', type=str, default='cur_dir', help="Default path is the current working directory")
    parser.add_argument('-c' , '--chapter', type=str, required=True, help="Enter the chapter you want to download")
    args = parser.parse_args()
    download(args.manga,args.chapter,args.path)

def download(manganame,ch,path):
    url = 'http://www.mangapanda.com/' + manganame + '/' + ch + "/"
    source = BS(urllib.request.urlopen(url),"html.parser")
    page_number = len(source.findAll("option"))
    for i in range(1,page_number+1):
        #This is for getting the image link from the mangas page 
        url = 'http://www.mangapanda.com/' + manganame + '/' + ch + "/" + str(i)
        source = BS(urllib.request.urlopen(url).read(),"html.parser")
        jpg = source.find("img")
        image = jpg["src"]
        #It ends here 
        #Using requests i save the image file using a proper header which the server accepts 
        req = requests.get(image)
        file = open(str(ch) + str(i),'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()

main()


        


