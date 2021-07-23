# importing files#

import requests
import hashlib

# function to get api data#

def get_api_data(pswrd):
  url = 'https://api.pwnedpasswords.com/range/' + pswrd
  response = requests.get(url)
  if response.status_code!=200:
    raise RuntimeError(f"error fetching api data:{response.status_code}")
  return response

def get_encrypted_check(password):
  encrypt_pswrd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
  head, tail = encrypt_pswrd[:5], encrypt_pswrd[5:]
  data = get_api_data(head)
  return get_data(data,tail)


def get_data(hashes,to_check):
  hashes = (line.split(':') for line in hashes.text.splitlines())
  for h,count in hashes:
    if h == to_check:
      return count
  return 0




