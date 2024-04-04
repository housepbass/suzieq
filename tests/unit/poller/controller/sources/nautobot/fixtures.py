EXPECTED_RESULT = {
    'nautobot-ns.172.100.100.10.22': {
        'address': '172.100.100.10',
        'devtype': None,
        'enable_password': None,
        'hostname': 'TESTDEVICE',
        'ignore_known_hosts': False,
        'jump_host': None,
        'jump_host_key_file': None,
        'namespace': 'nautobot-ns',
        'passphrase': None,
        'password': 'password',
        'per_cmd_auth': True,
        'port': 22,
        'retries_on_auth_fail': 0,
        'slow_host': False,
        'ssh_keyfile': None,
        'transport': 'ssh',
        'username': 'username',
    }
}

RESP1 = {
    "circuits": "http://localhost:8080/api/circuits/",
    "dcim": "http://localhost:8080/api/dcim/",
    "extras": "http://localhost:8080/api/extras/",
    "graphql": "http://localhost:8080/api/graphql/",
    "ipam": "http://localhost:8080/api/ipam/",
    "plugins": "http://localhost:8080/api/plugins/",
    "status": "http://localhost:8080/api/status/",
    "tenancy": "http://localhost:8080/api/tenancy/",
    "users": "http://localhost:8080/api/users/",
    "virtualization": "http://localhost:8080/api/virtualization/"
}

RESP2 = {'count': 3,
 'next': None,
 'previous': None,
 'results': [{'id': '9dacbca0-6f98-47f8-adcb-b501a0ff7769',
   'object_type': 'dcim.device',
   'display': 'TESTDEVICE',
   'url': 'http://localhost:8080/api/dcim/devices/9dacbca0-6f98-47f8-adcb-b501a0ff7769/',
   'natural_slug': 'TESTDEVICE__site1-chicago-il-ch1-eq-colo1_north-america_9dac',
   'face': None,
   'local_config_context_data': None,
   'local_config_context_data_owner_object_id': None,
   'name': 'TESTDEVICE',
   'serial': '',
   'asset_tag': None,
   'position': None,
   'device_redundancy_group_priority': None,
   'vc_position': None,
   'vc_priority': None,
   'comments': '',
   'local_config_context_schema': None,
   'local_config_context_data_owner_content_type': None,
   'device_type': {'id': '27c9f123-2363-4062-b515-46385b4ba3f0',
    'object_type': 'dcim.devicetype',
    'url': 'http://localhost:8080/api/dcim/device-types/27c9f123-2363-4062-b515-46385b4ba3f0/'},
   'status': {'id': '0a6a469e-428c-4007-aa4a-46ea02794dc8',
    'object_type': 'extras.status',
    'url': 'http://localhost:8080/api/extras/statuses/0a6a469e-428c-4007-aa4a-46ea02794dc8/'},
   'role': {'id': '1d40556f-aca5-4482-9db9-b3aaef40f330',
    'object_type': 'extras.role',
    'url': 'http://localhost:8080/api/extras/roles/1d40556f-aca5-4482-9db9-b3aaef40f330/'},
   'tenant': None,
   'platform': {'id': '8009d894-385f-4be0-b8c9-b7df749ccf04',
    'object_type': 'dcim.platform',
    'url': 'http://localhost:8080/api/dcim/platforms/8009d894-385f-4be0-b8c9-b7df749ccf04/'},
   'location': {'id': 'e3c17e29-89de-49ef-809e-7540a309548d',
    'object_type': 'dcim.location',
    'url': 'http://localhost:8080/api/dcim/locations/e3c17e29-89de-49ef-809e-7540a309548d/'},
   'rack': None,
   'primary_ip4': {'id': '83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1',
    'object_type': 'ipam.ipaddress',
    'url': 'http://localhost:8080/api/ipam/ip-addresses/83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1/'},
   'primary_ip6': None,
   'cluster': None,
   'virtual_chassis': None,
   'device_redundancy_group': None,
   'secrets_group': None,
   'created': '2024-04-02T12:49:55.768972Z',
   'last_updated': '2024-04-03T14:17:39.946893Z',
   'tags': [{'id': '851f6936-0a25-41a1-90a0-71e359156d6e',
     'object_type': 'extras.tag',
     'url': 'http://localhost:8080/api/extras/tags/851f6936-0a25-41a1-90a0-71e359156d6e/'},
    {'id': '51cf43a4-7477-41b5-8efc-27b156fed2dd',
     'object_type': 'extras.tag',
     'url': 'http://localhost:8080/api/extras/tags/51cf43a4-7477-41b5-8efc-27b156fed2dd/'},
    {'id': '44533e21-65d7-419f-920f-4de8b8a42d9b',
     'object_type': 'extras.tag',
     'url': 'http://localhost:8080/api/extras/tags/44533e21-65d7-419f-920f-4de8b8a42d9b/'},
    {'id': '2161ec75-9200-4fe7-966c-4212de18f0d0',
     'object_type': 'extras.tag',
     'url': 'http://localhost:8080/api/extras/tags/2161ec75-9200-4fe7-966c-4212de18f0d0/'},
    {'id': 'ef4da85c-7dbd-4218-9862-757dd80959ff',
     'object_type': 'extras.tag',
     'url': 'http://localhost:8080/api/extras/tags/ef4da85c-7dbd-4218-9862-757dd80959ff/'},
    {'id': '3298f76c-917e-421b-a6a2-11cc980ecddf',
     'object_type': 'extras.tag',
     'url': 'http://localhost:8080/api/extras/tags/3298f76c-917e-421b-a6a2-11cc980ecddf/'}],
   'notes_url': 'http://localhost:8080/api/dcim/devices/9dacbca0-6f98-47f8-adcb-b501a0ff7769/notes/',
   'custom_fields': {},
   'parent_bay': None}]}

