# Manga Downloader

This is a very simple command-line tool for downloading manga written in Python. This is the first properly working version. A lot of features to be included in the next commits.
## To Do

*   MangaHere support
*   CBR archive support
* ✔ Support for downloading a range of chapters instead of only one.
* ✔ Better exception handling
* ✔ Better directory handling


## Getting Started
Just clone the repository to get started.
````
git clone http://github.com/erenkibar/mangadownloader.git
````
### Dependencies
	Python 3
	BeautifulSoup
	Requests

#### On Arch Linux 
```
sudo pacman -S python-beautifulsoup4 python-requests
```

#### On Debian/Ubuntu/Ubuntu-based distros(e.g Linux Mint)
```
sudo apt-get install python3-bs4 python3-requests
```
## Usage
You can start the program with:

````
python mangadownloader.py
````

````
usage: mangadownloader.py [-h] -m MANGA [-p PATH] -fc FIRSTCHAPTER -lc LASTCHAPTER

This is a command line toolfor downloading manga.

optional arguments:
  -h, --help            show this help message and exit
  -m MANGA, --manga MANGA
  -p PATH, --path PATH  Default path is the current working directory
  -fc FIRSTCHAPTER, --firstchapter FIRSTCHAPTER
                        First chapter to download
  -lc LASTCHAPTER, --lastchapter LASTCHAPTER
                        Last chapter to download
````
````
python mangadownloader.py -m fairy-tail -fc 8 -lc 10
````
The above example will download chapters between 8 and 10 of Fairy Tail.
If you want to download only one chapter pass the same value to -fc and -lc.
While passing the mange name it is important to use "-" instead of spaces.
The program itself creates the directory for manga and chapters. Path is current working directory unless specified with the argument --path.
## Authors

* **Eren Kibar** - *Initial work* - [erenkibar](https://github.com/erenkibar)


## License

This project is licensed under GPLv3 - see the [LICENSE](LICENSE) file for details
