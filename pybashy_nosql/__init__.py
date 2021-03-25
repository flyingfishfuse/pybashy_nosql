#blarp!
#From some person on stackoverflow
from collections import Counter
import linecache
import os
import tracemalloc


#TODO: Do something with this to get, set, the environment for pybashy to run properly
class CustomException(Exception):
    '''Base Class for Internal Exception Labeling'''

class CommandFormatException(CustomException):
    '''Failure in the text of a Command(command_input)
    An internal Error unless you are feeding JSON directly
    to:
        - Command.init_self(json_str : json)'''
    def __init__(self, derp:str, errors):
        ''' narf!'''

def display_top(snapshot, key_type='lineno', limit=3):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))


tracemalloc.start()

counts = Counter()
fname = '/usr/share/dict/american-english'
with open(fname) as words:
    words = list(words)
    for word in words:
        prefix = word[:3]
        counts[prefix] += 1
print('Top prefixes:', counts.most_common(3))

    
########################################################################
####                    TESTING EXEC POOL NOW                       ####
###             # NEVER FEAR, THE END IS FUCKING NEAR!#              ###
########################################################################
import pybashy_no_sqlalchemy
from pybashy_no_sqlalchemy import *
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
        exec_pool.exec_command(exec_pool.test1.ls_home.cmd_line)
        greenprint("=======================================")
        critical_message('[+] TEST FUNCTION : ls -la ./')
        #run the whole functionset()
        blueprint("exec_pool.run_function(exec_pool.test1)")
        greenprint("=======================================")
        exec_pool.run_function(exec_pool.test1)
except Exception:
    error_printer("WAAAAGHHH!\n\n")