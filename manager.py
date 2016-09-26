#!/usr/bin/env python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__))))

from script_manager import Manager
from punch import punch_manager, time_manager

manager = Manager(description='The Manager')
manager.add_command('punch', punch_manager)
manager.add_command('time', time_manager)

if __name__ == '__main__':
    manager.run()
