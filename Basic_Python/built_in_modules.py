'''
* @Author: Uthsavi KP
* @Date: 2020-01-05 2:16:42 
* @Last Modified by:   Uthsavi KP
* @Last Modified time: 2020-01-05 2:43:07
* @Title : To Find Built-in Modules.
'''

import sys
import textwrap #This  wraps the input paragraph 
module_name = ', '.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width=70))
