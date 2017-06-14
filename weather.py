import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/ebb3e0cf5059cce8/conditions/q/RO/Cluj-Napoca.json')
json_string = f.read()
parsed_json = json.loads(json_string)
location = parsed_json['current_observation']['display_location']['city']
temp_c = parsed_json['current_observation']['temp_c']
clouds = parsed_json['current_observation']['weather']
print "The temperature in %s is %s and the sky is: %s" % (location, temp_c, clouds)
f.close()