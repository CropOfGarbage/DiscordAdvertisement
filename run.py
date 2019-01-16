import api, json
from random import randint
print('Created by GhostHunter')
print('      For free!')
print('===========================')
print('     Donations')
print('BTC: 1NguzEuZGDXs54PvY92nKhuzZSqNJ6fKWJ')
print('PayPal: message me on V3RM for my PP email')
##################################################
api.warn('The current DM delay is 5s, to avoid ratelimiting')

gid = input('Please enter the GUILDID: ')
msg = input('Please enter the MESSAGE TO SEND: ')

print('token - Enter a token')
print('list - Loop through tokens.json')
choice = input('Mode: ')
if choice == 'token':
   token = input('Enter your token: ')
   api.advert(token, msg, gid)
if choice == 'list':
   try:
      tokenlist = json.loads(open('tokenlist.json').read()) 
      for tokens in tokenlist:
          api.success('adverting with: ' + tokens)
          api.advert(tokens, msg, gid)
          time.sleep(1) 
   except: 
       api.error('fatal error with the method: List')
 
