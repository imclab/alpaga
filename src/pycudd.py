# This file was created automatically by SWIG 1.3.28.
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

"""
PyCUDD 2.0.1
Python interface to Colorado University Decision Diagram package
With BREL support
Compiled on Mar  1 2007, 11:50:04
Bugs to:aravind@engr.ucsb.edu
"""

import _pycudd
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


DOCSTRING = _pycudd.DOCSTRING
class RangeError(_object):
    """Proxy of C++ RangeError class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, RangeError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RangeError, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ RangeError instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        """__init__(self) -> RangeError"""
        this = _pycudd.new_RangeError(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_RangeError
    __del__ = lambda self : None;
_pycudd.RangeError_swigregister(RangeError)
cvar = _pycudd.cvar

class IntArray(_object):
    """Proxy of C++ IntArray class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, IntArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntArray, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ IntArray instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["vec"] = _pycudd.IntArray_vec_set
    __swig_getmethods__["vec"] = _pycudd.IntArray_vec_get
    if _newclass:vec = property(_pycudd.IntArray_vec_get, _pycudd.IntArray_vec_set)
    def __init__(self, *args):
        """__init__(self, int size) -> IntArray"""
        this = _pycudd.new_IntArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_IntArray
    __del__ = lambda self : None;
    def AssignVect(*args):
        """AssignVect(self, int str, int size)"""
        return _pycudd.IntArray_AssignVect(*args)

    def AssignComplVect(*args):
        """AssignComplVect(self, int str, int size, int univ)"""
        return _pycudd.IntArray_AssignComplVect(*args)

    def ArrayAddress(*args):
        """ArrayAddress(self) -> int"""
        return _pycudd.IntArray_ArrayAddress(*args)

    def __getitem__(*args):
        """__getitem__(self, int j) -> int"""
        return _pycudd.IntArray___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int j, int val)"""
        return _pycudd.IntArray___setitem__(*args)

    def __len__(*args):
        """__len__(self) -> int"""
        return _pycudd.IntArray___len__(*args)

    def Assign(*args):
        """Assign(self, int list, int k)"""
        return _pycudd.IntArray_Assign(*args)

    def Swap(*args):
        """Swap(self, int i, int j)"""
        return _pycudd.IntArray_Swap(*args)

_pycudd.IntArray_swigregister(IntArray)

class StringArray(_object):
    """Proxy of C++ StringArray class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, StringArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringArray, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ StringArray instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["vec"] = _pycudd.StringArray_vec_set
    __swig_getmethods__["vec"] = _pycudd.StringArray_vec_get
    if _newclass:vec = property(_pycudd.StringArray_vec_get, _pycudd.StringArray_vec_set)
    def __init__(self, *args):
        """__init__(self, int size) -> StringArray"""
        this = _pycudd.new_StringArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_StringArray
    __del__ = lambda self : None;
    def ArrayAddress(*args):
        """ArrayAddress(self) -> char"""
        return _pycudd.StringArray_ArrayAddress(*args)

    def __getitem__(*args):
        """__getitem__(self, int j) -> char"""
        return _pycudd.StringArray___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int j, char val)"""
        return _pycudd.StringArray___setitem__(*args)

    def __len__(*args):
        """__len__(self) -> int"""
        return _pycudd.StringArray___len__(*args)

    def Assign(*args):
        """Assign(self, char list, int k)"""
        return _pycudd.StringArray_Assign(*args)

    def Swap(*args):
        """Swap(self, int i, int j)"""
        return _pycudd.StringArray_Swap(*args)

_pycudd.StringArray_swigregister(StringArray)

class DoubleArray(_object):
    """Proxy of C++ DoubleArray class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, DoubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleArray, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ DoubleArray instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_setmethods__["vec"] = _pycudd.DoubleArray_vec_set
    __swig_getmethods__["vec"] = _pycudd.DoubleArray_vec_get
    if _newclass:vec = property(_pycudd.DoubleArray_vec_get, _pycudd.DoubleArray_vec_set)
    def __init__(self, *args):
        """__init__(self, int size) -> DoubleArray"""
        this = _pycudd.new_DoubleArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_DoubleArray
    __del__ = lambda self : None;
    def __getitem__(*args):
        """__getitem__(self, int j) -> double"""
        return _pycudd.DoubleArray___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int j, double val)"""
        return _pycudd.DoubleArray___setitem__(*args)

    def Assign(*args):
        """Assign(self, double list, int k)"""
        return _pycudd.DoubleArray_Assign(*args)

    def Swap(*args):
        """Swap(self, int i, int j)"""
        return _pycudd.DoubleArray_Swap(*args)

_pycudd.DoubleArray_swigregister(DoubleArray)

class DdArray(_object):
    """Proxy of C++ DdArray class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, DdArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DdArray, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ DdArray instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __doc__ = "This class provides an array of DdNodes. This is an addition to the CUDD package. Create a DdArray by calling the constructor with the length of the array. In terms of Python array-like behaviour, you can index it, assign individual elements and take its length. Typically, these arrays are populated via the Push method. Refer pycudd.h and pycudd.cpp for function details.<br>"

    __swig_setmethods__["sz"] = _pycudd.DdArray_sz_set
    __swig_getmethods__["sz"] = _pycudd.DdArray_sz_get
    if _newclass:sz = property(_pycudd.DdArray_sz_get, _pycudd.DdArray_sz_set)
    __swig_setmethods__["vec"] = _pycudd.DdArray_vec_set
    __swig_getmethods__["vec"] = _pycudd.DdArray_vec_get
    if _newclass:vec = property(_pycudd.DdArray_vec_get, _pycudd.DdArray_vec_set)
    def __init__(self, *args):
        """__init__(self, int size) -> DdArray"""
        this = _pycudd.new_DdArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_DdArray
    __del__ = lambda self : None;
    def __getitem__(*args):
        """__getitem__(self, int j) -> DdNode"""
        return _pycudd.DdArray___getitem__(*args)

    def __setitem__(*args):
        """__setitem__(self, int j, DdNode val)"""
        return _pycudd.DdArray___setitem__(*args)

    def __len__(*args):
        """__len__(self) -> int"""
        return _pycudd.DdArray___len__(*args)

    def Swap(*args):
        """Swap(self, int i, int j)"""
        return _pycudd.DdArray_Swap(*args)

    def Pop(*args):
        """Pop(self) -> DdNode"""
        return _pycudd.DdArray_Pop(*args)

    def And(*args):
        """And(self) -> DdNode"""
        return _pycudd.DdArray_And(*args)

    def Or(*args):
        """Or(self) -> DdNode"""
        return _pycudd.DdArray_Or(*args)

    def AtLeastN(*args):
        """AtLeastN(self, int n) -> DdNode"""
        return _pycudd.DdArray_AtLeastN(*args)

    def ExactlyN(*args):
        """ExactlyN(self, int n) -> DdNode"""
        return _pycudd.DdArray_ExactlyN(*args)

    def UpToN(*args):
        """UpToN(self, int n) -> DdNode"""
        return _pycudd.DdArray_UpToN(*args)

    def Constraint(*args):
        """Constraint(self, int low, int high) -> DdNode"""
        return _pycudd.DdArray_Constraint(*args)

    def Compose(*args):
        """Compose(self, DdNode term) -> DdNode"""
        return _pycudd.DdArray_Compose(*args)

    def Assign(*args):
        """Assign(self, DdNode list, int k)"""
        return _pycudd.DdArray_Assign(*args)

    def Push(*args):
        """Push(self, DdNode val)"""
        return _pycudd.DdArray_Push(*args)

    def SwapNodes(*args):
        """SwapNodes(self, int i, int j)"""
        return _pycudd.DdArray_SwapNodes(*args)

    def Fill(*args):
        """Fill(self, int offset, int mod)"""
        return _pycudd.DdArray_Fill(*args)

    def FillWithIntArray(*args):
        """FillWithIntArray(self, IntArray t)"""
        return _pycudd.DdArray_FillWithIntArray(*args)

    def OrderVector(*args):
        """OrderVector(self, int left, int right)"""
        return _pycudd.DdArray_OrderVector(*args)

    def SupportVector(*args):
        """SupportVector(self, DdNode term)"""
        return _pycudd.DdArray_SupportVector(*args)

    def SetVarMap(*args):
        """SetVarMap(self, DdArray other) -> int"""
        return _pycudd.DdArray_SetVarMap(*args)

    def VectorSupport(*args):
        """VectorSupport(self) -> DdNode"""
        return _pycudd.DdArray_VectorSupport(*args)

    def VectorSupportIndex(*args):
        """VectorSupportIndex(self, int dum_sup) -> int"""
        return _pycudd.DdArray_VectorSupportIndex(*args)

    def PickOneMinterm(*args):
        """PickOneMinterm(self, DdNode term) -> DdNode"""
        return _pycudd.DdArray_PickOneMinterm(*args)

    def HoldTR(*args):
        """HoldTR(self, DdArray other) -> DdNode"""
        return _pycudd.DdArray_HoldTR(*args)

    def Find(*args):
        """Find(self, DdNode term) -> int"""
        return _pycudd.DdArray_Find(*args)

    def Save(*args):
        """Save(self, char filename) -> int"""
        return _pycudd.DdArray_Save(*args)

    def SaveText(*args):
        """SaveText(self, char filename) -> int"""
        return _pycudd.DdArray_SaveText(*args)

    def Load(*args):
        """Load(self, char filename) -> int"""
        return _pycudd.DdArray_Load(*args)

    def LoadText(*args):
        """LoadText(self, char filename) -> int"""
        return _pycudd.DdArray_LoadText(*args)

    def ArrayLoad(*args):
        """
        ArrayLoad(self, int rootmatchmode, StringArray rootmatchnames, int varmatchmode, 
            StringArray varmatchnames, IntArray varmatchauxids, 
            IntArray varcomposeids, 
            int mode, char filename, FILE fp=None) -> int
        ArrayLoad(self, int rootmatchmode, StringArray rootmatchnames, int varmatchmode, 
            StringArray varmatchnames, IntArray varmatchauxids, 
            IntArray varcomposeids, 
            int mode, char filename) -> int
        """
        return _pycudd.DdArray_ArrayLoad(*args)

    def ArrayStore(*args):
        """
        ArrayStore(self, char ddname, StringArray rootnames, StringArray varnames, 
            IntArray auxids, int mode, int varinfo, 
            char filename, FILE fp=None) -> int
        ArrayStore(self, char ddname, StringArray rootnames, StringArray varnames, 
            IntArray auxids, int mode, int varinfo, 
            char filename) -> int
        """
        return _pycudd.DdArray_ArrayStore(*args)

_pycudd.DdArray_swigregister(DdArray)

