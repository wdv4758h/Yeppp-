#
#                      Yeppp! library implementation
#
# This file is part of Yeppp! library and licensed under the New BSD license.
# See library/LICENSE.txt for the full text of the license.
#

import yeppp.module

import yeppp.library.core.x86
import yeppp.library.core.x64

def generate_add(module):
	with yeppp.module.Function(module, 'Add', 'Addition') as function:
		function.c_documentation = """
@brief	Adds corresponding elements in two %(InputType0)s arrays, producing an array of %(OutputType0)s elements.
@param[in]	x	Pointer the first array of %(InputType0)s elements to be added.
@param[in]	y	Pointer the second array of %(InputType1)s elements to be added.
@param[out]	sum	Pointer the array of %(OutputType0)s elements where the pairwise sums will be stored.
@param[in]	length	The length of the arrays specified by @a x and @a y, and @a sum.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.AddSub_VXusVXus_VYus_SSE) 
		function.assembly_implementations.append(yeppp.library.core.x64.AddSub_VXusVXus_VYus_AVX)
		function.assembly_implementations.append(yeppp.library.core.x64.AddSubMulMinMax_VfVf_Vf_SSE) 
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s sum = x + y;
	*sumPointer++ = sum;
}
return YepStatusOk;
"""
		function.generate("yepCore_Add_V8uV8u_V8u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V8uV8u_V16u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V8sV8s_V16s(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V16uV16u_V16u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V16uV16u_V32u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V16sV16s_V32s(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V32uV32u_V32u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V32uV32u_V64u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V32sV32s_V64s(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V64uV64u_V64u(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V32fV32f_V32f(x, y, sum, YepSize length)")
		function.generate("yepCore_Add_V64fV64f_V64f(x, y, sum, YepSize length)")

# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	const Yep%(OutputType0)s x = *xPointer++;
# 	const Yep%(OutputType0)s sum = x + y;
# 	*sumPointer++ = sum;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Add_V8uS8u_V8u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V8uS8u_V16u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V8sS8s_V16s(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V16uS16u_V16u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V16uS16u_V32u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V16sS16s_V32s(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V32uS32u_V32u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V32uS32u_V64u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V32sS32s_V64s(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V64uS64u_V64u(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V32fS32f_V32f(x, y, sum, YepSize length)")
# 		function.generate("yepCore_Add_V64fS64f_V64f(x, y, sum, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	Yep%(OutputType0)s x = *xPointer;
# 	const Yep%(OutputType0)s y = *yPointer++;
# 	x += y;
# 	*xPointer++ = x;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Add_IV8uV8u_IV8u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV16uV16u_IV16u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV32uV32u_IV32u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV64uV64u_IV64u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV32fV32f_IV32f(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV64fV64f_IV64f(x, y, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	Yep%(OutputType0)s x = *xPointer;
# 	x += y;
# 	*xPointer++ = x;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Add_IV8uS8u_IV8u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV16uS16u_IV16u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV32uS32u_IV32u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV64uS64u_IV64u(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV32fS32f_IV32f(x, y, YepSize length)")
# 		function.generate("yepCore_Add_IV64fS64f_IV64f(x, y, YepSize length)")

