import requests

def getModule():
    print('get Module start..')

    try:
        url = 'http://ec2-65-2-148-13.ap-south-1.compute.amazonaws.com:8080/server/gps/test/ddd/127.312,32.3213/'
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


