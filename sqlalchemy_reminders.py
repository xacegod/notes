# faster counting
def get_count(q):
    count_q = q.statement.with_only_columns([func.count()]).order_by(None)
    count = q.session.execute(count_q).scalar()
    return count

# Slow: SELECT COUNT(*) FROM (SELECT ... FROM TestModel WHERE ...) ...
print(q.count())

# Fast: SELECT COUNT(*) FROM TestModel WHERE ...
print(get_count(q))
qry = session.query(User).filter(User.createdat>=to_date,User.createdat<from_date)
test = get_count(qry)
print(test)

# order by
order_by(Node.amount.desc())

q = session.query(Profile).filter(Profile).order_by(...)

to_date = datetime.datetime.utcnow() - datetime.timedelta(days=30)
from_date = datetime.datetime.utcnow()

q = session.query(Profile.user_uid).filter(Profile.sponsor_user_uid == token_user_data['uid']).all()

new_q = [r[0] for r in q]



# returns from tabel the column we pass as variable in String
getattr(model, "column_in_string")

# order by said column
if order_by == None: 
    q = q.order_by(Task.end_date.desc())
elif any(u in order_by for u in ('createdat', 'title', 'number', 'begin_date', 'end_date', 'enabled', 'created_by_user', 'updated_by_user' )):
    q = q.order_by(getattr(Task, order_by).desc())

##### counts the number of times said data is repeated in database
q = session.query(Node.uid, User.username, func.count(Node.user_uid).label('count'))
q = q.filter(Node.user_uid == User.uid)
q = q.group_by(Node.user_uid)
q = q.order_by('count')
q = q.limit(10)
nodes_count = q.all()

q = session.query(User.username, Task.user_uid, func.count(Task.user_uid).label('count'))
q = q.filter(Task.user_uid == User.uid)
q = q.group_by(Task.user_uid)
q = q.order_by('count').desc()
#q = q.order_by(User.createdat.asc())
q = q.limit(number)
q = q.all()

# if we need slice of data returned we use this
.slice(0, 10).all()

# results that have said values
having(func.count(Address.id) > 2)

# only distinct results
distinct(Transaction.currency)

# filter by accepts kwargs
.filter_by('name'='John')
.filter_by(kwargs) # key word arguments

# filter test if ==
.filter(User.name == 'John')

# not in ~
query.filter(~User.name.in_(['lee', 'sonal', 'akshay']))

########
# and_
from sqlalchemy import and_
filter(and_(User.name == 'leela', User.fullname == 'leela dharan'))

#or, default without and_ method comma separated list of conditions are AND
filter(User.name == 'leela', User.fullname == 'leela dharan')

# or call filter()/filter_by() multiple times
filter(User.name == 'leela').filter(User.fullname == 'leela dharan')
########

#######
# or_
from sqlalchemy import or_
filter(or_(User.name == 'leela', User.name == 'akshay'))
#######

###
# match
query.filter(User.name.match('leela'))
###

col_name = 'name'
db_session.query(User).filter(getattr(User, col_name).like("%" + query + "%"))
# test if it will work with the bottom one
model_name = "User"
db_session.query(model_name).filter(getattr(model_name, col_name).like("%" + query + "%"))

#######

# count with more things, last adds support for view 
from sqlalchemy import func, distinct
from sqlalchemy.orm import lazyload

def get_count(q):
    disable_group_by = False
    if len(q._entities) > 1:
        # currently support only one entity
        raise Exception('only one entity is supported for get_count, got: %s' % q)
    entity = q._entities[0]
    if hasattr(entity, 'column'):
        # _ColumnEntity has column attr - on case: query(Model.column)...
        col = entity.column
        if q._group_by and q._distinct:
            # which query can have both?
            raise NotImplementedError
        if q._group_by or q._distinct:
            col = distinct(col)
        if q._group_by:
            # need to disable group_by and enable distinct - we can do this because we have only 1 entity
            disable_group_by = True
        count_func = func.count(col)
    else:
        # _MapperEntity doesn't have column attr - on case: query(Model)...
        count_func = func.count()
    if q._group_by and not disable_group_by:
        count_func = count_func.over(None)
    count_q = q.options(lazyload('*')).statement.with_only_columns([count_func]).order_by(None)
    if disable_group_by:
        count_q = count_q.group_by(None)
    return q.session.execute(count_q).scalar()


    if hasattr(model_class, 'columns'):
        q = q.filter(model_class.columns.get('uid') == model_class.columns.get('uid'))
    else:
        q = q.filter(getattr(model_class, 'uid') == getattr(model_class, 'uid'))

#####

subquery = session.query(Task.package_uid, func.count('*').label('package_count')).group_by(Task.package_uid).subquery()
qry = session.query(Package) \
    .outerjoin((subquery, Package.uid == subquery.c.package_uid)) \
    .order_by(Package.uid).filter(subquery.c.package_count >= 5)

qry = qry.all()

print(qry)


##### 