def generate_subtract(module):
	with yeppp.module.Function(module, 'Subtract', 'Subtraction') as function:
		function.c_documentation = """
@brief	Subtracts corresponding elements in two %(InputType0)s arrays, producing an array of %(OutputType0)s elements.
@param[in]	x	Pointer the minuend array of %(InputType0)s elements to be subtracted from.
@param[in]	y	Pointer the subtrahend array of %(InputType1)s elements to be subtracted.
@param[out]	difference	Pointer the array of %(OutputType0)s elements where the pairwise differences will be stored.
@param[in]	length	The length of the arrays specified by @a x and @a y, and @a sum.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.AddSub_VXusVXus_VYus_SSE) 
		function.assembly_implementations.append(yeppp.library.core.x64.AddSub_VXusVXus_VYus_AVX)
		function.assembly_implementations.append(yeppp.library.core.x64.AddSubMulMinMax_VfVf_Vf_SSE) 
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s difference = x - y;
	*differencePointer++ = difference;
}
return YepStatusOk;
"""
		function.generate("yepCore_Subtract_V8uV8u_V8u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V8uV8u_V16u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V8sV8s_V16s(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V16uV16u_V16u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V16uV16u_V32u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V16sV16s_V32s(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V32uV32u_V32u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V32uV32u_V64u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V32sV32s_V64s(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V64uV64u_V64u(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V32fV32f_V32f(x, y, difference, YepSize length)")
		function.generate("yepCore_Subtract_V64fV64f_V64f(x, y, difference, YepSize length)")
	
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	const Yep%(OutputType0)s x = *xPointer++;
# 	const Yep%(OutputType0)s difference = x - y;
# 	*differencePointer++ = difference;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Subtract_V8uS8u_V8u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V8uS8u_V16u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V8sS8s_V16s(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V16uS16u_V16u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V16uS16u_V32u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V16sS16s_V32s(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V32uS32u_V32u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V32uS32u_V64u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V32sS32s_V64s(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V64uS64u_V64u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V32fS32f_V32f(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_V64fS64f_V64f(x, y, difference, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	const Yep%(OutputType0)s y = *yPointer++;
# 	const Yep%(OutputType0)s difference = x - y;
# 	*differencePointer++ = difference;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Subtract_S8uV8u_V8u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S8uV8u_V16u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S8sV8s_V16s(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S16uV16u_V16u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S16uV16u_V32u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S16sV16s_V32s(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S32uV32u_V32u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S32uV32u_V64u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S32sV32s_V64s(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S64uV64u_V64u(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S32fV32f_V32f(x, y, difference, YepSize length)")
# 		function.generate("yepCore_Subtract_S64fV64f_V64f(x, y, difference, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	Yep%(OutputType0)s x = *xPointer;
# 	const Yep%(OutputType0)s y = *yPointer++;
# 	x -= y;
# 	*xPointer++ = x;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Subtract_IV8uV8u_IV8u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV16uV16u_IV16u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV32uV32u_IV32u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV64uV64u_IV64u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV32fV32f_IV32f(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV64fV64f_IV64f(x, y, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	const Yep%(OutputType0)s x = *xPointer++;
# 	Yep%(OutputType0)s y = *yPointer;
# 	y = x - y;
# 	*yPointer++ = y;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Subtract_V8uIV8u_IV8u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_V16uIV16u_IV16u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_V32uIV32u_IV32u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_V64uIV64u_IV64u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_V32fIV32f_IV32f(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_V64fIV64f_IV64f(x, y, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	Yep%(OutputType0)s x = *xPointer;
# 	x -= y;
# 	*xPointer++ = x;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Subtract_IV8uS8u_IV8u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV16uS16u_IV16u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV32uS32u_IV32u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV64uS64u_IV64u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV32fS32f_IV32f(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_IV64fS64f_IV64f(x, y, YepSize length)")
# 
# 		function.c_documentation = None
# 		function.assembly_implementations = []
# 		function.c_implementation = """
# while (length-- != 0) {
# 	Yep%(OutputType0)s y = *yPointer;
# 	y = x - y;
# 	*yPointer++ = y;
# }
# return YepStatusOk;
# """
# 		function.generate("yepCore_Subtract_S8uIV8u_IV8u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_S16uIV16u_IV16u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_S32uIV32u_IV32u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_S64uIV64u_IV64u(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_S32fIV32f_IV32f(x, y, YepSize length)")
# 		function.generate("yepCore_Subtract_S64fIV64f_IV64f(x, y, YepSize length)")

def generate_negate(module):
	with yeppp.module.Function(module, 'Negate', 'Negation') as function:
		function.c_documentation = """
@brief	Negates a vector of %(InputType0)s elements.
@param[in]	numberPointer	Pointer the input array of %(InputType0)s elements to be negated from.
@param[out]	negatedNumberPointer	Pointer the output array of %(OutputType0)s negated elements.
@param[in]	length	The length of the arrays pointed by @a numberPointer and @a negatedNumberPointer.
@retval	#YepStatusOk	The computations finished successfully.
@retval	#YepStatusNullPointer	One of the @a numberPointer or @a negatedNumberPointer arguments is null.
@retval	#YepStatusMisalignedPointer	One of the @a numberPointer or @a negatedNumberPointer arguments is not properly aligned.
"""
		function.assembly_implementations = []
