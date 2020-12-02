from twilio.rest import Client 

account_sid = 'AC41a4a2878aee184a1ab8822fe8c6c501' 
auth_token = '6665969e8ef75a6c2560046e16d995de' 
client = Client(account_sid, auth_token) 

def send_chat():
    message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='Halo Bro. Aku test bot xixixi🤣🤣🤣',      
        # to='whatsapp:+628973461646' 
        to='whatsapp:+6285156566164' 
    ) 

    print(message.sid)