@route(app, 'POST', '/v1/get_task')
@json_response
async def post_v1_get_task(request):
    data = await request.json()

    token = data.get('token', None)    

    if token == None: # or it not token:
        return {'error':'no token'}

    try:
        user_dict = token_decode(token)
        
        session = ReadOnlySession()
        user = session.query(User).filter(User.uid == user_dict['uid'] ).first()
        if not user:
            session.close()
            return {'error':'error'}

        if user_dict['logged_in'] != user.logged_in:
            session.close()
            return {'error':'signed in already'}

        now = datetime.datetime.utcnow()
        yesterday = get_yesterday() # fucntion for today - 1 day
        
        day_of_week = datetime.datetime.today().weekday() # int [0 - 6]

        ## All done by user
        p = session.query(Package.uid)
        p = p.filter(Package.uid == Task.package_uid)
        p = p.filter(Task.user_uid == user.uid)
        p = p.filter(Task.createdat >= yesterday)
        p = p.filter(Task.deletedat == None)
        p = p.all()
        
        if p:
            done_p = [i[0] for i in p]

        q = session.query(Package)

        # q = q.filter(Package.start_date_for_package <= now)
        # q = q.filter(Package.end_date_for_package >= now)

        q = q.filter(Package.deletedat == None)
        q = q.filter(Package.accepted == True)
        q = q.filter(Package.template == False)        

        # Today's available from Packages
        if day_of_week == 0: # monday
            q = q.filter(Package.monday_to_advertise == True)
        elif day_of_week == 1: # tuesday
            q = q.filter(Package.tuesday_to_advertise == True)
        elif day_of_week == 2: # wend
            q = q.filter(Package.wednesday_to_advertise == True)
        elif day_of_week == 3: # thursday
            q = q.filter(Package.thursday_to_advertise == True)
        elif day_of_week == 4: # friday
            q = q.filter(Package.friday_to_advertise == True)
        elif day_of_week == 5: # saturday
            q = q.filter(Package.saturday_to_advertise == True)
        elif day_of_week == 6: # sunday
            q = q.filter(Package.sunday_to_advertise == True)
        
        if p == None or p == []:
            pass
        else:
            ##### IMPORTANT!!! #####
            # For this to work each Package needs to have at least 1 done task
            # We do this by letting super on approve get a done task
            # This way when he checks if link is valid it is counted as a view, or done task
            ########################
            s = session.query(
                Task.package_uid, 
                func.count('*').label('package_count')
            )

            ### Doesnt work for hours for whatever reason
            yes = datetime.datetime.utcnow() - datetime.timedelta(days =1)

            s = s.filter(Task.createdat>=yes)
            s = s.group_by(Task.package_uid)

            subquery = s.subquery('subquery')

            s = session.query(
                Task.package_uid, 
                func.count('*').label('package_count_total')
            )
            s = s.group_by(Task.package_uid)
            
            subquery_tot = s.subquery('subquery_tot')

            q = q.outerjoin(
                subquery, 
                and_(
                    Package.uid==subquery.c.package_uid,
                    Package.daily_number_of_clicks > subquery.c.package_count,
                )
            )

            q = q.outerjoin(
                subquery_tot, 
                and_(
                    Package.uid==subquery_tot.c.package_uid,
                    Package.total_number_of_clicks > subquery_tot.c.package_count_total,
                )
            )            

            # filter by not being in done tasks by user
            q = q.filter(~Package.uid.in_(done_p))

        q = q.order_by(Package.priority.desc())


        result = q.first()
        print('result',result)
        if result:
            res = result.object_to_dict()            
        else:
            res = None
        
        session.close()
        return {
            'result':res        
        }
        
    except Exception as e:
        traceback.print_exc()
        error = e # or it may return "error"
        session.close()
        return {'error': error}


### Closure table ###
# Closure Table is designed to make graph representation easier in column oriented databases. How it works:    
# It extends the _Base model that is empty model, and it adds three columns, one for ancestors and one for children of that ancestor and finally depth of those nodes/children. This speeds up search since you can easily join Nodes with children uid from closure table. This speed is sacrificed for more space used, but storage is cheaper than processing power, hence this is a good solution.

# __table_args defines primary key, which is made of both the ancestor and children uids, that are unique.

class ClosureTable(_Base):

    ancestor_uid = Column(String(36))
    children_uid = Column(String(36))
    depth = Column(Integer, default= 0)
    __table_args__ = (PrimaryKeyConstraint('ancestor_uid', 'children_uid') , {})    
    
    @classmethod
    def add_node(cls, session, ancestor_uid, children_uid):
        try:
            sql = text(
                '''
                INSERT INTO closuretable (ancestor_uid, children_uid, depth)
                SELECT t.ancestor_uid, :new_node_uid, t.depth+1
                FROM closuretable AS t
                WHERE t.children_uid = :parent_uid
                UNION ALL SELECT :new_node_uid, :new_node_uid, 0
                ''')

            sql = sql.bindparams(new_node_uid=children_uid, parent_uid=ancestor_uid)

            session.execute(sql)
            return None
        except Exception as e:
            print("error",e)
            session.rollback()
            session.close()
            return e        