#		function.assembly_implementations = [yeppp.library.core.x86.Negate_Vf_Vf_implementation]
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = -x;
	*yPointer++ = y;
}
return YepStatusOk;
"""
		function.generate("yepCore_Negate_V8s_V8s(x, y, YepSize length)")
		function.generate("yepCore_Negate_V16s_V16s(x, y, YepSize length)")
		function.generate("yepCore_Negate_V32s_V32s(x, y, YepSize length)")
		function.generate("yepCore_Negate_V64s_V64s(x, y, YepSize length)")
		function.generate("yepCore_Negate_V32f_V32f(x, y, YepSize length)")
		function.generate("yepCore_Negate_V64f_V64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s v = *vPointer;
	const Yep%(OutputType0)s minusV = -v;
	*vPointer++ = minusV;
}
return YepStatusOk;
"""
		function.generate("yepCore_Negate_IV8s_IV8s(v, YepSize length)")
		function.generate("yepCore_Negate_IV16s_IV16s(v, YepSize length)")
		function.generate("yepCore_Negate_IV32s_IV32s(v, YepSize length)")
		function.generate("yepCore_Negate_IV64s_IV64s(v, YepSize length)")
		function.generate("yepCore_Negate_IV32f_IV32f(v, YepSize length)")
		function.generate("yepCore_Negate_IV64f_IV64f(v, YepSize length)")
	
def generate_multiply(module):
	with yeppp.module.Function(module, 'Multiply', 'Multiplication') as function:
		function.c_documentation = """
@brief	Multiples corresponding elements in two %(InputType0)s arrays, producing an array of %(OutputType0)s elements.
@param[in]	x	Pointer the first array of %(InputType0)s elements to be multiplied.
@param[in]	y	Pointer the second array of %(InputType1)s elements to be multiplied.
@param[out]	product	Pointer the array of %(OutputType0)s elements where the pairwise products will be stored.
@param[in]	length	The length of the arrays specified by @a x and @a y, and @a product.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.Multiply_VXuVXu_VXu)
		function.assembly_implementations.append(yeppp.library.core.x64.Multiply_V16usV16us_V32us)
		function.assembly_implementations.append(yeppp.library.core.x64.Multiply_V32usV32us_V64us)
		function.assembly_implementations.append(yeppp.library.core.x64.AddSubMulMinMax_VfVf_Vf_SSE)
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s product = x * y;
	*productPointer++ = product;
}
return YepStatusOk;
"""
		function.generate("yepCore_Multiply_V8uV8u_V8u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V8uV8u_V16u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V8sV8s_V16s(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V16uV16u_V16u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V16uV16u_V32u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V16sV16s_V32s(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32uV32u_V32u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32uV32u_V64u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32sV32s_V64s(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V64uV64u_V64u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32fV32f_V32f(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V64fV64f_V64f(x, y, product, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s product = x * y;
	*productPointer++ = product;
}
return YepStatusOk;
"""
		function.generate("yepCore_Multiply_V8uS8u_V8u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V8uS8u_V16u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V8sS8s_V16s(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V16uS16u_V16u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V16uS16u_V32u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V16sS16s_V32s(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32uS32u_V32u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32uS32u_V64u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32sS32s_V64s(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V64uS64u_V64u(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V32fS32f_V32f(x, y, product, YepSize length)")
		function.generate("yepCore_Multiply_V64fS64f_V64f(x, y, product, YepSize length)")

		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	const Yep%(OutputType0)s y = *yPointer++;
	x *= y;
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Multiply_IV8uV8u_IV8u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV16uV16u_IV16u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV32uV32u_IV32u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV64uV64u_IV64u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV32fV32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV64fV64f_IV64f(x, y, YepSize length)")

		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	x *= y;
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Multiply_IV8uS8u_IV8u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV16uS16u_IV16u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV32uS32u_IV32u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV64uS64u_IV64u(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV32fS32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Multiply_IV64fS64f_IV64f(x, y, YepSize length)")

def generate_multiply_add(module):
	with yeppp.module.Function(module, 'MultiplyAdd', 'Multiplication and addition') as function:

		function.c_documentation = """
