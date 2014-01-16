import urllib, urllib2, StringIO, json

f = open('CrashData.csv', 'r')
rows = [line.split() for line in f.readlines()]
addresses = [' '.join(rows[i]).replace(',', ' ') for i in range(1, len(rows))]
def address_to_coor(address):
        params = {
                'address': address,
                'sensor': 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
        response = urllib2.urlopen(url)
        responseBody = response.read()

        body = StringIO.StringIO(responseBody)
        result = json.load( body )
        if 'status' not in result or result['status'] != 'OK':
                pass
        else:
                return {
                        "latitude": result['results'][0]['geometry']['location']['lat'],
                        "longitude": result['results'][0]['geometry']['location']['lng']
                }
coordinates = [address_to_coor(address) for address in addresses]
f = open('coordinates.txt', 'w')
print >> f, coordinates
