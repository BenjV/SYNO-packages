import socket, ssl, sys, os, platform, json, re
from urllib import request

print('\nPlatform information:')

try:
    with open('/etc.defaults/synoinfo.conf', 'r') as fp:
        info = fp.read()
        re_info=re.compile('^unique="(.*)"', re.MULTILINE)
        SynoInfo = re_info.search(info).group(1).replace('_',' ')
        print(f'{"System":<20}: {SynoInfo}')
except:
    print(f'{"System":<20}: {"No Synology Device"}')
print(f'{"Cpu count":<20}: {os.cpu_count()}')

Info = platform.uname()
for Index in range(0, len(Info)):
    print(f'{Info._fields[Index]:<20}: {Info[Index]}')

#try:
#    print(f'{"Wan Ip adress":<20}: {request.urlopen("https://api.ipify.org:443").read().decode("utf-8")}')
#except Exception as Error:
#    print(Error, file=sys.stderr)
#
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.connect(("8.8.8.8", 80))
#print(f'{"Lan Ip adress":<20}: {sock.getsockname()[0]}')

print('\nCertificate search path:')
print()
try:
    CertPath = ssl.get_default_verify_paths()
    for Index in range(0, len(CertPath)):
        print(f'{CertPath._fields[Index]:<20}: {CertPath[Index]}')
    print()
except Exception as Error:
    print(Error, file=sys.stderr)

print()
try:
    Data = request.urlopen('https://www.howsmyssl.com/a/check').read().decode('utf-8')
    Resp = json.loads(Data)
    for Key, Value in Resp.items():
        if Key == "given_cipher_suites":
            print ("Available cyphers:\n")
            for Cypher in Value:
                print(Cypher)
            print('\nOther ssl info:\n')
        elif Key =='insecure_cipher_suites':
            for Key, Value in Resp['insecure_cipher_suites']:
                Print(f'{Key}: {Value}')
        else:
            print (f'{Key:<37}: {Value}')
except Exception as Error:
    print(Error, file=sys.stderr)
print()

#Make a soccket connection with diferent website who specific tls versions and encryptions
print('Testing sites support only certain TLS versions.')
TestSites = [
             ('tls-v1-0.badssl.com', 1010),
             ('tls-v1-1.badssl.com', 1011),
             ('tls-v1-2.badssl.com', 1012),
             ('sha256.badssl.com', 443),
             ('sha384.badssl.com', 443),
             ('sha512.badssl.com', 443),
             ('www.github.com', 443),
             ('www.google.com', 443)
           ]
context = ssl.create_default_context()
for Site in TestSites:
    try:
        with socket.create_connection(Site, 5) as sock:
            with context.wrap_socket(sock, server_hostname=Site[0]) as ssock:
                print(f'{Site[0]:<20}: {ssock.cipher()}')
    except Exception as Error:
        print(Error)