@brief	Computes pairwise products of %(InputType0)s elements in two arrays and then adds the third %(InputType2)s array to the result, producing an array of %(OutputType0)s elements.
@param[in]	x	Pointer the first input array of %(InputType0)s elements to be multiplied.
@param[in]	y	Pointer the second input array of %(InputType1)s elements to be multiplied.
@param[in]	z	Pointer the input array of %(InputType2)s elements to be added to the intermediate multiplication result.
@param[out]	mac	Pointer the output array of %(OutputType0)s elements.
@param[in]	length	The length of the arrays pointed by @a x, @a y, @a z, and @a mac.
"""
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s z = *zPointer++;
	const Yep%(OutputType0)s mac = x * y + z;
	*macPointer++ = mac;
}
return YepStatusOk;
"""
		function.generate("yepCore_MultiplyAdd_V32fV32fV32f_V32f(x, y, z, mac, YepSize length)")
		function.generate("yepCore_MultiplyAdd_V64fV64fV64f_V64f(x, y, z, mac, YepSize length)")

		function.c_documentation = """
@brief	Computes pairwise products of %(InputType0)s elements in two arrays and then adds the third %(InputType2)s array to the result, overwriting the third array.
@param[in]	x	Pointer the first input array of %(InputType0)s elements to be multiplied.
@param[in]	y	Pointer the second input array of %(InputType1)s elements to be multiplied.
@param[in,out]	z	Pointer the input/output array of %(InputType2)s elements to be added to the intermediate multiplication result.
@param[in]	length	The length of the arrays pointed by @a xPointer, @a yPointer, and @a zPointer.
"""
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	Yep%(OutputType0)s z = *zPointer;
	z = x * y + z;
	*zPointer++ = z;
}
return YepStatusOk;
"""
		function.generate("yepCore_MultiplyAdd_V32fS32fIV32f_IV32f(x, y, z, YepSize length)")
		function.generate("yepCore_MultiplyAdd_V64fS64fIV64f_IV64f(x, y, z, YepSize length)")

def generate_divide(module):
	with yeppp.module.Function(module, 'Divide', 'Division') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s fraction = x / y;
	*fractionPointer++ = fraction;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_V32fV32f_V32f(x, y, fraction, YepSize length)")
		function.generate("yepCore_Divide_V64fV64f_V64f(x, y, fraction, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s fraction = x / y;
	*fractionPointer++ = fraction;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_V32fS32f_V32f(x, y, fraction, YepSize length)")
		function.generate("yepCore_Divide_V64fS64f_V64f(x, y, fraction, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s fraction = x / y;
	*fractionPointer++ = fraction;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_S32fV32f_V32f(x, y, fraction, YepSize length)")
		function.generate("yepCore_Divide_S64fV64f_V64f(x, y, fraction, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	const Yep%(OutputType0)s y = *yPointer++;
	x /= y;
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_IV32fV32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Divide_IV64fV64f_IV64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	Yep%(OutputType0)s y = *yPointer;
	y = x / y;
	*yPointer++ = y;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_V32fIV32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Divide_V64fIV64f_IV64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	x /= y;
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_IV32fS32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Divide_IV64fS64f_IV64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s y = *yPointer;
	y = x / y;
	*yPointer++ = y;
}
return YepStatusOk;
"""
		function.generate("yepCore_Divide_S32fIV32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Divide_S64fIV64f_IV64f(x, y, YepSize length)")
	
def generate_copy(module):
	with yeppp.module.Function(module, 'Copy', 'Memory copy') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s element = *sourcePointer++;
	*destinationPointer++ = element;
}
return YepStatusOk;
"""
		function.generate("yepCore_Copy_V8u_V8u(source, destination, YepSize length)")

def generate_zero(module):
	with yeppp.module.Function(module, 'Zero', 'Zero copy') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	*destinationPointer++ = Yep%(OutputType0)s(0);
}
return YepStatusOk;
"""
		function.generate("yepCore_Zero__V8u(destination, YepSize length)")

