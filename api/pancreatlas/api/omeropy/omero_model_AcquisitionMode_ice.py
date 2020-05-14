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
# Generated from file `AcquisitionMode.ice'
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

# Start of module omero.model.enums
_M_omero.model.enums = Ice.openModule('omero.model.enums')
__name__ = 'omero.model.enums'

_M_omero.model.enums.AcquisitionModeWideField = "WideField"

_M_omero.model.enums.AcquisitionModeLaserScanningConfocalMicroscopy = "LaserScanningConfocalMicroscopy"

_M_omero.model.enums.AcquisitionModeSpinningDiskConfocal = "SpinningDiskConfocal"

_M_omero.model.enums.AcquisitionModeSlitScanConfocal = "SlitScanConfocal"

_M_omero.model.enums.AcquisitionModeMultiPhotonMicroscopy = "MultiPhotonMicroscopy"

_M_omero.model.enums.AcquisitionModeStructuredIllumination = "StructuredIllumination"

_M_omero.model.enums.AcquisitionModeSingleMoleculeImaging = "SingleMoleculeImaging"

_M_omero.model.enums.AcquisitionModeTotalInternalReflection = "TotalInternalReflection"

_M_omero.model.enums.AcquisitionModeFluorescenceLifetime = "FluorescenceLifetime"

_M_omero.model.enums.AcquisitionModeSpectralImaging = "SpectralImaging"

_M_omero.model.enums.AcquisitionModeFluorescenceCorrelationSpectroscopy = "FluorescenceCorrelationSpectroscopy"

_M_omero.model.enums.AcquisitionModeNearFieldScanningOpticalMicroscopy = "NearFieldScanningOpticalMicroscopy"

_M_omero.model.enums.AcquisitionModeSecondHarmonicGenerationImaging = "SecondHarmonicGenerationImaging"

_M_omero.model.enums.AcquisitionModePALM = "PALM"

_M_omero.model.enums.AcquisitionModeSTORM = "STORM"

_M_omero.model.enums.AcquisitionModeSTED = "STED"

_M_omero.model.enums.AcquisitionModeTIRF = "TIRF"

_M_omero.model.enums.AcquisitionModeFSM = "FSM"

_M_omero.model.enums.AcquisitionModeLCM = "LCM"

_M_omero.model.enums.AcquisitionModeOther = "Other"

_M_omero.model.enums.AcquisitionModeUnknown = "Unknown"

_M_omero.model.enums.AcquisitionModeBrightField = "BrightField"

_M_omero.model.enums.AcquisitionModeSweptFieldConfocal = "SweptFieldConfocal"

_M_omero.model.enums.AcquisitionModeSPIM = "SPIM"

# End of module omero.model.enums

__name__ = 'omero.model'

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'AcquisitionMode' not in _M_omero.model.__dict__:
    _M_omero.model.AcquisitionMode = Ice.createTempClass()
    class AcquisitionMode(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _value=None):
            if Ice.getType(self) == _M_omero.model.AcquisitionMode:
                raise RuntimeError('omero.model.AcquisitionMode is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._value = _value

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::AcquisitionMode', '::omero::model::IObject')

        def ice_id(self, current=None):
            return '::omero::model::AcquisitionMode'

        def ice_staticId():
            return '::omero::model::AcquisitionMode'
        ice_staticId = staticmethod(ice_staticId)

        def getValue(self, current=None):
            pass

        def setValue(self, theValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_AcquisitionMode)

        __repr__ = __str__

    _M_omero.model.AcquisitionModePrx = Ice.createTempClass()
    class AcquisitionModePrx(_M_omero.model.IObjectPrx):

        def getValue(self, _ctx=None):
            return _M_omero.model.AcquisitionMode._op_getValue.invoke(self, ((), _ctx))

        def begin_getValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.AcquisitionMode._op_getValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getValue(self, _r):
            return _M_omero.model.AcquisitionMode._op_getValue.end(self, _r)

        def setValue(self, theValue, _ctx=None):
            return _M_omero.model.AcquisitionMode._op_setValue.invoke(self, ((theValue, ), _ctx))

        def begin_setValue(self, theValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.AcquisitionMode._op_setValue.begin(self, ((theValue, ), _response, _ex, _sent, _ctx))

        def end_setValue(self, _r):
            return _M_omero.model.AcquisitionMode._op_setValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.AcquisitionModePrx.ice_checkedCast(proxy, '::omero::model::AcquisitionMode', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.AcquisitionModePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::AcquisitionMode'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_AcquisitionModePrx = IcePy.defineProxy('::omero::model::AcquisitionMode', AcquisitionModePrx)

    _M_omero.model._t_AcquisitionMode = IcePy.declareClass('::omero::model::AcquisitionMode')

    _M_omero.model._t_AcquisitionMode = IcePy.defineClass('::omero::model::AcquisitionMode', AcquisitionMode, -1, (), True, False, _M_omero.model._t_IObject, (), (('_value', (), _M_omero._t_RString, False, 0),))
    AcquisitionMode._ice_type = _M_omero.model._t_AcquisitionMode

    AcquisitionMode._op_getValue = IcePy.Operation('getValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    AcquisitionMode._op_setValue = IcePy.Operation('setValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.AcquisitionMode = AcquisitionMode
    del AcquisitionMode

    _M_omero.model.AcquisitionModePrx = AcquisitionModePrx
    del AcquisitionModePrx

# End of module omero.model

__name__ = 'omero'

# End of module omero
