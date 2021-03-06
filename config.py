###########################################################################
#
#  Copyright 2017 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

import os

EXECUTE_PATH = os.environ.get('STARTHINKER_PATH', "/home/starthinker") + '/'

# In production simply create this file: touch /mnt/SERVER
DEVELOPMENT_MODE = not os.path.isfile('/mnt/SERVER')

# This is always set to False ( setting it to True does nothing productive )
INTERNAL_MODE = False

# Used for local testing, 
if DEVELOPMENT_MODE:
 
  # credentials used to manage universal information such as logs, and project that does NOT store data
  UI_PROJECT = 'cloud-project-id-test'
  UI_CLIENT = '/home/credentials/test/starthinker_client.json'
  UI_SERVICE = '/home/credentials/test/starthinker_service.json'

  # used to run jobs ( if UI_TOPIC use pub/sub, if UI_CRON write recipe to folder, assumes cron tab executes starthinker/ui/ui/crontab.py )
  UI_TOPIC = '' 
  UI_CRON = '/mnt/starthinker'

  # used to log job execution ( optional, leave blank )
  UI_LOG_NAMESPACE = 'StarThinker'
  UI_LOG_KIND = 'Recipe_Execution'

  # used to log job execution
  UI_LOG_DATASET = 'starthinker-test-log'
  UI_LOG_TABLE = 'test-worker'

  # used to multiply all buffer sizes for scaling on larger or smaller machines, can be a float
  BUFFER_SCALE = 1

else:
  # credentials used to manage universal infomation such as logs, and project that does NOT store data
  UI_PROJECT = 'UI CLOUD PROJECT'
  UI_CLIENT = 'UI CLIENT CREDENTIALS PATH'
  UI_SERVICE = 'UI SERVICE CREDENTIALS PATH'

  # used to run jobs ( if UI_TOPIC use pub/sub, if UI_CRON write recipe to folder, assumes cron tab executes starthinker/ui/ui/crontab.py )
  UI_TOPIC = '' #'default_test_worker'
  UI_CRON = 'CRON DIRECTORY'

  # used to log job execution ( optional, leave blank )
  UI_LOG_NAMESPACE = 'StarThinker'
  UI_LOG_KIND = 'Recipe_Execution'

  # used to log job execution
  UI_LOG_DATASET = 'starthinker-log'
  UI_LOG_TABLE = 'worker'

  # used to multiply all buffer sizes for scaling on larger or smaller machines, can be a float
  BUFFER_SCALE = 6
