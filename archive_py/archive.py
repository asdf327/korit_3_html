import requests
import time
import concurrent.futures

links = [
    'https://bbs.tunaground.net/trace.php/anchor/1596255065/536/635',
    'https://bbs.tunaground.net/trace.php/anchor/1596255065/641/776',
    'https://bbs.tunaground.net/trace.php/anchor/1596255065/789/1001',
    'https://bbs.tunaground.net/trace.php/anchor/1596256065/1/214',
    'https://bbs.tunaground.net/trace.php/anchor/1596256065/230/375',
    'https://bbs.tunaground.net/trace.php/anchor/1596256065/384/597',
    'https://bbs.tunaground.net/trace.php/anchor/1596256065/614/1001',
    'https://bbs.tunaground.net/trace.php/anchor/1596257089/1/249',
    'https://bbs.tunaground.net/trace.php/anchor/1596257089/309/704',
    'https://bbs.tunaground.net/trace.php/anchor/1596257089/707/891',
    'https://bbs.tunaground.net/trace.php/anchor/1596257089/895/1001',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/1/120',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/129/172',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/179/332',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/339/595',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/602/660',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/664/837',
    'https://bbs.tunaground.net/trace.php/anchor/1596258103/847/1001',
    'https://bbs.tunaground.net/trace.php/anchor/1596258182/1/201',
    'https://bbs.tunaground.net/trace.php/anchor/1596258182/206/1001',
    'https://bbs.tunaground.net/trace.php/anchor/1596258209/1/15',
    'https://bbs.tunaground.net/trace.php/anchor/1596258209/17/412',
    'https://bbs.tunaground.net/trace.php/anchor/1596258209/42/103',
    'https://bbs.tunaground.net/trace.php/anchor/1596258209/433/502',
    'https://bbs.tunaground.net/trace.php/anchor/1596258209/509/700',
    'https://bbs.tunaground.net/trace.php/anchor/1596258209/710/1001',
    'https://bbs.tunaground.net/trace.php/anchor/1596258240/1/109',
    'https://bbs.tunaground.net/trace.php/anchor/1596258240/113/263'
    ]

def archive_link(link):
    try:
        response = requests.get(f'http://web.archive.org/save/{link}')
        if response.status_code == 200:
            print(f'Successfully archived: {link}')
        else:
            print(f'Failed to archive: {link} - Status Code: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Error with {link}: {e}')
    time.sleep(3)  # 요청 간 간격을 넉넉하게 줘야 안전함

# 최대 동시 처리 수를 제한
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(archive_link, links)

print("Archiving process completed.")