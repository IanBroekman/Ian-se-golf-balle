import ctypes
import numpy as np

def GetCTypesDataType(datatype):
	switcher = {
		"bool" : ctypes.c_bool,
		"int8" : ctypes.c_int8,
		"int16" : ctypes.c_int16,
		"int32" : ctypes.c_int32,
		"int64" : ctypes.c_int64,
		"uint8" : ctypes.c_uint8,
		"uint16" : ctypes.c_uint16,
		"uint32" : ctypes.c_uint32,
		"uint64" : ctypes.c_uint64,
		"float"	: ctypes.c_float,
		"double" : ctypes.c_double
	}
	return switcher.get(datatype, "void")

def NumpyDatatypeToString(datatype):
	if (datatype == np.bool):
		return "bool"
	elif (datatype == np.int8):
		return "int8"
	elif (datatype == np.int16):
		return "int16"
	elif (datatype == np.int32):
		return "int32"
	elif (datatype == np.int64):
		return "int64"
	elif (datatype == np.uint8):
		return "uint8"
	elif (datatype == np.uint16):
		return "uint16"
	elif (datatype == np.uint32):
		return "uint32"
	elif (datatype == np.uint64):
		return "uint64"
	elif (datatype == np.float32):
		return "float"
	elif (datatype == np.float64):
		return "double"
	return "void"

def CPtrToNumpy(arr, shape, datatype):
	ctypesDataType = GetCTypesDataType(datatype)
	arr = ctypes.cast(arr, ctypes.POINTER(ctypesDataType))
	nparr = np.ctypeslib.as_array(arr, shape=shape)	
	return nparr.copy()

def NumpyToCPtr(numpyArr):
	cArrPtr = np.ctypeslib.as_ctypes(numpyArr)	
	cArr = ctypes.cast(cArrPtr, ctypes.c_void_p)	
	return (cArr.value, numpyArr.shape)

def GetNumpyDims(numpyArr):
	return numpyArr.shape
	
def IsNumpyArray(obj):
	return (type(obj) is np.ndarray)

def GetNumpyArrayElementDatatype(numpyArr):
	elemType = numpyArr.dtype
	return NumpyDatatypeToString(elemType)