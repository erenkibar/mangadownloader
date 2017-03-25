# Manga Downloader

This is a very simple command-line tool for downloading manga. This is the first properly working version. A lot of features to be included in the next commits.

## Getting Started

Manga Downloader is written in Python. 
Just fetch the repository to get started.
### Dependencies
	Python 3
	BeautifulSoup
	Requests

#### On Arch Linux 
```
sudo pacman -S python-beautifulsoup4 python-requests
```
#### On Ubuntu
```
sudo apt-get install python-beautifulsoup python-requests
```
## Usage
You can start the program with:

````
python mangadownloader.py
````

````
manga [-h] -m MANGA [-p PATH] -c CHAPTER

optional arguments:
  -h, --help            show this help message and exit
  -m MANGA, --manga MANGA
  -p PATH, --path PATH
  -c CHAPTER, --chapter CHAPTER
                        Enter the chapter you want to download

````
## Authors

* **Eren Kibar** - *Initial work* - [erenkibar](https://github.com/erenkibar)


## License

This project is licensed under GPLv3 - see the [LICENSE.md](LICENSE.md) file for details
## To Do

* Support for downloading a range of chapters instead of only one.
* Better exception handling
* Better directory handling 
