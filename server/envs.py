import os


class DjangoConfig:
    def __init__(self):
        self.PROJECT_NAME = 'HOMEWINS'
        self.SECRET_KEY = os.getenv(self.PROJECT_NAME + '_SECRET_KEY', None)
        if os.getenv('DJANGO_MODE') == 'production':
            self.IS_DEBUG = False
        elif os.getenv('DJANGO_MODE') == 'development':
            self.IS_DEBUG = True
        else:
            self.IS_DEBUG = None

        self.DB_NAME = os.getenv(self.PROJECT_NAME + "_DB_DB", None)
        self.DB_USER = os.getenv(self.PROJECT_NAME + "_DB_USER", None)
        self.DB_PASSWORD = os.getenv(self.PROJECT_NAME + "_DB_PASSWORD", None)
        self.DB_HOST = os.getenv(self.PROJECT_NAME + "_DB_HOST", None)
        self.DB_PORT = int(os.getenv(self.PROJECT_NAME + "_DB_PORT", None))

    def check_env(self):
        attrs = [i for i in dir(self) if not i.startswith('_') and i.isupper()]
        for attr in attrs:
            if getattr(self, attr) is None:
                raise Exception('Env \'{}\' is missing.'.format(attr))
