## Description
> Soruda paylaşılan dosya PyInstaller ile paketlenmişti. Pyinstxtractor kullanarak paketi ayrıştırdık. Sonrasında uncompyle6 kullanarak kaynak kodlarını elde ettik. Kaynak kodları şu şekilde.
```
import random, string, datetime, uuid, requests

def hayde():
    print('Hoşgeldin yaaaar, yüreğimeeee,boşver be, elalem ne der se de sin haydi haydi haydi. Böyle devam krall bi incele bakayım buraları.')


def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format(uuid.getnode() >> ele & 255) for ele in range(0, 48, 8)][::-1])
    return mac_address


def generate_domain(seed):
    random.seed(seed)
    domain_length = random.randint(5, 10)
    domain = ''.join((random.choice(string.ascii_lowercase) for _ in range(domain_length)))
    return domain


def generate_dga_domains(num_domains):
    domains = []
    seed = datetime.datetime.now().strftime('%Y%m%d%H')
    for _ in range(num_domains):
        domain = generate_domain(seed)
        domains.append(domain)
        seed = domain

    return domains


def main():
    num_domains = 2
    dga_domains = generate_dga_domains(num_domains)
    try:
        url = f"https://{dga_domains[0]}.github.io/{dga_domains[1]}.flg"
        print('DGA başlatıldı...')
        res = requests.post(url)
    except:
        print('The server cannot communicate!')


if __name__ == '__main__':
    allowed_corp = '00:15:17'
    mac = get_mac_address()
    if mac.startswith(allowed_corp):
        print('The system is among the targets, attack started')
        main()
    else:
        print('Your MAC: ' + mac)
        print('The system is not among the targets')
```

Kısaca MAC kontrolünü ortadan kaldırdık ve seed değerine göre aynı algoritmayla domain üretecek bir script yazdım. Bu ay içerisindeki tüm saatleri hesapaladım kesin sonuç alabilmek için. Sonrasında bulduğum reponun github hesabında flag'i buldum.

## Solution
```
import random
import string
import datetime
import requests

start_date = datetime.datetime(2023, 6, 1)
end_date = datetime.datetime(2023, 6, 30)

seeds = []

current_date = start_date
while current_date <= end_date:
    for hour in range(24):
        seed = current_date.replace(hour=hour).strftime('%Y%m%d%H')
        seeds.append(seed)
    current_date += datetime.timedelta(days=1)


def generate_domain(seed):
    random.seed(seed)
    domain_length = random.randint(5, 10)
    domain = ''.join((random.choice(string.ascii_lowercase) for _ in range(domain_length)))
    return domain

def generate_dga_domains():
    domains = []
    for seed in seeds:
        print(seed)
        domain = generate_domain(seed)
        domains.append(domain)

    return domains

def main():
    dga_domains = generate_dga_domains()
    try:
        for domain in dga_domains:
            url = f"https://{domain}.github.io/{domain}.flg"
            res = requests.get(url)
            if "isn't" in res.text:
                pass
            else:
                print(url)
                print(res.text)
    except:
        print('???????????????????????.')

main()
```
