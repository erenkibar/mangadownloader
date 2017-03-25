#    A simple command-line to download manga.
#    Copyright (C) <year>  <name of author>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.



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


        


