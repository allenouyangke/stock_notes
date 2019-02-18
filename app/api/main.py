from flask import request
from flask_restful import reqparse
from . import api
import json

@api.route('/api/v1/<table_name>/<action>',methods=['POST'])
def parse_request(table_name,action):
    print 'it is arrive here'
    print "table_name %s " % table_name
    print "action %s " % action
    # parser = reqparse.RequestParser()
    # parser.add_argument('table',type=str)
    # parser.add_argument('action',type=str)
    # parser.add_argument('query',type=json)
    # args = parser.parse_args()
    # print  args
    data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
    j = json.dumps(data)
    return j