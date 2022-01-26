'''
Copyright 2022 Airbus SAS

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from sos_trades_core.execution_engine.sos_discipline import SoSDiscipline
from sos_trades_core.execution_engine.data_connector.mock_connector import MockConnector


class Disc2_data_connector(SoSDiscipline):
    _maturity = 'Fake'

    data_connection_dict = {'connector_type': MockConnector.NAME,
                            'hostname': 'test_hostname',
                            'connector_request': 'test_request'}
    dremio_path = '"test_request"'

    DESC_IN = {
        'y': {'type': 'float', 'visibility': SoSDiscipline.SHARED_VISIBILITY, 'namespace': 'ns_ac',
              SoSDiscipline.CONNECTOR_DATA: data_connection_dict},
        'constant': {'type': 'float'},
        'power': {'type': 'int'},
    }
    DESC_OUT = {
        'z': {'type': 'float', 'visibility': SoSDiscipline.SHARED_VISIBILITY, 'namespace': 'ns_ac'}
    }

    def run(self):
        y = self.get_sosdisc_inputs('y')
        z = 1.0
        dict_values = {'z': z}
        self.store_sos_outputs_values(dict_values)