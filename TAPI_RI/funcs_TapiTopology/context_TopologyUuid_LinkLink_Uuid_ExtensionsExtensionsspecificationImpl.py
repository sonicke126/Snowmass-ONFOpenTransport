import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_TopologyUuid_LinkLink_Uuid_ExtensionsExtensionsspecificationImpl:

    @classmethod
    def get(cls, uuid, link_uuid, extensionsSpecification):
        print 'handling get'
        if uuid in be.Context._topology:
            if link_uuid in be.Context._topology[uuid]._link:
                if extensionsSpecification in be.Context._topology[uuid]._link[link_uuid]._extensions:
                    return be.Context._topology[uuid]._link[link_uuid]._extensions[extensionsSpecification]
                else:
                    raise KeyError('extensionsSpecification')
            else:
                raise KeyError('link_uuid')
        else:
            raise KeyError('uuid')
