# -*- coding: utf-8 -*-

"""
This will do disk operations 
  Necessary Lib for SANDBOX!

"""
#import os
#import sys
#import pathlib
#import subprocess
#from pathlib import Path

#class DiskOperations:
#    '''
#    Does disk stuff
#    '''
#    def __init__(self, kwargs):
#        for (k, v) in kwargs.items():
#            setattr(self, k, v)
        
#def setup_disk_for_liveusb(self, diskname, efi_dir, persistance_dir, temp_boot_dir, live_disk_dir):
def function_setup_disk_for_liveusb(diskname, efi_dir, persistance_dir, temp_boot_dir, live_disk_dir):
        # This creates the basic disk structure of an EFI disk with a single OS.
        # You CAN boot .ISO Files from the persistance partition if you mount in GRUB2 
        ## EFI
        steps = { 'partition_{}1'.format(diskname):
                ["parted /dev/{}--script mkpart EFI fat16 1MiB 100MiB".format(diskname),
                '[+] Success','[-] Failure'],
        ## LIVE disk partition
                'partition_{}2'.format(diskname):
                ["parted /dev/{}--script mkpart live fat16 100MiB 3GiB".format(diskname),
                '[+] Success','[-] Failure'],
        ## Persistance Partition
                'partition_{}3'.format(diskname):
                ["parted /dev/{}--script mkpart persistence ext4 3GiB 100%".format(diskname),
                '[+] Success','[-] Failure'],
        ## Sets filesystem flag
                'set_msftdata':
                ["parted /dev/{}--script set 1 msftdata on".format(diskname),
                '[+] Success','[-] Failure'],
                ## Sets boot flag for legacy (NON-EFI) BIOS
                'set_legacy_boot':
                ["parted /dev/{}--script set 2 legacy_boot on".format(diskname),
                '[+] Success','[-] Failure'],
                'set_msftdata2':
                ["parted /dev/{}--script set 2 msftdata on".format(diskname),
                '[+] Success','[-] Failure'],
                # Here we make the filesystems for the OS to live on
                ## EFI,
                'format_EFI':
                ["mkfs.vfat -n EFI /dev/{}1".format(diskname),
                '[+] Success','[-] Failure'],
                ## LIVE disk partition
                'format_main_disk':
                ["mkfs.vfat -n LIVE /dev/{}2".format(diskname),
                '[+] Success','[-] Failure'],
                ## Persistance Partition
                'format_persistance':
                ["mkfs.ext4 -F -L persistence /dev/{}3".format(diskname),
                '[+] Success','[-] Failure'],
                }
        #stepper = Stepper.step(steps)
        #if isinstance(stepper, Exception):
        #    error_exit("[-] Disk Formatting Failed! Check the logfile!", stepper)
        #else:
        #    greenprint("[+] Disk Formatting Finished Sucessfully!")

#    def move_system_files(self, efi_dir, live_disk_dir,persistance_dir,file_source_dir):
def function_move_system_files(efi_dir, live_disk_dir,persistance_dir,file_source_dir):
        # Creating Temporary work directories
        steps = { 'make_directories'  : 
                    ["mkdir {} {} {} {}".format(efi_dir, live_disk_dir ,persistance_dir, file_source_dir),
                    '[+] Success','[-] Failure'],
                  'mount_partition1'  :
                    ["mount /dev/{}1 {}".format(diskname, efi_dir ),
                    '[+] Success','[-] Failure'],    
                  'mount_partition2' :
                    ["mount /dev/{}2 {}".format(diskname, live_disk_dir),
                    '[+] Success','[-] Failure'],
                  'mount_partition3'  :
                    ["mount /dev/{}3 {}".format(diskname, persistance_dir),
                    '[+] Success','[-] Failure'],
                  'mount_file_source' :
                    ["mount -oro {} {}".format(live_iso, file_source_dir),
                    '[+] Success','[-] Failure'],
                  'move_from_source_to_dest' :
                    ["cp -ar {}/* {}".format(file_source_dir, live_disk_dir) ,
                    '[+] Success','[-] Failure']  
                }
        #stepper = Stepper.step(steps)
        #if isinstance(stepper, Exception):
        #info_message("[+] File Moving Finished Sucessfully!")
        #else:
        #error_exit("[-] File Moving Failed! Check the logfile!", stepper)

#    def establish_usb_persistance(self):
def function_establish_usb_persistance():
        # IMPORTANT! This establishes persistance! UNION is a special mounting option 
        # https://unix.stackexchange.com/questions/282393/union-mount-on-linux
        steps = {'persistance' :
                ['echo "/ union" > {}/persistence.conf'.format(persistance_dir),
                 '[+] Persistance Established' , '[-] Persistance Failed!']
                }
        #stepper = Stepper.step(steps=steps)
        #if isinstance(stepper, Exception):
#        print("")
        #else:
        #    error_exit("", stepper)