def generate_reciprocal(module):
	with yeppp.module.Function(module, 'Reciprocal', 'Reciprocal') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = Yep%(OutputType0)s(1) / x;
	*yPointer++ = y;
}
return YepStatusOk;
"""
		function.generate("yepCore_Reciprocal_V32f_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V64f_V64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(InputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = Yep%(OutputType0)s(1) / yepBuiltin_Convert_%(InputType0)s_%(OutputType0)s(x);
	*yPointer++ = y;
}
return YepStatusOk;
"""
		function.generate("yepCore_Reciprocal_V8u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V8s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V16u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V16s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V32u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V32s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V64u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V64s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V8u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V8s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V16u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V16s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V32u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V32s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V64u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Reciprocal_V64s_V64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s v = *vPointer;
	const Yep%(OutputType0)s rcpV = Yep%(OutputType0)s(1) / v;
	*vPointer++ = rcpV;
}
return YepStatusOk;
"""
		function.generate("yepCore_Reciprocal_IV32f_IV32f(v, YepSize length)")
		function.generate("yepCore_Reciprocal_IV64f_IV64f(v, YepSize length)")

def generate_convert(module):
	with yeppp.module.Function(module, 'Convert', 'Type conversion') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = yepBuiltin_Convert_%(InputType0)s_%(OutputType0)s(x);
	*yPointer++ = y;
}
return YepStatusOk;
"""
		function.generate("yepCore_Convert_V8s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V8u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V16s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V16u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V32s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V32u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V64s_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V64u_V32f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V8s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V8u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V16s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V16u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V32s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V32u_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V64s_V64f(x, y, YepSize length)")
		function.generate("yepCore_Convert_V64u_V64f(x, y, YepSize length)")

def generate_min(module):
	with yeppp.module.Function(module, 'Min', 'Minimum') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
