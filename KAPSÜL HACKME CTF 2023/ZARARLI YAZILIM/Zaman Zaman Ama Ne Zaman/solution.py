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
