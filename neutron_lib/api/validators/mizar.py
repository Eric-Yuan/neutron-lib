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
import six
from neutron_lib._i18n import _


def validate_endpoint_type(endpoint_type, valid_values=None):
    if not isinstance(endpoint_type, six.string_types):
        return _("Endpoint type not supported.")

    supported_endpoint_type_list = {
        "simple",
        # "scaled",
        # "proxied"
    }
    endpoint_type = str(endpoint_type).lower()
    if endpoint_type not in supported_endpoint_type_list:
        return _("Endpoint type not supported.")



