"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0xe000300, 0xd3022820L, 0x1d000940, 0x28104770, 0x900d302, 0x47701cc0, 0x47700880, 0x49414842, 
    0x49426041, 0x21006041, 0x68c16001, 0x431122f0, 0x694060c1, 0xd4060680L, 0x493d483e, 0x21066001, 
    0x493d6041, 0x20006081, 0x48374770, 0x5426901, 0x61014311, 0x47702000, 0x4833b510, 0x24046901, 
    0x61014321, 0x3a26901, 0x61014311, 0x4a314933, 0x6011e000, 0x3db68c3, 0x6901d4fb, 0x610143a1, 
    0xbd102000L, 0xf7ffb530L, 0x4927ffbb, 0x23f068ca, 0x60ca431a, 0x610c2402, 0x700690a, 0x43020e40, 
    0x6908610a, 0x431003e2, 0x48246108, 0xe0004a21L, 0x68cd6010, 0xd4fb03edL, 0x43a06908, 0x68c86108, 
    0xf000600, 0x68c8d003, 0x60c84318, 0xbd302001L, 0x4d15b570, 0x8891cc9, 0x8968eb, 0x433326f0, 
    0x230060eb, 0x4b16612b, 0x692ce017, 0x612c431c, 0x60046814, 0x3e468ec, 0x692cd4fc, 0x640864, 
    0x68ec612c, 0xf240624, 0x68e8d004, 0x60e84330, 0xbd702001L, 0x1d121d00, 0x29001f09, 0x2000d1e5, 
    0xbd70, 0x45670123, 0x40023c00, 0xcdef89abL, 0x5555, 0x40003000, 0xfff, 0xaaaa, 
    0x201, 0x0, 
                                ],
               'pc_init' : 0x2000003D,
               'pc_eraseAll' : 0x20000079,
               'pc_erase_sector' : 0x200000A5,
               'pc_program_page' : 0x200000F1,
               'begin_stack' : 0x20001000,
               'begin_data' : 0x20002000,
               'static_base' : 0x20000144,
               'page_size' : 1024
              };

class Flash_stm32f407(Flash):
    
    def __init__(self, target):
        super(Flash_stm32f407, self).__init__(target, flash_algo)
    
