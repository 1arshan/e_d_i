class ProjectSecretKey:
    project_secret = 'n#^5ij8q6u4a75xsn_e5m&c)6y_e2w9m4gw0@b9^b%jf2a=txp'


class DatabaseSecret:
    name = 'edifi_database'
    user = 'arshan'
    password = 'postgres'
    host = 'localhost'
    port = '5432'
    engine = 'django.db.backends.postgresql_psycopg2'


class SmsToken:
    secret_key = "0a5cff8944545d919a3ba5f3a38be391"
    sid_key = "AC7be6ab07022a5265bc79d0ae59d188f2"
    phone_number = "+12056971226"


class EmailToken:
    from_email = 'onearshanahmad@outlook.com'
    sendgrid_token = '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 '