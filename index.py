import requests,os
import subprocess
from colorama import init,Fore,Style
import sys

init(autoreset=True)

class Migracion():
    id_sect = []
    x = 0
    chaves = []
    conteudo = []

    def __init__(self, id):     
        for i in id:
            self.id_sect.append(i)
            

            if self.x == 7 or self.x == 11 or self.x == 15 or self.x == 19:
                self.id_sect.append('-')
            self.x += 1

        self.id_final = ''.join(self.id_sect)
        #print(self.id_final)


    def request(self,id):
        self.url = 'https://www.notion.so/api/v3/loadCachedPageChunk'
        self.headers = {
            "accept": '*/*',
            "accept-language": 'pt;q=0.7',
            "content-type": 'application/json',
            'cookie': 'device_id=ebb8da8e-2ed6-4761-973b-90620c5e8414; notion_experiment_device_id=aed34408-4b00-47d4-a07a-79abd5649901; token_v2=v02%3Auser_token_or_cookies%3Ak8oBmSGaGcwGOP7C6ul7VQ65k-39W3MgBsaaGLQ2m9xqLcbuONKjn0MXfOiB7qllTU1J_ZrnDsmVz8fBm9QdKrkjlKYLN7tJdZjqJ3NdwPeXF25d8SxSgqn82zZPJTDWXqE3; notion_user_id=be696b5b-aac1-47ee-aee6-4bbf0059894c; NEXT_LOCALE=en-US; notion_users=[%22be696b5b-aac1-47ee-aee6-4bbf0059894c%22]; notion_check_cookie_consent=false; _cfuvid=LEVwAc_6FkHNEWBsulE5wdUe99.56QM3ggIAmoMLV9Q-1716651513431-0.0.1.1-604800000; notion_cookie_consent={%22id%22:%2282a41727-b652-4011-a0a4-13a4499c039a%22%2C%22permission%22:{%22necessary%22:true%2C%22preference%22:true%2C%22performance%22:false%2C%22targeting%22:false}%2C%22policy_version%22:%22v8%22}; notion_check_cookie_consent=true; __cf_bm=L3THcl6Q3zQ4idy08Z338GLDSGFryKIadrxChAuhTAs-1716654337-1.0.1.1-QCerdO2v5KbQz4rqzlHOkYOeR7IAyx11FPZnk7SSaf5PV36.UKGGgmVnPL2ng_S6PKmnV5Z4vynnCliAzH._cQ; notion_locale=en-US%2Fuser_choice',
            'notion-audit-log-platform': 'web',
            'notion-client-version': '23.13.0.242',
            'origin': 'https://www.notion.so',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Linux",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'x-notion-active-user-header': 'be696b5b-aac1-47ee-aee6-4bbf0059894c',
        }
        self.data = {
            "page": {"id": f"{id}"},
            "limit": int(sys.argv[2]),
            
            "chunkNumber": 0,
            "verticalColumns": False
        }
        
        self.req = requests.post(self.url, headers=self.headers, json=self.data).json()
    
        #print(self.req)
    def pull_keys(self):
        if 'recordMap' in self.req and 'block' in self.req['recordMap']:
            for key, value in self.req['recordMap']['block'].items():
            #print(f"ID: {key}, Data: {value}")
                self.chaves.append(f'{key}')
        else:
            print("Dados não encontrados na resposta.")


    def img_dw(self,source, id,name,newn):
        sourcef = source.replace('/', '%2F').replace(':', '%3A')
        newn = newn.replace('/', '-')
        #url = f'https://www.notion.so/signed/{sourcef}?table=block&id={id}&spaceId=2229cc5c-3568-44f8-b4cd-320e30c97a05&name{name}&download=true&userId=be696b5b-aac1-47ee-aee6-4bbf0059894c&cache=v2'
        #print(name)
        try:
            req2 = subprocess.check_output(f"""
                curl -s 'https://www.notion.so/signed/{sourcef}?table=block&id={id}&spaceId=2229cc5c-3568-44f8-b4cd-320e30c97a05&name={name}&download=true&userId=be696b5b-aac1-47ee-aee6-4bbf0059894c&cache=v2' \
                    -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8' \
                    -H 'accept-language: pt;q=0.6' \
                    -H 'cookie: device_id=ebb8da8e-2ed6-4761-973b-90620c5e8414; notion_experiment_device_id=aed34408-4b00-47d4-a07a-79abd5649901; token_v2=v02%3Auser_token_or_cookies%3Ak8oBmSGaGcwGOP7C6ul7VQ65k-39W3MgBsaaGLQ2m9xqLcbuONKjn0MXfOiB7qllTU1J_ZrnDsmVz8fBm9QdKrkjlKYLN7tJdZjqJ3NdwPeXF25d8SxSgqn82zZPJTDWXqE3; notion_user_id=be696b5b-aac1-47ee-aee6-4bbf0059894c; NEXT_LOCALE=en-US; notion_users=[%22be696b5b-aac1-47ee-aee6-4bbf0059894c%22]; notion_check_cookie_consent=false; _cfuvid=hJ9.LOdH00Z2uRoNqOcy.dcUZ6hPaZuzGbkXqR1diww-1717410207808-0.0.1.1-604800000; notion_check_cookie_consent=true; notion_cookie_consent={{%22id%22:%2282a41727-b652-4011-a0a4-13a4499c039a%22%2C%22permission%22:{{%22necessary%22:true%2C%22preference%22:true%2C%22performance%22:false%2C%22targeting%22:false}}%2C%22policy_version%22:%22v8%22}}; notion_locale=en-US/user_choice; __cf_bm=UvZaNm.WUkPMKVAmMDtWFx4x7E8lZJgvkfIQ3idGZyM-1717440279-1.0.1.1-dTdIcSyMVFFHAiSVc2qr7SOj4r9TxLrk5kn_VK7xjydxl11nKAkHksPO_S_Dq7P0ioZXLt3txq0EhfyiRnRLaw' \
                    -H 'priority: u=0, i' \
                    -H 'sec-ch-ua: "Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
                    -H 'sec-ch-ua-mobile: ?0' \
                    -H 'sec-ch-ua-platform: "Linux"' \
                    -H 'sec-fetch-dest: document' \
                    -H 'sec-fetch-mode: navigate' \
                    -H 'sec-fetch-site: same-origin' \
                    -H 'sec-fetch-user: ?1' \
                    -H 'sec-gpc: 1' \
                    -H 'upgrade-insecure-requests: 1' \
                    -H 'user-agent: "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"'
                """, shell=True)
            
            links = (str(req2[34:397]).replace('&amp', '').replace(';', '&').replace('"', ''))
            link_f = (links[2:394].replace("'", ''))
            #print(link_f)
            #url = 'https://file.notion.so/f/f/2229cc5c-3568-44f8-b4cd-320e30c97a05/d7e06e6e-7a33-43c7-8c2d-d4a04d920e6c/Untitled.png?id=feb69ace-8e8c-4ae1-8223-433d5f823f82&table=block&spaceId=2229cc5c-3568-44f8-b4cd-320e30c97a05&expirationTimestamp=1717718400000&signature=lY1E7ZqTP1lKug5g2Q4sKg4OX-ZFpmvSMiKLyMPu_g8&download=true&downloadName=Untitled.png'

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'pt;q=0.9',
                'cookie': 'file_token=v02%3Afile_token%3A3Z-87Q0BXSoLHwSZFVxTTQIq39D7tA3PkQvkY2igAH7Wn3zCg2oqU5y81Vl61mTZRF2XbUQ2aH1m_He9uwMI8OAqaU_8CBIaN5ezNRG_u0dlz38LpL75Txyu8tNmqE7Yd7F3lt-F-_HAXLkaaJaucaZMXpht; __cf_bm=OZ8AngzlPqlz6jN8q1PoVoLCR8MRjv6.foO70vP7ukc-1718419421-1.0.1.1-xBNhqnEJXlk4U_vKDjj.DbchUU0V08SSHGz9Q1TeS8_f6xTICQDwXcIrSLt_qpzYhQWZaeInHAwO.oU1yzxh_Q; _cfuvid=df1Nnm8oV0cS.jroJRD2406uHy1c3uw6hF5pF9IiiGk-1718419421814-0.0.1.1-604800000; notion_check_cookie_consent=true; notion_cookie_consent={%22id%22:%2282a41727-b652-4011-a0a4-13a4499c039a%22%2C%22permission%22:{%22necessary%22:true%2C%22preference%22:true%2C%22performance%22:false%2C%22targeting%22:false}%2C%22policy_version%22:%22v8%22}',
                'priority': 'u=0, i',
                'referer': 'https://www.notion.so/',
                'sec-ch-ua': '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-site',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            }

            response = requests.get(link_f, headers=headers)
            #print(response.content)
            #print(f'file/{newn}')
            with open(f'files/{newn}', 'wb') as file:
                
                file.write(response.content)
            #print(response.content)
        except:
            pass

        
        
        

    def extract_content(self):
        self.img =0
        self.root_id = self.chaves[0]
        t = ''
        space = []
        
        for k in self.chaves:
            if self.req['recordMap']['block'][k]['value']['value']['type'] == 'external_object_instance':
                self.conteudo.append(['external_object_instance',self.req['recordMap']['block'][k]['value']['value']['format']['uri'] ])

                if self.req['recordMap']['block'][k]['value']['value']['parent_id'] != self.root_id:
                        space.append('  ')
                else:
                    space.append('')
                
            if self.req['recordMap']['block'][k]['value']['value']['type'] == 'divider':
                self.conteudo.append(['divider','\n---'])
            
            
            if 'properties' in self.req['recordMap']['block'][k]['value']['value']:
                if 'source' in self.req['recordMap']['block'][k]['value']['value']['properties']:
                    
                    #print(f'{self.conteudo[0][1][0][0]}{self.img}.png')
                    self.conteudo.append(['Untitled.png',f'{self.conteudo[0][1][0][0]}{self.img}.png'])
                    
                    if '.png' in self.req['recordMap']['block'][k]['value']['value']['properties']['title'][0][0]:
                        self.img_dw(self.req['recordMap']['block'][k]['value']['value']['properties']['source'][0][0],k,self.req['recordMap']['block'][k]['value']['value']['properties']['title'][0][0].replace(' ', '_'),f'{self.conteudo[0][1][0][0]}{self.img}.png')
                    else:
                        self.img_dw(self.req['recordMap']['block'][k]['value']['value']['properties']['source'][0][0],k,self.req['recordMap']['block'][k]['value']['value']['properties']['title'][0][0]+'.png',f'{self.conteudo[0][1][0][0]}{self.img}.png')
                    
                    
                    self.img += 1
                if self.req['recordMap']['block'][k]['value']['value']['type'] == 'bulleted_list':
                    #print([k ,' ',self.req['recordMap']['block'][k]['value']['value']['properties']])
                    self.conteudo.append([self.req['recordMap']['block'][k]['value']['value']['type'], self.req['recordMap']['block'][k]['value']['value']['properties']['title'],self.req['recordMap']['block'][k]['value']['value']['version']])

                    if self.req['recordMap']['block'][k]['value']['value']['parent_id'] != self.root_id:
                        space.append('  ')
                    else:
                        space.append('')
                        
                #if self.req['recordMap']['block'][k]['value']['value']['type'] == 'table':
                    #self.conteudo.append([self.req['recordMap']['block'][k]['value']['value']['type'], 'tabela'])
                else:
            
                    try:
                        self.conteudo.append([self.req['recordMap']['block'][k]['value']['value']['type'], self.req['recordMap']['block'][k]['value']['value']['properties']['title']])
                    except:
                        self.conteudo.append(['table','teste'])
                         
                    if self.req['recordMap']['block'][k]['value']['value']['parent_id'] != self.root_id:
                        space.append('  ')
                    else:
                        space.append('')
    
                    
            
        
        self.file_name = self.conteudo[0][1][0][0]
        self.numt, self.numH, self.numL, self.numc = 0,0,0,0
        #print(len(space))
        s = 0 
        n = 0 # lista numerica 
        abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','v','u','w','x','y','z']
        for i in range(len(self.conteudo)):
            if i >= 3 :
                if s < len(space):
                    if space[s] == '  ':
                        #print(space[s],end='')
                        pass
                    else:
                        pass
                    s += 1
                ## Os Headers
                if self.conteudo[i][0] == 'sub_sub_header':
                    self.numH += 1
                    #print(self.conteudo[i])
                    n = 0
                    print('### ',end='')
                    for li_sub_sub in range(len(self.conteudo[i][1])):
                        tag_close = 0
                        #print(self.conteudo[i][1][li_sub_sub])
                        
                        for l in range(len(self.conteudo[i][1][li_sub_sub])-1,-1,-1):
                            #print(self.conteudo[i][1][li_sub_sub])
                            #print()
                                
                            try:
                                if ['h', 'yellow_background'] in self.conteudo[i][1][li_sub_sub][l]:
                                    #print('a')
                                    print('<mark style="background: #FFF3A3A6;">',end='')
                                    tag_close = 1
                                    
                            except:
                                tag_close = 0
                            try:
                                if ['_'] in (self.conteudo[i][1][li_sub_sub][l]) and ['h', 'yellow_background'] not in self.conteudo[i][1][li_sub_sub][l]:                          
                                    print('<mark style="background: #CACFD9A6;">',end='')
                                    tag_close = 2

                            except:
                                tag_close = 0
                                
                            try:
                                if ['_'] not in (self.conteudo[i][1][li_sub_sub][l]) and ['h', 'yellow_background'] not in self.conteudo[i][1][li_sub_sub][l]:
                                    pass
                            except:
                                if tag_close != 1 and tag_close !=2:
                                    print(self.conteudo[i][1][li_sub_sub][0],end='')
                                    tag_close = 3
                            else:
                                if tag_close == 1:
                                    print(self.conteudo[i][1][li_sub_sub][0],'</mark>',end='')
                                    break
                            
                                if tag_close == 2:
                                    print(self.conteudo[i][1][li_sub_sub][0],'</mark>',end='')
                                    break
                                    
                                if tag_close == 0:
                                    print(self.conteudo[i][1][li_sub_sub][0],end='')
                                    break
                                    
                    print()
                
                if self.conteudo[i][0] == 'sub_header':
                    self.numH += 1
                    n = 0
                    #print(self.conteudo[i])
                    print('## ',end='')
                    for li_sub_sub in range(len(self.conteudo[i][1])):
                        tag_close = 0
                        #print(self.conteudo[i][1][li_sub_sub])
                        
                        for l in range(len(self.conteudo[i][1][li_sub_sub])-1,-1,-1):
                            #print(self.conteudo[i][1][li_sub_sub])
                            #print()
                                
                            try:
                                if ['h', 'yellow_background'] in self.conteudo[i][1][li_sub_sub][l]:
                                    #print('a')
                                    print('<mark style="background: #FFF3A3A6;">',end='')
                                    tag_close = 1
                                    
                            except:
                                tag_close = 0
                            try:
                                if ['_'] in (self.conteudo[i][1][li_sub_sub][l]) and ['h', 'yellow_background'] not in self.conteudo[i][1][li_sub_sub][l]:                          
                                    print('<mark style="background: #CACFD9A6;">',end='')
                                    tag_close = 2

                            except:
                                tag_close = 0
                                
                            try:
                                if ['_'] not in (self.conteudo[i][1][li_sub_sub][l]) and ['h', 'yellow_background'] not in self.conteudo[i][1][li_sub_sub][l]:
                                    pass
                            except:
                                if tag_close != 1 and tag_close !=2:
                                    print(self.conteudo[i][1][li_sub_sub][0],end='')
                                    tag_close = 3
                            else:
                                if tag_close == 1:
                                    print(self.conteudo[i][1][li_sub_sub][0],'</mark>',end='')
                                    break
                            
                                if tag_close == 2:
                                    print(self.conteudo[i][1][li_sub_sub][0],'</mark>',end='')
                                    break
                                    
                                if tag_close == 0:
                                    print(self.conteudo[i][1][li_sub_sub][0],end='')
                                    break
                                    
                    print()
                
                
                if self.conteudo[i][0] == 'header':
                    self.numH += 1
                    n = 0
                    #print(self.conteudo[i])
                    print('# ',end='')
                    for li_sub_sub in range(len(self.conteudo[i][1])):
                        tag_close = 0
                        #print(self.conteudo[i][1][li_sub_sub])
                        
                        for l in range(len(self.conteudo[i][1][li_sub_sub])-1,-1,-1):
                            #print(self.conteudo[i][1][li_sub_sub])
                            #print()
                                
                            try:
                                if ['h', 'yellow_background'] in self.conteudo[i][1][li_sub_sub][l]:
                                    #print('a')
                                    print('<mark style="background: #FFF3A3A6;">',end='')
                                    tag_close = 1
                                    
                            except:
                                tag_close = 0
                            try:
                                if ['_'] in (self.conteudo[i][1][li_sub_sub][l]) and ['h', 'yellow_background'] not in self.conteudo[i][1][li_sub_sub][l]:                          
                                    print('<mark style="background: #CACFD9A6;">',end='')
                                    tag_close = 2

                            except:
                                tag_close = 0
                                
                            try:
                                if ['_'] not in (self.conteudo[i][1][li_sub_sub][l]) and ['h', 'yellow_background'] not in self.conteudo[i][1][li_sub_sub][l]:
                                    pass
                            except:
                                if tag_close != 1 and tag_close !=2:
                                    print(self.conteudo[i][1][li_sub_sub][0],end='')
                                    tag_close = 3
                            else:
                                if tag_close == 1:
                                    print(self.conteudo[i][1][li_sub_sub][0],'</mark>',end='')
                                    break
                            
                                if tag_close == 2:
                                    print(self.conteudo[i][1][li_sub_sub][0],'</mark>',end='')
                                    break
                                    
                                if tag_close == 0:
                                    print(self.conteudo[i][1][li_sub_sub][0],end='')
                                    break
                                    
                    print()
                
                
                # buleted list, ficou meio bugado
                if self.conteudo[i][0] == 'bulleted_list':
                    self.numL += 1
                    n = 0
                    print(f'- ',end='')
                    for li in range(len(self.conteudo[i][1])):
                        tag_closeU = 0
                        tag_closeH = 0
                        for l in range(len(self.conteudo[i][1][li])):
                            #print(['h', 'default'] in list(self.conteudo[i][1][li][l]))
                            
                            if ['h', 'yellow_background'] in list(self.conteudo[i][1][li][l]):
                                print(f'<mark style="background: #FFF3A3A6;">',end='')
                                tag_closeH = 1
                                continue
                            if ['_'] in list(self.conteudo[i][1][li][l]): #and len(self.conteudo[i][1][li][l]) == 1:#['h'] not in list(self.conteudo[i][1][li][l]):
                                print(f'<mark style="background: #CACFD9A6;">',end='')
                                tag_closeU = 1
                                continue
                                
                            if ['h', 'default'] in list(self.conteudo[i][1][li][l]):
                                continue
                                
                            else: 
                                text = self.conteudo[i][1][li][0]
                    
                           #print(text, end='')
                        if tag_closeU ==0 and tag_closeH == 0:
                            print(text, end='')
                            
                        if tag_closeU == 1 or tag_closeH == 1:
                            print(text,'</mark>',end='')
                            tag_closeU = 0
                            tag_closeH = 0         
                    print()          
                        
                
                if self.conteudo[i][0] == 'Untitled.png':
                    n = 0
                    print(f'![[files/{self.conteudo[i][1]}]]')
                    #self.pull_content(self.file_name,(f'![[file/{self.conteudo[i][1]}]]'+'\n'))
                    
                #print(self.conteudo[i])

                if self.conteudo[i][0] == 'external_object_instance':
                    print(self.conteudo[i][1],end='\n')
                    n = 0
                    #self.pull_content(self.file_name,(self.conteudo[i][1]+'\n'))
                    
                
                if self.conteudo[i][0] == 'divider':
                    n = 0
                    print(self.conteudo[i][1])
                    #self.pull_content(self.file_name,(self.conteudo[i][1]))
                
                
                if self.conteudo[i][0] == 'quote':
                    n = 0
                    self.numc += 1
                    print('> ',end='')
                    for li in range(len(self.conteudo[i][1])):
                        if len(self.conteudo[i][1][li][0]) <= 1:
                            pass
                        else:
                            #print(self.conteudo[i][1][li])
                            tag_close = 0
                            for jo in range(len(self.conteudo[i][1][li])-1,-1,-1):
                               #
                                if len(self.conteudo[i][1][li][jo]) == 2:
                                    print('<mark style="background: #FFF3A3A6;">',end='')
                                    tag_close = 1
                                if len(self.conteudo[i][1][li][jo]) == 1: 
                                    if 'yellow_background' in self.conteudo[i][1][li][jo][0]:
                                        print('<mark style="background: #FFF3A3A6;">',end='')
                                        tag_close = 1
                                    if '_' in self.conteudo[i][1][li][jo][0]:
                                        print('<mark style="background: #CACFD9A6;">',end='')
                                        tag_close = 2

                                else:
                                    
                                    if tag_close == 1:
                                        print(self.conteudo[i][1][li][0],'</mark>',end='') 
                                        break
                                    if tag_close == 2:
                                        print(self.conteudo[i][1][li][0],'</mark>',end='')
                                        break
                                            
                                    else:
                                        print(self.conteudo[i][1][li][0],end='')
                                        break
                    print('\n')    
                    
                # Arrumar essa duas
                if self.conteudo[i][0] == 'numbered_list':
                    #print(self.conteudo[i])
                    self.numL += 1
                    
                    
                    #print(space[s-1],'aa')
                    if space[s-1] == '    ' and n >= 1:
                        print(f'{abc[n-1]}. ',end='')
                    else:
                        n +=1
                        print(f'{n}. ',end='')
                    
                    for li in range(len(self.conteudo[i][1])):
                        tag_closeU = 0
                        tag_closeH = 0
                        for l in range(len(self.conteudo[i][1][li])):
                            #print(['h', 'default'] in list(self.conteudo[i][1][li][l]))
                            
                            if ['h', 'yellow_background'] in list(self.conteudo[i][1][li][l]):
                                print(f'<mark style="background: #FFF3A3A6;">',end='')
                                tag_closeH = 1
                                continue
                            if ['_'] in list(self.conteudo[i][1][li][l]): #and len(self.conteudo[i][1][li][l]) == 1:#['h'] not in list(self.conteudo[i][1][li][l]):
                                print(f'<mark style="background: #CACFD9A6;">',end='')
                                tag_closeU = 1
                                continue
                                
                            if ['h', 'default'] in list(self.conteudo[i][1][li][l]):
                                continue
                                
                            else: 
                                text = self.conteudo[i][1][li][0]
                    
                           #print(text, end='')
                        if tag_closeU ==0 and tag_closeH == 0:
                            print(text, end='')
                            
                        if tag_closeU == 1 or tag_closeH == 1:
                            print(text,'</mark>',end='')
                            tag_closeU = 0
                            tag_closeH = 0         
                    print()
                       
