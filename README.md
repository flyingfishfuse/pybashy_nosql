# pybashy
	framework for leveraging python to run sets of shell commands for specific tasks. 
	
	Monolithic file is the most complete, seems to have morphed into a json input and things have streamlined, my workflow is wonky

Right now, this is more of a spec for me to follow and will change until the first release

Only one set of commands can be at the top level of a file (now in JSON!)
  - Command Sets are stored as dicts in seperate files and loaded dynamically.
  - Multiple sets can be placed in thier own unique functions
  - functions MUST START with "function"
  - Classes not allowed as implied inheritance isnt working yet

you import modules with :

	new_command = CommandRunner()
	new_command.dynamic_import('commandtest')


All functions become thier own CommandSet()

	>>> isinstance(new_command, CommandSet())
	>>> True
		
  - from "steps" to "failure_message" is considered a CommandSet()
  - All "steps" are turned into Command() 's 
	
All `CommandSet()` are added to `ExecutionPool()`

to run either a whole CommandSet(), or singular Command(), or function inside a Command() in the execution pool, you use the:

     exec_pool = ExecutionPool()
     exec_pool.worker_bee(CommandSet().__name__ , function_or_Command_name : optional_str)

For example

	finished_command = exec_pool.worker_bee(new_command.__name__ , "function_test_function1")

This would run the entire module, assuming the module was coded to perform that way.

	finished_command = new_command.worker_bee(new_command , new_command.__name__)


Example `loader.py` code:
	
	exec_pool   = ExecutionPool()
	exec_pool.new_command_set(CommandRunner().dynamic_import('commandtest'))
	
	# run function
	finished_command = exec_pool.worker_bee('commandtest' , "function_test_function1")
	# run the top level dict "steps" from imported module
	finished_command = exec_pool.worker_bee('commandtest' , new_command.__name__)

Every command is .. json.. ugh:
	
  'ls_etc' : { 
			 "command"         : "ls -la /etc",
             "info_message"    : "[+] Info Text",
             "success_message" : "[+] Command Sucessful", 
             "failure_message" : "[-] ls -la Failed! Check the logfile!"
            }
	
	Fields are as follows:
  	  - Name of Command : 		key
  	      - Command 		value[0]
  	      - Informational message	value[1]
  	      - Success message		value[2]
  	      - Failure message		value[3]

Multiple commands can be placed in a ... json whatever... that are run sequentially:

  steps = {
           'ls_etc' : { "command"         : "ls -la /etc" ,
                        "info_message"    : "[+] Info Text",
                        "success_message" : "[+] Command Sucessful", 
                        "failure_message" : "[-] ls -la Failed! Check the logfile!"
                    },
            'ls_home' : { "command"         : "ls -la ~/"            ,
                          "info_message"    : "[+] Info Text"        ,
                          "success_message" : "[+] Command Sucessful", 
                          "failure_message" : "[-] ls -la Failed! Check the logfile!"
                        }
          }

Basic structure of an extension/script is as thus

    steps = { 'ls_user' : ["ls -la ~/", "[+] Command Sucessful", "[-]  Command Failed! Check the logfile!"],
	      'ls_root' : ["ls -la /", "[+] Command Sucessful!", "[-]  Command Failed! Check the logfile!"],
	      'ls_etc'  : ["ls -la /etc", "[+] Command Sucessful", "[-] ls -la Failed! Check the logfile!"]
           }
    info_message = "[+] Informational Text!"
    success_message = "[+] Test Sucessful!"
    failure_message = "[-] Test Failure!"

    def function_test_function1(params):
      steps = { 'ls_user' : ["ls -la ~/", "[+] Command Sucessful", "[-]  Command Failed! Check the logfile!"],
		'ls_root' : ["ls -la /", "[+] Command Sucessful!", "[-]  Command Failed! Check the logfile!"],
		'ls_etc'  : ["ls -la /etc", "[+] Command Sucessful", "[-] ls -la Failed! Check the logfile!"]
			    }
      info_message    = "[+] Informational Text!"
      success_message = "[+] Test Sucessful!"
      failure_message = "[-] Test Failure!"

Obvoiusly you can perform `str.format(thing)` on the commands, provided they are formatted properly for `os.popen()`
Thereby allowing you to perform complex shell scripting through a pythonic interface. I suggest you use bpython with it 
Until I manage to incorporate that environment

TADAAA! version 0.99-alpha is ready for not-release!
lookit mee! Lets get the exec pool working!
  
  moop@devboxen:~/Desktop/pybashy-master/pybashy/pybashy$ bpython
  bpython version 0.21 on top of Python 3.7.3 /usr/bin/python3
  >>> import pybashy_monilithic
  ============================== 
  -----[+] BEGINNING TEST! ----- 
  ============================== 
  [+] Adding command_dict to FunctionSet() 
  [+] Adding command_dict to ModuleSet() 
  [+] Adding FunctionSet() to ModuleSet() 
  INTERNAL: ModuleSet().add_function(FunctionSet()) 

  [+] Adding ModuleSet() to ExecutionPool() 
  [+] Adding command_dict to FunctionSet() 
  [+] Adding command_dict to ModuleSet() 
  [+] Adding FunctionSet() to ModuleSet() 
  INTERNAL: ModuleSet().add_function(FunctionSet()) 

  [+] Adding ModuleSet() to ExecutionPool() 
  >>> from pybashy_monilithic import *


  >>> type(exec_pool.test1)
  <class 'pybashy_monilithic.ModuleSet'>
  >>> type(exec_pool.test1.ls_etc)
  <class 'pybashy_monilithic.Command'>
  