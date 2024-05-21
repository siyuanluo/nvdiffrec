# Copyright 2023 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ruff: noqa

import datetime
from numpy import array, float32, complex64

data_2023_06_19 = {}

# Pasted from the test output (see back_compat_test.py module docstring)
data_2023_06_19["f32"] = dict(
    testdata_version=1,
    platform='cpu',
    custom_call_targets=['lapack_sgeev'],
    serialized_date=datetime.date(2023, 6, 19),
    inputs=(),
    expected_outputs=(array([ 3.2464241e+01+0.j, -2.4642489e+00+0.j,  1.4189274e-07+0.j,
       -4.0686123e-07+0.j], dtype=complex64), array([[-0.40377745 +0.j, -0.82883257 +0.j, -0.06733338 +0.j,
        -0.5208027  +0.j],
       [-0.46480742 +0.j, -0.4371466  +0.j,  0.49492982 +0.j,
         0.82081676 +0.j],
       [-0.52583724 +0.j, -0.045459956+0.j, -0.78785884 +0.j,
        -0.07922471 +0.j],
       [-0.5868671  +0.j,  0.3462263  +0.j,  0.36026272 +0.j,
        -0.2207891  +0.j]], dtype=complex64), array([[-0.11417642+0.j, -0.73277813+0.j,  0.16960056+0.j,
        -0.5435681 +0.j],
       [-0.33000448+0.j, -0.28974825+0.j,  0.16204938+0.j,
         0.67456985+0.j],
       [-0.54583275+0.j,  0.15328142+0.j, -0.8329006 +0.j,
         0.28156415+0.j],
       [-0.761661  +0.j,  0.5963111 +0.j,  0.5012507 +0.j,
        -0.41256607+0.j]], dtype=complex64)),
    mlir_module_text=r"""
module @jit_func attributes {mhlo.num_partitions = 1 : i32, mhlo.num_replicas = 1 : i32} {
  func.func public @main() -> (tensor<4xcomplex<f32>> {jax.result_info = "[0]"}, tensor<4x4xcomplex<f32>> {jax.result_info = "[1]"}, tensor<4x4xcomplex<f32>> {jax.result_info = "[2]"}) {
    %0 = stablehlo.iota dim = 0 : tensor<16xf32> loc(#loc3)
    %1 = stablehlo.reshape %0 : (tensor<16xf32>) -> tensor<4x4xf32> loc(#loc4)
    %2 = stablehlo.constant dense<1> : tensor<i32> loc(#loc5)
    %3 = stablehlo.constant dense<4> : tensor<i32> loc(#loc5)
    %4 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %5 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %6:8 = stablehlo.custom_call @lapack_sgeev(%2, %3, %4, %5, %1) {api_version = 2 : i32, operand_layouts = [dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<[0, 1]> : tensor<2xindex>], result_layouts = [dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<0> : tensor<1xindex>, dense<0> : tensor<1xindex>, dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<> : tensor<0xindex>]} : (tensor<i32>, tensor<i32>, tensor<ui8>, tensor<ui8>, tensor<4x4xf32>) -> (tensor<4x4xf32>, tensor<4x4xf32>, tensor<4x4xf32>, tensor<4xf32>, tensor<4xf32>, tensor<4x4xcomplex<f32>>, tensor<4x4xcomplex<f32>>, tensor<i32>) loc(#loc5)
    %7 = stablehlo.complex %6#3, %6#4 : tensor<4xcomplex<f32>> loc(#loc5)
    %8 = stablehlo.constant dense<0> : tensor<i32> loc(#loc5)
    %9 = stablehlo.broadcast_in_dim %8, dims = [] : (tensor<i32>) -> tensor<i32> loc(#loc5)
    %10 = stablehlo.compare  EQ, %6#7, %9,  SIGNED : (tensor<i32>, tensor<i32>) -> tensor<i1> loc(#loc5)
    %11 = stablehlo.broadcast_in_dim %10, dims = [] : (tensor<i1>) -> tensor<1xi1> loc(#loc5)
    %12 = stablehlo.constant dense<(0x7FC00000,0x7FC00000)> : tensor<complex<f32>> loc(#loc5)
    %13 = stablehlo.broadcast_in_dim %12, dims = [] : (tensor<complex<f32>>) -> tensor<4xcomplex<f32>> loc(#loc5)
    %14 = stablehlo.broadcast_in_dim %11, dims = [0] : (tensor<1xi1>) -> tensor<4xi1> loc(#loc5)
    %15 = stablehlo.select %14, %7, %13 : tensor<4xi1>, tensor<4xcomplex<f32>> loc(#loc5)
    %16 = stablehlo.broadcast_in_dim %10, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %17 = stablehlo.constant dense<(0x7FC00000,0x7FC00000)> : tensor<complex<f32>> loc(#loc5)
    %18 = stablehlo.broadcast_in_dim %17, dims = [] : (tensor<complex<f32>>) -> tensor<4x4xcomplex<f32>> loc(#loc5)
    %19 = stablehlo.broadcast_in_dim %16, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %20 = stablehlo.select %19, %6#5, %18 : tensor<4x4xi1>, tensor<4x4xcomplex<f32>> loc(#loc5)
    %21 = stablehlo.broadcast_in_dim %10, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %22 = stablehlo.constant dense<(0x7FC00000,0x7FC00000)> : tensor<complex<f32>> loc(#loc5)
    %23 = stablehlo.broadcast_in_dim %22, dims = [] : (tensor<complex<f32>>) -> tensor<4x4xcomplex<f32>> loc(#loc5)
    %24 = stablehlo.broadcast_in_dim %21, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %25 = stablehlo.select %24, %6#6, %23 : tensor<4x4xi1>, tensor<4x4xcomplex<f32>> loc(#loc5)
    return %15, %20, %25 : tensor<4xcomplex<f32>>, tensor<4x4xcomplex<f32>>, tensor<4x4xcomplex<f32>> loc(#loc)
  } loc(#loc)
} loc(#loc)
#loc = loc(unknown)
#loc1 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":496:0)
#loc2 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":497:0)
#loc3 = loc("jit(func)/jit(main)/iota[dtype=float32 shape=(16,) dimension=0]"(#loc1))
#loc4 = loc("jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]"(#loc1))
#loc5 = loc("jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]"(#loc2))
""",
    mlir_module_serialized=b"ML\xefR\x01StableHLO_v0.9.0\x00\x01%\x05\x01\x03\x01\x03\x05\x03\x15\x07\t\x0b\r\x0f\x11\x13\x15\x17\x19\x03\xe7\x9b9\x01[\x0f\x13\x0b\x07\x0b\x13\x0f\x0b\x17\x0b\x13\x13#\x0b\x0b\x0b3\x0b\x0b\x0b\x0b\x13\x0b\x0f\x0b\x0f\x0b\x13\x0b\x17\x13K\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x13\x1b\x0b\x0b\x13\x03AO\x0f\x0b\x0b/\x0b\x17\x13\x0b\x13\x0b\x13\x0b\x0b\x0b\x0f\x1f\x1f\x13\x0b\x0b\x0b\x0b\x1f+\x1f\x0f\x0b\x0b//O\x01\x03\x0f\x037\x17\x0f\x07\x13\x07\x07\x17\x0f\x0b\x0f\x07\x13\x17\x17\x1b\x13\x07\x07\x13\x13\x13\x13\x0f\x13\x13\x13\x13\x02v\x06\x1d9;\x03\x03\t\x8f\x05\x1b\x1f\x05\x1d\x03\x03\x05\x95\x11\x01\x05\x05\x1f\x17\x13\xc2\x07\x01\x05!\x03\x03\x05\x7f\x03\x03\t\x99\x03\x07\x1b\r\x1d\r\x0f\x1f\x05#\x05%\x05'\x03\x0b#_%e'g\x0fu)w\x05)\x05+\x05-\x05/\x03\x03-y\x051\x1d1\x11\x053\x1d5\x11\x055\x03\x03\x05{\x057\x17\x13\xc6\x07\x01\x03\x03\x05}\x03\x11A\x81C\x83E\x85G_I\x87K\x89M_O\x8b\x059\x05;\x05=\x05?\x05A\x05C\x05E\x05G\x03\x03\x05\x8d\x03\x05U\x91W\x93\x05I\x05K\x03\x03\t\x97\x1f)!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x1f'\x01\x03\x01\x1dM\x1f+\x11\x00\x00\x00\x00\x00\x00\x00\x00#\x1f\x03\x07imq\r\x03ak\x1dO\r\x03ao\x1dQ\r\x03as\x1dS\x1dU\x1dW\x13\r\x01\x1f\x05\t\x01\x00\x00\x00\x1f\x05\t\x04\x00\x00\x00\x1f\x15\x03V\x0b\x05\x1dY\x1d[\x05\x01\x03\x0b]]]][\x03\x11[[[cc[[]\x1f\x05\t\x00\x00\x00\x00\x1f-\x01\t\x07\x07\x01\x1f\x11\x11\x00\x00\xc0\x7f\x00\x00\xc0\x7f\x1f5\x11\x00\x00\x00\x00\x00\x00\x00\x00\x1f7!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x02\x02)\x05\x11\x11\x13)\x01#\x01)\x03\x11\x13\t\x1d)\x05\x11\x11\x0b)\x01\x13\x03\x0b)\x01%\x13)\x03\x11\x0b)\x05\x05\x05\x07)\x05\x11\x11\x07\x11\x01\x07\t\x03\x03)\x03A\x0b\x1b!)\x03\x01\x17)\x03\t\x17)\x03\x05\x17)\x03\x01\r)\x01\x07)\x03\x05\x07)\x03\x11\x07)\x03\x05\r)\x03\t\r\x04\x92\x03\x05\x01\x11\x07\x19\x07\x03\x01\x05\t\x11\x07!\x05\x03Cm\x0b\x03/+\x03!\r\x063\x03\x0f\x03\x01\x05\x03\x017\x03\x05\x05\x03\x01=\x03\x05\x05\x03\x01\x15\x03\x15\x05\x03\x01\x15\x03\x15\x0f\x07\x01?\x11\x0f\x0f\x0f\x19\x19\x03\x03\x05\x0b\x05\x07\t\x0b\x03\x11\x06\x01\x03\t\x05\x13\x15\x05\x03\x01Q\x03\x05\x03\x07\x01\x03\x03\x05\x03\x1f\x13\x07\x01S\x03/\x05\x1b!\x03\x07\x01\x03\x031\x03#\x05\x03\x01\x0b\x03\x11\x03\x07\x01\x03\x03\t\x03'\x03\x07\x01Y\x033\x03%\x07\x06\x01\x03\t\x07+\x1d)\x03\x07\x01\x03\x03\x1b\x03#\x05\x03\x01\x0b\x03\x11\x03\x07\x01\x03\x03\x03\x031\x03\x07\x01\x17\x03\x1d\x03/\x07\x06\x01\x03\x03\x075\x173\x03\x07\x01\x03\x03\x1b\x03#\x05\x03\x01\x0b\x03\x11\x03\x07\x01\x03\x03\x03\x03;\x03\x07\x01\x17\x03\x1d\x039\x07\x06\x01\x03\x03\x07?\x19=\x15\x04\x07\x07-7A\x06\x03\x01\x05\x01\x00&\r]\x1b\x03\x0f\x0b\t\t\t!+\x1b\x1f/!!)#\x1f\x19\xb1}\x81\x1f\x1f\x15\x1d\x15\x13%)\x97\x13+\r\x15\x17\x17\x1f\x17\x11\x11\x15\x19)\x0f\x0b\x11builtin\x00vhlo\x00module\x00broadcast_in_dim_v1\x00constant_v1\x00select_v1\x00func_v1\x00iota_v1\x00reshape_v1\x00custom_call_v1\x00complex_v1\x00compare_v1\x00return_v1\x00value\x00broadcast_dimensions\x00sym_name\x00/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py\x00mhlo.num_partitions\x00mhlo.num_replicas\x00jit_func\x00arg_attrs\x00function_type\x00res_attrs\x00sym_visibility\x00iota_dimension\x00jit(func)/jit(main)/iota[dtype=float32 shape=(16,) dimension=0]\x00jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]\x00jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]\x00api_version\x00backend_config\x00call_target_name\x00called_computations\x00has_side_effect\x00operand_layouts\x00output_operand_aliases\x00result_layouts\x00compare_type\x00comparison_direction\x00jax.result_info\x00[0]\x00[1]\x00[2]\x00main\x00public\x00\x00lapack_sgeev\x00",
    xla_call_module_version=6,
)  # End paste


