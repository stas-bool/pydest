import aiohttp

class API:

    def __init__(self, api_key):
        self.api_key = api_key


    async def _get_request(self, url):
        """Make an async GET request"""
        headers = {'X-API-KEY':'{}'.format(self.api_key)}
        async with aiohttp.get(url, headers=headers) as r:
            return await r.json()


    def check_args(self, *args):
        for arg in args:
            arg = str(arg)
            if ('/' in arg) or ('\\' in arg):
                raise ValueError("arguments may not contain '/' or '\\'")


    async def search_destiny_player(self, membership_type, display_name):
        self.check_args(membership_type, display_name)
        url = 'https://www.bungie.net/Platform/Destiny/SearchDestinyPlayer/{}/{}/'
        url = url.format(membership_type, display_name)
        return await self._get_request(url)


    async def get_account_summary(self, membership_type, membership_id):
        self.check_args(membership_type, membership_id)
        url = 'https://www.bungie.net/Platform/Destiny/{}/Account/{}/Summary/'
        url = url.format(membership_type, membership_id)
        return await self._get_request(url)