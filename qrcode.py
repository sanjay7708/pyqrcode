import pyqrcode
import png
from pyqrcode import QRCode
url=pyqrcode.create("https://www.linkedin.com/in/sanjay-m-493999200/")
url.svg("myqr.png",scale=8)
url.png("myqr.png",scale=6)
