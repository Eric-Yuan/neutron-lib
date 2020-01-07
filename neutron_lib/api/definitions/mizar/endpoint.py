# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from neutron_lib import constants
from neutron_lib.api import converters
from neutron_lib.api.definitions.mizar import vpc, vpcnet, droplet
from neutron_lib.api.validators import validators, mizar
from neutron_lib.db import constants as db_const


validators.add_validator('endpoint_type', mizar.validate_endpoint_type)

ALIAS = 'endpoint'
IS_SHIM_EXTENSION = False
IS_STANDARD_ATTR_EXTENSION = False
NAME = 'Endpoint Extension'
API_PREFIX = 'mizar'
DESCRIPTION = "Mizar Network model"
UPDATED_TIMESTAMP = "2019-11-30T10:00:00-00:00"

ENDPOINT = 'endpoint'
ENDPOINTS = 'endpoints'

RESOURCE_ATTRIBUTE_MAP = {
    ENDPOINTS: {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_filter': True,
               'is_sort_key': True,
               'is_visible': True, 'primary_key': True},
        'net_id': {'allow_post': True, 'allow_put': True,
                   'validate': {'type:uuid': None},
                   'is_filter': True,
                   'is_sort_key': True,
                   'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'required_by_policy': True,
                      'validate':
                          {'type:string': db_const.PROJECT_ID_FIELD_SIZE},
                      'is_filter': True,
                      'is_sort_key': True,
                      'is_visible': True},
        'ip_address': {'allow_post': True, 'allow_put': True,
                       'default': constants.ATTR_NOT_SPECIFIED,
                       'convert_to': converters.convert_ip_to_canonical_format,
                       'validate': {'type:ip_address_or_none': None},
                       'is_filter': True,
                       'is_sort_key': True,
                       'is_visible': True},
        'endpoint_type': {'allow_post': True, 'allow_put': False,
                          'default': 'simple',
                          'validate': {'type:endpoint_type': None},
                          'is_filter': True,
                          'is_sort_key': True,
                          'is_visible': True},
        'droplet': {'allow_post': False, 'allow_put': False,
                    'validate': {'type:uuid': None},
                    'is_filter': True,
                    'is_sort_key': True,
                    'is_visible': True}
    },
    droplet.DROPLET: {
        'endpoint': {'allow_post': False, 'allow_put': False,
                     'validate': {'type:uuid': None},
                     'is_filter': True,
                     'is_sort_key': True,
                     'is_visible': True},
    }
}

SUB_RESOURCE_ATTRIBUTE_MAP = {}

ACTION_MAP = {
}

ACTION_STATUS = {
}

REQUIRED_EXTENSIONS = [
    vpcnet.ALIAS,
    droplet.ALIAS
]

OPTIONAL_EXTENSIONS = [
]