# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.3
#
# <auto-generated>
#
# Generated from file `MetadataStore.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import Ice_BuiltinSequences_ice
import omero_ModelF_ice
import omero_ServicesF_ice
import omero_Scripts_ice
import omero_Repositories_ice

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Glacier2
_M_Glacier2 = Ice.openModule('Glacier2')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Included module omero.grid
_M_omero.grid = Ice.openModule('omero.grid')

# Included module omero.cmd
_M_omero.cmd = Ice.openModule('omero.cmd')

# Start of module omero
__name__ = 'omero'

# Start of module omero.constants
_M_omero.constants = Ice.openModule('omero.constants')
__name__ = 'omero.constants'

_M_omero.constants.METADATASTORE = "omero.api.MetadataStore"

# End of module omero.constants

__name__ = 'omero'

# Start of module omero.metadatastore
_M_omero.metadatastore = Ice.openModule('omero.metadatastore')
__name__ = 'omero.metadatastore'
_M_omero.metadatastore.__doc__ = """
Types used during import.
"""

if 'IObjectContainer' not in _M_omero.metadatastore.__dict__:
    _M_omero.metadatastore.IObjectContainer = Ice.createTempClass()
    class IObjectContainer(Ice.Object):
        """
        Container-class used by the import mechanism. Passed to
        omero.api.MetadataStore
        """
        def __init__(self, LSID='', indexes=None, sourceObject=None):
            self.LSID = LSID
            self.indexes = indexes
            self.sourceObject = sourceObject

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::metadatastore::IObjectContainer')

        def ice_id(self, current=None):
            return '::omero::metadatastore::IObjectContainer'

        def ice_staticId():
            return '::omero::metadatastore::IObjectContainer'
        ice_staticId = staticmethod(ice_staticId)

        def __str__(self):
            return IcePy.stringify(self, _M_omero.metadatastore._t_IObjectContainer)

        __repr__ = __str__

    _M_omero.metadatastore.IObjectContainerPrx = Ice.createTempClass()
    class IObjectContainerPrx(Ice.ObjectPrx):

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.metadatastore.IObjectContainerPrx.ice_checkedCast(proxy, '::omero::metadatastore::IObjectContainer', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.metadatastore.IObjectContainerPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::metadatastore::IObjectContainer'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.metadatastore._t_IObjectContainerPrx = IcePy.defineProxy('::omero::metadatastore::IObjectContainer', IObjectContainerPrx)

    _M_omero.metadatastore._t_IObjectContainer = IcePy.declareClass('::omero::metadatastore::IObjectContainer')

    _M_omero.metadatastore._t_IObjectContainer = IcePy.defineClass('::omero::metadatastore::IObjectContainer', IObjectContainer, -1, (), False, False, None, (), (
        ('LSID', (), IcePy._t_string, False, 0),
        ('indexes', (), _M_omero.api._t_StringIntMap, False, 0),
        ('sourceObject', (), _M_omero.model._t_IObject, False, 0)
    ))
    IObjectContainer._ice_type = _M_omero.metadatastore._t_IObjectContainer

    _M_omero.metadatastore.IObjectContainer = IObjectContainer
    del IObjectContainer

    _M_omero.metadatastore.IObjectContainerPrx = IObjectContainerPrx
    del IObjectContainerPrx

if '_t_IObjectContainerArray' not in _M_omero.metadatastore.__dict__:
    _M_omero.metadatastore._t_IObjectContainerArray = IcePy.defineSequence('::omero::metadatastore::IObjectContainerArray', (), _M_omero.metadatastore._t_IObjectContainer)

# End of module omero.metadatastore

__name__ = 'omero'

# Start of module omero.api
__name__ = 'omero.api'

if 'MetadataStore' not in _M_omero.api.__dict__:
    _M_omero.api.MetadataStore = Ice.createTempClass()
    class MetadataStore(_M_omero.api.StatefulServiceInterface):
        """
        Server-side interface for import.
        """
        def __init__(self):
            if Ice.getType(self) == _M_omero.api.MetadataStore:
                raise RuntimeError('omero.api.MetadataStore is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::api::MetadataStore', '::omero::api::ServiceInterface', '::omero::api::StatefulServiceInterface')

        def ice_id(self, current=None):
            return '::omero::api::MetadataStore'

        def ice_staticId():
            return '::omero::api::MetadataStore'
        ice_staticId = staticmethod(ice_staticId)

        def createRoot_async(self, _cb, current=None):
            pass

        def updateObjects_async(self, _cb, objects, current=None):
            pass

        def updateReferences_async(self, _cb, references, current=None):
            pass

        def saveToDB_async(self, _cb, activity, current=None):
            pass

        def populateMinMax_async(self, _cb, imageChannelGlobalMinMax, current=None):
            pass

        def setPixelsFile_async(self, _cb, pixelsId, file, repo, current=None):
            pass

        def postProcess_async(self, _cb, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.api._t_MetadataStore)

        __repr__ = __str__

    _M_omero.api.MetadataStorePrx = Ice.createTempClass()
    class MetadataStorePrx(_M_omero.api.StatefulServiceInterfacePrx):

        def createRoot(self, _ctx=None):
            return _M_omero.api.MetadataStore._op_createRoot.invoke(self, ((), _ctx))

        def begin_createRoot(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_createRoot.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_createRoot(self, _r):
            return _M_omero.api.MetadataStore._op_createRoot.end(self, _r)

        def updateObjects(self, objects, _ctx=None):
            return _M_omero.api.MetadataStore._op_updateObjects.invoke(self, ((objects, ), _ctx))

        def begin_updateObjects(self, objects, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_updateObjects.begin(self, ((objects, ), _response, _ex, _sent, _ctx))

        def end_updateObjects(self, _r):
            return _M_omero.api.MetadataStore._op_updateObjects.end(self, _r)

        def updateReferences(self, references, _ctx=None):
            return _M_omero.api.MetadataStore._op_updateReferences.invoke(self, ((references, ), _ctx))

        def begin_updateReferences(self, references, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_updateReferences.begin(self, ((references, ), _response, _ex, _sent, _ctx))

        def end_updateReferences(self, _r):
            return _M_omero.api.MetadataStore._op_updateReferences.end(self, _r)

        def saveToDB(self, activity, _ctx=None):
            return _M_omero.api.MetadataStore._op_saveToDB.invoke(self, ((activity, ), _ctx))

        def begin_saveToDB(self, activity, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_saveToDB.begin(self, ((activity, ), _response, _ex, _sent, _ctx))

        def end_saveToDB(self, _r):
            return _M_omero.api.MetadataStore._op_saveToDB.end(self, _r)

        def populateMinMax(self, imageChannelGlobalMinMax, _ctx=None):
            return _M_omero.api.MetadataStore._op_populateMinMax.invoke(self, ((imageChannelGlobalMinMax, ), _ctx))

        def begin_populateMinMax(self, imageChannelGlobalMinMax, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_populateMinMax.begin(self, ((imageChannelGlobalMinMax, ), _response, _ex, _sent, _ctx))

        def end_populateMinMax(self, _r):
            return _M_omero.api.MetadataStore._op_populateMinMax.end(self, _r)

        def setPixelsFile(self, pixelsId, file, repo, _ctx=None):
            return _M_omero.api.MetadataStore._op_setPixelsFile.invoke(self, ((pixelsId, file, repo), _ctx))

        def begin_setPixelsFile(self, pixelsId, file, repo, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_setPixelsFile.begin(self, ((pixelsId, file, repo), _response, _ex, _sent, _ctx))

        def end_setPixelsFile(self, _r):
            return _M_omero.api.MetadataStore._op_setPixelsFile.end(self, _r)

        def postProcess(self, _ctx=None):
            return _M_omero.api.MetadataStore._op_postProcess.invoke(self, ((), _ctx))

        def begin_postProcess(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.api.MetadataStore._op_postProcess.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_postProcess(self, _r):
            return _M_omero.api.MetadataStore._op_postProcess.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.api.MetadataStorePrx.ice_checkedCast(proxy, '::omero::api::MetadataStore', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.api.MetadataStorePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::api::MetadataStore'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.api._t_MetadataStorePrx = IcePy.defineProxy('::omero::api::MetadataStore', MetadataStorePrx)

    _M_omero.api._t_MetadataStore = IcePy.defineClass('::omero::api::MetadataStore', MetadataStore, -1, (), True, False, None, (_M_omero.api._t_StatefulServiceInterface,), ())
    MetadataStore._ice_type = _M_omero.api._t_MetadataStore

    MetadataStore._op_createRoot = IcePy.Operation('createRoot', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (), (), None, (_M_omero._t_ServerError,))
    MetadataStore._op_updateObjects = IcePy.Operation('updateObjects', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.metadatastore._t_IObjectContainerArray, False, 0),), (), None, (_M_omero._t_ServerError,))
    MetadataStore._op_updateReferences = IcePy.Operation('updateReferences', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.api._t_StringStringArrayMap, False, 0),), (), None, (_M_omero._t_ServerError,))
    MetadataStore._op_saveToDB = IcePy.Operation('saveToDB', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.model._t_FilesetJobLink, False, 0),), (), ((), _M_omero.api._t_IObjectListMap, False, 0), (_M_omero._t_ServerError,))
    MetadataStore._op_populateMinMax = IcePy.Operation('populateMinMax', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (((), _M_omero.api._t_DoubleArrayArrayArray, False, 0),), (), None, (_M_omero._t_ServerError,))
    MetadataStore._op_setPixelsFile = IcePy.Operation('setPixelsFile', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, True, None, (), (((), IcePy._t_long, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), None, (_M_omero._t_ServerError,))
    MetadataStore._op_postProcess = IcePy.Operation('postProcess', Ice.OperationMode.Normal, Ice.OperationMode.Normal, True, None, (), (), (), ((), _M_omero.grid._t_InteractiveProcessorList, False, 0), (_M_omero._t_ServerError,))

    _M_omero.api.MetadataStore = MetadataStore
    del MetadataStore

    _M_omero.api.MetadataStorePrx = MetadataStorePrx
    del MetadataStorePrx

# End of module omero.api

__name__ = 'omero'

# End of module omero