Yep%(InputType0)s minimum = *vPointer++;
while (--length != 0) {
	const Yep%(InputType0)s v = *vPointer++;
	minimum = yepBuiltin_Min_%(InputType0)s%(InputType0)s_%(InputType0)s(v, minimum);
}
*minimumPointer++ = minimum;
return YepStatusOk;
"""
		function.generate("yepCore_Min_V8s_S8s(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V8u_S8u(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V16s_S16s(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V16u_S16u(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V32s_S32s(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V32u_S32u(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V64s_S64s(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V64u_S64u(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V32f_S32f(v, minimum, YepSize length)")
		function.generate("yepCore_Min_V64f_S64f(v, minimum, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s minimum = yepBuiltin_Min_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*minimumPointer++ = minimum;
}
return YepStatusOk;
"""
		function.generate("yepCore_Min_V8sV8s_V8s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V8uV8u_V8u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V16sV16s_V16s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V16uV16u_V16u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V32sV32s_V32s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V32uV32u_V32u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V64sV32s_V64s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V64uV32u_V64u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V32fV32f_V32f(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V64fV64f_V64f(x, y, minimum, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s minimum = yepBuiltin_Min_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*minimumPointer++ = minimum;
}
return YepStatusOk;
"""
		function.generate("yepCore_Min_V8sS8s_V8s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V8uS8u_V8u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V16sS16s_V16s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V16uS16u_V16u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V32sS32s_V32s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V32uS32u_V32u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V64sS32s_V64s(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V64uS32u_V64u(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V32fS32f_V32f(x, y, minimum, YepSize length)")
		function.generate("yepCore_Min_V64fS64f_V64f(x, y, minimum, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	const Yep%(OutputType0)s y = *yPointer++;
	x = yepBuiltin_Min_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Min_IV8sV8s_IV8s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV8uV8u_IV8u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV16sV16s_IV16s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV16uV16u_IV16u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV32sV32s_IV32s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV32uV32u_IV32u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV64sV32s_IV64s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV64uV32u_IV64u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV32fV32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Min_IV64fV64f_IV64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	x = yepBuiltin_Min_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Min_IV8sS8s_IV8s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV8uS8u_IV8u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV16sS16s_IV16s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV16uS16u_IV16u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV32sS32s_IV32s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV32uS32u_IV32u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV64sS32s_IV64s(x, y, YepSize length)")
		function.generate("yepCore_Min_IV64uS32u_IV64u(x, y, YepSize length)")
		function.generate("yepCore_Min_IV32fS32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Min_IV64fS64f_IV64f(x, y, YepSize length)")

def generate_max(module):
	with yeppp.module.Function(module, 'Max', 'Maximum') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
Yep%(InputType0)s maximum = *vPointer++;
while (--length != 0) {
	const Yep%(InputType0)s v = *vPointer++;
	maximum = yepBuiltin_Max_%(InputType0)s%(InputType0)s_%(InputType0)s(v, maximum);
}
*maximumPointer = maximum;
return YepStatusOk;
"""
		function.generate("yepCore_Max_V8s_S8s(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V8u_S8u(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V16s_S16s(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V16u_S16u(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V32s_S32s(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V32u_S32u(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V64s_S64s(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V64u_S64u(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V32f_S32f(v, maximum, YepSize length)")
		function.generate("yepCore_Max_V64f_S64f(v, maximum, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s y = *yPointer++;
	const Yep%(OutputType0)s maximum = yepBuiltin_Max_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*maximumPointer++ = maximum;
}
return YepStatusOk;
"""
		function.generate("yepCore_Max_V8sV8s_V8s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V8uV8u_V8u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V16sV16s_V16s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V16uV16u_V16u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V32sV32s_V32s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V32uV32u_V32u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V64sV32s_V64s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V64uV32u_V64u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V32fV32f_V32f(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V64fV64f_V64f(x, y, maximum, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(OutputType0)s x = *xPointer++;
	const Yep%(OutputType0)s maximum = yepBuiltin_Max_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*maximumPointer++ = maximum;
}
return YepStatusOk;
"""
		function.generate("yepCore_Max_V8sS8s_V8s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V8uS8u_V8u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V16sS16s_V16s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V16uS16u_V16u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V32sS32s_V32s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V32uS32u_V32u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V64sS32s_V64s(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V64uS32u_V64u(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V32fS32f_V32f(x, y, maximum, YepSize length)")
		function.generate("yepCore_Max_V64fS64f_V64f(x, y, maximum, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	const Yep%(OutputType0)s y = *yPointer++;
	x = yepBuiltin_Max_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Max_IV8sV8s_IV8s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV8uV8u_IV8u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV16sV16s_IV16s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV16uV16u_IV16u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV32sV32s_IV32s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV32uV32u_IV32u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV64sV32s_IV64s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV64uV32u_IV64u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV32fV32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Max_IV64fV64f_IV64f(x, y, YepSize length)")
	
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	Yep%(OutputType0)s x = *xPointer;
	x = yepBuiltin_Max_%(OutputType0)s%(OutputType0)s_%(OutputType0)s(x, y);
	*xPointer++ = x;
}
return YepStatusOk;
"""
		function.generate("yepCore_Max_IV8sS8s_IV8s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV8uS8u_IV8u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV16sS16s_IV16s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV16uS16u_IV16u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV32sS32s_IV32s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV32uS32u_IV32u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV64sS32s_IV64s(x, y, YepSize length)")
		function.generate("yepCore_Max_IV64uS32u_IV64u(x, y, YepSize length)")
		function.generate("yepCore_Max_IV32fS32f_IV32f(x, y, YepSize length)")
		function.generate("yepCore_Max_IV64fS64f_IV64f(x, y, YepSize length)")

def generate_min_max(module):
	with yeppp.module.Function(module, 'MinMax', 'Minimum and maximum') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
Yep%(InputType0)s minimum = *vPointer++;
Yep%(InputType0)s maximum = minimum;
while (--length != 0) {
	const Yep%(InputType0)s v = *vPointer++;
	maximum = yepBuiltin_Max_%(InputType0)s%(InputType0)s_%(InputType0)s(v, maximum);
	minimum = yepBuiltin_Min_%(InputType0)s%(InputType0)s_%(InputType0)s(v, minimum);
}
*minimumPointer = minimum;
*maximumPointer = maximum;
return YepStatusOk;
"""
		function.generate("yepCore_MinMax_V8s_S8sS8s(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V8u_S8uS8u(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V16s_S16sS16s(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V16u_S16uS16u(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V32s_S32sS32s(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V32u_S32uS32u(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V64s_S64sS64s(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V64u_S64uS64u(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V32f_S32fS32f(v, minimum, maximum, YepSize length)")
		function.generate("yepCore_MinMax_V64f_S64fS64f(v, minimum, maximum, YepSize length)")
	
