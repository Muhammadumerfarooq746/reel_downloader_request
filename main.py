import requests,re,base64,random, configparser
import os ,urllib



# with importlib.resources.path("certifi", "cacert.pem") as ca_path:
#     print(ca_path)
# config = configparser.ConfigParser()
# config.read("config.ini")

# username = config.get("settings", "targetuser")
# reel = config.get("settings", "numberofreels")


def get_user_id_from_username(username):
    agent = "Instagram 117.0.0.28.123 Android (28/9.0; 420dpi; 1080x1920; OnePlus; ONEPLUS A3003; OnePlus3; qcom; en_US; 180322800)"
    res = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username='+username,headers={'user-agent': agent})
    id_= res.json().get('data').get('user').get('id')
    return id_
# print(get_user_id_from_username("nike")) 

def get_id(username):

    url = "https://instabig.net/s/bigpp"

    querystring = { "u": username }

    headers = {
        "host": "instabig.net",
        "connection": "keep-alive",
        "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
        "sec-ch-ua-mobile": "?0",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "sec-ch-ua-platform": "\"macOS\"",
        "accept": "*/*",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://instabig.net/download-instagram-instadp",
        "accept-encoding": "gzip",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "lang=en; _gid=GA1.2.1442936484.1675943631; __gads=ID=72e891bf3c29722a-228a31e6a8db0012:T=1675943632:RT=1675943632:S=ALNI_Mbf_5juiC5uw3s6PyIxZFPSyTGVnA; __gpi=UID=00000bd70202e393:T=1675943632:RT=1675943632:S=ALNI_MajlYdw61JIwE3Yo7Qu-U-tFNCA3g; PHPSESSID=efkndanb4s85vmqc41a9f1kmn9; _gat_gtag_UA_65465319_3=1; FCNEC=%5B%5B%22AKsRol-H27TGk29cbSiKxrQC6bPBUs3DVSA344fIFlgki51tLkE8DW2dFDC7rKqpGQFOyRqOGkitGmhSfQ06wShWVIyS4QCsuqERb34BGMxSuAJTVeWB5Y10aHEcUSYow3Ef3YTdHNVrsZNXIX9O96DfsO6Cn-ICXg%3D%3D%22%5D%2Cnull%2C%5B%5D%5D; _ga=GA1.1.728967113.1675943631; _ga_J13QVZHLPK=GS1.1.1675943631.1.1.1675943786.0.0.0"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()[0]['pk']

def download_content(url,paths,post_id):
    paths='reels'
    with open('links.txt', 'r') as file:
        existing_links = file.readlines()
    if post_id+'\n' not in existing_links:    
        with open('links.txt', 'a') as file:
            file.write(post_id+'\n')
            print("""---------------------------
            url save now downloaded reels
            -----------------------------""")
        folder = os.path.join(paths, username)

        if os.path.exists(folder):
            # folder = os.path.join(paths, username)
            print("---")
        else:
            # p_folder=os.path.join('reels')
            # folder = os.path.join(paths, username)
            # print(p_folder)
            if not os.path.exists(folder):
                os.mkdir(folder)
            # folder=os.path.exists(username)
        file_name=username+"_"+post_id
        # print(os.path.join(os.getcwd(),'reels',folder,f'{file_name}.mp4'))
        urllib.request.urlretrieve(url, os.path.join(os.getcwd(),folder,f'{file_name}.mp4')) 
        
    else:
        print("""----------------------------
        -----------no  new reel-------
        ----------------------""")
     
def config():
        config = configparser.ConfigParser()
        config.read("config.ini")

        username = config.get("settings", "targetuser")
        reel = config.get("settings", "numberofreels")




def list_of_reels(username):
    try:
        ID = get_id(username)
        print(ID)
    except:
        ID=get_user_id_from_username(username)
        print(ID)
    count=0
    max_id=""
    DATA=[]

    url = "https://i.instagram.com/api/v1/clips/user/"
    payload = "max_id={}&target_user_id={}".format(max_id,str(ID))
    headers = {
        "x-ig-app-locale": "en_US",
        "x-ig-device-locale": "en_US",
        "x-ig-mapped-locale": "en_US",
        "x-pigeon-rawclienttime": "1643479789.325",
        "x-ig-bandwidth-speed-kbps": "3699.000",
        "x-ig-bandwidth-totalbytes-b": "14674191",
        "x-ig-bandwidth-totaltime-ms": "5498",
        "x-ig-app-startup-country": "US",
        "x-ig-timezone-offset": "28800",
        "x-ig-nav-chain": "ClipsViewerFragment:clips_viewer_clips_tab:2,UserDetailFragment:profile:5,4Ae:clips_profile:6",
        "x-ig-connection-type": "WIFI",
        "x-ig-capabilities": "3brTvx0=",
        "priority": "u=3",
        "user-agent": "Instagram 207.0.0.39.120 Android (25/7.1.2; 240dpi; 720x1280; google; G011A; G011A; intel; en_US; 321039156)",
        "accept-language": "en-US",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "accept-encoding": "gzip, deflate",
        "host": "i.instagram.com",
        "x-fb-http-engine": "Liger",
        "x-fb-client-ip": "True",
        "x-fb-server-cluster": "True",
        "connection": "keep-alive"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    
    for i in response.json()['items']:
        # try:
        #     cover=i['media']["image_versions2"]["additional_candidates"]["first_frame"]["url"]
        # except:
        #     cover=i['media']["image_versions2"]["candidates"][0]["url"]

        # cover=cover_decode(cover)

        download_url=i['media']["video_versions"][-1]["url"]
        caption=""
        userr=i['media']['user']["username"]
        post_url=i['media']["code"]
        count+=1
        dat={"post_id":post_url,"download_url":download_url,"caption":caption,"user":userr}
        # print(dat)
        DATA.append(dat)
        url=dat["download_url"]
        post_id=dat["post_id"]
        # print(url)
        path= "reels"

        # download_content(url,path)

     
    
        more=response.json()["paging_info"]["more_available"]
        if more=="false":
            return DATA
        try:
            max_id=response.json()["paging_info"]["max_id"]
        except:
            return DATA
        download_content(url,path,post_id)
        if count==10:
            
            break



print("""
    _____   ________________   __________  ___    __  ___   ____  ____  ______
   /  _/ | / / ___/_  __/   | / ____/ __ \/   |  /  |/  /  / __ )/ __ \/_  __/
   / //  |/ /\__ \ / / / /| |/ / __/ /_/ / /| | / /|_/ /  / __  / / / / / /   
 _/ // /|  /___/ // / / ___ / /_/ / _, _/ ___ |/ /  / /  / /_/ / /_/ / / /    
/___/_/ |_//____//_/ /_/  |_\____/_/ |_/_/  |_/_/  /_/  /_____/\____/ /_/     
                                                                              
""")

username = input("Enter the username? ")
res=list_of_reels(username)
# print(res)