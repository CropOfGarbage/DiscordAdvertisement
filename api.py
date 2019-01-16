import requests
import time
import json
import sys
sys.tracebacklimit = 0
url = 'https://discordapp.com/api/v6/'
def warn(text):
    print('\033[93m' + '[WARN] ' + text + '\033[0m')
def success(text):
    print('\033[92m' + '[DONE] ' + text + '\033[0m')
def error(text):
    print('\033[91m' + '[ERROR] ' + text + '\033[0m')


def getme(token, retur=0,debug=0):
          headers = {'Authorization':token,
                     'Content-Type':'application/json'}
          get_request = requests.get(url+'users/@me', headers=headers)
          success('GETing current user...')
          if get_request.status_code == 401:
             error('Invaild token')
          if get_request.status_code == 200:
             success('Got user')
             if debug == 1:
                warn(get_request.text) 
          else:
             error('Error GETing user')
             error('Status code: ' + str(get_request.status_code))
             error('Response text: ' + get_request.text) 
          if retur == 1:
             return get_request.text

def join_server(token, code): 
          headers = {'Authorization' : token}
          join_request = requests.post(url+'invite/'+code, headers=headers)
          success('Sending join request...')
          if join_request.status_code == 200:
             success('Joined server')
          if join_request.status_code == 401:
             error('Invaild token.')
          else:
             error('Error joining server')
             error('Status code: ' + str(join_request.status_code))
             error('Response text: ' + join_request.text)

def message(token, cid, message):
          getmee = getme(token,1)
          localid = json.dumps(json.loads(getmee)['id'])  
          if localid.strip('"') == localid:
             print('Cannot message to our ID')
             return 

          headers = {'Authorization': token,
                    'Content-Type': 'application/json'
                    }
          
          POST_JSON = json.dumps({'content':message})
          message_request = requests.post(url+'channels/{}/messages'.format(cid),headers=headers,data=POST_JSON)
          success('Sending message...')
          if message_request.status_code == 200:
             success('Message sent')
          else:
              error('Error sending message')
              error('Status code: ' + str(message_request.status_code))
              error('Response text: ' + message_request.text)


def create_DM(token, id, retur=0):
          ourID = getme(token,1)
          jload = json.loads(ourID)
          ouruserid = json.dumps(jload['id'])
          if ouruserid.strip('"') == id:
             print('Cannot create DM with local user')
             return
         
          headers = {'Authorization':token,
                    'Content-Type':'application/json'}
          POST_JSON = json.dumps( {'recipient_id':id} )
          post_request = requests.post(url+'users/@me/channels',headers=headers,data=POST_JSON)
          if post_request.status_code == 401:
             error('Invaild token')
          if post_request.status_code == 200:
             success('Created DM')
          if retur == 1:
             return post_request.text
            
             
def get_members(token, id, retur=0):
          headers = {'Authorization':token,
             'Content-Type':'application/json'}
          get_request = requests.get(url+'guilds/'+id+'/members'+'?limit=1000',headers=headers)
          success('Sending GET guild members...')
          if get_request.status_code == 401:
             error('Invaild token')
          if get_request.status_code == 200:
             success('Get Members')
          else:
             error('Error GETing members')
             error('Status code: ' + str(get_request.status_code))
             error('Response text: ' + str(post_request.text))
          if retur == 1:
             return get_request.text
def advert(token, msgcontent, guildid):
          success('starting advertisement')
          test = get_members(token, guildid ,1)
          j1 = json.loads(test)
          for i in j1:
              dm = create_DM(token,i['user']['id'], 1)
              json_dm = json.loads(dm)
              print(json_dm)
              message(token,json_dm['id'],msgcontent)
              time.sleep(5)
