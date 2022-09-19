import requests

def getModule():
    print('get Module start..')

    try:
        url = 'http://127.0.0.1:8000/server/get/test/'
        response = requests.get(url)
        data = str(response.content)
        if data.find('off'):
            print('off')
        else:
            print('on')
    except:
        print('error!')

if __name__=='__main__':
    getModule()