# Pasted from the test output (see back_compat_test.py module docstring)
data_2023_06_19["f64"] = dict(
    testdata_version=1,
    platform='cpu',
    custom_call_targets=['lapack_dgeev'],
    serialized_date=datetime.date(2023, 6, 19),
    inputs=(),
    expected_outputs=(array([ 3.2464249196572972e+01+0.j, -2.4642491965729802e+00+0.j,
       -1.5210037805054253e-15+0.j,  1.2568096307462507e-16+0.j]), array([[-0.4037774907686232  +0.j,  0.8288327563197505  +0.j,
         0.5454962288885842  +0.j, -0.2420483778598153  +0.j],
       [-0.46480737115848986 +0.j,  0.43714638836388725 +0.j,
        -0.7640998541831632  +0.j, -0.04349021275982002 +0.j],
       [-0.5258372515483576  +0.j,  0.045460020408024715+0.j,
        -0.10828897829942748 +0.j,  0.8131255590990858  +0.j],
       [-0.5868671319382249  +0.j, -0.3462263475478384  +0.j,
         0.32689260359400607 +0.j, -0.5275869684794504  +0.j]]), array([[-0.11417645138733863+0.j,  0.7327780959803554 +0.j,
         0.49133754464261303+0.j, -0.04933420991901029+0.j],
       [-0.33000459866554765+0.j,  0.28974835239692637+0.j,
        -0.8355289351028521 +0.j, -0.3408099365295394 +0.j],
       [-0.545832745943757  +0.j, -0.1532813911865017 +0.j,
         0.1970452362778633 +0.j,  0.8296225028161098 +0.j],
       [-0.7616608932219663 +0.j, -0.5963111347699308 +0.j,
         0.14714615418237506+0.j, -0.43947835636755994+0.j]])),
    mlir_module_text=r"""
module @jit_func attributes {mhlo.num_partitions = 1 : i32, mhlo.num_replicas = 1 : i32} {
  func.func public @main() -> (tensor<4xcomplex<f64>> {jax.result_info = "[0]"}, tensor<4x4xcomplex<f64>> {jax.result_info = "[1]"}, tensor<4x4xcomplex<f64>> {jax.result_info = "[2]"}) {
    %0 = stablehlo.iota dim = 0 : tensor<16xf64> loc(#loc3)
    %1 = stablehlo.reshape %0 : (tensor<16xf64>) -> tensor<4x4xf64> loc(#loc4)
    %2 = stablehlo.constant dense<1> : tensor<i32> loc(#loc5)
    %3 = stablehlo.constant dense<4> : tensor<i32> loc(#loc5)
    %4 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %5 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %6:8 = stablehlo.custom_call @lapack_dgeev(%2, %3, %4, %5, %1) {api_version = 2 : i32, operand_layouts = [dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<[0, 1]> : tensor<2xindex>], result_layouts = [dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<0> : tensor<1xindex>, dense<0> : tensor<1xindex>, dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<> : tensor<0xindex>]} : (tensor<i32>, tensor<i32>, tensor<ui8>, tensor<ui8>, tensor<4x4xf64>) -> (tensor<4x4xf64>, tensor<4x4xf64>, tensor<4x4xf64>, tensor<4xf64>, tensor<4xf64>, tensor<4x4xcomplex<f64>>, tensor<4x4xcomplex<f64>>, tensor<i32>) loc(#loc5)
    %7 = stablehlo.complex %6#3, %6#4 : tensor<4xcomplex<f64>> loc(#loc5)
    %8 = stablehlo.constant dense<0> : tensor<i32> loc(#loc5)
    %9 = stablehlo.broadcast_in_dim %8, dims = [] : (tensor<i32>) -> tensor<i32> loc(#loc5)
    %10 = stablehlo.compare  EQ, %6#7, %9,  SIGNED : (tensor<i32>, tensor<i32>) -> tensor<i1> loc(#loc5)
    %11 = stablehlo.broadcast_in_dim %10, dims = [] : (tensor<i1>) -> tensor<1xi1> loc(#loc5)
    %12 = stablehlo.constant dense<(0x7FF8000000000000,0x7FF8000000000000)> : tensor<complex<f64>> loc(#loc5)
    %13 = stablehlo.broadcast_in_dim %12, dims = [] : (tensor<complex<f64>>) -> tensor<4xcomplex<f64>> loc(#loc5)
    %14 = stablehlo.broadcast_in_dim %11, dims = [0] : (tensor<1xi1>) -> tensor<4xi1> loc(#loc5)
    %15 = stablehlo.select %14, %7, %13 : tensor<4xi1>, tensor<4xcomplex<f64>> loc(#loc5)
    %16 = stablehlo.broadcast_in_dim %10, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %17 = stablehlo.constant dense<(0x7FF8000000000000,0x7FF8000000000000)> : tensor<complex<f64>> loc(#loc5)
    %18 = stablehlo.broadcast_in_dim %17, dims = [] : (tensor<complex<f64>>) -> tensor<4x4xcomplex<f64>> loc(#loc5)
    %19 = stablehlo.broadcast_in_dim %16, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %20 = stablehlo.select %19, %6#5, %18 : tensor<4x4xi1>, tensor<4x4xcomplex<f64>> loc(#loc5)
    %21 = stablehlo.broadcast_in_dim %10, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %22 = stablehlo.constant dense<(0x7FF8000000000000,0x7FF8000000000000)> : tensor<complex<f64>> loc(#loc5)
    %23 = stablehlo.broadcast_in_dim %22, dims = [] : (tensor<complex<f64>>) -> tensor<4x4xcomplex<f64>> loc(#loc5)
    %24 = stablehlo.broadcast_in_dim %21, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %25 = stablehlo.select %24, %6#6, %23 : tensor<4x4xi1>, tensor<4x4xcomplex<f64>> loc(#loc5)
    return %15, %20, %25 : tensor<4xcomplex<f64>>, tensor<4x4xcomplex<f64>>, tensor<4x4xcomplex<f64>> loc(#loc)
  } loc(#loc)
} loc(#loc)
#loc = loc(unknown)
#loc1 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":496:0)
#loc2 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":497:0)
#loc3 = loc("jit(func)/jit(main)/iota[dtype=float64 shape=(16,) dimension=0]"(#loc1))
#loc4 = loc("jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]"(#loc1))
#loc5 = loc("jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]"(#loc2))
""",
    mlir_module_serialized=b"ML\xefR\x01StableHLO_v0.9.0\x00\x01%\x05\x01\x03\x01\x03\x05\x03\x15\x07\t\x0b\r\x0f\x11\x13\x15\x17\x19\x03\xe7\x9b9\x01[\x0f\x13\x0b\x07\x0b\x13\x0f\x0b\x17\x0b\x13\x13#\x0b\x0b\x0b3\x0b\x0b\x0b\x0b\x13\x0b\x0f\x0b\x0f\x0b\x13\x0b\x17\x13K\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x13\x1b\x0b\x0b\x13\x03AO\x0f\x0b\x0b/\x0b\x17\x13\x0b\x13\x0b\x13\x0b\x0b\x0b\x0f\x1f\x1f\x13\x0b\x0b\x0b\x0b\x1f+\x1f\x0f\x0b\x0bO/O\x01\x03\x0f\x037\x17\x0f\x07\x13\x07\x07\x17\x0f\x0b\x0f\x07\x13\x17\x17\x1b\x13\x07\x07\x13\x13\x13\x13\x0f\x13\x13\x13\x13\x02\x96\x06\x1d9;\x03\x03\t\x8f\x05\x1b\x1f\x05\x1d\x03\x03\x05\x95\x11\x01\x05\x05\x1f\x17\x13\xc2\x07\x01\x05!\x03\x03\x05\x7f\x03\x03\t\x99\x03\x07\x1b\r\x1d\r\x0f\x1f\x05#\x05%\x05'\x03\x0b#_%e'g\x0fu)w\x05)\x05+\x05-\x05/\x03\x03-y\x051\x1d1\x11\x053\x1d5\x11\x055\x03\x03\x05{\x057\x17\x13\xc6\x07\x01\x03\x03\x05}\x03\x11A\x81C\x83E\x85G_I\x87K\x89M_O\x8b\x059\x05;\x05=\x05?\x05A\x05C\x05E\x05G\x03\x03\x05\x8d\x03\x05U\x91W\x93\x05I\x05K\x03\x03\t\x97\x1f)!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x1f'\x01\x03\x01\x1dM\x1f+\x11\x00\x00\x00\x00\x00\x00\x00\x00#\x1f\x03\x07imq\r\x03ak\x1dO\r\x03ao\x1dQ\r\x03as\x1dS\x1dU\x1dW\x13\r\x01\x1f\x05\t\x01\x00\x00\x00\x1f\x05\t\x04\x00\x00\x00\x1f\x15\x03V\x0b\x05\x1dY\x1d[\x05\x01\x03\x0b]]]][\x03\x11[[[cc[[]\x1f\x05\t\x00\x00\x00\x00\x1f-\x01\t\x07\x07\x01\x1f\x11!\x00\x00\x00\x00\x00\x00\xf8\x7f\x00\x00\x00\x00\x00\x00\xf8\x7f\x1f5\x11\x00\x00\x00\x00\x00\x00\x00\x00\x1f7!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x02\x02)\x05\x11\x11\x13)\x01#\x01)\x03\x11\x13\x0b\x1d)\x05\x11\x11\x0b)\x01\x13\x03\x0b)\x01%\x13)\x03\x11\x0b)\x05\x05\x05\x07)\x05\x11\x11\x07\x11\x01\x07\t\x03\x03)\x03A\x0b\x1b!)\x03\x01\x17)\x03\t\x17)\x03\x05\x17)\x03\x01\r)\x01\x07)\x03\x05\x07)\x03\x11\x07)\x03\x05\r)\x03\t\r\x04\x92\x03\x05\x01\x11\x07\x19\x07\x03\x01\x05\t\x11\x07!\x05\x03Cm\x0b\x03/+\x03!\r\x063\x03\x0f\x03\x01\x05\x03\x017\x03\x05\x05\x03\x01=\x03\x05\x05\x03\x01\x15\x03\x15\x05\x03\x01\x15\x03\x15\x0f\x07\x01?\x11\x0f\x0f\x0f\x19\x19\x03\x03\x05\x0b\x05\x07\t\x0b\x03\x11\x06\x01\x03\t\x05\x13\x15\x05\x03\x01Q\x03\x05\x03\x07\x01\x03\x03\x05\x03\x1f\x13\x07\x01S\x03/\x05\x1b!\x03\x07\x01\x03\x031\x03#\x05\x03\x01\x0b\x03\x11\x03\x07\x01\x03\x03\t\x03'\x03\x07\x01Y\x033\x03%\x07\x06\x01\x03\t\x07+\x1d)\x03\x07\x01\x03\x03\x1b\x03#\x05\x03\x01\x0b\x03\x11\x03\x07\x01\x03\x03\x03\x031\x03\x07\x01\x17\x03\x1d\x03/\x07\x06\x01\x03\x03\x075\x173\x03\x07\x01\x03\x03\x1b\x03#\x05\x03\x01\x0b\x03\x11\x03\x07\x01\x03\x03\x03\x03;\x03\x07\x01\x17\x03\x1d\x039\x07\x06\x01\x03\x03\x07?\x19=\x15\x04\x07\x07-7A\x06\x03\x01\x05\x01\x00&\r]\x1b\x03\x0f\x0b\t\t\t!+\x1b\x1f/!!)#\x1f\x19\xb1}\x81\x1f\x1f\x15\x1d\x15\x13%)\x97\x13+\r\x15\x17\x17\x1f\x17\x11\x11\x15\x19)\x0f\x0b\x11builtin\x00vhlo\x00module\x00broadcast_in_dim_v1\x00constant_v1\x00select_v1\x00func_v1\x00iota_v1\x00reshape_v1\x00custom_call_v1\x00complex_v1\x00compare_v1\x00return_v1\x00value\x00broadcast_dimensions\x00sym_name\x00/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py\x00mhlo.num_partitions\x00mhlo.num_replicas\x00jit_func\x00arg_attrs\x00function_type\x00res_attrs\x00sym_visibility\x00iota_dimension\x00jit(func)/jit(main)/iota[dtype=float64 shape=(16,) dimension=0]\x00jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]\x00jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]\x00api_version\x00backend_config\x00call_target_name\x00called_computations\x00has_side_effect\x00operand_layouts\x00output_operand_aliases\x00result_layouts\x00compare_type\x00comparison_direction\x00jax.result_info\x00[0]\x00[1]\x00[2]\x00main\x00public\x00\x00lapack_dgeev\x00",
    xla_call_module_version=6,
)  # End paste


