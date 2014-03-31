from BeautifulSoup import BeautifulSoup
import urllib2
import os
    
def main():
    url = raw_input("Enter link url: ")
    folderName = raw_input("Enter Folder Name: ")
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
    soup = BeautifulSoup(html)
    image =  ""
    imageCollection = []
    
    os.makedirs(folderName)
    folder = folderName + "/"
    while image != soup.find(id="mh").find("img").get("src"):
        image = soup.find(id="mh").find("img").get("src")
        imageCollection.append(image)
        pageRelativePath = soup.findAll(id="mhona")[-1].get("href")
        fullPath = url + pageRelativePath
        response = urllib2.urlopen(fullPath)
        html = response.read()
        response.close()
        soup = BeautifulSoup(html)

    for imageLink in imageCollection:
        img = urllib2.urlopen(imageLink)
        imageTitle = imageLink.split("/")[-1]
        localFile = open(folder + imageTitle, 'wb')
        localFile.write(img.read())
        localFile.close()
    
if __name__ == "__main__":
	main()
