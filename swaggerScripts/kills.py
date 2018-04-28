from esipy import App

# App.create(url, strict=True)
# with url = the swagger spec URL, leave strict to default
app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")

#appS = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")

from esipy import EsiClient

# basic client, for public endpoints only
client = EsiClient(
    retry_requests=True,  # set to retry on http 5xx error (default False)
    header={'User-Agent': 'Something CCP can use to contact you and that define your app'},
    raw_body_only=False,  # default False, set to True to never parse response and only return raw JSON string content.
)

# generate the operation tuple
# the parameters given are the actual parameters the endpoint requires
kills = app.op['get_universe_system_kills']()
response = client.request(kills)

print(response.data)

