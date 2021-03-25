########################################################################
####                    TESTING EXEC POOL NOW                       ####
###             # NEVER FEAR, THE END IS FUCKING NEAR!#              ###
########################################################################
import pybashy.pybashy_no_sqlalchemy
from pybashy.pybashy_no_sqlalchemy import *
cmdstrjson = {'ls_etc' : { "command": "ls -la /etc","info_message":"[+] Info Text","success_message" : "[+] Command Sucessful", "failure_message" : "[-] ls -la Failed! Check the logfile!"},'ls_home' : { "command" : "ls -la ~/","info_message" : "[+] Info Text","success_message" : "[+] Command Sucessful","failure_message" : "[-] ls -la Failed! Check the logfile!"}}
exec_pool          = ExecutionPool()
module_set         = ModuleSet('test1')
function_prototype = CommandSet()
new_function       = FunctionSet()
runner = CommandRunner(exec_pool = exec_pool)
#runner.get_stuff("test.py")
try:
    for command_name in cmdstrjson.keys():
        cmd_dict = cmdstrjson.get(command_name)
        critical_message('[+] Adding command_dict to FunctionSet()')
        new_function.add_command_dict(command_name,cmd_dict)

        critical_message('[+] Adding command_dict to ModuleSet()')
        module_set.add_command_dict(command_name, cmdstrjson.get(command_name))

        critical_message('[+] Adding FunctionSet() to ModuleSet()')
        module_set.add_function(new_function)

        critical_message('[+] Adding ModuleSet() to ExecutionPool()')
        setattr(exec_pool, module_set.__name__, module_set)
        greenprint("=======================================")
        critical_message('[+] TEST COMMAND : ls -la ./') 
        # feed it JUST the command str
        blueprint("exec_pool.exec_command(exec_pool.test1.ls_la.cmd_line)")
        greenprint("=======================================")
        exec_pool.exec_command(exec_pool.test.ls_la.cmd_line)
        greenprint("=======================================")
        critical_message('[+] TEST FUNCTION : ls -la ./')
        #run the whole functionset()
        blueprint("exec_pool.run_function(exec_pool.test1)")
        greenprint("=======================================")
        exec_pool.run_function(exec_pool.test1)
except Exception:
    error_printer("WAAAAGHHH!\n\n")