def generate_sum(module):
	with yeppp.module.Function(module, 'Sum', 'Sum') as function:
		function.c_documentation = """
@brief	Computes the sum of %(InputType0)s elements in the input array.
@param[in]	v	Pointer to the array of elements which will be summed up.
@param[out]	sum	Pointer to the variable where the sum will be stored.
@param[in]	length	The length of the array specified by @a v. The @a length is zero, the computed sum will be 0.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.Sum_VXf_SXf_SSE)
		function.assembly_implementations.append(yeppp.library.core.x64.Sum_VXf_SXf_AVX)
		function.c_implementation = """
Yep%(InputType0)s sum = Yep%(InputType0)s(0);
while (length-- != 0) {
	const Yep%(InputType0)s v = *vPointer++;
	sum += v;
}
*sumPointer = sum;
return YepStatusOk;
"""
		function.generate("yepCore_Sum_V32f_S32f(v, sum, YepSize length)")
		function.generate("yepCore_Sum_V64f_S64f(v, sum, YepSize length)")

def generate_sum_abs(module):
	with yeppp.module.Function(module, 'SumAbs', 'Sum of absolute values') as function:
		function.c_documentation = """
@brief	Computes the sum of absolute values of %(InputType0)s elements in the input array.
@param[in]	v	Pointer to the array of elements whose absolute values will be summed up.
@param[out]	sumAbs	Pointer to the variable where the sum of absolute values will be stored.
@param[in]	length	The length of the array specified by @a v. The @a length is zero, the computed sum will be 0.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.SumAbs_VXf_SXf_SSE)
		function.assembly_implementations.append(yeppp.library.core.x64.SumAbs_VXf_SXf_AVX)
		function.c_implementation = """
Yep%(InputType0)s sumAbs = Yep%(InputType0)s(0);
while (length-- != 0) {
	const Yep%(InputType0)s v = *vPointer++;
	sumAbs += yepBuiltin_Abs_%(InputType0)s_%(OutputType0)s(v);
}
*sumAbsPointer = sumAbs;
return YepStatusOk;
"""
		function.generate("yepCore_SumAbs_V32f_S32f(v, sumAbs, YepSize length)")
		function.generate("yepCore_SumAbs_V64f_S64f(v, sumAbs, YepSize length)")

def generate_sum_squares(module):
	with yeppp.module.Function(module, 'SumSquares', 'Sum of squares (squared L2 norm)') as function:
		function.c_documentation = """
@brief	Computes the sum of squares of %(InputType0)s elements in the input array.
@param[in]	v	Pointer to the array of elements which will be squared (without write-back) and summed up.
@param[out]	sumSquares	Pointer to the variable where the sum of squares will be stored.
@param[in]	length	The length of the array specified by @a v. The @a length is zero, the computed sum of squares will be 0.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.SumSquares_VXf_SXf_SSE)
		function.assembly_implementations.append(yeppp.library.core.x64.SumSquares_VXf_SXf_AVX)
		function.c_implementation = """
Yep%(InputType0)s sumSquares = Yep%(InputType0)s(0);
while (length-- != 0) {
	const Yep%(InputType0)s v = *vPointer++;
	sumSquares += v * v;
}
*sumSquaresPointer = sumSquares;
return YepStatusOk;
"""
		function.generate("yepCore_SumSquares_V32f_S32f(v, sumSquares, YepSize length)")
		function.generate("yepCore_SumSquares_V64f_S64f(v, sumSquares, YepSize length)")

def generate_dot_product(module):
	with yeppp.module.Function(module, 'DotProduct', 'Dot product') as function:
		function.c_documentation = """
@brief	Computes the dot product of %(InputType0)s elements in two arrays.
@param[in]	x	Pointer to the first vector of elements.
@param[in]	y	Pointer to the second vector of elements.
@param[out]	dotProduct	Pointer to the variable where the dot product value will be stored.
@param[in]	length	The length of the arrays specified by @a x and @a y.
"""
		function.assembly_implementations = list()
		function.assembly_implementations.append(yeppp.library.core.x64.DotProduct_VXfVXf_SXf_SSE)
		function.assembly_implementations.append(yeppp.library.core.x64.DotProduct_VXfVXf_SXf_AVX)
		function.c_implementation = """
