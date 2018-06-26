import webbrowser
import time
#print("Hello");
#a="Mashilheiba"
#print (a)
url1="http://www.twitter.com"
url2="http://www.github.com"
url3="http://www.apple.com"
i=0
while(i<3):
    time.sleep(10)
    webbrowser.open(url1)
    i=i+1
    time.sleep(9)
    webbrowser.open(url2)
    i=i+1
    time.sleep(8)
    webbrowser.open(url3)
    i=i+1

