#    A simple command-line tool to download manga.
#    Copyright (C) 2017  Eren Kibar
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

import os
import sys
import pwd
import urllib.request
import argparse

from bs4 import BeautifulSoup as BS
import requests

def main():
    
    cur_dir = os.getcwd()
    parser = argparse.ArgumentParser(description="This is a command line tool" 
                                                    "for downloading manga.")
    parser.add_argument('-m' , '--manga', 
                        type=str, 
                        required=True)
    parser.add_argument('-p' , '--path', 
                        type=str, 
                        default=cur_dir, 
                        help="Default path is the current working directory")
    parser.add_argument('-fc', '--firstchapter',
                        type=int,
                        required=True,
                        help='First chapter to download')
    parser.add_argument('-lc', '--lastchapter',
                        required=True,
                        type=int,
                        help='Last chapter to download')         
    args = parser.parse_args()
    if(args.firstchapter > args.lastchapter):
        print("First chapter cannot be greater than last chapter")
        sys.exit(0)
    download_range(args.manga,args.firstchapter,args.lastchapter,args.path)

def download_range(manganame,fchap,lchap,path): 
    #downloading and saving into proper folders
    for c in range(fchap,lchap+1):
    #Creating a folder for each chapter 
        url = 'http://www.mangapanda.com/' + manganame + '/' + str(c) + '/'
        source = BS(urllib.request.urlopen(url),'html.parser')
        page_number = len(source.findAll('option'))
        full_path = path + '/' + manganame + '/' + "Chapter"+ str(c);
        if not os.path.exists(full_path):
            os.makedirs(full_path,exist_ok=True)
        os.chdir(full_path)
        print("Downloading chapter " + str(c) )
        for i in range(1,page_number+1): 
            #This is for getting the image link from the mangas page
            url = 'http://www.mangapanda.com/' + manganame  + '/' + str(c) + '/' +str(i)
            source = BS(urllib.request.urlopen(url).read(),'html.parser')
            jpg = source.find('img')
            image = jpg['src']
            #It ends here
            #Saving the image file
            req = requests.get(image)
            file = open(str(i),'wb')
            for chunk in req.iter_content(100000):
                file.write(chunk)
            file.close()

main()
