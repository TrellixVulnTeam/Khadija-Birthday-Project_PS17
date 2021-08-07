import streamlit as st
import requests
from bs4 import BeautifulSoup
import smtplib
import time
def app():
	#################################################
	#Streamlit Design
	st.title('Nykaa')
	st.write('Enter a Nykaa URL and choose your chosen price to be notified at')
	chk_url = 'https://www.nykaa.com/lakme-absolute-matte-revolution-lip-color/p/531129?pps=3&productId=531129&ptype=product&skuId=531113'
	chk_url = st.text_input("Enter Nykaa URL", chk_url)
	chk_price= st.number_input("Enter the desired check price")
	notify = st.button("Notify")
	###########################################
	#ML Backend

	def get_price(chk_url, headers):
		page = requests.get(chk_url, headers = headers)
		# chk_price = int(input("Enter the desired check price"))
		soup = BeautifulSoup(page.content, 'html.parser')

		# title = soup.find(id = 'product-title').get_text().strip()

		price = soup.find('span',{"class": 'post-card__content-price-offer'}).get_text()
		price = float(price[1:len(price)].replace(',',''))

		# print(title)
		print(price)

		if price < chk_price:
			send_mail()
		else:
			pass

	def send_mail():
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()

		server.login('khadijascloset18@gmail.com','Khads@2021')

		subject = "Khadija's Closet: Price of an item you were looking at fell down"
		body = (f'Go to this link - {chk_url}')
		msg = f"Subject: {subject}\n\n{body}"
		# msg = str(msg)
		print(msg)
		server.sendmail('khadijascloset18@gmail.com','ishaanag.x@gmail.com',msg)
		print('Email sent!!!')
		st.write("You have been notified!")
		server.quit()

	headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'}

	x=0
	while x==0:
		get_price(chk_url, headers)
		time.sleep(60)
		x = 1
	###########################################