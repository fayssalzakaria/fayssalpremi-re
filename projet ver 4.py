import urllib.request

from bs4 import BeautifulSoup

import requests

import os
def scrapimage(lien,dossier):
    try:
        os.mkdir(os.path.join(os.getcwd(), dossier))
    #creer le dossier
    except:

        pass
    os.chdir(os.path.join(os.getcwd(),dossier))

    requ=requests.get(lien)

    soup=BeautifulSoup(requ.text,'html.parser')

    images = soup.find_all('img')

  #cherche les balise contenant ds image
    print(images)

    for image in images:
#parcours les balise img pour afficher que les lien et le nom des image
       lien=image['src']

       nom=image['alt']

       print(lien,nom)

       with open(nom+'.jpg','wb')as f:

        #creation d'un dossier contenant les image receuilli
            im=requests.get(lien)
            f.write(im.content)
scrapimage('https://www.myheroacademiascan.fr/manga/my-hero-academia-scan-343-vf/','mhascan')
