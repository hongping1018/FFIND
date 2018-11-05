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
# Generated from file `Event.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_model_RTypes_ice
import omero_System_ice
import omero_Collections_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'Experimenter' not in _M_omero.model.__dict__:
    _M_omero.model._t_Experimenter = IcePy.declareClass('::omero::model::Experimenter')
    _M_omero.model._t_ExperimenterPrx = IcePy.declareProxy('::omero::model::Experimenter')

if 'ExperimenterGroup' not in _M_omero.model.__dict__:
    _M_omero.model._t_ExperimenterGroup = IcePy.declareClass('::omero::model::ExperimenterGroup')
    _M_omero.model._t_ExperimenterGroupPrx = IcePy.declareProxy('::omero::model::ExperimenterGroup')

if 'EventType' not in _M_omero.model.__dict__:
    _M_omero.model._t_EventType = IcePy.declareClass('::omero::model::EventType')
    _M_omero.model._t_EventTypePrx = IcePy.declareProxy('::omero::model::EventType')

if 'Event' not in _M_omero.model.__dict__:
    _M_omero.model._t_Event = IcePy.declareClass('::omero::model::Event')
    _M_omero.model._t_EventPrx = IcePy.declareProxy('::omero::model::Event')

if 'EventLog' not in _M_omero.model.__dict__:
    _M_omero.model._t_EventLog = IcePy.declareClass('::omero::model::EventLog')
    _M_omero.model._t_EventLogPrx = IcePy.declareProxy('::omero::model::EventLog')

if 'Session' not in _M_omero.model.__dict__:
    _M_omero.model._t_Session = IcePy.declareClass('::omero::model::Session')
    _M_omero.model._t_SessionPrx = IcePy.declareProxy('::omero::model::Session')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if '_t_EventLogsSeq' not in _M_omero.model.__dict__:
    _M_omero.model._t_EventLogsSeq = IcePy.defineSequence('::omero::model::EventLogsSeq', (), _M_omero.model._t_EventLog)

