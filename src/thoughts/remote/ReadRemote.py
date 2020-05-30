from firebase_admin import firestore


class ReadRemote:

    def __init__(self, db):
        self.db = db
        self.collection = db.collection("hello")

    def get_remote_data(self):
        return self.collection.document("test").get()