#c75685697e594a328ca4fa3e83fc81a7
                
                #else:
                    # texto
                
                self.numt += 1
                if self.conteudo[i][0] == 'text' or self.conteudo[i][0] == 'toggle':
                    n = 0
                    #print(self.conteudo)
                    #print(self.conteudo[i][1])
                    if '‣' in self.conteudo[i][1][0]:
                        continue
                    for li in range(len(self.conteudo[i][1])):
                        tag_closeU = 0
                        tag_closeH = 0
                        for l in range(len(self.conteudo[i][1][li])):
                            #print(['h', 'default'] in list(self.conteudo[i][1][li][l]))
                            
                            if ['h', 'yellow_background'] in list(self.conteudo[i][1][li][l]):
                                print(f'<mark style="background: #FFF3A3A6;">',end='')
                                tag_closeH = 1
                                continue
                            if ['_'] in list(self.conteudo[i][1][li][l]): #and len(self.conteudo[i][1][li][l]) == 1:#['h'] not in list(self.conteudo[i][1][li][l]):
                                print(f'<mark style="background: #CACFD9A6;">',end='')
                                tag_closeU = 1
                                continue
                                
                            if ['h', 'default'] in list(self.conteudo[i][1][li][l]):
                                continue
                                
                            else: 
                                text = self.conteudo[i][1][li][0]
                    
                           #print(text, end='')
                        if tag_closeU ==0 and tag_closeH == 0:
                            print(text, end='')
                            
                        if tag_closeU == 1 or tag_closeH == 1:
                            print(text,'</mark>',end='')
                            tag_closeU = 0
                            tag_closeH = 0         
                    
                    print()

                
                if self.conteudo[i][0] == 'page':
                    print("Falta Link de pagina")
                ### Tabela não vai ter #table não tem title por isso não é adicionada
                if self.conteudo[i][0] == 'table':
                    print('Falta alguma coisa aqui')




if __name__ == "__main__":
    x = Migracion(sys.argv[1])
    x.request(x.id_final)
    x.pull_keys()
    x.extract_content()
    
    #print(f'{Fore.RED}Arquivo:', x.file_name, f'{Style.RESET_ALL}')
    #print(f'{Fore.BLUE}Com', x.img, f'{Fore.BLUE}imagens, ',x.numH, f'{Fore.BLUE}Titulos, ',x.numL, f'{Fore.BLUE}Lista e', x.numt, f'{Fore.BLUE}Linhas de texto', f'{Style.RESET_ALL}')
    
    #print(f'{Fore.GREEN}Finalizado!', f'{Style.RESET_ALL}')
    
    
    
    
    
    
    