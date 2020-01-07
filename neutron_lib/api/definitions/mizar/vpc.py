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
from neutron_lib.api import converters
from neutron_lib.api.definitions import l3
from neutron_lib.api.definitions.mizar import droplet
from neutron_lib.db import constants


ALIAS = 'vpc'
IS_SHIM_EXTENSION = False
IS_STANDARD_ATTR_EXTENSION = False
NAME = 'VPC Extension'
API_PREFIX = 'mizar'
DESCRIPTION = "Mizar VPC model"
UPDATED_TIMESTAMP = "2019-11-30T10:00:00-00:00"

VPC = 'vpc'
VPCS = 'vpcs'

RESOURCE_ATTRIBUTE_MAP = {
    VPCS: {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_filter': True,
               'is_sort_key': True,
               'is_visible': True, 'primary_key': True},
        'vni': {'allow_post': True, 'allow_put': True,
                'convert_to': converters.convert_to_int,
                'is_filter': True,
                'is_sort_key': True,
                'default': '', 'is_visible': True},
        'tenant_id': {'allow_post': True, 'allow_put': False,
                      'required_by_policy': True,
                      'validate':
                          {'type:string': constants.PROJECT_ID_FIELD_SIZE},
                      'is_filter': True,
                      'is_sort_key': True,
                      'is_visible': True},
        'cidr': {'allow_post': True, 'allow_put': False,
                 'required_by_policy': True,
                 'convert_to': converters.convert_cidr_to_canonical_format,
                 'validate': {'type:subnet_or_none': None},
                 'is_filter': True,
                 'is_sort_key': True,
                 'is_visible': True},
        'transit_routers': {'allow_post': False, 'allow_put': True,
                            'default': [],
                            'convert_list_to': converters.convert_none_to_empty_list,
                            'validate': {'type:uuid_list': None},
                            'is_filter': False,
                            'is_sort_key': False,
                            'is_visible': True}
    },
    droplet.DROPLET: {
        'vpc': {'allow_post': False, 'allow_put': False,
                'validate': {'type:uuid': None},
                'is_filter': True,
                'is_sort_key': True,
                'is_visible': True},
    }
}

SUB_RESOURCE_ATTRIBUTE_MAP = {}

ACTION_MAP = {
    VPC: {
        'add_transit_router': 'PUT',
        'remove_transit_router': 'PUT'
    }
}

ACTION_STATUS = {
}

REQUIRED_EXTENSIONS = [
    l3.ALIAS,
    droplet.ALIAS,
]

OPTIONAL_EXTENSIONS = [
]