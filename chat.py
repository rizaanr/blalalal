from twilio.rest import Client 
 
account_sid = 'AC41a4a2878aee184a1ab8822fe8c6c501' 
auth_token = '488b95cb4d2f218d428830213b14b306' 
client = Client(account_sid, auth_token) 
 
def darisana():
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='yogais',      
                                to='whatsapp:+6285156566164' 
                            ) 
 
    print(message.sid)