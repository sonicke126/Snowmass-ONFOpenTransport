import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathUuidImpl:

    @classmethod
    def get(cls, uuid):
        print 'handling get'
        if uuid in be.Context._path:
            return be.Context._path[uuid]
        else:
            raise KeyError('uuid')