class MtrNode(_object):
    """Proxy of C++ MtrNode class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, MtrNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MtrNode, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ MtrNode instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        """__init__(self) -> MtrNode"""
        this = _pycudd.new_MtrNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_MtrNode
    __del__ = lambda self : None;
_pycudd.MtrNode_swigregister(MtrNode)

class DdTlcInfo(_object):
    """Proxy of C++ DdTlcInfo class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, DdTlcInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DdTlcInfo, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ DdTlcInfo instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __doc__ = "Helper class for enumeration of two literal clauses. Look at example2.py for usage."

    def __init__(self, *args):
        """__init__(self) -> DdTlcInfo"""
        this = _pycudd.new_DdTlcInfo(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_DdTlcInfo
    __del__ = lambda self : None;
    def ReadIthClause(*args):
        """
        ReadIthClause(self, int i, DdHalfWord dum_var1, DdHalfWord dum_var2, int dum_phase1, 
            int dum_phase2) -> int
        """
        return _pycudd.DdTlcInfo_ReadIthClause(*args)

_pycudd.DdTlcInfo_swigregister(DdTlcInfo)

class EpDouble(_object):
    """Proxy of C++ EpDouble class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, EpDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EpDouble, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ EpDouble instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __doc__ = "This provides the functionality of CUDD's extended precision library. In particular, instances of EpDouble may be passed to DdNode.EpdCountMinterm to retrieve the extended counts. Note also that the basic arithmetic operators (+,-,*,/) have been overloaded for use with EpDouble instances"

    def __init__(self, *args):
        """
        __init__(self) -> EpDouble
        __init__(self, double value) -> EpDouble
        __init__(self, EpDouble value) -> EpDouble
        """
        this = _pycudd.new_EpDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_EpDouble
    __del__ = lambda self : None;
    def EpdConvert(*args):
        """EpdConvert(self, double value)"""
        return _pycudd.EpDouble_EpdConvert(*args)

    def EpdNormalize(*args):
        """EpdNormalize(self)"""
        return _pycudd.EpDouble_EpdNormalize(*args)

    def EpdNormalizeDecimal(*args):
        """EpdNormalizeDecimal(self)"""
        return _pycudd.EpDouble_EpdNormalizeDecimal(*args)

    def EpdMakeInf(*args):
        """EpdMakeInf(self, int sign)"""
        return _pycudd.EpDouble_EpdMakeInf(*args)

    def EpdMakeZero(*args):
        """EpdMakeZero(self, int sign)"""
        return _pycudd.EpDouble_EpdMakeZero(*args)

    def EpdMakeNan(*args):
        """EpdMakeNan(self)"""
        return _pycudd.EpDouble_EpdMakeNan(*args)

    def EpdCopy(*args):
        """EpdCopy(self, EpDouble to)"""
        return _pycudd.EpDouble_EpdCopy(*args)

    def EpdGetValueAndDecimalExponent(*args):
        """EpdGetValueAndDecimalExponent(self, double dum_value, int dum_exponent)"""
        return _pycudd.EpDouble_EpdGetValueAndDecimalExponent(*args)

    def EpdMultiply(*args):
        """EpdMultiply(self, double value)"""
        return _pycudd.EpDouble_EpdMultiply(*args)

    def EpdMultiply2(*args):
        """EpdMultiply2(self, EpDouble epd2)"""
        return _pycudd.EpDouble_EpdMultiply2(*args)

    def EpdMultiply2Decimal(*args):
        """EpdMultiply2Decimal(self, EpDouble epd2)"""
        return _pycudd.EpDouble_EpdMultiply2Decimal(*args)

    def EpdMultiply3(*args):
        """EpdMultiply3(self, EpDouble epd2, EpDouble epd3)"""
        return _pycudd.EpDouble_EpdMultiply3(*args)

    def EpdMultiply3Decimal(*args):
        """EpdMultiply3Decimal(self, EpDouble epd2, EpDouble epd3)"""
        return _pycudd.EpDouble_EpdMultiply3Decimal(*args)

    def EpdDivide(*args):
        """EpdDivide(self, double value)"""
        return _pycudd.EpDouble_EpdDivide(*args)

    def EpdDivide2(*args):
        """EpdDivide2(self, EpDouble epd2)"""
        return _pycudd.EpDouble_EpdDivide2(*args)

    def EpdDivide3(*args):
        """EpdDivide3(self, EpDouble epd2, EpDouble epd3)"""
        return _pycudd.EpDouble_EpdDivide3(*args)

    def EpdAdd(*args):
        """EpdAdd(self, double value)"""
        return _pycudd.EpDouble_EpdAdd(*args)

    def EpdAdd2(*args):
        """EpdAdd2(self, EpDouble epd2)"""
        return _pycudd.EpDouble_EpdAdd2(*args)

    def EpdAdd3(*args):
        """EpdAdd3(self, EpDouble epd2, EpDouble epd3)"""
        return _pycudd.EpDouble_EpdAdd3(*args)

    def EpdSubtract(*args):
        """EpdSubtract(self, double value)"""
        return _pycudd.EpDouble_EpdSubtract(*args)

    def EpdSubtract2(*args):
        """EpdSubtract2(self, EpDouble epd2)"""
        return _pycudd.EpDouble_EpdSubtract2(*args)

    def EpdSubtract3(*args):
        """EpdSubtract3(self, EpDouble epd2, EpDouble epd3)"""
        return _pycudd.EpDouble_EpdSubtract3(*args)

    def EpdPow2(*args):
        """EpdPow2(self, int n)"""
        return _pycudd.EpDouble_EpdPow2(*args)

    def EpdPow2Decimal(*args):
        """EpdPow2Decimal(self, int n)"""
        return _pycudd.EpDouble_EpdPow2Decimal(*args)

    def __add__(*args):
        """
        __add__(self, EpDouble other) -> EpDouble
        __add__(self, double other) -> EpDouble
        """
        return _pycudd.EpDouble___add__(*args)

    def __sub__(*args):
        """
        __sub__(self, EpDouble other) -> EpDouble
        __sub__(self, double other) -> EpDouble
        """
        return _pycudd.EpDouble___sub__(*args)

    def __mul__(*args):
        """
        __mul__(self, EpDouble other) -> EpDouble
        __mul__(self, double other) -> EpDouble
        """
        return _pycudd.EpDouble___mul__(*args)

    def __div__(*args):
        """
        __div__(self, EpDouble other) -> EpDouble
        __div__(self, double other) -> EpDouble
        """
        return _pycudd.EpDouble___div__(*args)

    def EpdCmp(*args):
        """EpdCmp(self, EpDouble other) -> bool"""
        return _pycudd.EpDouble_EpdCmp(*args)

    def EpdIsInf(*args):
        """EpdIsInf(self) -> bool"""
        return _pycudd.EpDouble_EpdIsInf(*args)

    def EpdIsZero(*args):
        """EpdIsZero(self) -> bool"""
        return _pycudd.EpDouble_EpdIsZero(*args)

    def EpdIsNan(*args):
        """EpdIsNan(self) -> bool"""
        return _pycudd.EpDouble_EpdIsNan(*args)

    def EpdIsNanOrInf(*args):
        """EpdIsNanOrInf(self) -> bool"""
        return _pycudd.EpDouble_EpdIsNanOrInf(*args)

    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _pycudd.EpDouble___nonzero__(*args)

    def __eq__(*args):
        """__eq__(self, EpDouble other) -> bool"""
        return _pycudd.EpDouble___eq__(*args)

    def __ne__(*args):
        """__ne__(self, EpDouble other) -> bool"""
        return _pycudd.EpDouble___ne__(*args)

_pycudd.EpDouble_swigregister(EpDouble)


def EpdGetExponent(*args):
    """EpdGetExponent(double value) -> int"""
    return _pycudd.EpdGetExponent(*args)

def EpdGetExponentDecimal(*args):
    """EpdGetExponentDecimal(double value) -> int"""
    return _pycudd.EpdGetExponentDecimal(*args)

def IsInfDouble(*args):
    """IsInfDouble(double value) -> bool"""
    return _pycudd.IsInfDouble(*args)

def IsNanDouble(*args):
    """IsNanDouble(double value) -> bool"""
    return _pycudd.IsNanDouble(*args)

def IsNanOrInfDouble(*args):
    """IsNanOrInfDouble(double value) -> bool"""
    return _pycudd.IsNanOrInfDouble(*args)
class DdManager(_object):
    """Proxy of C++ DdManager class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, DdManager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DdManager, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ DdManager instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __doc__ = "This class wraps around the DdManager. The methods defined by this class provide themselves as the DdManager option (if needed). To use PyCUDD, you must have at least one DdManager instance and you must set DdManager.SetDefault before using any of the other functions. These functions are provided through ddmanager.i."

    def __init__(self, *args):
        """
        __init__(self, unsigned int numVars=0, unsigned int numVarsZ=0, unsigned int numSlots=CUDD_UNIQUE_SLOTS, 
            unsigned int cacheSize=CUDD_CACHE_SLOTS, 
            unsigned long maxMemory=0) -> DdManager
        __init__(self, unsigned int numVars=0, unsigned int numVarsZ=0, unsigned int numSlots=CUDD_UNIQUE_SLOTS, 
            unsigned int cacheSize=CUDD_CACHE_SLOTS) -> DdManager
        __init__(self, unsigned int numVars=0, unsigned int numVarsZ=0, unsigned int numSlots=CUDD_UNIQUE_SLOTS) -> DdManager
        __init__(self, unsigned int numVars=0, unsigned int numVarsZ=0) -> DdManager
        __init__(self, unsigned int numVars=0) -> DdManager
        __init__(self) -> DdManager
        """
        this = _pycudd.new_DdManager(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_DdManager
    __del__ = lambda self : None;
    def KillNode(*args):
        """KillNode(self, long num)"""
        return _pycudd.DdManager_KillNode(*args)

    def IsPsVar(*args):
        """IsPsVar(self, int index) -> int"""
        return _pycudd.DdManager_IsPsVar(*args)

    def IsNsVar(*args):
        """IsNsVar(self, int index) -> int"""
        return _pycudd.DdManager_IsNsVar(*args)

    def SetPsVar(*args):
        """SetPsVar(self, int index) -> int"""
        return _pycudd.DdManager_SetPsVar(*args)

    def SetNsVar(*args):
        """SetNsVar(self, int index) -> int"""
        return _pycudd.DdManager_SetNsVar(*args)

    def SetPairIndex(*args):
        """SetPairIndex(self, int index, int pairIndex) -> int"""
        return _pycudd.DdManager_SetPairIndex(*args)

    def ReadPairIndex(*args):
        """ReadPairIndex(self, int index) -> int"""
        return _pycudd.DdManager_ReadPairIndex(*args)

    def SetVarToBeGrouped(*args):
        """SetVarToBeGrouped(self, int index) -> int"""
        return _pycudd.DdManager_SetVarToBeGrouped(*args)

    def SetVarHardGroup(*args):
        """SetVarHardGroup(self, int index) -> int"""
        return _pycudd.DdManager_SetVarHardGroup(*args)

    def ResetVarToBeGrouped(*args):
        """ResetVarToBeGrouped(self, int index) -> int"""
        return _pycudd.DdManager_ResetVarToBeGrouped(*args)

    def IsVarToBeGrouped(*args):
        """IsVarToBeGrouped(self, int index) -> int"""
        return _pycudd.DdManager_IsVarToBeGrouped(*args)

    def IsVarHardGroup(*args):
        """IsVarHardGroup(self, int index) -> int"""
        return _pycudd.DdManager_IsVarHardGroup(*args)

    def SetVarToBeUngrouped(*args):
        """SetVarToBeUngrouped(self, int index) -> int"""
        return _pycudd.DdManager_SetVarToBeUngrouped(*args)

    def IsVarToBeUngrouped(*args):
        """IsVarToBeUngrouped(self, int index) -> int"""
        return _pycudd.DdManager_IsVarToBeUngrouped(*args)

    def SetPiVar(*args):
        """SetPiVar(self, int index) -> int"""
        return _pycudd.DdManager_SetPiVar(*args)

    def IsPiVar(*args):
        """IsPiVar(self, int index) -> int"""
        return _pycudd.DdManager_IsPiVar(*args)

    def BindVar(*args):
        """BindVar(self, int index) -> int"""
        return _pycudd.DdManager_BindVar(*args)

    def UnbindVar(*args):
        """UnbindVar(self, int index) -> int"""
        return _pycudd.DdManager_UnbindVar(*args)

    def VarIsBound(*args):
        """VarIsBound(self, int index) -> int"""
        return _pycudd.DdManager_VarIsBound(*args)

    def ReadMaxGrowthAlternate(*args):
        """ReadMaxGrowthAlternate(self) -> double"""
        return _pycudd.DdManager_ReadMaxGrowthAlternate(*args)

    def SetMaxGrowthAlternate(*args):
        """SetMaxGrowthAlternate(self, double mg)"""
        return _pycudd.DdManager_SetMaxGrowthAlternate(*args)

    def ReadReorderingCycle(*args):
        """ReadReorderingCycle(self) -> int"""
        return _pycudd.DdManager_ReadReorderingCycle(*args)

    def SetReorderingCycle(*args):
        """SetReorderingCycle(self, int cycle)"""
        return _pycudd.DdManager_SetReorderingCycle(*args)

    def PrintCover(*args):
        """PrintCover(self, DdNode l, DdNode u) -> int"""
        return _pycudd.DdManager_PrintCover(*args)

    def Prime(*args):
        """Prime(self, unsigned int p) -> unsigned int"""
        return _pycudd.DdManager_Prime(*args)

    def __len__(*args):
        """__len__(self) -> int"""
        return _pycudd.DdManager___len__(*args)

    def __getitem__(*args):
        """__getitem__(self, int i) -> DdNode"""
        return _pycudd.DdManager___getitem__(*args)

    def addNewVar(*args):
        """addNewVar(self) -> DdNode"""
        return _pycudd.DdManager_addNewVar(*args)

    def addNewVarAtLevel(*args):
        """addNewVarAtLevel(self, int level) -> DdNode"""
        return _pycudd.DdManager_addNewVarAtLevel(*args)

    def NewVar(*args):
        """NewVar(self) -> DdNode"""
        return _pycudd.DdManager_NewVar(*args)

    def NewVarAtLevel(*args):
        """NewVarAtLevel(self, int level) -> DdNode"""
        return _pycudd.DdManager_NewVarAtLevel(*args)

    def addIthVar(*args):
        """addIthVar(self, int i) -> DdNode"""
        return _pycudd.DdManager_addIthVar(*args)

    def IthVar(*args):
        """IthVar(self, int i) -> DdNode"""
        return _pycudd.DdManager_IthVar(*args)

    def zddIthVar(*args):
        """zddIthVar(self, int i) -> DdNode"""
        return _pycudd.DdManager_zddIthVar(*args)

    def zddVarsFromBddVars(*args):
        """zddVarsFromBddVars(self, int multiplicity) -> int"""
        return _pycudd.DdManager_zddVarsFromBddVars(*args)

    def addConst(*args):
        """addConst(self, CUDD_VALUE_TYPE c) -> DdNode"""
        return _pycudd.DdManager_addConst(*args)

    def AutodynEnable(*args):
        """AutodynEnable(self, int method)"""
        return _pycudd.DdManager_AutodynEnable(*args)

    def AutodynDisable(*args):
        """AutodynDisable(self)"""
        return _pycudd.DdManager_AutodynDisable(*args)

    def ReorderingStatus(*args):
        """ReorderingStatus(self, int dum_status) -> int"""
        return _pycudd.DdManager_ReorderingStatus(*args)

    def AutodynEnableZdd(*args):
        """AutodynEnableZdd(self, int method)"""
        return _pycudd.DdManager_AutodynEnableZdd(*args)

    def AutodynDisableZdd(*args):
        """AutodynDisableZdd(self)"""
        return _pycudd.DdManager_AutodynDisableZdd(*args)

    def ReorderingStatusZdd(*args):
        """ReorderingStatusZdd(self, int dum_status) -> int"""
        return _pycudd.DdManager_ReorderingStatusZdd(*args)

    def zddRealignmentEnabled(*args):
        """zddRealignmentEnabled(self) -> int"""
        return _pycudd.DdManager_zddRealignmentEnabled(*args)

    def zddRealignEnable(*args):
        """zddRealignEnable(self)"""
        return _pycudd.DdManager_zddRealignEnable(*args)

    def zddRealignDisable(*args):
        """zddRealignDisable(self)"""
        return _pycudd.DdManager_zddRealignDisable(*args)

    def RealignmentEnabled(*args):
        """RealignmentEnabled(self) -> int"""
        return _pycudd.DdManager_RealignmentEnabled(*args)

    def RealignEnable(*args):
        """RealignEnable(self)"""
        return _pycudd.DdManager_RealignEnable(*args)

    def RealignDisable(*args):
        """RealignDisable(self)"""
        return _pycudd.DdManager_RealignDisable(*args)

    def ReadOne(*args):
        """ReadOne(self) -> DdNode"""
        return _pycudd.DdManager_ReadOne(*args)

    def ReadZddOne(*args):
        """ReadZddOne(self, int i) -> DdNode"""
        return _pycudd.DdManager_ReadZddOne(*args)

    def ReadZero(*args):
        """ReadZero(self) -> DdNode"""
        return _pycudd.DdManager_ReadZero(*args)

    def ReadLogicZero(*args):
        """ReadLogicZero(self) -> DdNode"""
        return _pycudd.DdManager_ReadLogicZero(*args)

    def ReadPlusInfinity(*args):
        """ReadPlusInfinity(self) -> DdNode"""
        return _pycudd.DdManager_ReadPlusInfinity(*args)

    def ReadMinusInfinity(*args):
        """ReadMinusInfinity(self) -> DdNode"""
        return _pycudd.DdManager_ReadMinusInfinity(*args)

    def ReadBackground(*args):
        """ReadBackground(self) -> DdNode"""
        return _pycudd.DdManager_ReadBackground(*args)

    def ReadCacheSlots(*args):
        """ReadCacheSlots(self) -> unsigned int"""
        return _pycudd.DdManager_ReadCacheSlots(*args)

    def ReadCacheUsedSlots(*args):
        """ReadCacheUsedSlots(self) -> double"""
        return _pycudd.DdManager_ReadCacheUsedSlots(*args)

    def ReadCacheLookUps(*args):
        """ReadCacheLookUps(self) -> double"""
        return _pycudd.DdManager_ReadCacheLookUps(*args)

    def ReadCacheHits(*args):
        """ReadCacheHits(self) -> double"""
        return _pycudd.DdManager_ReadCacheHits(*args)

    def ReadRecursiveCalls(*args):
        """ReadRecursiveCalls(self) -> double"""
        return _pycudd.DdManager_ReadRecursiveCalls(*args)

    def ReadMinHit(*args):
        """ReadMinHit(self) -> unsigned int"""
        return _pycudd.DdManager_ReadMinHit(*args)

    def SetMinHit(*args):
        """SetMinHit(self, unsigned int hr)"""
        return _pycudd.DdManager_SetMinHit(*args)

    def ReadLooseUpTo(*args):
        """ReadLooseUpTo(self) -> unsigned int"""
        return _pycudd.DdManager_ReadLooseUpTo(*args)

    def SetLooseUpTo(*args):
        """SetLooseUpTo(self, unsigned int lut)"""
        return _pycudd.DdManager_SetLooseUpTo(*args)

    def ReadMaxCache(*args):
        """ReadMaxCache(self) -> unsigned int"""
        return _pycudd.DdManager_ReadMaxCache(*args)

    def ReadMaxCacheHard(*args):
        """ReadMaxCacheHard(self) -> unsigned int"""
        return _pycudd.DdManager_ReadMaxCacheHard(*args)

    def SetMaxCacheHard(*args):
        """SetMaxCacheHard(self, unsigned int mc)"""
        return _pycudd.DdManager_SetMaxCacheHard(*args)

    def ReadSize(*args):
        """ReadSize(self) -> int"""
        return _pycudd.DdManager_ReadSize(*args)

    def ReadZddSize(*args):
        """ReadZddSize(self) -> int"""
        return _pycudd.DdManager_ReadZddSize(*args)

    def ReadSlots(*args):
        """ReadSlots(self) -> unsigned int"""
        return _pycudd.DdManager_ReadSlots(*args)

    def ReadUsedSlots(*args):
        """ReadUsedSlots(self) -> double"""
        return _pycudd.DdManager_ReadUsedSlots(*args)

    def ExpectedUsedSlots(*args):
        """ExpectedUsedSlots(self) -> double"""
        return _pycudd.DdManager_ExpectedUsedSlots(*args)

    def ReadKeys(*args):
        """ReadKeys(self) -> unsigned int"""
        return _pycudd.DdManager_ReadKeys(*args)

    def ReadDead(*args):
        """ReadDead(self) -> unsigned int"""
        return _pycudd.DdManager_ReadDead(*args)

    def ReadMinDead(*args):
        """ReadMinDead(self) -> unsigned int"""
        return _pycudd.DdManager_ReadMinDead(*args)

    def ReadReorderings(*args):
        """ReadReorderings(self) -> int"""
        return _pycudd.DdManager_ReadReorderings(*args)

    def ReadReorderingTime(*args):
        """ReadReorderingTime(self) -> long"""
        return _pycudd.DdManager_ReadReorderingTime(*args)

    def ReadGarbageCollections(*args):
        """ReadGarbageCollections(self) -> int"""
        return _pycudd.DdManager_ReadGarbageCollections(*args)

    def ReadGarbageCollectionTime(*args):
        """ReadGarbageCollectionTime(self) -> long"""
        return _pycudd.DdManager_ReadGarbageCollectionTime(*args)

    def GarbageCollect(*args):
        """GarbageCollect(self, int clearCache) -> int"""
        return _pycudd.DdManager_GarbageCollect(*args)

    def ReadNodesFreed(*args):
        """ReadNodesFreed(self) -> double"""
        return _pycudd.DdManager_ReadNodesFreed(*args)

    def ReadNodesDropped(*args):
        """ReadNodesDropped(self) -> double"""
        return _pycudd.DdManager_ReadNodesDropped(*args)

    def ReadUniqueLookUps(*args):
        """ReadUniqueLookUps(self) -> double"""
        return _pycudd.DdManager_ReadUniqueLookUps(*args)

    def ReadUniqueLinks(*args):
        """ReadUniqueLinks(self) -> double"""
        return _pycudd.DdManager_ReadUniqueLinks(*args)

    def ReadSiftMaxVar(*args):
        """ReadSiftMaxVar(self) -> int"""
        return _pycudd.DdManager_ReadSiftMaxVar(*args)

    def SetSiftMaxVar(*args):
        """SetSiftMaxVar(self, int smv)"""
        return _pycudd.DdManager_SetSiftMaxVar(*args)

    def ReadSiftMaxSwap(*args):
        """ReadSiftMaxSwap(self) -> int"""
        return _pycudd.DdManager_ReadSiftMaxSwap(*args)

    def SetSiftMaxSwap(*args):
        """SetSiftMaxSwap(self, int sms)"""
        return _pycudd.DdManager_SetSiftMaxSwap(*args)

    def ReadMaxGrowth(*args):
        """ReadMaxGrowth(self) -> double"""
        return _pycudd.DdManager_ReadMaxGrowth(*args)

    def SetMaxGrowth(*args):
        """SetMaxGrowth(self, double mg)"""
        return _pycudd.DdManager_SetMaxGrowth(*args)

    def ReadTree(*args):
        """ReadTree(self) -> MtrNode"""
        return _pycudd.DdManager_ReadTree(*args)

    def SetTree(*args):
        """SetTree(self, MtrNode tree)"""
        return _pycudd.DdManager_SetTree(*args)

    def FreeTree(*args):
        """FreeTree(self)"""
        return _pycudd.DdManager_FreeTree(*args)

    def ReadZddTree(*args):
        """ReadZddTree(self) -> MtrNode"""
        return _pycudd.DdManager_ReadZddTree(*args)

    def SetZddTree(*args):
        """SetZddTree(self, MtrNode tree)"""
        return _pycudd.DdManager_SetZddTree(*args)

    def FreeZddTree(*args):
        """FreeZddTree(self)"""
        return _pycudd.DdManager_FreeZddTree(*args)

    def ReadPerm(*args):
        """ReadPerm(self, int i) -> int"""
        return _pycudd.DdManager_ReadPerm(*args)

    def ReadPermZdd(*args):
        """ReadPermZdd(self, int i) -> int"""
        return _pycudd.DdManager_ReadPermZdd(*args)

    def ReadInvPerm(*args):
        """ReadInvPerm(self, int i) -> int"""
        return _pycudd.DdManager_ReadInvPerm(*args)

    def ReadInvPermZdd(*args):
        """ReadInvPermZdd(self, int i) -> int"""
        return _pycudd.DdManager_ReadInvPermZdd(*args)

    def ReadVars(*args):
        """ReadVars(self, int i) -> DdNode"""
        return _pycudd.DdManager_ReadVars(*args)

    def ReadEpsilon(*args):
        """ReadEpsilon(self) -> CUDD_VALUE_TYPE"""
        return _pycudd.DdManager_ReadEpsilon(*args)

    def SetEpsilon(*args):
        """SetEpsilon(self, CUDD_VALUE_TYPE ep)"""
        return _pycudd.DdManager_SetEpsilon(*args)

    def ReadGroupcheck(*args):
        """ReadGroupcheck(self) -> Cudd_AggregationType"""
        return _pycudd.DdManager_ReadGroupcheck(*args)

    def SetGroupcheck(*args):
        """SetGroupcheck(self, Cudd_AggregationType gc)"""
        return _pycudd.DdManager_SetGroupcheck(*args)

    def GarbageCollectionEnabled(*args):
        """GarbageCollectionEnabled(self) -> int"""
        return _pycudd.DdManager_GarbageCollectionEnabled(*args)

    def EnableGarbageCollection(*args):
        """EnableGarbageCollection(self)"""
        return _pycudd.DdManager_EnableGarbageCollection(*args)

    def DisableGarbageCollection(*args):
        """DisableGarbageCollection(self)"""
        return _pycudd.DdManager_DisableGarbageCollection(*args)

    def DeadAreCounted(*args):
        """DeadAreCounted(self) -> int"""
        return _pycudd.DdManager_DeadAreCounted(*args)

    def TurnOnCountDead(*args):
        """TurnOnCountDead(self)"""
        return _pycudd.DdManager_TurnOnCountDead(*args)

    def TurnOffCountDead(*args):
        """TurnOffCountDead(self)"""
        return _pycudd.DdManager_TurnOffCountDead(*args)

    def ReadRecomb(*args):
        """ReadRecomb(self) -> int"""
        return _pycudd.DdManager_ReadRecomb(*args)

    def SetRecomb(*args):
        """SetRecomb(self, int recomb)"""
        return _pycudd.DdManager_SetRecomb(*args)

    def ReadSymmviolation(*args):
        """ReadSymmviolation(self) -> int"""
        return _pycudd.DdManager_ReadSymmviolation(*args)

    def SetSymmviolation(*args):
        """SetSymmviolation(self, int symmviolation)"""
        return _pycudd.DdManager_SetSymmviolation(*args)

    def ReadArcviolation(*args):
        """ReadArcviolation(self) -> int"""
        return _pycudd.DdManager_ReadArcviolation(*args)

    def SetArcviolation(*args):
        """SetArcviolation(self, int arcviolation)"""
        return _pycudd.DdManager_SetArcviolation(*args)

    def ReadPopulationSize(*args):
        """ReadPopulationSize(self) -> int"""
        return _pycudd.DdManager_ReadPopulationSize(*args)

    def SetPopulationSize(*args):
        """SetPopulationSize(self, int populationSize)"""
        return _pycudd.DdManager_SetPopulationSize(*args)

    def ReadNumberXovers(*args):
        """ReadNumberXovers(self) -> int"""
        return _pycudd.DdManager_ReadNumberXovers(*args)

    def SetNumberXovers(*args):
        """SetNumberXovers(self, int numberXovers)"""
        return _pycudd.DdManager_SetNumberXovers(*args)

    def ReadMemoryInUse(*args):
        """ReadMemoryInUse(self) -> long"""
        return _pycudd.DdManager_ReadMemoryInUse(*args)

    def PrintInfo(*args):
        """PrintInfo(self, FILE fp) -> int"""
        return _pycudd.DdManager_PrintInfo(*args)

    def ReadPeakNodeCount(*args):
        """ReadPeakNodeCount(self) -> long"""
        return _pycudd.DdManager_ReadPeakNodeCount(*args)

    def ReadPeakLiveNodeCount(*args):
        """ReadPeakLiveNodeCount(self) -> int"""
        return _pycudd.DdManager_ReadPeakLiveNodeCount(*args)

    def ReadNodeCount(*args):
        """ReadNodeCount(self) -> long"""
        return _pycudd.DdManager_ReadNodeCount(*args)

    def zddReadNodeCount(*args):
        """zddReadNodeCount(self) -> long"""
        return _pycudd.DdManager_zddReadNodeCount(*args)

    def EnableReorderingReporting(*args):
        """EnableReorderingReporting(self) -> int"""
        return _pycudd.DdManager_EnableReorderingReporting(*args)

    def DisableReorderingReporting(*args):
        """DisableReorderingReporting(self) -> int"""
        return _pycudd.DdManager_DisableReorderingReporting(*args)

    def ReorderingReporting(*args):
        """ReorderingReporting(self) -> int"""
        return _pycudd.DdManager_ReorderingReporting(*args)

    def ReadErrorCode(*args):
        """ReadErrorCode(self) -> Cudd_ErrorType"""
        return _pycudd.DdManager_ReadErrorCode(*args)

    def ClearErrorCode(*args):
        """ClearErrorCode(self)"""
        return _pycudd.DdManager_ClearErrorCode(*args)

    def ReadStdout(*args):
        """ReadStdout(self) -> FILE"""
        return _pycudd.DdManager_ReadStdout(*args)

    def SetStdout(*args):
        """SetStdout(self, FILE fp)"""
        return _pycudd.DdManager_SetStdout(*args)

    def ReadStderr(*args):
        """ReadStderr(self) -> FILE"""
        return _pycudd.DdManager_ReadStderr(*args)

    def SetStderr(*args):
        """SetStderr(self, FILE fp)"""
        return _pycudd.DdManager_SetStderr(*args)

    def ReadNextReordering(*args):
        """ReadNextReordering(self) -> unsigned int"""
        return _pycudd.DdManager_ReadNextReordering(*args)

    def ReadSwapSteps(*args):
        """ReadSwapSteps(self) -> double"""
        return _pycudd.DdManager_ReadSwapSteps(*args)

    def ReadMaxLive(*args):
        """ReadMaxLive(self) -> unsigned int"""
        return _pycudd.DdManager_ReadMaxLive(*args)

    def SetMaxLive(*args):
        """SetMaxLive(self, unsigned int maxLive)"""
        return _pycudd.DdManager_SetMaxLive(*args)

    def ReadMaxMemory(*args):
        """ReadMaxMemory(self) -> long"""
        return _pycudd.DdManager_ReadMaxMemory(*args)

    def SetMaxMemory(*args):
        """SetMaxMemory(self, long maxMemory)"""
        return _pycudd.DdManager_SetMaxMemory(*args)

    def SetNextReordering(*args):
        """SetNextReordering(self, unsigned int next)"""
        return _pycudd.DdManager_SetNextReordering(*args)

    def DebugCheck(*args):
        """DebugCheck(self) -> int"""
        return _pycudd.DdManager_DebugCheck(*args)

    def CheckKeys(*args):
        """CheckKeys(self) -> int"""
        return _pycudd.DdManager_CheckKeys(*args)

    def MakeTreeNode(*args):
        """MakeTreeNode(self, unsigned int low, unsigned int size, unsigned int type) -> MtrNode"""
        return _pycudd.DdManager_MakeTreeNode(*args)

    def PrintLinear(*args):
        """PrintLinear(self) -> int"""
        return _pycudd.DdManager_PrintLinear(*args)

    def ReadLinear(*args):
        """ReadLinear(self, int x, int y) -> int"""
        return _pycudd.DdManager_ReadLinear(*args)

    def CheckZeroRef(*args):
        """CheckZeroRef(self) -> int"""
        return _pycudd.DdManager_CheckZeroRef(*args)

    def ReduceHeap(*args):
        """ReduceHeap(self, int heuristic, int minsize) -> int"""
        return _pycudd.DdManager_ReduceHeap(*args)

    def ShuffleHeap(*args):
        """ShuffleHeap(self, IntArray permutation) -> int"""
        return _pycudd.DdManager_ShuffleHeap(*args)

    def SymmProfile(*args):
        """SymmProfile(self, int lower, int upper)"""
        return _pycudd.DdManager_SymmProfile(*args)

    def IndicesToCube(*args):
        """IndicesToCube(self, IntArray array, int n) -> DdNode"""
        return _pycudd.DdManager_IndicesToCube(*args)

    def AverageDistance(*args):
        """AverageDistance(self) -> double"""
        return _pycudd.DdManager_AverageDistance(*args)

    def MakeZddTreeNode(*args):
        """MakeZddTreeNode(self, unsigned int low, unsigned int size, unsigned int type) -> MtrNode"""
        return _pycudd.DdManager_MakeZddTreeNode(*args)

    def zddPrintSubtable(*args):
        """zddPrintSubtable(self)"""
        return _pycudd.DdManager_zddPrintSubtable(*args)

    def zddReduceHeap(*args):
        """zddReduceHeap(self, int heuristic, int minsize) -> int"""
        return _pycudd.DdManager_zddReduceHeap(*args)

    def zddShuffleHeap(*args):
        """zddShuffleHeap(self, IntArray permutation) -> int"""
        return _pycudd.DdManager_zddShuffleHeap(*args)

    def zddSymmProfile(*args):
        """zddSymmProfile(self, int lower, int upper)"""
        return _pycudd.DdManager_zddSymmProfile(*args)

    def BddToAdd(*args):
        """BddToAdd(self, DdNode B) -> DdNode"""
        return _pycudd.DdManager_BddToAdd(*args)

    def addBddPattern(*args):
        """addBddPattern(self, DdNode f) -> DdNode"""
        return _pycudd.DdManager_addBddPattern(*args)

    def addBddThreshold(*args):
        """addBddThreshold(self, DdNode f, CUDD_VALUE_TYPE value) -> DdNode"""
        return _pycudd.DdManager_addBddThreshold(*args)

    def addBddStrictThreshold(*args):
        """addBddStrictThreshold(self, DdNode f, CUDD_VALUE_TYPE value) -> DdNode"""
        return _pycudd.DdManager_addBddStrictThreshold(*args)

    def addBddInterval(*args):
        """addBddInterval(self, DdNode f, CUDD_VALUE_TYPE lower, CUDD_VALUE_TYPE upper) -> DdNode"""
        return _pycudd.DdManager_addBddInterval(*args)

    def addBddIthBit(*args):
        """addBddIthBit(self, DdNode f, int bit) -> DdNode"""
        return _pycudd.DdManager_addBddIthBit(*args)

    def zddPortFromBdd(*args):
        """zddPortFromBdd(self, DdNode B) -> DdNode"""
        return _pycudd.DdManager_zddPortFromBdd(*args)

    def zddPortToBdd(*args):
        """zddPortToBdd(self, DdNode f) -> DdNode"""
        return _pycudd.DdManager_zddPortToBdd(*args)

    def MakeBddFromZddCover(*args):
        """MakeBddFromZddCover(self, DdNode node) -> DdNode"""
        return _pycudd.DdManager_MakeBddFromZddCover(*args)

    def PrintVersion(*args):
        """PrintVersion(self, FILE fp)"""
        return _pycudd.DdManager_PrintVersion(*args)

    def Random(*args):
        """Random(self) -> long"""
        return _pycudd.DdManager_Random(*args)

    def Srandom(*args):
        """Srandom(self, long seed)"""
        return _pycudd.DdManager_Srandom(*args)

    def OutOfMem(*args):
        """OutOfMem(self, long size)"""
        return _pycudd.DdManager_OutOfMem(*args)

    def Transfer(*args):
        """Transfer(self, DdManager ddDestination, DdNode f) -> DdNode"""
        return _pycudd.DdManager_Transfer(*args)

    def CubeArrayToBdd(*args):
        """CubeArrayToBdd(self, IntArray y) -> DdNode"""
        return _pycudd.DdManager_CubeArrayToBdd(*args)

    def SetVarMap(*args):
        """SetVarMap(self, DdArray x, DdArray y, int n) -> int"""
        return _pycudd.DdManager_SetVarMap(*args)

    def ComputeCube(*args):
        """ComputeCube(self, DdArray vars, IntArray phase, int n) -> DdNode"""
        return _pycudd.DdManager_ComputeCube(*args)

    def zddDumpDot(*args):
        """zddDumpDot(self, int n, DdArray f, char inames, char onames, FILE fp) -> int"""
        return _pycudd.DdManager_zddDumpDot(*args)

    def DumpBlif(*args):
        """
        DumpBlif(self, int n, DdArray f, char inames, char onames, char mname, 
            FILE fp) -> int
        """
        return _pycudd.DdManager_DumpBlif(*args)

    def DumpBlifBody(*args):
        """DumpBlifBody(self, int n, DdArray f, char inames, char onames, FILE fp) -> int"""
        return _pycudd.DdManager_DumpBlifBody(*args)

    def DumpDot(*args):
        """DumpDot(self, int n, DdArray f, char inames, char onames, FILE fp) -> int"""
        return _pycudd.DdManager_DumpDot(*args)

    def DumpDaVinci(*args):
        """DumpDaVinci(self, int n, DdArray f, char inames, char onames, FILE fp) -> int"""
        return _pycudd.DdManager_DumpDaVinci(*args)

    def DumpDDcal(*args):
        """DumpDDcal(self, int n, DdArray f, char inames, char onames, FILE fp) -> int"""
        return _pycudd.DdManager_DumpDDcal(*args)

    def DumpFactoredForm(*args):
        """DumpFactoredForm(self, int n, DdArray f, char inames, char onames, FILE fp) -> int"""
        return _pycudd.DdManager_DumpFactoredForm(*args)

    def ArrayLoad(*args):
        """
        ArrayLoad(self, int rootmatchmode, char rootmatchnames, int varmatchmode, 
            char varmatchnames, IntArray varmatchauxids, 
            IntArray varcomposeids, int mode, char filename, 
            FILE fp, DdArray pproots) -> int
        """
        return _pycudd.DdManager_ArrayLoad(*args)

    def ArrayStore(*args):
        """
        ArrayStore(self, char ddname, DdArray roots, char rootnames, char varnames, 
            IntArray auxids, int mode, int varinfo, 
            char filename, FILE fp) -> int
        """
        return _pycudd.DdManager_ArrayStore(*args)

    def BddLoad(*args):
        """
        BddLoad(self, int varmatchmode, char varmatchnames, IntArray varmatchauxids, 
            IntArray varcomposeids, int mode, 
            char filename, FILE fp) -> DdNode
        """
        return _pycudd.DdManager_BddLoad(*args)

    def BddStore(*args):
        """
        BddStore(self, char ddname, DdNode f, char varnames, IntArray auxids, 
            int mode, int varinfo, char fname, FILE fp) -> int
        """
        return _pycudd.DdManager_BddStore(*args)

    def Bin2Text(*args):
        """Bin2Text(self, char filein, char fileout) -> int"""
        return _pycudd.DdManager_Bin2Text(*args)

    def DisplayBinary(*args):
        """DisplayBinary(self, char filein, char fileout) -> int"""
        return _pycudd.DdManager_DisplayBinary(*args)

    def Text2Bin(*args):
        """Text2Bin(self, char filein, char fileout) -> int"""
        return _pycudd.DdManager_Text2Bin(*args)

    def VectorSupportSize(*args):
        """VectorSupportSize(self, DdArray F, int n) -> int"""
        return _pycudd.DdManager_VectorSupportSize(*args)

    def ClassifySupport(*args):
        """
        ClassifySupport(self, DdNode f, DdNode g, DdArray common, DdArray onlyF, 
            DdArray onlyG) -> int
        """
        return _pycudd.DdManager_ClassifySupport(*args)

    def Xgty(*args):
        """Xgty(self, int N, DdArray z, DdArray x, DdArray y) -> DdNode"""
        return _pycudd.DdManager_Xgty(*args)

    def Xeqy(*args):
        """Xeqy(self, int N, DdArray x, DdArray y) -> DdNode"""
        return _pycudd.DdManager_Xeqy(*args)

    def Dxygtdxz(*args):
        """Dxygtdxz(self, int N, DdArray x, DdArray y, DdArray z) -> DdNode"""
        return _pycudd.DdManager_Dxygtdxz(*args)

    def Dxygtdyz(*args):
        """Dxygtdyz(self, int N, DdArray x, DdArray y, DdArray z) -> DdNode"""
        return _pycudd.DdManager_Dxygtdyz(*args)

    def SharingSize(*args):
        """SharingSize(self, DdArray nodeArray, int n) -> int"""
        return _pycudd.DdManager_SharingSize(*args)

    def ReadIndex(*args):
        """ReadIndex(self, int i) -> int"""
        return _pycudd.DdManager_ReadIndex(*args)

    def addPlus(*args):
        """addPlus(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addPlus(*args)

    def addTimes(*args):
        """addTimes(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addTimes(*args)

    def addThreshold(*args):
        """addThreshold(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addThreshold(*args)

    def addSetNZ(*args):
        """addSetNZ(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addSetNZ(*args)

    def addDivide(*args):
        """addDivide(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addDivide(*args)

    def addMinus(*args):
        """addMinus(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addMinus(*args)

    def addMinimum(*args):
        """addMinimum(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addMinimum(*args)

    def addMaximum(*args):
        """addMaximum(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addMaximum(*args)

    def addOneZeroMaximum(*args):
        """addOneZeroMaximum(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addOneZeroMaximum(*args)

    def addDiff(*args):
        """addDiff(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addDiff(*args)

    def addAgreement(*args):
        """addAgreement(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addAgreement(*args)

    def addOr(*args):
        """addOr(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addOr(*args)

    def addNand(*args):
        """addNand(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addNand(*args)

    def addNor(*args):
        """addNor(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addNor(*args)

    def addXor(*args):
        """addXor(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addXor(*args)

    def addXnor(*args):
        """addXnor(self, DdArray f, DdArray g) -> DdNode"""
        return _pycudd.DdManager_addXnor(*args)

    def addWalsh(*args):
        """addWalsh(self, DdArray x, DdArray y, int n) -> DdNode"""
        return _pycudd.DdManager_addWalsh(*args)

    def addHamming(*args):
        """addHamming(self, DdArray xVars, DdArray yVars, int nVars) -> DdNode"""
        return _pycudd.DdManager_addHamming(*args)

    def addComputeCube(*args):
        """addComputeCube(self, DdArray vars, IntArray phase, int n) -> DdNode"""
        return _pycudd.DdManager_addComputeCube(*args)

    def addResidue(*args):
        """addResidue(self, int n, int m, int options, int top) -> DdNode"""
        return _pycudd.DdManager_addResidue(*args)

    def addXeqy(*args):
        """addXeqy(self, int N, DdArray x, DdArray y) -> DdNode"""
        return _pycudd.DdManager_addXeqy(*args)

    def ApaNumberOfDigits(*args):
        """ApaNumberOfDigits(self, int binaryDigits) -> int"""
        return _pycudd.DdManager_ApaNumberOfDigits(*args)

    def NewApaNumber(*args):
        """NewApaNumber(self, int digits) -> DdApaNumber"""
        return _pycudd.DdManager_NewApaNumber(*args)

    def ApaCopy(*args):
        """ApaCopy(self, int digits, DdApaNumber source, DdApaNumber dest)"""
        return _pycudd.DdManager_ApaCopy(*args)

    def ApaAdd(*args):
        """ApaAdd(self, int digits, DdApaNumber a, DdApaNumber b, DdApaNumber sum) -> DdApaDigit"""
        return _pycudd.DdManager_ApaAdd(*args)

    def ApaSubtract(*args):
        """ApaSubtract(self, int digits, DdApaNumber a, DdApaNumber b, DdApaNumber diff) -> DdApaDigit"""
        return _pycudd.DdManager_ApaSubtract(*args)

    def ApaShortDivision(*args):
        """
        ApaShortDivision(self, int digits, DdApaNumber dividend, DdApaDigit divisor, 
            DdApaNumber quotient) -> DdApaDigit
        """
        return _pycudd.DdManager_ApaShortDivision(*args)

    def ApaIntDivision(*args):
        """
        ApaIntDivision(self, int digits, DdApaNumber dividend, unsigned int divisor, 
            DdApaNumber quotient) -> unsigned int
        """
        return _pycudd.DdManager_ApaIntDivision(*args)

    def ApaShiftRight(*args):
        """ApaShiftRight(self, int digits, DdApaDigit in, DdApaNumber a, DdApaNumber b)"""
        return _pycudd.DdManager_ApaShiftRight(*args)

    def ApaSetToLiteral(*args):
        """ApaSetToLiteral(self, int digits, DdApaNumber number, DdApaDigit literal)"""
        return _pycudd.DdManager_ApaSetToLiteral(*args)

    def ApaPowerOfTwo(*args):
        """ApaPowerOfTwo(self, int digits, DdApaNumber number, int power)"""
        return _pycudd.DdManager_ApaPowerOfTwo(*args)

    def ApaCompare(*args):
        """
        ApaCompare(self, int digitsFirst, DdApaNumber first, int digitsSecond, 
            DdApaNumber second) -> int
        """
        return _pycudd.DdManager_ApaCompare(*args)

    def ApaCompareRatios(*args):
        """
        ApaCompareRatios(self, int digitsFirst, DdApaNumber firstNum, unsigned int firstDen, 
            int digitsSecond, DdApaNumber secondNum, 
            unsigned int secondDen) -> int
        """
        return _pycudd.DdManager_ApaCompareRatios(*args)

    def ApaPrintHex(*args):
        """ApaPrintHex(self, FILE fp, int digits, DdApaNumber number) -> int"""
        return _pycudd.DdManager_ApaPrintHex(*args)

    def ApaPrintDecimal(*args):
        """ApaPrintDecimal(self, FILE fp, int digits, DdApaNumber number) -> int"""
        return _pycudd.DdManager_ApaPrintDecimal(*args)

    def ApaPrintExponential(*args):
        """ApaPrintExponential(self, FILE fp, int digits, DdApaNumber number, int precision) -> int"""
        return _pycudd.DdManager_ApaPrintExponential(*args)

    def One(*args):
        """One(self) -> DdNode"""
        return _pycudd.DdManager_One(*args)

    def Zero(*args):
        """Zero(self) -> DdNode"""
        return _pycudd.DdManager_Zero(*args)

    def Sort(*args):
        """Sort(self, DdNode leftnd, DdNode rightnd) -> int"""
        return _pycudd.DdManager_Sort(*args)

    def PrintStdOut(*args):
        """PrintStdOut(self) -> int"""
        return _pycudd.DdManager_PrintStdOut(*args)

    def StateCube(*args):
        """StateCube(self, char cube, int base, int offset, int scale) -> DdNode"""
        return _pycudd.DdManager_StateCube(*args)

    def SetDefault(*args):
        """SetDefault(self)"""
        return _pycudd.DdManager_SetDefault(*args)

_pycudd.DdManager_swigregister(DdManager)

class DdGen(_object):
    """Proxy of C++ DdGen class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, DdGen, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DdGen, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ DdGen instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __doc__ = "Not expected to be used directly."

    def __init__(self, *args):
        """
        __init__(self, DdNode node1, int method, DdNode node2=None) -> DdGen
        __init__(self, DdNode node1, int method) -> DdGen
        """
        this = _pycudd.new_DdGen(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_DdGen
    __del__ = lambda self : None;
_pycudd.DdGen_swigregister(DdGen)

class DdNode(_object):
    """Proxy of C++ DdNode class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, DdNode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DdNode, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ DdNode instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __iter__(self):
      global iter_meth, cudd_version
      if iter_meth == 0:
        return ForeachCubeIterator(self)
      elif iter_meth == 1:
        return ForeachNodeIterator(self)
      elif iter_meth == 2:
        if cudd_version < 0x020400:
          print "Cannot iterate over primes with CUDD < 2.4.0"
          raise RuntimeError
        npair = NodePair(self,self)
        return ForeachPrimeIterator(npair)
    def __deepcopy__(self,memo):
      return self
    __doc__ = "This class wraps around the basic DdNode. The methods defined by this class take the default manager as their DdManager option (if needed) and provide themselves as the first DdNode option that those functions require, as indicated by the self argument. These functions may be found in ddnode.i."

    def __init__(self, *args):
        """__init__(self) -> DdNode"""
        this = _pycudd.new_DdNode(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_DdNode
    __del__ = lambda self : None;
    def FirstCube(*args):
        """FirstCube(self, DdGen gen, int dum_cube) -> int"""
        return _pycudd.DdNode_FirstCube(*args)

    def NextCube(*args):
        """NextCube(self, DdGen gen, int dum_cube) -> int"""
        return _pycudd.DdNode_NextCube(*args)

    def FirstNode(*args):
        """FirstNode(self, DdGen gen, DdNode dum_y) -> int"""
        return _pycudd.DdNode_FirstNode(*args)

    def NextNode(*args):
        """NextNode(self, DdGen gen, DdNode dum_y) -> int"""
        return _pycudd.DdNode_NextNode(*args)

    def AndAbstractLimit(*args):
        """AndAbstractLimit(self, DdNode g, DdNode cube, unsigned int limit) -> DdNode"""
        return _pycudd.DdNode_AndAbstractLimit(*args)

    def AndLimit(*args):
        """AndLimit(self, DdNode g, unsigned int limit) -> DdNode"""
        return _pycudd.DdNode_AndLimit(*args)

    def NPAnd(*args):
        """NPAnd(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_NPAnd(*args)

    def FindTwoLiteralClauses(*args):
        """FindTwoLiteralClauses(self) -> DdTlcInfo"""
        return _pycudd.DdNode_FindTwoLiteralClauses(*args)

    def EpdCountMinterm(*args):
        """EpdCountMinterm(self, int nvars, EpDouble epd) -> int"""
        return _pycudd.DdNode_EpdCountMinterm(*args)

    def ApproxConjDecomp(*args):
        """ApproxConjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_ApproxConjDecomp(*args)

    def ApproxDisjDecomp(*args):
        """ApproxDisjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_ApproxDisjDecomp(*args)

    def IterConjDecomp(*args):
        """IterConjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_IterConjDecomp(*args)

    def IterDisjDecomp(*args):
        """IterDisjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_IterDisjDecomp(*args)

    def GenConjDecomp(*args):
        """GenConjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_GenConjDecomp(*args)

    def GenDisjDecomp(*args):
        """GenDisjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_GenDisjDecomp(*args)

    def VarConjDecomp(*args):
        """VarConjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_VarConjDecomp(*args)

    def VarDisjDecomp(*args):
        """VarDisjDecomp(self, DdNode dum_juncts) -> int"""
        return _pycudd.DdNode_VarDisjDecomp(*args)

    def ClosestCube(*args):
        """ClosestCube(self, DdNode g, int dum_distance) -> DdNode"""
        return _pycudd.DdNode_ClosestCube(*args)

    def LeqUnless(*args):
        """LeqUnless(self, DdNode g, DdNode D) -> int"""
        return _pycudd.DdNode_LeqUnless(*args)

    def MakePrime(*args):
        """MakePrime(self, DdNode f) -> DdNode"""
        return _pycudd.DdNode_MakePrime(*args)

    def CountPathsToNonZero(*args):
        """CountPathsToNonZero(self) -> double"""
        return _pycudd.DdNode_CountPathsToNonZero(*args)

    def SupportIndex(*args):
        """SupportIndex(self, int dum_sup) -> int"""
        return _pycudd.DdNode_SupportIndex(*args)

    def ExistAbstract(*args):
        """ExistAbstract(self, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_ExistAbstract(*args)

    def XorExistAbstract(*args):
        """XorExistAbstract(self, DdNode g, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_XorExistAbstract(*args)

    def UnivAbstract(*args):
        """UnivAbstract(self, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_UnivAbstract(*args)

    def BooleanDiff(*args):
        """BooleanDiff(self, int x) -> DdNode"""
        return _pycudd.DdNode_BooleanDiff(*args)

    def AndAbstract(*args):
        """AndAbstract(self, DdNode g, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_AndAbstract(*args)

    def VarIsDependent(*args):
        """VarIsDependent(self, DdNode var) -> int"""
        return _pycudd.DdNode_VarIsDependent(*args)

    def Correlation(*args):
        """Correlation(self, DdNode g) -> double"""
        return _pycudd.DdNode_Correlation(*args)

    def CorrelationWeights(*args):
        """CorrelationWeights(self, DdNode g, DoubleArray prob) -> double"""
        return _pycudd.DdNode_CorrelationWeights(*args)

    def Ite(*args):
        """Ite(self, DdNode g, DdNode h) -> DdNode"""
        return _pycudd.DdNode_Ite(*args)

    def IteConstant(*args):
        """IteConstant(self, DdNode g, DdNode h) -> DdNode"""
        return _pycudd.DdNode_IteConstant(*args)

    def Intersect(*args):
        """Intersect(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Intersect(*args)

    def FIntersect(*args):
        """FIntersect(self, DdNode g) -> int"""
        return _pycudd.DdNode_FIntersect(*args)

    def And(*args):
        """And(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_And(*args)

    def Or(*args):
        """Or(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Or(*args)

    def Nand(*args):
        """Nand(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Nand(*args)

    def Nor(*args):
        """Nor(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Nor(*args)

    def Xor(*args):
        """Xor(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Xor(*args)

    def Xnor(*args):
        """Xnor(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Xnor(*args)

    def ClippingAnd(*args):
        """ClippingAnd(self, DdNode g, int maxDepth, int direction) -> DdNode"""
        return _pycudd.DdNode_ClippingAnd(*args)

    def ClippingAndAbstract(*args):
        """ClippingAndAbstract(self, DdNode g, DdNode cube, int maxDepth, int direction) -> DdNode"""
        return _pycudd.DdNode_ClippingAndAbstract(*args)

    def LICompaction(*args):
        """LICompaction(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_LICompaction(*args)

    def Squeeze(*args):
        """Squeeze(self, DdNode u) -> DdNode"""
        return _pycudd.DdNode_Squeeze(*args)

    def Minimize(*args):
        """Minimize(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_Minimize(*args)

    def Constrain(*args):
        """Constrain(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_Constrain(*args)

    def Restrict(*args):
        """Restrict(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_Restrict(*args)

    def PickOneCube(*args):
        """PickOneCube(self, char string) -> int"""
        return _pycudd.DdNode_PickOneCube(*args)

    def PickOneMinterm(*args):
        """PickOneMinterm(self, DdArray vars, int n) -> DdNode"""
        return _pycudd.DdNode_PickOneMinterm(*args)

    def PickArbitraryMinterms(*args):
        """PickArbitraryMinterms(self, DdArray vars, int n, int k) -> DdArray"""
        return _pycudd.DdNode_PickArbitraryMinterms(*args)

    def Compose(*args):
        """Compose(self, DdNode g, int v) -> DdNode"""
        return _pycudd.DdNode_Compose(*args)

    def Permute(*args):
        """Permute(self, IntArray permut) -> DdNode"""
        return _pycudd.DdNode_Permute(*args)

    def VarMap(*args):
        """VarMap(self) -> DdNode"""
        return _pycudd.DdNode_VarMap(*args)

    def LiteralSetIntersection(*args):
        """LiteralSetIntersection(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_LiteralSetIntersection(*args)

    def IsVarEssential(*args):
        """IsVarEssential(self, int id, int phase) -> int"""
        return _pycudd.DdNode_IsVarEssential(*args)

    def Leq(*args):
        """Leq(self, DdNode g) -> bool"""
        return _pycudd.DdNode_Leq(*args)

    def CharToVect(*args):
        """CharToVect(self) -> DdArray"""
        return _pycudd.DdNode_CharToVect(*args)

    def ConstrainDecomp(*args):
        """ConstrainDecomp(self) -> DdArray"""
        return _pycudd.DdNode_ConstrainDecomp(*args)

    def Isop(*args):
        """Isop(self, DdNode U) -> DdNode"""
        return _pycudd.DdNode_Isop(*args)

    def SwapVariables(*args):
        """SwapVariables(self, DdArray x, DdArray y, int n) -> DdNode"""
        return _pycudd.DdNode_SwapVariables(*args)

    def AdjPermuteX(*args):
        """AdjPermuteX(self, DdArray x, int n) -> DdNode"""
        return _pycudd.DdNode_AdjPermuteX(*args)

    def VectorCompose(*args):
        """VectorCompose(self, DdArray vector) -> DdNode"""
        return _pycudd.DdNode_VectorCompose(*args)

    def SetBackground(*args):
        """SetBackground(self)"""
        return _pycudd.DdNode_SetBackground(*args)

    def UnderApprox(*args):
        """UnderApprox(self, int numVars, int threshold, int safe, double quality) -> DdNode"""
        return _pycudd.DdNode_UnderApprox(*args)

    def OverApprox(*args):
        """OverApprox(self, int numVars, int threshold, int safe, double quality) -> DdNode"""
        return _pycudd.DdNode_OverApprox(*args)

    def RemapUnderApprox(*args):
        """RemapUnderApprox(self, int numVars, int threshold, double quality) -> DdNode"""
        return _pycudd.DdNode_RemapUnderApprox(*args)

    def RemapOverApprox(*args):
        """RemapOverApprox(self, int numVars, int threshold, double quality) -> DdNode"""
        return _pycudd.DdNode_RemapOverApprox(*args)

    def BiasedUnderApprox(*args):
        """
        BiasedUnderApprox(self, DdNode b, int numVars, int threshold, double quality1, 
            double quality0) -> DdNode
        """
        return _pycudd.DdNode_BiasedUnderApprox(*args)

    def BiasedOverApprox(*args):
        """
        BiasedOverApprox(self, DdNode b, int numVars, int threshold, double quality1, 
            double quality0) -> DdNode
        """
        return _pycudd.DdNode_BiasedOverApprox(*args)

    def Cofactor(*args):
        """Cofactor(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_Cofactor(*args)

    def FindEssential(*args):
        """FindEssential(self) -> DdNode"""
        return _pycudd.DdNode_FindEssential(*args)

    def SubsetCompress(*args):
        """SubsetCompress(self, int nvars, int threshold) -> DdNode"""
        return _pycudd.DdNode_SubsetCompress(*args)

    def SupersetCompress(*args):
        """SupersetCompress(self, int nvars, int threshold) -> DdNode"""
        return _pycudd.DdNode_SupersetCompress(*args)

    def CProjection(*args):
        """CProjection(self, DdNode Y) -> DdNode"""
        return _pycudd.DdNode_CProjection(*args)

    def MinHammingDist(*args):
        """MinHammingDist(self, IntArray minterm, int upperBound) -> int"""
        return _pycudd.DdNode_MinHammingDist(*args)

    def Eval(*args):
        """Eval(self, IntArray inputs) -> DdNode"""
        return _pycudd.DdNode_Eval(*args)

    def ShortestPath(*args):
        """ShortestPath(self, IntArray weight, IntArray support, IntArray length) -> DdNode"""
        return _pycudd.DdNode_ShortestPath(*args)

    def LargestCube(*args):
        """LargestCube(self, IntArray length) -> DdNode"""
        return _pycudd.DdNode_LargestCube(*args)

    def ShortestLength(*args):
        """ShortestLength(self, IntArray weight) -> int"""
        return _pycudd.DdNode_ShortestLength(*args)

    def Decreasing(*args):
        """Decreasing(self, int i) -> DdNode"""
        return _pycudd.DdNode_Decreasing(*args)

    def Increasing(*args):
        """Increasing(self, int i) -> DdNode"""
        return _pycudd.DdNode_Increasing(*args)

    def EquivDC(*args):
        """EquivDC(self, DdNode G, DdNode D) -> int"""
        return _pycudd.DdNode_EquivDC(*args)

    def EqualSupNorm(*args):
        """EqualSupNorm(self, DdNode g, CUDD_VALUE_TYPE tolerance, int pr) -> int"""
        return _pycudd.DdNode_EqualSupNorm(*args)

    def CofMinterm(*args):
        """CofMinterm(self) -> DoubleArray"""
        return _pycudd.DdNode_CofMinterm(*args)

    def VerifySol(*args):
        """VerifySol(self, DdArray G, IntArray yIndex, int n) -> DdNode"""
        return _pycudd.DdNode_VerifySol(*args)

    def SplitSet(*args):
        """SplitSet(self, DdArray xVars, int n, double m) -> DdNode"""
        return _pycudd.DdNode_SplitSet(*args)

    def SubsetHeavyBranch(*args):
        """SubsetHeavyBranch(self, int numVars, int threshold) -> DdNode"""
        return _pycudd.DdNode_SubsetHeavyBranch(*args)

    def SupersetHeavyBranch(*args):
        """SupersetHeavyBranch(self, int numVars, int threshold) -> DdNode"""
        return _pycudd.DdNode_SupersetHeavyBranch(*args)

    def SubsetShortPaths(*args):
        """SubsetShortPaths(self, int numVars, int threshold, int hardlimit) -> DdNode"""
        return _pycudd.DdNode_SubsetShortPaths(*args)

    def SupersetShortPaths(*args):
        """SupersetShortPaths(self, int numVars, int threshold, int hardlimit) -> DdNode"""
        return _pycudd.DdNode_SupersetShortPaths(*args)

    def BddToCubeArray(*args):
        """BddToCubeArray(self, IntArray y) -> int"""
        return _pycudd.DdNode_BddToCubeArray(*args)

    def PrintMinterm(*args):
        """PrintMinterm(self) -> int"""
        return _pycudd.DdNode_PrintMinterm(*args)

    def PrintDebug(*args):
        """PrintDebug(self, int n, int pr) -> int"""
        return _pycudd.DdNode_PrintDebug(*args)

    def EstimateCofactor(*args):
        """EstimateCofactor(self, int i, int phase) -> int"""
        return _pycudd.DdNode_EstimateCofactor(*args)

    def CountMinterm(*args):
        """CountMinterm(self, int nvars) -> double"""
        return _pycudd.DdNode_CountMinterm(*args)

    def Support(*args):
        """Support(self) -> DdNode"""
        return _pycudd.DdNode_Support(*args)

    def SupportSize(*args):
        """SupportSize(self) -> int"""
        return _pycudd.DdNode_SupportSize(*args)

    def Density(*args):
        """Density(self, int nvars) -> double"""
        return _pycudd.DdNode_Density(*args)

    def NodeReadIndex(*args):
        """NodeReadIndex(self) -> int"""
        return _pycudd.DdNode_NodeReadIndex(*args)

    def IsNonConstant(*args):
        """IsNonConstant(self) -> int"""
        return _pycudd.DdNode_IsNonConstant(*args)

    def DagSize(*args):
        """DagSize(self) -> int"""
        return _pycudd.DdNode_DagSize(*args)

    def EstimateCofactorSimple(*args):
        """EstimateCofactorSimple(self, int i) -> int"""
        return _pycudd.DdNode_EstimateCofactorSimple(*args)

    def CountPath(*args):
        """CountPath(self) -> double"""
        return _pycudd.DdNode_CountPath(*args)

    def CountLeaves(*args):
        """CountLeaves(self) -> int"""
        return _pycudd.DdNode_CountLeaves(*args)

    def BddStore(*args):
        """
        BddStore(self, char ddname, char varnames, IntArray auxids, int mode, 
            int varinfo, char fname, FILE fp) -> int
        """
        return _pycudd.DdNode_BddStore(*args)

    def IsConstant(*args):
        """IsConstant(self) -> int"""
        return _pycudd.DdNode_IsConstant(*args)

    def Not(*args):
        """Not(self) -> DdNode"""
        return _pycudd.DdNode_Not(*args)

    def NotCond(*args):
        """NotCond(self, int c) -> DdNode"""
        return _pycudd.DdNode_NotCond(*args)

    def Regular(*args):
        """Regular(self) -> DdNode"""
        return _pycudd.DdNode_Regular(*args)

    def Complement(*args):
        """Complement(self) -> DdNode"""
        return _pycudd.DdNode_Complement(*args)

    def IsComplement(*args):
        """IsComplement(self) -> int"""
        return _pycudd.DdNode_IsComplement(*args)

    def T(*args):
        """T(self) -> DdNode"""
        return _pycudd.DdNode_T(*args)

    def E(*args):
        """E(self) -> DdNode"""
        return _pycudd.DdNode_E(*args)

    def V(*args):
        """V(self) -> double"""
        return _pycudd.DdNode_V(*args)

    def ReadIndex(*args):
        """ReadIndex(self, int index) -> int"""
        return _pycudd.DdNode_ReadIndex(*args)

    def addExistAbstract(*args):
        """addExistAbstract(self, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_addExistAbstract(*args)

    def addUnivAbstract(*args):
        """addUnivAbstract(self, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_addUnivAbstract(*args)

    def addOrAbstract(*args):
        """addOrAbstract(self, DdNode cube) -> DdNode"""
        return _pycudd.DdNode_addOrAbstract(*args)

    def addFindMax(*args):
        """addFindMax(self) -> DdNode"""
        return _pycudd.DdNode_addFindMax(*args)

    def addFindMin(*args):
        """addFindMin(self) -> DdNode"""
        return _pycudd.DdNode_addFindMin(*args)

    def addIthBit(*args):
        """addIthBit(self, int bit) -> DdNode"""
        return _pycudd.DdNode_addIthBit(*args)

    def addScalarInverse(*args):
        """addScalarInverse(self, DdNode epsilon) -> DdNode"""
        return _pycudd.DdNode_addScalarInverse(*args)

    def addIte(*args):
        """addIte(self, DdNode g, DdNode h) -> DdNode"""
        return _pycudd.DdNode_addIte(*args)

    def addIteConstant(*args):
        """addIteConstant(self, DdNode g, DdNode h) -> DdNode"""
        return _pycudd.DdNode_addIteConstant(*args)

    def addEvalConst(*args):
        """addEvalConst(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_addEvalConst(*args)

    def addLeq(*args):
        """addLeq(self, DdNode g) -> int"""
        return _pycudd.DdNode_addLeq(*args)

    def addCmpl(*args):
        """addCmpl(self) -> DdNode"""
        return _pycudd.DdNode_addCmpl(*args)

    def addNegate(*args):
        """addNegate(self) -> DdNode"""
        return _pycudd.DdNode_addNegate(*args)

    def addRoundOff(*args):
        """addRoundOff(self, int N) -> DdNode"""
        return _pycudd.DdNode_addRoundOff(*args)

    def addCompose(*args):
        """addCompose(self, DdNode g, int v) -> DdNode"""
        return _pycudd.DdNode_addCompose(*args)

    def addPermute(*args):
        """addPermute(self, IntArray permut) -> DdNode"""
        return _pycudd.DdNode_addPermute(*args)

    def addConstrain(*args):
        """addConstrain(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_addConstrain(*args)

    def addRestrict(*args):
        """addRestrict(self, DdNode c) -> DdNode"""
        return _pycudd.DdNode_addRestrict(*args)

    def addMatrixMultiply(*args):
        """addMatrixMultiply(self, DdNode B, DdArray z, int nz) -> DdNode"""
        return _pycudd.DdNode_addMatrixMultiply(*args)

    def addTimesPlus(*args):
        """addTimesPlus(self, DdNode B, DdArray z, int nz) -> DdNode"""
        return _pycudd.DdNode_addTimesPlus(*args)

    def addTriangle(*args):
        """addTriangle(self, DdNode g, DdArray z, int nz) -> DdNode"""
        return _pycudd.DdNode_addTriangle(*args)

    def addVectorCompose(*args):
        """addVectorCompose(self, DdArray vector) -> DdNode"""
        return _pycudd.DdNode_addVectorCompose(*args)

    def addNonSimCompose(*args):
        """addNonSimCompose(self, DdArray vector) -> DdNode"""
        return _pycudd.DdNode_addNonSimCompose(*args)

    def addSwapVariables(*args):
        """addSwapVariables(self, DdArray x, DdArray y, int n) -> DdNode"""
        return _pycudd.DdNode_addSwapVariables(*args)

    def zddProduct(*args):
        """zddProduct(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_zddProduct(*args)

    def zddUnateProduct(*args):
        """zddUnateProduct(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_zddUnateProduct(*args)

    def zddWeakDiv(*args):
        """zddWeakDiv(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_zddWeakDiv(*args)

    def zddDivide(*args):
        """zddDivide(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_zddDivide(*args)

    def zddWeakDivF(*args):
        """zddWeakDivF(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_zddWeakDivF(*args)

    def zddDivideF(*args):
        """zddDivideF(self, DdNode g) -> DdNode"""
        return _pycudd.DdNode_zddDivideF(*args)

    def zddComplement(*args):
        """zddComplement(self) -> DdNode"""
        return _pycudd.DdNode_zddComplement(*args)

    def zddIte(*args):
        """zddIte(self, DdNode g, DdNode h) -> DdNode"""
        return _pycudd.DdNode_zddIte(*args)

    def zddUnion(*args):
        """zddUnion(self, DdNode Q) -> DdNode"""
        return _pycudd.DdNode_zddUnion(*args)

    def zddIntersect(*args):
        """zddIntersect(self, DdNode Q) -> DdNode"""
        return _pycudd.DdNode_zddIntersect(*args)

    def zddDiff(*args):
        """zddDiff(self, DdNode Q) -> DdNode"""
        return _pycudd.DdNode_zddDiff(*args)

    def zddDiffConst(*args):
        """zddDiffConst(self, DdNode Q) -> DdNode"""
        return _pycudd.DdNode_zddDiffConst(*args)

    def zddSubset1(*args):
        """zddSubset1(self, int var) -> DdNode"""
        return _pycudd.DdNode_zddSubset1(*args)

    def zddSubset0(*args):
        """zddSubset0(self, int var) -> DdNode"""
        return _pycudd.DdNode_zddSubset0(*args)

    def zddChange(*args):
        """zddChange(self, int var) -> DdNode"""
        return _pycudd.DdNode_zddChange(*args)

    def zddCount(*args):
        """zddCount(self) -> int"""
        return _pycudd.DdNode_zddCount(*args)

    def zddCountDouble(*args):
        """zddCountDouble(self) -> double"""
        return _pycudd.DdNode_zddCountDouble(*args)

    def zddPrintMinterm(*args):
        """zddPrintMinterm(self) -> int"""
        return _pycudd.DdNode_zddPrintMinterm(*args)

    def zddPrintCover(*args):
        """zddPrintCover(self) -> int"""
        return _pycudd.DdNode_zddPrintCover(*args)

    def zddPrintDebug(*args):
        """zddPrintDebug(self, int n, int pr) -> int"""
        return _pycudd.DdNode_zddPrintDebug(*args)

    def zddCountMinterm(*args):
        """zddCountMinterm(self, int path) -> double"""
        return _pycudd.DdNode_zddCountMinterm(*args)

    def zddIsop(*args):
        """zddIsop(self, DdNode U, DdArray zdd_I) -> DdNode"""
        return _pycudd.DdNode_zddIsop(*args)

    def zddDagSize(*args):
        """zddDagSize(self, DdNode p_node) -> int"""
        return _pycudd.DdNode_zddDagSize(*args)

    def ApaPrintMinterm(*args):
        """ApaPrintMinterm(self, FILE fp, int nvars) -> int"""
        return _pycudd.DdNode_ApaPrintMinterm(*args)

    def ApaPrintMintermExp(*args):
        """ApaPrintMintermExp(self, FILE fp, int nvars, int precision) -> int"""
        return _pycudd.DdNode_ApaPrintMintermExp(*args)

    def ApaPrintDensity(*args):
        """ApaPrintDensity(self, FILE fp, int nvars) -> int"""
        return _pycudd.DdNode_ApaPrintDensity(*args)

    def ApaCountMinterm(*args):
        """ApaCountMinterm(self, int nvars, IntArray digits) -> DdApaNumber"""
        return _pycudd.DdNode_ApaCountMinterm(*args)

    def __hash__(*args):
        """__hash__(self) -> int"""
        return _pycudd.DdNode___hash__(*args)

    def __int__(*args):
        """__int__(self) -> int"""
        return _pycudd.DdNode___int__(*args)

    def __and__(*args):
        """__and__(self, DdNode other) -> DdNode"""
        return _pycudd.DdNode___and__(*args)

    def __or__(*args):
        """__or__(self, DdNode other) -> DdNode"""
        return _pycudd.DdNode___or__(*args)

    def __xor__(*args):
        """__xor__(self, DdNode other) -> DdNode"""
        return _pycudd.DdNode___xor__(*args)

    def __invert__(*args):
        """__invert__(self) -> DdNode"""
        return _pycudd.DdNode___invert__(*args)

    def __rshift__(*args):
        """__rshift__(self, DdNode other) -> DdNode"""
        return _pycudd.DdNode___rshift__(*args)

    def __cmp__(*args):
        """__cmp__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___cmp__(*args)

    def __sub__(*args):
        """__sub__(self, DdNode other) -> DdNode"""
        return _pycudd.DdNode___sub__(*args)

    def __add__(*args):
        """__add__(self, DdNode other) -> DdNode"""
        return _pycudd.DdNode___add__(*args)

    def __lt__(*args):
        """__lt__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___lt__(*args)

    def __le__(*args):
        """__le__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___le__(*args)

    def __eq__(*args):
        """__eq__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___eq__(*args)

    def __ne__(*args):
        """__ne__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___ne__(*args)

    def __gt__(*args):
        """__gt__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___gt__(*args)

    def __ge__(*args):
        """__ge__(self, DdNode other) -> bool"""
        return _pycudd.DdNode___ge__(*args)

    def __nonzero__(*args):
        """__nonzero__(self) -> bool"""
        return _pycudd.DdNode___nonzero__(*args)

    def __len__(*args):
        """__len__(self) -> int"""
        return _pycudd.DdNode___len__(*args)

    def SizeOf(*args):
        """SizeOf(self) -> int"""
        return _pycudd.DdNode_SizeOf(*args)

    def Show(*args):
        """Show(self, char name, int op1, int op2)"""
        return _pycudd.DdNode_Show(*args)

    def Empty(*args):
        """Empty(self) -> bool"""
        return _pycudd.DdNode_Empty(*args)

    def DumpDot(*args):
        """DumpDot(self) -> int"""
        return _pycudd.DdNode_DumpDot(*args)

    def DumpBlif(*args):
        """DumpBlif(self) -> int"""
        return _pycudd.DdNode_DumpBlif(*args)

    def Vector(*args):
        """Vector(self) -> DdArray"""
        return _pycudd.DdNode_Vector(*args)

_pycudd.DdNode_swigregister(DdNode)

class NodePair(_object):
    """Proxy of C++ NodePair class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr_nondynamic(self, NodePair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NodePair, name)
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ NodePair instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __iter__(self):
      global iter_meth
      if iter_meth != 2:
        print "Can only enumerate primes for a NodePair. Setting iter_meth == 2 and proceeding"
        iter_meth == 2
      return ForeachPrimeIterator(self)
    __doc__="This is used to provide the functionality of prime enumeration in CUDD 2.4.0. Create the NodePair by passing the DdNodes for lower and upper to the constructor. Once that is done, you can iterate over the primes of the NodePair using the Python for statement. There is no need to do this if you are interested in the primes of a simple DdNode -- the package automatically creates the NodePair and destroys it in that case."


    def __init__(self, *args):
        """__init__(self, DdNode lwr, DdNode upr) -> NodePair"""
        this = _pycudd.new_NodePair(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pycudd.delete_NodePair
    __del__ = lambda self : None;
    def LOWER(*args):
        """LOWER(self) -> DdNode"""
        return _pycudd.NodePair_LOWER(*args)

    def UPPER(*args):
        """UPPER(self) -> DdNode"""
        return _pycudd.NodePair_UPPER(*args)

    def FirstPrime(*args):
        """FirstPrime(self, DdGen gen, int dum_cube) -> int"""
        return _pycudd.NodePair_FirstPrime(*args)

    def NextPrime(*args):
        """NextPrime(self, DdGen gen, int dum_cube) -> int"""
        return _pycudd.NodePair_NextPrime(*args)

_pycudd.NodePair_swigregister(NodePair)

cudd_version = 0x020400

###############################
#
# iter_meth is used to set, surprise, the iteration method for DdNodes
# 0 -- over cubes
# 1 -- over nodes
# 2 -- over primes
# Note that iteration over primes is only available in CUDD >= 2.4.0
#
################################
iter_meth = 0

def set_iter_meth(meth,verbose = False):
  global iter_meth
  methods = ["cubes", "nodes", "primes"]
  if verbose:
      print "Setting iter method to iterate over ",methods[meth]
  iter_meth = meth

class ForeachCubeIterator:
    def __init__(self,Dd):
        self.gen = DdGen(Dd,iter_meth)
        self.node = Dd
        self.done = 0
        self.ret_val = Dd.FirstCube(self.gen)
        if not self.ret_val[0]: self.done = 1
        
    def __iter__(self):
        return self

    def next(self):
        if self.done: raise StopIteration
        to_ret = self.ret_val[1:]
        self.ret_val = self.node.NextCube(self.gen)
        if not self.ret_val[0]:
	    self.done = 1
        return to_ret

class ForeachNodeIterator:
    def __init__(self,Dd):
        self.gen = DdGen(Dd,iter_meth)
        self.node = Dd
        self.done = 0
        self.ret_val = Dd.FirstNode(self.gen)
        if not self.ret_val[0]: self.done = 1
        
    def __iter__(self):
        return self

    def next(self):
        if self.done: raise StopIteration
        to_ret = self.ret_val[1]
        self.ret_val = self.node.NextNode(self.gen)
        if not self.ret_val[0]:
            self.done = 1
        return to_ret

class ForeachPrimeIterator:
    def __init__(self,npair):
        global cudd_version
        if cudd_version < 0x020400:
            print "CUDD versions < 2.4.0 do not support iteration over primes"
            raise RuntimeError
        self.gen = DdGen(npair.LOWER(), iter_meth, npair.UPPER())
        self.npair = npair
        self.done = 0
        self.ret_val = npair.FirstPrime(self.gen)
        if not self.ret_val[0]: self.done = 1
    def __iter__(self):
        return self

    def next(self):
        if self.done: raise StopIteration
        to_ret = self.ret_val[1:]
        self.ret_val = self.npair.NextPrime(self.gen)
	if not self.ret_val[0]:
            self.done = 1
        return to_ret

def cube_tuple_to_str(cube_tup):
    res = ""
    for char in cube_tup:
        if char == 2: res += '-'
        else: res += str(char)
    return res

def imp(a, b):
    return ~a | b

def iff(a, b):
    return imp(a, b) & imp(b, a)

def allSat(f, domain):
    l = []
    #iterate over cubes
    set_iter_meth(0) 
    for metacube in f:
        cubes = [[]]
        for i in domain:
            if(metacube[i] < 2):
                for c in cubes:
                    c.append(metacube[i])
            else:
                cubes2 = [[e for e in c] for c in cubes]
                for c in cubes:
                    c.append(0)
                for c in cubes2:
                    c.append(1)
                cubes += cubes2
        l += cubes
    return l

def anySat(f, domain):
    # TODO : you can do MUCH better than this
    return allSat(f, domain)[0]

global cudd
cudd = DdManager()