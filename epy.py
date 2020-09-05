# github.com/secwayz/ePy

import requests


def un_shorten(url):
    """
    Un shorting any URL

    Keywords arguments:
        url -- Short URL

    :return: full url
    """

    return requests.head(url, allow_redirects=True).url


class api:
    def __init__(self):
        self.client_id = ''
        self.client_secret = ''

        self.access_token = ''
        self.refresh_token = ''


    def auth(self, client_id, client_secret):
        """
        Authorize method with client- SECRET and ID

        :return: access_token
        """
        self.client_id = client_id
        self.client_secret = client_secret

        payload = {'grant_type': 'client_credential', 'client_id': client_id, 'client_secret': client_secret}
        response = requests.post("https://oauth2.epn.bz/token", data=payload,
                                 headers={'X-API-VERSION': '2', 'X-SSID': self.ssid()})

        self.access_token = response.json()["data"]["attributes"]["access_token"]
        self.refresh_token = response.json()["data"]["attributes"]["refresh_token"]

        return self.access_token


    def token_refresh(self):
        """
        Refresh the token function

        :return: new refresh_token
        """

        response = requests.post("https://oauth2.epn.bz/token/refresh",
                                 data={"grant_type": "refresh_token", "refresh_token": self.refresh_token,
                                       "client_id": self.client_id}, headers={'X-API-VERSION': '2'})

        self.access_token = response.json()["data"]["attributes"]["access_token"]
        self.refresh_token = response.json()["data"]["attributes"]["refresh_token"]

        return self.refresh_token


    def ssid(self):
        """
        Get SSID for access to API

        :return: SSID
        """

        response = requests.get("https://oauth2.epn.bz/ssid?client_id=" + self.client_id,
                                headers={'X-API-VERSION': '2'})
        return response.json()["data"]["attributes"]["ssid_token"]


    def short_link(self, link, cutter="ali.pub"):
        """
        Create a short link from full partner link

        :param link: partner link
        :param cutter: ali.pub got.by ozn.by ...
        :return: short link
        """

        response = requests.post("https://app.epn.bz/link-reduction",
                                 data={"urlContainer": link, "domainCutter": cutter},
                                 headers={'X-ACCESS-TOKEN': self.access_token})

        return response.json()["data"]["attributes"][0]["result"]


    def create_link(self, source_link):
        """
        Create a partner link

        Keywords arguments:
            source_link -- Full aliexpress link
            description -- Description or comment for link

        :return: link or error
        """

        response = requests.post("https://app.epn.bz/creative/create",
                                 data={"link": source_link, "offerId": 1, "description": "Test desc",
                                       "type": "deeplink"},
                                 headers={'ACCEPT-LANGUAGE': 'RU', 'X-ACCESS-TOKEN': self.access_token})

        if response.status_code == 200:
            return response.json()["data"]["attributes"]["code"]
        else:
            return response.json()["errors"][0]["error_description"]
