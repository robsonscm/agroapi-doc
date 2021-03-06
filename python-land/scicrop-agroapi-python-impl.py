###############################################################################
#
# Copyright [2017]	Jose Ricardo de Oliveira Damico
# 			SciCrop Informacao e Tecnologia S.A.
# 			info@scicrop.com  https:scicrop.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:www.apache.orglicensesLICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
##############################################################################

import sys, requests, json

hostname = 'engine.scicrop.com'
protocol = 'http://'
url = protocol+hostname+'/scicrop-engine-web/api/v1'

username = input("Enter your username: ")
password = input("Enter your password: ")
api_id = input("Enter your api_id: ")

print(username)

rest = '/status/my';

session = requests.Session()
session.auth = (username, password)


auth = session.post(protocol + hostname)
response = session.get(protocol + hostname + '/scicrop-engine-web/api/v1' + rest)

print('\n\nGET RESPONSE FOR ['+rest+'] CALL\n\n')
print(response)
print(response.content)

data = {"authEntity":{"userEntity":{"email":""+username+"", "api_id": ""+api_id+""}},"payloadEntity":{},"responseEntity":{"returnId":"0"}}

rest = '/station/scicrop';

headers = {'Content-type': 'application/x-www-form-urlencoded'}
rresponse = session.post(url + rest, json.dumps(data), headers=headers)

print('\n\nPOST RESPONSE FOR ['+  rest + '] CALL\n\n')
print(rresponse)
print(rresponse.content)
