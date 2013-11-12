class AppRouter(object):
    """
    A router to control all database operations on models in the
    myapp application.
    """

    app_name = 'myapp'
    db_name = 'aux_db'

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        if model._meta.app_label == self.app_name:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        if model._meta.app_label == self.app_name:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth app is involved.
        """
        if obj1._meta.app_label == self.app_name or \
           obj2._meta.app_label == self.app_name:
           return True
        return None

    def allow_migrate(self, db, model):
        """
        Make sure the auth app only appears in the self.db_name
        database.
        """
        if db == self.db_name:
            return model._meta.app_label == self.app_name
        elif model._meta.app_label == self.app_name:
            return False
        return None

    def allow_syncdb(self, db, model):
        if db == self.db_name:
            return model._meta.app_label == self.app_name
        elif model._meta.app_label == self.app_name:
            return False
        return None
