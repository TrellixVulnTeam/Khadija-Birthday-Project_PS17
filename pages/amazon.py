import streamlit as st
import requests
from bs4 import BeautifulSoup
import smtplib
import time
def app():
	#################################################
	#Streamlit Design
	st.title('Amazon')
	st.write('Enter a Amazon URL and choose your chosen price to be notified at')
	chk_url = 'https://www.amazon.in/Moroccanoil-Hydrating-Shampoo-8-5-Oz/dp/B0098QPV3I/ref=sr_1_2_sspa?dchild=1&keywords=morrocan+oil&qid=1628269421&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExWE9VQUVaRkEzWUdQJmVuY3J5cHRlZElkPUEwNDEyOTU2V0RBOThIT0U4WU4zJmVuY3J5cHRlZEFkSWQ9QTA2MzQ4MTYxOEJNNFc0SVJERzhVJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
	chk_url = st.text_input("Enter Amazon URL", chk_url)
	chk_price= st.number_input("Enter the desired check price")

	notify = st.button("Notify")
	###########################################
	#ML Backend

	def get_price(chk_url, headers):
		page = requests.get(chk_url, headers = headers)
		# chk_price = int(input("Enter the desired check price"))
		soup = BeautifulSoup(page.content, 'html.parser')

		title = soup.find(id='title_feature_div').get_text().strip()

		price = soup.find(id='priceblock_ourprice').get_text()
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
		body = (f'Go to this link -{chk_url}')
		msg = f"Subject: {subject}\n\n{body}"
		# msg = str(msg)
		print(msg)
		server.sendmail('khadijascloset18@gmail.com','khadijabandukwala4@gmail.com',msg)
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