# ePy
e-Commerce Partner API (epn.bz)

#### (use) un_shorten(url)
Find end link, example: adf.ly/qGB -> example.com/index.php

#### (use) api.auth(client_id, client_secret)
Authorization epn.bz with clients ID and SECRET.
Return access token.

#### (system) api.token_refresh()
Get refresh_token.

#### (system) api.ssid()
Get SSID key for access API.

#### (use) api.short_link(link, cutter)
Default cutter - ali.pub. Short your partner link.

#### (use) api.create_link(aliexpress_link)
Create long partner link.


## Use library
Copy **epy.py** in your project directory.

```
import epy

# Initialization
ali = epy.api()
ali.auth(client_id, client_secret)

# Create and short partner link
long_link = ali.create_link(aliexpress_link)
short_link = ali.short_link(long_link)

print(short_link)  # output ali.pub link
```

# Contact us
Telegram: https://t.me/secwayz

