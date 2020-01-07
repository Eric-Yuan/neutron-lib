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


ALIAS = 'droplet'
IS_SHIM_EXTENSION = False
IS_STANDARD_ATTR_EXTENSION = False
NAME = 'Droplet Extension'
API_PREFIX = 'mizar'
DESCRIPTION = "Mizar droplet model"
UPDATED_TIMESTAMP = "2019-11-30T10:00:00-00:00"

DROPLET = 'droplet'
DROPLETS = 'droplets'

RESOURCE_ATTRIBUTE_MAP = {
    DROPLETS: {
        'id': {'allow_post': False, 'allow_put': False,
               'validate': {'type:uuid': None},
               'is_filter': True,
               'is_sort_key': True,
               'is_visible': True, 'primary_key': True},
        'vtep_ip': {'allow_post': False, 'allow_put': False,
                    'convert_to': converters.convert_ip_to_canonical_format,
                    'validate': {'type:ip_address_or_none': None},
                    'is_filter': True,
                    'is_sort_key': True,
                    'is_visible': True},
    },
}

SUB_RESOURCE_ATTRIBUTE_MAP = {}

ACTION_MAP = {
}

ACTION_STATUS = {
}

REQUIRED_EXTENSIONS = [
]

OPTIONAL_EXTENSIONS = [
]