Yep%(InputType0)s dotProduct = Yep%(InputType0)s(0);
while (length-- != 0) {
	const Yep%(InputType0)s x = *xPointer++;
	const Yep%(InputType0)s y = *yPointer++;
	dotProduct += x * y;
}
*dotProductPointer = dotProduct;
return YepStatusOk;
"""
		function.generate("yepCore_DotProduct_V32fV32f_S32f(x, y, dotProduct, YepSize length)")
		function.generate("yepCore_DotProduct_V64fV64f_S64f(x, y, dotProduct, YepSize length)")

def generate_gather(module):
	with yeppp.module.Function(module, 'Gather', 'Gather') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const YepSize index = YepSize(*indexPointer++);
	const Yep%(InputType0)s element = sourcePointer[index];
	*destinationPointer++ = element;
}
return YepStatusOk;
"""
		function.generate("yepCore_Gather_V8uV8u_V8u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V8uV16u_V8u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V8uV32u_V8u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V8uV64u_V8u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V16uV8u_V16u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V16uV16u_V16u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V16uV32u_V16u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V16uV64u_V16u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V32uV8u_V32u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V32uV16u_V32u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V32uV32u_V32u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V32uV64u_V32u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V64uV8u_V64u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V64uV16u_V64u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V64uV32u_V64u(source, index, destination, YepSize length)")
		function.generate("yepCore_Gather_V64uV64u_V64u(source, index, destination, YepSize length)")

def generate_scatter_increment(module):
	with yeppp.module.Function(module, 'ScatterIncrement', 'Scatter-increment') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const YepSize index = YepSize(*indexPointer++);
	basePointer[index] += 1;
}
return YepStatusOk;
"""
		function.generate("yepCore_ScatterIncrement_IV8uV8u_IV8u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV16uV8u_IV16u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV32uV8u_IV32u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV64uV8u_IV64u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV8uV16u_IV8u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV16uV16u_IV16u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV32uV16u_IV32u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV64uV16u_IV64u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV8uV32u_IV8u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV16uV32u_IV16u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV32uV32u_IV32u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV64uV32u_IV64u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV8uV64u_IV8u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV16uV64u_IV16u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV32uV64u_IV32u(base, index, YepSize length)")
		function.generate("yepCore_ScatterIncrement_IV64uV64u_IV64u(base, index, YepSize length)")

def generate_scatter_add(module):
	with yeppp.module.Function(module, 'ScatterAdd', 'Scatter-add') as function:
		function.c_documentation = None
		function.assembly_implementations = []
		function.c_implementation = """
while (length-- != 0) {
	const Yep%(InputType0)s weight = *weightPointer++;
	const YepSize index = YepSize(*indexPointer++);
	basePointer[index] += weight;
}
return YepStatusOk;
"""
		function.generate("yepCore_ScatterAdd_IV8uV8uV8u_IV8u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV8uV8u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV8uV16u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV8uV8u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV8uV16u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV8uV32u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV8uV8u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV8uV16u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV8uV32u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV8uV64u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV8uV16uV8u_IV8u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV16uV8u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV16uV16u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV16uV8u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV16uV16u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV16uV32u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV16uV8u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV16uV16u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV16uV32u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV16uV64u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV8uV32uV8u_IV8u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV32uV8u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV32uV16u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV32uV8u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV32uV16u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV32uV32u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV32uV8u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV32uV16u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV32uV32u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV32uV64u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV8uV64uV8u_IV8u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV64uV8u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV16uV64uV16u_IV16u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV64uV8u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV64uV16u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV32uV64uV32u_IV32u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV64uV8u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV64uV16u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV64uV32u_IV64u(base, index, weight, YepSize length)")
		function.generate("yepCore_ScatterAdd_IV64uV64uV64u_IV64u(base, index, weight, YepSize length)")

if __name__ == '__main__':
	with yeppp.module.Module('Core', 'Basic arithmetic operations') as module:
# 		generate_copy(module)
# 		generate_zero(module)
		generate_add(module)
		generate_subtract(module)
# 		generate_negate(module)
		generate_multiply(module)
# 		generate_multiply_add(module)
# 		generate_divide(module)
# 		generate_reciprocal(module)
# 		generate_convert(module)
# 		generate_min(module)
# 		generate_max(module)
		generate_min_max(module)
		generate_sum(module)
		generate_sum_abs(module)
		generate_sum_squares(module)
		generate_dot_product(module)
# 		generate_gather(module)
# 		generate_scatter_increment(module)
# 		generate_scatter_add(module)

