# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://am23mylcusd-signease-signease-8apqso.streamlit.app/#welcome-to-streamlit"
  
# Generate QR code
url = pyqrcode.create(s)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)
