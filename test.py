import requests

def getModule():
    print('get Module start..')

    try:
        url = 'http://ec2-65-2-148-13.ap-south-1.compute.amazonaws.com:8080/server/get/test/127.1497655,36.850711/'
        response = requests.get(url)
        data = str(response.content)
        if data.find('off') != -1:
            print('off')
        else:
            print('on')
        print(data.find('off'))
    except:
        print('error!')

if __name__=='__main__':
    getModule()


