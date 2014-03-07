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

from flash_kl02z import Flash_kl02z
from flash_kl05z import Flash_kl05z
from flash_kl25z import Flash_kl25z
from flash_kl26z import Flash_kl26z
from flash_kl46z import Flash_kl46z
from flash_k20d50m import Flash_k20d50m
from flash_k64f import Flash_k64f
from flash_lpc800 import Flash_lpc800
from flash_lpc11u24 import Flash_lpc11u24
from flash_lpc1768 import Flash_lpc1768
from flash_stm32f407 import Flash_stm32f407
from flash_nrf51822 import Flash_nrf51822

FLASH = {
         'flash_kl02z': Flash_kl02z,
         'flash_kl05z': Flash_kl05z,
         'flash_kl25z': Flash_kl25z,
         'flash_kl26z': Flash_kl26z,
         'flash_kl46z': Flash_kl46z,
         'flash_k20d50m': Flash_k20d50m,
         'flash_k64f': Flash_k64f,
         'flash_lpc800': Flash_lpc800,
         'flash_lpc11u24': Flash_lpc11u24,
         'flash_lpc1768': Flash_lpc1768,
         'flash_stm32f407': Flash_stm32f407,
         'flash_nrf51822' : Flash_nrf51822,
         }
