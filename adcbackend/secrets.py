class ProjectSecretKey:
    project_secret = 'n#^5ij8q6u4a75xsn_e5m&c)6y_e2w9m4gw0@b9^b%jf2a=txp'


class DatabaseSecretLocal:
    name = 'test1'
    user = 'arshan'
    password = 'palindrome'
    host = 'localhost'
    port = '5432'
    engine = 'django.db.backends.postgresql_psycopg2'


class DatabaseSecretCloud:
    name = 'test1'
    user = 'arshan'
    password = 'nomansland'
    host = 'edifi-server-db.chvkllrtnsw8.ap-south-1.rds.amazonaws.com'
    port = '5432'
    engine = 'django.db.backends.postgresql_psycopg2'


class SmsToken:
    secret_key = "564bdadba4cf636cb6b97d98551cd410"
    sid_key = "AC7be6ab07022a5265bc79d0ae59d188f2"
    phone_number = "+12056971226"


class EmailToken:
    from_email = 'onearshanahmad@outlook.com'
    sendgrid_token = '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 '


class Cloud:
    allowed_host = ['ec2-15-206-67-239.ap-south-1.compute.amazonaws.com', 'localhost', '127.0.0.1'
        , 'ec2-13-126-196-234.ap-south-1.compute.amazonaws.com']