# Pasted from the test output (see back_compat_test.py module docstring)
data_2023_06_19["c64"] = dict(
    testdata_version=1,
    platform='cpu',
    custom_call_targets=['lapack_cgeev'],
    serialized_date=datetime.date(2023, 6, 19),
    inputs=(),
    expected_outputs=(array([ 3.2464237e+01+0.j, -2.4642489e+00+0.j, -5.7737714e-07+0.j,
        1.4719126e-07+0.j], dtype=complex64), array([[ 0.4037776  +0.j,  0.8288327  +0.j, -0.53126234 -0.j,
         0.052026853-0.j],
       [ 0.46480742 +0.j,  0.43714646 -0.j,  0.80768156 +0.j,
        -0.47577178 -0.j],
       [ 0.52583724 +0.j,  0.045459922-0.j, -0.021575088-0.j,
         0.79546237 +0.j],
       [ 0.5868671  +0.j, -0.3462263  -0.j, -0.25484383 -0.j,
        -0.3717177  -0.j]], dtype=complex64), array([[ 0.114176475+0.j,  0.7327782  +0.j, -0.5452461  -0.j,
        -0.13326685 -0.j],
       [ 0.3300045  +0.j,  0.28974816 -0.j,  0.68821603 +0.j,
        -0.2182906  -0.j],
       [ 0.5458328  +0.j, -0.1532814  -0.j,  0.25930583 -0.j,
         0.8363818  +0.j],
       [ 0.76166093 +0.j, -0.5963111  -0.j, -0.40227592 -0.j,
        -0.4848244  -0.j]], dtype=complex64)),
    mlir_module_text=r"""
module @jit_func attributes {mhlo.num_partitions = 1 : i32, mhlo.num_replicas = 1 : i32} {
  func.func public @main() -> (tensor<4xcomplex<f32>> {jax.result_info = "[0]"}, tensor<4x4xcomplex<f32>> {jax.result_info = "[1]"}, tensor<4x4xcomplex<f32>> {jax.result_info = "[2]"}) {
    %0 = stablehlo.iota dim = 0 : tensor<16xcomplex<f32>> loc(#loc3)
    %1 = stablehlo.reshape %0 : (tensor<16xcomplex<f32>>) -> tensor<4x4xcomplex<f32>> loc(#loc4)
    %2 = stablehlo.constant dense<1> : tensor<i32> loc(#loc5)
    %3 = stablehlo.constant dense<4> : tensor<i32> loc(#loc5)
    %4 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %5 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %6:6 = stablehlo.custom_call @lapack_cgeev(%2, %3, %4, %5, %1) {api_version = 2 : i32, operand_layouts = [dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<[0, 1]> : tensor<2xindex>], result_layouts = [dense<[0, 1]> : tensor<2xindex>, dense<0> : tensor<1xindex>, dense<0> : tensor<1xindex>, dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<> : tensor<0xindex>]} : (tensor<i32>, tensor<i32>, tensor<ui8>, tensor<ui8>, tensor<4x4xcomplex<f32>>) -> (tensor<4x4xcomplex<f32>>, tensor<8xf32>, tensor<4xcomplex<f32>>, tensor<4x4xcomplex<f32>>, tensor<4x4xcomplex<f32>>, tensor<i32>) loc(#loc5)
    %7 = stablehlo.constant dense<0> : tensor<i32> loc(#loc5)
    %8 = stablehlo.broadcast_in_dim %7, dims = [] : (tensor<i32>) -> tensor<i32> loc(#loc5)
    %9 = stablehlo.compare  EQ, %6#5, %8,  SIGNED : (tensor<i32>, tensor<i32>) -> tensor<i1> loc(#loc5)
    %10 = stablehlo.broadcast_in_dim %9, dims = [] : (tensor<i1>) -> tensor<1xi1> loc(#loc5)
    %11 = stablehlo.constant dense<(0x7FC00000,0x7FC00000)> : tensor<complex<f32>> loc(#loc5)
    %12 = stablehlo.broadcast_in_dim %11, dims = [] : (tensor<complex<f32>>) -> tensor<4xcomplex<f32>> loc(#loc5)
    %13 = stablehlo.broadcast_in_dim %10, dims = [0] : (tensor<1xi1>) -> tensor<4xi1> loc(#loc5)
    %14 = stablehlo.select %13, %6#2, %12 : tensor<4xi1>, tensor<4xcomplex<f32>> loc(#loc5)
    %15 = stablehlo.broadcast_in_dim %9, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %16 = stablehlo.constant dense<(0x7FC00000,0x7FC00000)> : tensor<complex<f32>> loc(#loc5)
    %17 = stablehlo.broadcast_in_dim %16, dims = [] : (tensor<complex<f32>>) -> tensor<4x4xcomplex<f32>> loc(#loc5)
    %18 = stablehlo.broadcast_in_dim %15, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %19 = stablehlo.select %18, %6#3, %17 : tensor<4x4xi1>, tensor<4x4xcomplex<f32>> loc(#loc5)
    %20 = stablehlo.broadcast_in_dim %9, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %21 = stablehlo.constant dense<(0x7FC00000,0x7FC00000)> : tensor<complex<f32>> loc(#loc5)
    %22 = stablehlo.broadcast_in_dim %21, dims = [] : (tensor<complex<f32>>) -> tensor<4x4xcomplex<f32>> loc(#loc5)
    %23 = stablehlo.broadcast_in_dim %20, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %24 = stablehlo.select %23, %6#4, %22 : tensor<4x4xi1>, tensor<4x4xcomplex<f32>> loc(#loc5)
    return %14, %19, %24 : tensor<4xcomplex<f32>>, tensor<4x4xcomplex<f32>>, tensor<4x4xcomplex<f32>> loc(#loc)
  } loc(#loc)
} loc(#loc)
#loc = loc(unknown)
#loc1 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":496:0)
#loc2 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":497:0)
#loc3 = loc("jit(func)/jit(main)/iota[dtype=complex64 shape=(16,) dimension=0]"(#loc1))
#loc4 = loc("jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]"(#loc1))
#loc5 = loc("jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]"(#loc2))
""",
    mlir_module_serialized=b"ML\xefR\x01StableHLO_v0.9.0\x00\x01#\x05\x01\x03\x01\x03\x05\x03\x13\x07\t\x0b\r\x0f\x11\x13\x15\x17\x03\xe5\x9b7\x01[\x0f\x13\x0b\x07\x0b\x13\x0f\x0b\x17\x0b\x13\x13#\x0b\x0b\x0b3\x0b\x0b\x0b\x0b\x13\x0b\x0f\x0b\x0f\x0b\x13\x0b\x17\x13K\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x13\x1b\x0b\x0b\x13\x03A\x0fO\x0b\x0b/\x0b\x17\x13\x0b\x13\x0b\x13\x0b\x0b\x0b\x0f\x1f\x1f\x13\x0b\x0b\x0b\x0b\x1f#\x1f\x0f\x0b\x0b//O\x01\x03\x0f\x035\x17\x0f\x07\x13\x0b\x07\x0f\x0f\x07\x07\x17\x17\x1b\x13\x07\x07\x13\x13\x13\x13\x13\x0f\x13\x13\x13\x13\x02Z\x06\x1d9;\x03\x03\t\x8f\x05\x19\x1f\x05\x1b\x03\x03\x05\x95\x11\x01\x05\x05\x1d\x17\x13\xc2\x07\x01\x05\x1f\x03\x03\x05\x7f\x03\x03\t\x99\x03\x07\x1b\r\x1d\r\x0f\x1f\x05!\x05#\x05%\x03\x0b#_%e'g\x0fu)w\x05'\x05)\x05+\x05-\x03\x03-y\x05/\x1d1\x11\x051\x1d5\x11\x053\x03\x03\x05{\x055\x17\x13\xc6\x07\x01\x03\x03\x05}\x03\x11A\x81C\x83E\x85G_I\x87K\x89M_O\x8b\x057\x059\x05;\x05=\x05?\x05A\x05C\x05E\x03\x03\x05\x8d\x03\x05U\x91W\x93\x05G\x05I\x03\x03\t\x97\x1f%\x01\x1f'!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x01\x1dK\x1f)\x11\x00\x00\x00\x00\x00\x00\x00\x00#\x1b\x03\x07imq\r\x03ak\x1dM\r\x03ao\x1dO\r\x03as\x1dQ\x1dS\x1dU\x13\r\x01\x1f\x05\t\x01\x00\x00\x00\x1f\x05\t\x04\x00\x00\x00\x1f\x11\x03V\x0b\x05\x1dW\x1dY\x05\x01\x03\x0b[[[[]\x03\r]cc]][\x1f\x05\t\x00\x00\x00\x00\x1f+\x01\t\x07\x07\x01\x1f\x0f\x11\x00\x00\xc0\x7f\x00\x00\xc0\x7f\x1f3\x11\x00\x00\x00\x00\x00\x00\x00\x00\x1f5!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x02\x02)\x05\x11\x11\x0b)\x01\x1f\x01)\x03\x11\x0b\x03\x15\x1d)\x01\x0b)\x01!\x13\t)\x05\x05\x05\x07)\x05\x11\x11\x07\x11\x01\x07\t\x03\x03)\x03A\x0b\x1b!)\x03!\x15)\x03\x01\x13)\x03\t\x13)\x03\x05\x13)\x03\x01\r)\x01\x07)\x03\x05\x07)\x03\x11\x07)\x03\x05\r)\x03\t\r\x04j\x03\x05\x01\x11\x07\x19\x07\x03\x01\x05\t\x11\x07!\x05\x03=i\x0b\x03/+\x03\x1d\r\x063\x03\x03\x03\x01\x05\x03\x017\x03\x05\x05\x03\x01=\x03\x05\x05\x03\x01\x15\x03\x11\x05\x03\x01\x15\x03\x11\x0f\x07\x01?\r\x03#\t\x03\x03\x05\x0b\x05\x07\t\x0b\x03\x05\x03\x01Q\x03\x05\x03\x07\x01\x03\x03\x05\x03\x19\x11\x07\x01S\x03-\x05\x17\x1b\x03\x07\x01\x03\x03/\x03\x1d\x05\x03\x01\x0b\x03\x0f\x03\x07\x01\x03\x03\t\x03!\x03\x07\x01Y\x031\x03\x1f\x07\x06\x01\x03\t\x07%\x11#\x03\x07\x01\x03\x03\x17\x03\x1d\x05\x03\x01\x0b\x03\x0f\x03\x07\x01\x03\x03\x03\x03+\x03\x07\x01\x17\x03\x19\x03)\x07\x06\x01\x03\x03\x07/\x13-\x03\x07\x01\x03\x03\x17\x03\x1d\x05\x03\x01\x0b\x03\x0f\x03\x07\x01\x03\x03\x03\x035\x03\x07\x01\x17\x03\x19\x033\x07\x06\x01\x03\x03\x079\x157\x13\x04\x07\x07'1;\x06\x03\x01\x05\x01\x00\xfe\x0c[\x1b\x03\x0f\x0b\t\t\t!+\x1b\x1f/!!)#\x1f\x19\xb1}\x85\x1f\x1f\x15\x1d\x15\x13%)\x97\x13+\r\x15\x17\x1f\x17\x11\x11\x15\x19)\x0f\x0b\x11builtin\x00vhlo\x00module\x00broadcast_in_dim_v1\x00constant_v1\x00select_v1\x00func_v1\x00iota_v1\x00reshape_v1\x00custom_call_v1\x00compare_v1\x00return_v1\x00value\x00broadcast_dimensions\x00sym_name\x00/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py\x00mhlo.num_partitions\x00mhlo.num_replicas\x00jit_func\x00arg_attrs\x00function_type\x00res_attrs\x00sym_visibility\x00iota_dimension\x00jit(func)/jit(main)/iota[dtype=complex64 shape=(16,) dimension=0]\x00jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]\x00jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]\x00api_version\x00backend_config\x00call_target_name\x00called_computations\x00has_side_effect\x00operand_layouts\x00output_operand_aliases\x00result_layouts\x00compare_type\x00comparison_direction\x00jax.result_info\x00[0]\x00[1]\x00[2]\x00main\x00public\x00\x00lapack_cgeev\x00",
    xla_call_module_version=6,
)  # End paste


