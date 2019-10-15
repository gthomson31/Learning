import requests
import json


buildpack_types = [ 

'java-buildpack',
'dotnet-core-buildpack',
'staticfile-buildpack',
'python-buildpack',
'binary-buildpack'
]


for buildpack_type in buildpack_types:
	response = requests.get('https://network.pivotal.io/api/v2/products/'+ buildpack_type + '/releases/')
	parsed_json = json.loads(response.content)

	print (buildpack_type)

	for buildpack in parsed_json['releases']:
		
		buildpack_link = buildpack['_links']['product_files']['href']

		print ('')
		print ('------------')
		print (buildpack['version'])
		print ('------------')

		bp_link_response = requests.get(buildpack_link)
		parsed_json_download = json.loads(bp_link_response.content)

		for product in parsed_json_download['product_files']:
			print ('')
			print (product['name'])
			print (product['_links']['download']['href'])


		# print('---------------------')

	



# https://network.pivotal.io/api/v2/products//releases/478074/product_files/501830/download