RESP3 = {'id': '83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1',
 'object_type': 'ipam.ipaddress',
 'display': '172.100.100.10/24',
 'url': 'http://localhost:8080/api/ipam/ip-addresses/83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1/',
 'natural_slug': 'global_172-100-100-10_83db',
 'address': '172.100.100.10/24',
 'host': '172.100.100.10',
 'mask_length': 24,
 'type': 'host',
 'ip_version': 4,
 'dns_name': 'clab-leafspine-dc1-leaf-1.custom_mgmt',
 'description': '',
 'status': {'id': '0a6a469e-428c-4007-aa4a-46ea02794dc8',
  'object_type': 'extras.status',
  'url': 'http://localhost:8080/api/extras/statuses/0a6a469e-428c-4007-aa4a-46ea02794dc8/'},
 'role': None,
 'parent': {'id': '795bc427-87cf-46b8-b5df-49dd18ad8256',
  'object_type': 'ipam.prefix',
  'url': 'http://localhost:8080/api/ipam/prefixes/795bc427-87cf-46b8-b5df-49dd18ad8256/'},
 'tenant': None,
 'nat_inside': None,
 'created': '2024-04-02T12:49:56.261387Z',
 'last_updated': '2024-04-03T14:17:39.737927Z',
 'tags': [],
 'notes_url': 'http://localhost:8080/api/ipam/ip-addresses/83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1/notes/',
 'custom_fields': {},
 'nat_outside_list': [],
 'interfaces': [{'id': '74747faa-8068-4bf9-beac-624873012131',
   'object_type': 'dcim.interface',
   'url': 'http://localhost:8080/api/dcim/interfaces/74747faa-8068-4bf9-beac-624873012131/'}],
 'vm_interfaces': []}

RESP4 = {'id': 'e3c17e29-89de-49ef-809e-7540a309548d',
 'object_type': 'dcim.location',
 'display': 'North America → Site1 = Chicago, IL, CH1-EQ-COLO1',
 'url': 'http://localhost:8080/api/dcim/locations/e3c17e29-89de-49ef-809e-7540a309548d/',
 'natural_slug': 'site1-chicago-il-ch1-eq-colo1_north-america_e3c1',
 'tree_depth': 1,
 'time_zone': None,
 'circuit_count': 0,
 'device_count': 2,
 'prefix_count': 0,
 'rack_count': 0,
 'virtual_machine_count': 0,
 'vlan_count': 0,
 'name': 'Site1 = Chicago, IL, CH1-EQ-COLO1',
 'description': '',
 'facility': '',
 'asn': None,
 'physical_address': '',
 'shipping_address': '',
 'latitude': None,
 'longitude': None,
 'contact_name': '',
 'contact_phone': '',
 'contact_email': '',
 'comments': '',
 'parent': {'id': '2aca3200-7bb9-4b8d-b55f-deafefccb1ff',
  'object_type': 'dcim.location',
  'url': 'http://localhost:8080/api/dcim/locations/2aca3200-7bb9-4b8d-b55f-deafefccb1ff/'},
 'location_type': {'id': 'e3fd7a0d-996e-44bf-84fa-0271993272c9',
  'object_type': 'dcim.locationtype',
  'url': 'http://localhost:8080/api/dcim/location-types/e3fd7a0d-996e-44bf-84fa-0271993272c9/'},
 'status': {'id': '0a6a469e-428c-4007-aa4a-46ea02794dc8',
  'object_type': 'extras.status',
  'url': 'http://localhost:8080/api/extras/statuses/0a6a469e-428c-4007-aa4a-46ea02794dc8/'},
 'tenant': None,
 'created': '2024-04-02T12:49:53.824192Z',
 'last_updated': '2024-04-02T12:49:53.824216Z',
 'tags': [],
 'notes_url': 'http://localhost:8080/api/dcim/locations/e3c17e29-89de-49ef-809e-7540a309548d/notes/',
 'custom_fields': {'remedy_id': None}}

TEST_URLS = {
    "http://127.0.0.1:8080/api/": RESP1,
    "http://127.0.0.1:8080/api/dcim/devices/": RESP2,
    "http://localhost:8080/api/ipam/ip-addresses/83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1/": RESP3,
    "http://localhost:8080/api/dcim/locations/e3c17e29-89de-49ef-809e-7540a309548d/": RESP4,
    "https://127.0.0.1:8080/api/": RESP1,
    "https://127.0.0.1:8080/api/dcim/devices/": RESP2,
    "https://localhost:8080/api/ipam/ip-addresses/83dbe0a9-cc69-4a71-9d7e-ebe9dc5b85e1/": RESP3,
    "https://localhost:8080/api/dcim/locations/e3c17e29-89de-49ef-809e-7540a309548d/": RESP4,
}