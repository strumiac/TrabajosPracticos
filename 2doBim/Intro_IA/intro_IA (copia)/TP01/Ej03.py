import numpy as np

class UsersID(object):

  def __init__(self):
    users_id  = np.array([15,12,14,10,1,2,1])
    users_idx = np.array([ 0, 1, 2, 3,4,5,4])
    self.id, self.idx = np.unique(users_id, return_index = True)

  def id2idx (self, user_id):
    if self.idx[self.id == user_id].size > 0:
      index = self.idx[self.id == user_id][0]
    else:
      index = -1
    print ('El usuario', user_id,'tiene el indice', index)
    return

  def idx2id (self, user_idx):
    if self.id[self.idx == user_idx].size > 0:
      usu = self.id[self.idx == user_idx][0]
    else:
      usu = -1
    print ('El indice', user_idx,'pertenece al usuario', usu)
    return

usuario=UsersID()
usuario.idx2id(3)
usuario.id2idx(10)
