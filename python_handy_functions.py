def time_prev_month(current):
    _first_day = current.replace(day=1)
    prev_month_lastday = _first_day - datetime.timedelta(days=1)
    return prev_month_lastday.replace(day=1)
   

#### Start connection
import os
import datetime

from aiohttp import ClientSession
import asyncio
import json
import traceback

url = f'http://192.168.1.2:5566/v1/customer/users_get_all'

async def get_users_for_import_from(url, handshake=None):
    async with ClientSession() as client:
        async with client.post(
            url=url,
            data=json.dumps({
                'handshake':"29f7fcc3d19f70f50210b003f35547b9d870c19e828e7051c6c44d6777754892",
                'slice_top': 0,
                'slice_bottom': 30,
                'createdat': None
             })
         ) as resp:
            assert resp.status == 200
            text = await resp.text()
            data = json.loads(text)
            print(len(data['result']) , data['count'], data['admin'])

            try:
                active_to_date = datetime.datetime.utcnow()

                for each in data['result']:
                    print('\neach:', each)
                
            except Exception as e:
                traceback.print_exc()
                return None

            return data

loop = asyncio.get_event_loop()
loop.run_until_complete(get_users_for_import_from(url))
#### END connection from client

# defined in model ClosureTable
    @classmethod
    def get_nodes_from_closure_table_with_user(cls, session, node_uid):
        q = session.query(User,Node,ClosureTable)
        q = q.filter(Node.uid == ClosureTable.children_uid)
        q = q.filter(Node.user_uid == User.uid)
        q = q.filter(ClosureTable.ancestor_uid == node_uid)
        q = q.order_by(ClosureTable.depth.asc())
        return q.all()

# called from route - api
nodes = ClosureTable.get_nodes_from_closure_table_with_user_depth_from_to_and_plan(session, node.uid, from_depth, to_depth)
        
result = []
count = len(nodes)
for user, node, closure_table in nodes:

    node_dict = node.object_to_dict()    
    node_dict['depth'] = closure_table.depth
    node_dict['name'] = user.username
    del node_dict['user_uid']    

    result.append(node_dict)
return result
