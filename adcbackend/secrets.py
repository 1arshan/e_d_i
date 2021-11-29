class ProjectSecretKey:
    project_secret = 'n#^5ij8q6u4a75xsn_e5m&c)6y_e2jf2a=txp'


class DatabaseSecretLocal:
    name = 'test1'
    user = 'arshan'
    password = 'paome'
    host = 'localhost'
    port = '5432'
    engine = 'django.db.backends.postgresql_psycopg2'


"""
class DatabaseSecretCloud:
    name = 'test1'
    user = 'arshan'
    password = 'nomansland'
    host = 'edifi-server-db.chvkllrtnsw8.ap-south-1.rds.amazonaws.com'
    port = '5432'
    engine = 'django.db.backends.postgresql_psycopg2'
"""


class DatabaseSecretCloud:
    name = 'test1'
    user = 'arshan'
    password = 'nomansland'
    host = 'edifi-server-db.c5tuhbzowmw5.ap-south-1.rds.amazonaws.com'
    port = '5432'
    engine = 'django.db.backends.postgresql_psycopg2'


class SmsToken:
    secret_key = "564bdadba4cf68551cd410"
    sid_key = "AC7be6ab065bc79d0ae59d188f2"
    phone_number = "+1206"


class EmailToken:
    from_email = 'nahmad@outlook.com'
    sendgrid_token = 'SG.Sqg7JP48TK2cKzBbTBYsSA.JQBWqvUq9vWicR11wOSCl9p8czWs '


class Cloud:
    allowed_host = ['ec2-15-206-67-239.ap-south-1.amazonaws.com',
                    'ec2-15-206-153-238.ap-south-1amazonaws.com', 'localhost', '127.0.0.1']


class Jwt:
    signing_key = "h77qfnbmydu9=f0k0o4=-oxkpf#@ee6_!l)@ku7"