if 'Event' not in _M_omero.model.__dict__:
    _M_omero.model.Event = Ice.createTempClass()
    class Event(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _status=None, _time=None, _experimenter=None, _experimenterGroup=None, _type=None, _containingEvent=None, _logsSeq=None, _logsLoaded=False, _session=None):
            if Ice.getType(self) == _M_omero.model.Event:
                raise RuntimeError('omero.model.Event is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._status = _status
            self._time = _time
            self._experimenter = _experimenter
            self._experimenterGroup = _experimenterGroup
            self._type = _type
            self._containingEvent = _containingEvent
            self._logsSeq = _logsSeq
            self._logsLoaded = _logsLoaded
            self._session = _session

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Event', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::Event'

        def ice_staticId():
            return '::omero::model::Event'
        ice_staticId = staticmethod(ice_staticId)

        def getStatus(self, current=None):
            pass

        def setStatus(self, theStatus, current=None):
            pass

        def getTime(self, current=None):
            pass

        def setTime(self, theTime, current=None):
            pass

        def getExperimenter(self, current=None):
            pass

        def setExperimenter(self, theExperimenter, current=None):
            pass

        def getExperimenterGroup(self, current=None):
            pass

        def setExperimenterGroup(self, theExperimenterGroup, current=None):
            pass

        def getType(self, current=None):
            pass

        def setType(self, theType, current=None):
            pass

        def getContainingEvent(self, current=None):
            pass

        def setContainingEvent(self, theContainingEvent, current=None):
            pass

        def unloadLogs(self, current=None):
            pass

        def sizeOfLogs(self, current=None):
            pass

        def copyLogs(self, current=None):
            pass

        def addEventLog(self, target, current=None):
            pass

        def addAllEventLogSet(self, targets, current=None):
            pass

        def removeEventLog(self, theTarget, current=None):
            pass

        def removeAllEventLogSet(self, targets, current=None):
            pass

        def clearLogs(self, current=None):
            pass

        def reloadLogs(self, toCopy, current=None):
            pass

        def getSession(self, current=None):
            pass

        def setSession(self, theSession, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Event)

        __repr__ = __str__

    _M_omero.model.EventPrx = Ice.createTempClass()
    class EventPrx(_M_omero.model.IObjectPrx):

        def getStatus(self, _ctx=None):
            return _M_omero.model.Event._op_getStatus.invoke(self, ((), _ctx))

        def begin_getStatus(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getStatus.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getStatus(self, _r):
            return _M_omero.model.Event._op_getStatus.end(self, _r)

        def setStatus(self, theStatus, _ctx=None):
            return _M_omero.model.Event._op_setStatus.invoke(self, ((theStatus, ), _ctx))

        def begin_setStatus(self, theStatus, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setStatus.begin(self, ((theStatus, ), _response, _ex, _sent, _ctx))

        def end_setStatus(self, _r):
            return _M_omero.model.Event._op_setStatus.end(self, _r)

        def getTime(self, _ctx=None):
            return _M_omero.model.Event._op_getTime.invoke(self, ((), _ctx))

        def begin_getTime(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getTime.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getTime(self, _r):
            return _M_omero.model.Event._op_getTime.end(self, _r)

        def setTime(self, theTime, _ctx=None):
            return _M_omero.model.Event._op_setTime.invoke(self, ((theTime, ), _ctx))

        def begin_setTime(self, theTime, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setTime.begin(self, ((theTime, ), _response, _ex, _sent, _ctx))

        def end_setTime(self, _r):
            return _M_omero.model.Event._op_setTime.end(self, _r)

        def getExperimenter(self, _ctx=None):
            return _M_omero.model.Event._op_getExperimenter.invoke(self, ((), _ctx))

        def begin_getExperimenter(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getExperimenter.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getExperimenter(self, _r):
            return _M_omero.model.Event._op_getExperimenter.end(self, _r)

        def setExperimenter(self, theExperimenter, _ctx=None):
            return _M_omero.model.Event._op_setExperimenter.invoke(self, ((theExperimenter, ), _ctx))

        def begin_setExperimenter(self, theExperimenter, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setExperimenter.begin(self, ((theExperimenter, ), _response, _ex, _sent, _ctx))

        def end_setExperimenter(self, _r):
            return _M_omero.model.Event._op_setExperimenter.end(self, _r)

        def getExperimenterGroup(self, _ctx=None):
            return _M_omero.model.Event._op_getExperimenterGroup.invoke(self, ((), _ctx))

        def begin_getExperimenterGroup(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getExperimenterGroup.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getExperimenterGroup(self, _r):
            return _M_omero.model.Event._op_getExperimenterGroup.end(self, _r)

        def setExperimenterGroup(self, theExperimenterGroup, _ctx=None):
            return _M_omero.model.Event._op_setExperimenterGroup.invoke(self, ((theExperimenterGroup, ), _ctx))

        def begin_setExperimenterGroup(self, theExperimenterGroup, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setExperimenterGroup.begin(self, ((theExperimenterGroup, ), _response, _ex, _sent, _ctx))

        def end_setExperimenterGroup(self, _r):
            return _M_omero.model.Event._op_setExperimenterGroup.end(self, _r)

        def getType(self, _ctx=None):
            return _M_omero.model.Event._op_getType.invoke(self, ((), _ctx))

        def begin_getType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getType(self, _r):
            return _M_omero.model.Event._op_getType.end(self, _r)

        def setType(self, theType, _ctx=None):
            return _M_omero.model.Event._op_setType.invoke(self, ((theType, ), _ctx))

        def begin_setType(self, theType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setType.begin(self, ((theType, ), _response, _ex, _sent, _ctx))

        def end_setType(self, _r):
            return _M_omero.model.Event._op_setType.end(self, _r)

        def getContainingEvent(self, _ctx=None):
            return _M_omero.model.Event._op_getContainingEvent.invoke(self, ((), _ctx))

        def begin_getContainingEvent(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getContainingEvent.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getContainingEvent(self, _r):
            return _M_omero.model.Event._op_getContainingEvent.end(self, _r)

        def setContainingEvent(self, theContainingEvent, _ctx=None):
            return _M_omero.model.Event._op_setContainingEvent.invoke(self, ((theContainingEvent, ), _ctx))

        def begin_setContainingEvent(self, theContainingEvent, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setContainingEvent.begin(self, ((theContainingEvent, ), _response, _ex, _sent, _ctx))

        def end_setContainingEvent(self, _r):
            return _M_omero.model.Event._op_setContainingEvent.end(self, _r)

        def unloadLogs(self, _ctx=None):
            return _M_omero.model.Event._op_unloadLogs.invoke(self, ((), _ctx))

        def begin_unloadLogs(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_unloadLogs.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_unloadLogs(self, _r):
            return _M_omero.model.Event._op_unloadLogs.end(self, _r)

        def sizeOfLogs(self, _ctx=None):
            return _M_omero.model.Event._op_sizeOfLogs.invoke(self, ((), _ctx))

        def begin_sizeOfLogs(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_sizeOfLogs.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_sizeOfLogs(self, _r):
            return _M_omero.model.Event._op_sizeOfLogs.end(self, _r)

        def copyLogs(self, _ctx=None):
            return _M_omero.model.Event._op_copyLogs.invoke(self, ((), _ctx))

        def begin_copyLogs(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_copyLogs.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copyLogs(self, _r):
            return _M_omero.model.Event._op_copyLogs.end(self, _r)

        def addEventLog(self, target, _ctx=None):
            return _M_omero.model.Event._op_addEventLog.invoke(self, ((target, ), _ctx))

        def begin_addEventLog(self, target, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_addEventLog.begin(self, ((target, ), _response, _ex, _sent, _ctx))

        def end_addEventLog(self, _r):
            return _M_omero.model.Event._op_addEventLog.end(self, _r)

        def addAllEventLogSet(self, targets, _ctx=None):
            return _M_omero.model.Event._op_addAllEventLogSet.invoke(self, ((targets, ), _ctx))

        def begin_addAllEventLogSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_addAllEventLogSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_addAllEventLogSet(self, _r):
            return _M_omero.model.Event._op_addAllEventLogSet.end(self, _r)

        def removeEventLog(self, theTarget, _ctx=None):
            return _M_omero.model.Event._op_removeEventLog.invoke(self, ((theTarget, ), _ctx))

        def begin_removeEventLog(self, theTarget, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_removeEventLog.begin(self, ((theTarget, ), _response, _ex, _sent, _ctx))

        def end_removeEventLog(self, _r):
            return _M_omero.model.Event._op_removeEventLog.end(self, _r)

        def removeAllEventLogSet(self, targets, _ctx=None):
            return _M_omero.model.Event._op_removeAllEventLogSet.invoke(self, ((targets, ), _ctx))

        def begin_removeAllEventLogSet(self, targets, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_removeAllEventLogSet.begin(self, ((targets, ), _response, _ex, _sent, _ctx))

        def end_removeAllEventLogSet(self, _r):
            return _M_omero.model.Event._op_removeAllEventLogSet.end(self, _r)

        def clearLogs(self, _ctx=None):
            return _M_omero.model.Event._op_clearLogs.invoke(self, ((), _ctx))

        def begin_clearLogs(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_clearLogs.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_clearLogs(self, _r):
            return _M_omero.model.Event._op_clearLogs.end(self, _r)

        def reloadLogs(self, toCopy, _ctx=None):
            return _M_omero.model.Event._op_reloadLogs.invoke(self, ((toCopy, ), _ctx))

        def begin_reloadLogs(self, toCopy, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_reloadLogs.begin(self, ((toCopy, ), _response, _ex, _sent, _ctx))

        def end_reloadLogs(self, _r):
            return _M_omero.model.Event._op_reloadLogs.end(self, _r)

        def getSession(self, _ctx=None):
            return _M_omero.model.Event._op_getSession.invoke(self, ((), _ctx))

        def begin_getSession(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_getSession.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getSession(self, _r):
            return _M_omero.model.Event._op_getSession.end(self, _r)

        def setSession(self, theSession, _ctx=None):
            return _M_omero.model.Event._op_setSession.invoke(self, ((theSession, ), _ctx))

        def begin_setSession(self, theSession, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Event._op_setSession.begin(self, ((theSession, ), _response, _ex, _sent, _ctx))

        def end_setSession(self, _r):
            return _M_omero.model.Event._op_setSession.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.EventPrx.ice_checkedCast(proxy, '::omero::model::Event', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.EventPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Event'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_EventPrx = IcePy.defineProxy('::omero::model::Event', EventPrx)

    _M_omero.model._t_Event = IcePy.defineClass('::omero::model::Event', Event, -1, (), True, False, _M_omero.model._t_IObject, (), (
        ('_status', (), _M_omero._t_RString, False, 0),
        ('_time', (), _M_omero._t_RTime, False, 0),
        ('_experimenter', (), _M_omero.model._t_Experimenter, False, 0),
        ('_experimenterGroup', (), _M_omero.model._t_ExperimenterGroup, False, 0),
        ('_type', (), _M_omero.model._t_EventType, False, 0),
        ('_containingEvent', (), _M_omero.model._t_Event, False, 0),
        ('_logsSeq', (), _M_omero.model._t_EventLogsSeq, False, 0),
        ('_logsLoaded', (), IcePy._t_bool, False, 0),
        ('_session', (), _M_omero.model._t_Session, False, 0)
    ))
    Event._ice_type = _M_omero.model._t_Event

    Event._op_getStatus = IcePy.Operation('getStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    Event._op_setStatus = IcePy.Operation('setStatus', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())
    Event._op_getTime = IcePy.Operation('getTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RTime, False, 0), ())
    Event._op_setTime = IcePy.Operation('setTime', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RTime, False, 0),), (), None, ())
    Event._op_getExperimenter = IcePy.Operation('getExperimenter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Experimenter, False, 0), ())
    Event._op_setExperimenter = IcePy.Operation('setExperimenter', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Experimenter, False, 0),), (), None, ())
    Event._op_getExperimenterGroup = IcePy.Operation('getExperimenterGroup', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ExperimenterGroup, False, 0), ())
    Event._op_setExperimenterGroup = IcePy.Operation('setExperimenterGroup', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ExperimenterGroup, False, 0),), (), None, ())
    Event._op_getType = IcePy.Operation('getType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_EventType, False, 0), ())
    Event._op_setType = IcePy.Operation('setType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_EventType, False, 0),), (), None, ())
    Event._op_getContainingEvent = IcePy.Operation('getContainingEvent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Event, False, 0), ())
    Event._op_setContainingEvent = IcePy.Operation('setContainingEvent', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Event, False, 0),), (), None, ())
    Event._op_unloadLogs = IcePy.Operation('unloadLogs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Event._op_sizeOfLogs = IcePy.Operation('sizeOfLogs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    Event._op_copyLogs = IcePy.Operation('copyLogs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_EventLogsSeq, False, 0), ())
    Event._op_addEventLog = IcePy.Operation('addEventLog', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_EventLog, False, 0),), (), None, ())
    Event._op_addAllEventLogSet = IcePy.Operation('addAllEventLogSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_EventLogsSeq, False, 0),), (), None, ())
    Event._op_removeEventLog = IcePy.Operation('removeEventLog', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_EventLog, False, 0),), (), None, ())
    Event._op_removeAllEventLogSet = IcePy.Operation('removeAllEventLogSet', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_EventLogsSeq, False, 0),), (), None, ())
    Event._op_clearLogs = IcePy.Operation('clearLogs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Event._op_reloadLogs = IcePy.Operation('reloadLogs', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Event, False, 0),), (), None, ())
    Event._op_getSession = IcePy.Operation('getSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Session, False, 0), ())
    Event._op_setSession = IcePy.Operation('setSession', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_Session, False, 0),), (), None, ())

    _M_omero.model.Event = Event
    del Event

    _M_omero.model.EventPrx = EventPrx
    del EventPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