# Pasted from the test output (see back_compat_test.py module docstring)
data_2023_06_19["c128"] = dict(
    testdata_version=1,
    platform='cpu',
    custom_call_targets=['lapack_zgeev'],
    serialized_date=datetime.date(2023, 6, 19),
    inputs=(),
    expected_outputs=(array([ 3.2464249196572965e+01+0.j, -2.4642491965729807e+00+0.j,
       -1.6035677295293283e-15+0.j,  1.2218554396786611e-16+0.j]), array([[ 0.40377749076862335 +0.j,  0.8288327563197505  +0.j,
        -0.5457111210844892  +0.j, -0.2322136424094458  -0.j],
       [ 0.46480737115848997 +0.j,  0.4371463883638875  -0.j,
         0.7625701354883243  +0.j, -0.06012408092789514 -0.j],
       [ 0.5258372515483578  +0.j,  0.045460020408024694-0.j,
         0.1119930922768192  +0.j,  0.8168890890841272  +0.j],
       [ 0.5868671319382247  +0.j, -0.34622634754783854 -0.j,
        -0.32885210668065423 +0.j, -0.5245513657467864  -0.j]]), array([[ 0.11417645138733871+0.j,  0.7327780959803554 +0.j,
        -0.49606131100796214+0.j, -0.04689746607984153-0.j],
       [ 0.3300045986655476 +0.j,  0.2897483523969264 -0.j,
         0.8344969112540657 +0.j, -0.34421909950105706-0.j],
       [ 0.5458327459437571 +0.j, -0.15328139118650172-0.j,
        -0.18080988948424467+0.j,  0.8291305972416383 +0.j],
       [ 0.7616608932219663 +0.j, -0.5963111347699308 -0.j,
        -0.1576257107618584 +0.j, -0.4380140316607401 -0.j]])),
    mlir_module_text=r"""
module @jit_func attributes {mhlo.num_partitions = 1 : i32, mhlo.num_replicas = 1 : i32} {
  func.func public @main() -> (tensor<4xcomplex<f64>> {jax.result_info = "[0]"}, tensor<4x4xcomplex<f64>> {jax.result_info = "[1]"}, tensor<4x4xcomplex<f64>> {jax.result_info = "[2]"}) {
    %0 = stablehlo.iota dim = 0 : tensor<16xcomplex<f64>> loc(#loc3)
    %1 = stablehlo.reshape %0 : (tensor<16xcomplex<f64>>) -> tensor<4x4xcomplex<f64>> loc(#loc4)
    %2 = stablehlo.constant dense<1> : tensor<i32> loc(#loc5)
    %3 = stablehlo.constant dense<4> : tensor<i32> loc(#loc5)
    %4 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %5 = stablehlo.constant dense<86> : tensor<ui8> loc(#loc5)
    %6:6 = stablehlo.custom_call @lapack_zgeev(%2, %3, %4, %5, %1) {api_version = 2 : i32, operand_layouts = [dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<> : tensor<0xindex>, dense<[0, 1]> : tensor<2xindex>], result_layouts = [dense<[0, 1]> : tensor<2xindex>, dense<0> : tensor<1xindex>, dense<0> : tensor<1xindex>, dense<[0, 1]> : tensor<2xindex>, dense<[0, 1]> : tensor<2xindex>, dense<> : tensor<0xindex>]} : (tensor<i32>, tensor<i32>, tensor<ui8>, tensor<ui8>, tensor<4x4xcomplex<f64>>) -> (tensor<4x4xcomplex<f64>>, tensor<8xf64>, tensor<4xcomplex<f64>>, tensor<4x4xcomplex<f64>>, tensor<4x4xcomplex<f64>>, tensor<i32>) loc(#loc5)
    %7 = stablehlo.constant dense<0> : tensor<i32> loc(#loc5)
    %8 = stablehlo.broadcast_in_dim %7, dims = [] : (tensor<i32>) -> tensor<i32> loc(#loc5)
    %9 = stablehlo.compare  EQ, %6#5, %8,  SIGNED : (tensor<i32>, tensor<i32>) -> tensor<i1> loc(#loc5)
    %10 = stablehlo.broadcast_in_dim %9, dims = [] : (tensor<i1>) -> tensor<1xi1> loc(#loc5)
    %11 = stablehlo.constant dense<(0x7FF8000000000000,0x7FF8000000000000)> : tensor<complex<f64>> loc(#loc5)
    %12 = stablehlo.broadcast_in_dim %11, dims = [] : (tensor<complex<f64>>) -> tensor<4xcomplex<f64>> loc(#loc5)
    %13 = stablehlo.broadcast_in_dim %10, dims = [0] : (tensor<1xi1>) -> tensor<4xi1> loc(#loc5)
    %14 = stablehlo.select %13, %6#2, %12 : tensor<4xi1>, tensor<4xcomplex<f64>> loc(#loc5)
    %15 = stablehlo.broadcast_in_dim %9, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %16 = stablehlo.constant dense<(0x7FF8000000000000,0x7FF8000000000000)> : tensor<complex<f64>> loc(#loc5)
    %17 = stablehlo.broadcast_in_dim %16, dims = [] : (tensor<complex<f64>>) -> tensor<4x4xcomplex<f64>> loc(#loc5)
    %18 = stablehlo.broadcast_in_dim %15, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %19 = stablehlo.select %18, %6#3, %17 : tensor<4x4xi1>, tensor<4x4xcomplex<f64>> loc(#loc5)
    %20 = stablehlo.broadcast_in_dim %9, dims = [] : (tensor<i1>) -> tensor<1x1xi1> loc(#loc5)
    %21 = stablehlo.constant dense<(0x7FF8000000000000,0x7FF8000000000000)> : tensor<complex<f64>> loc(#loc5)
    %22 = stablehlo.broadcast_in_dim %21, dims = [] : (tensor<complex<f64>>) -> tensor<4x4xcomplex<f64>> loc(#loc5)
    %23 = stablehlo.broadcast_in_dim %20, dims = [0, 1] : (tensor<1x1xi1>) -> tensor<4x4xi1> loc(#loc5)
    %24 = stablehlo.select %23, %6#4, %22 : tensor<4x4xi1>, tensor<4x4xcomplex<f64>> loc(#loc5)
    return %14, %19, %24 : tensor<4xcomplex<f64>>, tensor<4x4xcomplex<f64>>, tensor<4x4xcomplex<f64>> loc(#loc)
  } loc(#loc)
} loc(#loc)
#loc = loc(unknown)
#loc1 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":496:0)
#loc2 = loc("/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py":497:0)
#loc3 = loc("jit(func)/jit(main)/iota[dtype=complex128 shape=(16,) dimension=0]"(#loc1))
#loc4 = loc("jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]"(#loc1))
#loc5 = loc("jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]"(#loc2))
""",
    mlir_module_serialized=b"ML\xefR\x01StableHLO_v0.9.0\x00\x01#\x05\x01\x03\x01\x03\x05\x03\x13\x07\t\x0b\r\x0f\x11\x13\x15\x17\x03\xe5\x9b7\x01[\x0f\x13\x0b\x07\x0b\x13\x0f\x0b\x17\x0b\x13\x13#\x0b\x0b\x0b3\x0b\x0b\x0b\x0b\x13\x0b\x0f\x0b\x0f\x0b\x13\x0b\x17\x13K\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x13\x1b\x0b\x0b\x13\x03A\x0fO\x0b\x0b/\x0b\x17\x13\x0b\x13\x0b\x13\x0b\x0b\x0b\x0f\x1f\x1f\x13\x0b\x0b\x0b\x0b\x1f#\x1f\x0f\x0b\x0bO/O\x01\x03\x0f\x035\x17\x0f\x07\x13\x0b\x07\x0f\x0f\x07\x07\x17\x17\x1b\x13\x07\x07\x13\x13\x13\x13\x13\x0f\x13\x13\x13\x13\x02z\x06\x1d9;\x03\x03\t\x8f\x05\x19\x1f\x05\x1b\x03\x03\x05\x95\x11\x01\x05\x05\x1d\x17\x13\xc2\x07\x01\x05\x1f\x03\x03\x05\x7f\x03\x03\t\x99\x03\x07\x1b\r\x1d\r\x0f\x1f\x05!\x05#\x05%\x03\x0b#_%e'g\x0fu)w\x05'\x05)\x05+\x05-\x03\x03-y\x05/\x1d1\x11\x051\x1d5\x11\x053\x03\x03\x05{\x055\x17\x13\xc6\x07\x01\x03\x03\x05}\x03\x11A\x81C\x83E\x85G_I\x87K\x89M_O\x8b\x057\x059\x05;\x05=\x05?\x05A\x05C\x05E\x03\x03\x05\x8d\x03\x05U\x91W\x93\x05G\x05I\x03\x03\t\x97\x1f%\x01\x1f'!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x01\x1dK\x1f)\x11\x00\x00\x00\x00\x00\x00\x00\x00#\x1b\x03\x07imq\r\x03ak\x1dM\r\x03ao\x1dO\r\x03as\x1dQ\x1dS\x1dU\x13\r\x01\x1f\x05\t\x01\x00\x00\x00\x1f\x05\t\x04\x00\x00\x00\x1f\x11\x03V\x0b\x05\x1dW\x1dY\x05\x01\x03\x0b[[[[]\x03\r]cc]][\x1f\x05\t\x00\x00\x00\x00\x1f+\x01\t\x07\x07\x01\x1f\x0f!\x00\x00\x00\x00\x00\x00\xf8\x7f\x00\x00\x00\x00\x00\x00\xf8\x7f\x1f3\x11\x00\x00\x00\x00\x00\x00\x00\x00\x1f5!\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x02\x02)\x05\x11\x11\x0b)\x01\x1f\x01)\x03\x11\x0b\x03\x15\x1d)\x01\x0b)\x01!\x13\x0b)\x05\x05\x05\x07)\x05\x11\x11\x07\x11\x01\x07\t\x03\x03)\x03A\x0b\x1b!)\x03!\x15)\x03\x01\x13)\x03\t\x13)\x03\x05\x13)\x03\x01\r)\x01\x07)\x03\x05\x07)\x03\x11\x07)\x03\x05\r)\x03\t\r\x04j\x03\x05\x01\x11\x07\x19\x07\x03\x01\x05\t\x11\x07!\x05\x03=i\x0b\x03/+\x03\x1d\r\x063\x03\x03\x03\x01\x05\x03\x017\x03\x05\x05\x03\x01=\x03\x05\x05\x03\x01\x15\x03\x11\x05\x03\x01\x15\x03\x11\x0f\x07\x01?\r\x03#\t\x03\x03\x05\x0b\x05\x07\t\x0b\x03\x05\x03\x01Q\x03\x05\x03\x07\x01\x03\x03\x05\x03\x19\x11\x07\x01S\x03-\x05\x17\x1b\x03\x07\x01\x03\x03/\x03\x1d\x05\x03\x01\x0b\x03\x0f\x03\x07\x01\x03\x03\t\x03!\x03\x07\x01Y\x031\x03\x1f\x07\x06\x01\x03\t\x07%\x11#\x03\x07\x01\x03\x03\x17\x03\x1d\x05\x03\x01\x0b\x03\x0f\x03\x07\x01\x03\x03\x03\x03+\x03\x07\x01\x17\x03\x19\x03)\x07\x06\x01\x03\x03\x07/\x13-\x03\x07\x01\x03\x03\x17\x03\x1d\x05\x03\x01\x0b\x03\x0f\x03\x07\x01\x03\x03\x03\x035\x03\x07\x01\x17\x03\x19\x033\x07\x06\x01\x03\x03\x079\x157\x13\x04\x07\x07'1;\x06\x03\x01\x05\x01\x00\x02\r[\x1b\x03\x0f\x0b\t\t\t!+\x1b\x1f/!!)#\x1f\x19\xb1}\x87\x1f\x1f\x15\x1d\x15\x13%)\x97\x13+\r\x15\x17\x1f\x17\x11\x11\x15\x19)\x0f\x0b\x11builtin\x00vhlo\x00module\x00broadcast_in_dim_v1\x00constant_v1\x00select_v1\x00func_v1\x00iota_v1\x00reshape_v1\x00custom_call_v1\x00compare_v1\x00return_v1\x00value\x00broadcast_dimensions\x00sym_name\x00/Users/necula/Source/jax/jax/experimental/jax2tf/tests/back_compat_test.py\x00mhlo.num_partitions\x00mhlo.num_replicas\x00jit_func\x00arg_attrs\x00function_type\x00res_attrs\x00sym_visibility\x00iota_dimension\x00jit(func)/jit(main)/iota[dtype=complex128 shape=(16,) dimension=0]\x00jit(func)/jit(main)/reshape[new_sizes=(4, 4) dimensions=None]\x00jit(func)/jit(main)/eig[compute_left_eigenvectors=True compute_right_eigenvectors=True]\x00api_version\x00backend_config\x00call_target_name\x00called_computations\x00has_side_effect\x00operand_layouts\x00output_operand_aliases\x00result_layouts\x00compare_type\x00comparison_direction\x00jax.result_info\x00[0]\x00[1]\x00[2]\x00main\x00public\x00\x00lapack_zgeev\x00",
    xla_call_module_version=6,
)  # End paste
