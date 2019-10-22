import pickle

from msilib.schema import File


class FileManager:
   def _init_(self, filename):
        self.filename = filename

   def save(self, data):
        f = open(self.filename,"wb")
        pickle.dump(data, f)
        f.close()

   def load(self):
        try:
            f = open(self.filename,"rb")
            data = pickle.load(f)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError
        return data
