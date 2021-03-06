
import enum

NAMESPACE_FIELD_XMLNS = "xmlns"
NAMESPACE_FIELD_XSI = "xsi"
NAMESPACE_FIELD_ATTRIB_CONTENT = "{0}:{1}".format(NAMESPACE_FIELD_XMLNS, NAMESPACE_FIELD_XSI)
TEST_TICKET_ID = "test"
SCRIPTED_CONDITION_TRUE = "<response><condition_result>true</condition_result></response>"
SCRIPTED_CONDITION_FALSE = "<response><condition_result>false</condition_result></response>"

SERVICE_OBJECT_TYPE_PREDEFINED = "PREDEFINED"
SERVICE_OBJECT_TYPE_PROTOCOL = "PROTOCOL"
SERVICE_OBJECT_TYPE_APPLICATION_IDENTITY = "APPLICATION_IDENTITY"
TYPE_ANY = "ANY"
TYPE_INTERNET = "INTERNET"
TYPE_ATTRIB = "type"
TYPE_DNS = "DNS"
TYPE_IP = "IP"
TYPE_OBJECT = "Object"
TYPE_HOST = "HOST"
TYPE_NETWORK = "NETWORK"
TYPE_OTHER = "OTHER"
TYPE_RANGE = "RANGE"
XML_ATTRIB_IDENTIFIER = "_attribs"
XML_TAG_IDENTIFIER = "_xml_tag"
XSI_NAMESPACE_URL = "http://www.w3.org/2001/XMLSchema-instance"


class Attributes:
    ACL__BINDING = "acl__binding"
    BLOCK_CELL_VIOLATION = "blocked_cell_violation"
    BLOCK_ONLY_MATRIX_CELL_VIOLATION = "blocked_only_matrix_cell_violation"
    CONCRETE = "concrete"
    CUSTOM = "custom"
    DEVICE_NETWORK = "device_network"
    DEVICE_SERVICE = "device_service"
    DNS = "dns"
    FIELD_TYPE_APPROVE_REJECT = "approve_reject"
    FIELD_TYPE_CHECKBOX = "checkbox"
    FIELD_TYPE_DATE = "date"
    FIELD_TYPE_DROP_DOWN_LIST = "drop_down_list"
    FIELD_TYPE_HYPERLINK = "hyperlink"
    FIELD_TYPE_MANAGER = "manager"
    FIELD_TYPE_MULTIPLE_SELECTION = "multiple_selection"
    FIELD_TYPE_MULTI_ACCESS_REQUEST = "multi_access_request"
    FIELD_TYPE_MULTI_GROUP_CHANGE = "multi_group_change"
    FIELD_TYPE_MULTI_HYPERLINK = "multi_hyperlink"
    FIELD_TYPE_MULTI_NETWORK_OBJECT = "multi_network_object"
    FIELD_TYPE_MULTI_SERVICE = "multi_service"
    FIELD_TYPE_MULTI_TARGET = "multi_target"
    FIELD_TYPE_MULTI_TEXT = "multi_text_field"
    FIELD_TYPE_MULTI_TEXT_AREA = "multi_text_area"
    FIELD_TYPE_TEXT = "text_field"
    FIELD_TYPE_TEXT_AREA = "text_area"
    FIELD_TYPE_TIME = "time"
    GROUP = "group"
    HREF = "href"
    HOST_NETWORK_OBJECT = "host_network_object"
    INTERFACE_TYPE = "interfaceDTO"
    NETWORK_OBJECT_TYPE_BASIC = "basicNetworkObjectDTO"
    NETWORK_OBJECT_TYPE_GROUP = "networkObjectGroupDTO"
    NETWORK_OBJECT_TYPE_HOST = "hostNetworkObjectDTO"
    NETWORK_OBJECT_TYPE_HOST_WITH_INTERFACES = "hostNetworkObjectWithInterfacesDTO"
    NETWORK_OBJECT_TYPE_RANGE = "rangeNetworkObjectDTO"
    NETWORK_OBJECT_TYPE_SUBNET = "subnetNetworkObjectDTO"
    NETWORK_OBJECT_TYPE_INTERNET = "internetNetworkObjectDTO"
    NETWORK_OBJECT_TYPE_CLOUD = "cloudSecurityGroupDTO"
    NETWORK_OBJECT_TYPE_VIRTUAL_SERVER = "networkObjectVirtualServerDTO"
    NETWORK_OBJECT_TYPE_VM_INSTANCE = "vmInstanceDTO"
    POLICY__BINDING = "policy__binding"
    POOL_MEMBER = "poolMember"
    POOL_MEMBERS = "poolMembers"
    PREDEFINED = "predefined"
    RANGE_NETWORK = "range_network"
    RANGE_SERVICE = "range_service"
    RESTRICTED_CELL_VIOLATION = 'restricted_cell_violation'
    SECURITY_ZONE_MATRIX = "securityZoneMatrixDTO"
    SECURITY_REQUIREMENT_TYPE_MATRIX = "matrixRequirementDTO"
    SECURITY_REQUIREMENT_TYPE_PCI = "pciRequirementDTO"
    SERVICE_TYPE_GROUP = "serviceGroupDTO"
    SERVICE_TYPE_SINGLE = "singleServiceDTO"
    SUBNET = "subnet"
    SUBNET_NETWORK_OBJECT = "subnet_network_object"
    TRANSPORT_SERVICE = "transport_service"
    TYPE = ":type"
    VIOLATION_ANY_NETWORK_OBJECT = "any_network_object"
    VIOLATION_ANY_SERVICE = "any_service"
    VIOLATION_GROUP_NETWORK_OBJECT = "group_member_network_object"
    VIOLATION_IP_NETWORK_OBJECT = "ip_network_object"
    VIOLATION_GROUP_MEMBER_SERVICE_OBJECT = "group_member_service_object"
    VIOLATION_RANGE_NETWORK_OBJECT = "range_network_object"
    VIOLATION_SINGLE_NETWORK_OBJECT = "single_network_object"
    VIOLATION_SINGLE_SERVICE = "single_service"
    VIOLATION_SINGLE_SERVICE_OBJECT = "single_service_object"
    XSI_NAMESPACE_TYPE = "{{{0}}}type".format(XSI_NAMESPACE_URL)
    XSI_TYPE = "{0}:type".format(NAMESPACE_FIELD_XSI)
    ZONE = "zone"
    ZONE__BINDING = "zone__binding"


class Elements:
    CREATE_DATE = "createDate"
    ID = "id"
    TICKET_INFO = "ticket_info"
    UPDATE_DATE = "updateDate"
    CURRENT_STAGE = "current_stage"
    OPEN_REQUEST_STAGE = "open_request_stage"
    COMPLETION_DATA = "completion_data"
    ACCEPTINGRULESDTO = "acceptingRulesDTO"
    ACCESS_REQUEST = "access_request"
    ACCESS_REQUESTS = "access_requests"
    ACCESS_REQUEST_ID = "access_request_id"
    ACCESS_REQUEST_VERIFIER_RESULT = "access_request_verifier_result"
    ACCESS_TYPE = "access_type"
    ACL = "acl"
    ACL_NAME = "acl_name"
    ACTION = "action"
    ADDITIONAL_INFO = "additional_info"
    ADDRESS = "address"
    ADDRESS_BOOK = "address_book"
    ADMIN = "admin"
    ADMIN_DOMAIN = "admin_domain"
    ADMINISTRATOR = "administrator"
    ALLOWED_SERVICE = "allowed_service"
    ALLOWED_SERVICES = "allowed_services"
    ANCESTOR_MANAGEMENT_ID = "ancestor_management_id"
    ANCESTOR_MANAGEMENT_NAME = "ancestor_management_name"
    ANCESTOR_MANAGEMENT_REVISION_ID = "ancestor_management_revision_id"
    APP_NAME = "app_name"
    APPLICATION_NAME = "application_name"
    APP_OWNER = "app_owner"
    APPLICATION = "application"
    APPLICATION_ID = "application_id"
    APPLICATION_DETAILS = "application_details"
    APPLICATION_INTERFACE = "application_interface"
    APPLICATION_INTERFACES = "application_interfaces"
    APPLICATION_INTERFACE_ID = "application_interface_id"
    APPLICATION_PACK = "application_pack"
    APPLICATIONS = "applications"
    APPROVED = "approved"
    APPROVED_BY = "approved_by"
    ASSIGNED = "ASSIGNED"
    ASSIGNEE = "assignee"
    ASSIGNMENT = "assignment"
    ASSIGNEE_ID = "assignee_id"
    AUDITLOG = "auditLog"
    AUTHENTICATION_METHOD = "authentication_method"
    AUTHORIZATIONSTATUS = "authorizationStatus"
    AUTOMATIC = "automatic"
    AVAILABILITY_ZONE = "availability_zone"
    BINDING = "binding"
    BINDING_NAME = "binding_name"
    BINDING_SUGGESTION = "binding_suggestion"
    BINDING_UID = "binding_uid"
    BINDINGS = "bindings"
    BINDING_AND_RULES = "binding_and_rules"
    BINDINGS_AND_RULES = "bindings_and_rules"
    BLOCKINGRULESDTO = "blockingRulesDTO"
    BLOCKSTART = "blockStart"
    BLOCKEND = "blockEnd"
    BLOCKED_SERVICES = "blocked_services"
    BNPP_REGION_REQUEST = "bnpp_region_request"
    BUSINESSOWNEREMAIL = "businessOwnerEmail"
    BUSINESSOWNERNAME = "businessOwnerName"
    CHANGE_AUTHORIZATION = "change_authorization"
    CHANGE_AUTHORIZATION_BINDING = "change_authorization_binding"
    CHANGE_AUTHORIZATION_BINDINGS = "change_authorization_bindings"
    CHANGE_ID = "change_id"
    CHANGE_IMPLEMENTATION_STATUS = "change_implementation_status"
    CIDR = "cidr"
    CLASS_NAME = "class_name"
    CLEANUP = "cleanup"
    CLEANUPS = "cleanups"
    CLEANUP_SET = "cleanup_set"
    CLOUD_SECURITY_GROUP = "cloud_security_group"
    CLOUD_SECURITY_GROUPS = "cloud_security_groups"
    CODE = "code"
    COLOR = "color"
    COMMENT = "comment"
    COMMENTS = "comments"
    USE_TOPOLOGY = "use_topology"
    COMPLIANCE_POLICIES = "compliance_policies"
    COMPLIANCE_POLICY = "compliance_policy"
    COMPLIANCE_RULE = "compliance_rule"
    COMPLIANCE_RULES = "compliance_rules"
    CONNECTION = "connection"
    CONNECTION_EXTENDED = "connection_extended"
    CONNECTIONS_EXTENDED = "connections_extended"
    CONNECTIONS = "connections"
    CONNECTION_TO_APPLICATION = "connection_to_application"
    CONNECTION_TO_APPLICATIONS = "connection_to_applications"
    CONNECTIONS_TO_APPLICATIONS = "connections_to_applications"
    CONNECTION_TO_APPLICATION_PACK = "connection_to_application_pack"
    CONNECTION_TO_APPLICATION_PACKS = "connection_to_application_packs"
    CONNECTED_SERVERS = "connected_servers"
    CONTENT = "content"
    COUNT = "count"
    CP_INSPECT_STREAMING_NAME = "cp_inspect_streaming_name"
    CP_UID = 'cp_uid'
    CP_PROTOTYPE_NAME = "cp_prototype_name"
    CREATED = "created"
    CREATED_BY = "created_by"
    CREATION_DATE = "creation_date"
    CURRENT_STEP = "current_step"
    CUSTOMER = "customer"
    CUSTOMER_ID = "customer_id"
    CUSTOMERS = "customers"
    DATE = "date"
    DCR_PRODUCT = "dcr_product"
    DCR_TEST_CONCRETE = "dcr_test_concrete"
    DCR_TEST_GROUP = "dcr_test_group"
    DCR_TEST = "dcr_test"
    DCR_TESTS = "dcr_tests"
    DECOMMISSIONED = "decommissioned"
    DEFAULT = "default"
    DESCRIPTION = "description"
    DESIGNER_COMMAND = "designer_command"
    DESIGNER_COMMANDS = "designer_commands"
    DESIGNER_RESULT = "designer_result"
    DESIGNER_RESULTS = "designer_results"
    DESTINATION = "destination"
    DESTINATION_DOMAIN = "destination_domain"
    DESTINATIONS = "destinations"
    DESTINATIONS_IN_ZONE = "destinations_in_zone"
    DEST_NETWORKS_NEGATED = "dest_networks_negated"
    DESTINATIONSERVICES = "destinationServices"
    DEST_NETWORK_COLLECTION = "dest_network_collection"
    DESTNETWORKS = "destinationNetworks"
    DEST_SERVICES_NEGATED = "dest_services_negated"
    DEVICE = "device"
    DEVICE_NAME = "name"
    DEVICE_INFO = "device_info"
    DEVICE_TYPE = "device_type"
    DEVICES = "devices"
    DEVICES_AND_BINDINGS = "devices_and_bindings"
    DEVICE_AND_BINDINGS = "device_and_bindings"
    DEVICE_CONFIG = "device_config"
    DEVICE_ID = "device_id"
    DEVICE_SUGGESTION = "device_suggestion"
    DIRECTION = "direction"
    DISABLED = "disabled"
    DISPLAYNAME = "displayName"
    DISPLAY_NAME = "display_name"
    DNSADDRESS = "dnsAddress"
    DNS_IP_ADDRESSES = 'dns_ip_addresses'
    DST = "dst"
    DOCUMENTATION = "documentation"
    RULE_DOCUMENTATION = "rule_documentation"
    DOMAIN = "domain"
    DOMAINS = "domains"
    DOMAIN_ID = "domain_id"
    DOMAIN_NAME = "domain_name"
    DST_NETWORK = "dst_network"
    DST_NETWORKS = "dst_networks"
    DST_SERVICE = "dst_service"
    DST_SERVICES = "dst_services"
    EDIT_MODE = "edit_mode"
    EDITORS = "editors"
    EDITOR = "editor"
    EMAIL = "email"
    EXCLUDE_ANY= "exclude_any"
    EXEMPTED_TRAFFIC = "exempted_traffic"
    EXEMPTED_TRAFFIC_LIST = "exempted_traffic_list"
    EXPIRATION_DATE = "expiration_date"
    EXPIRATION_FIELD_NAME = "expiration_field_name"
    EXPIREDATE = "expireDate"
    EXPRESSION = "expression"
    EXTERNAL = "external"
    FIELD = "field"
    FIELDS = "fields"
    FIRST_IP = "first_ip"
    FIRST_NAME = "first_name"
    FROM = "from"
    FLOW = "flow"
    FLOW_DESTINATION = 'flow_destination'
    FLOW_DESTINATION_VIOLATIONS = "flow_destination_violations"
    FLOW_DESTINATIONS = 'flow_destinations'
    FLOW_SOURCE = "flow_source"
    FLOW_SOURCE_VIOLATIONS = "flow_source_violations"
    FLOW_SOURCES = "flow_sources"
    FROM_DOMAIN = "from_domain"
    FROM_ZONE = "from_zone"
    F5_DEVICE_NAME = "f5_device_name"
    GENERIC_DEVICES = "generic_devices"
    GLOBAL = "global"
    GROUP = "group"
    GROUP_CHANGE = "group_change"
    GROUP_ID = "group_id"
    GROUP_MEMBER = "group_member"
    GROUP_MEMBER_PATH = "group_member_path"
    GROUPPERMISSION = "groupPermission"
    GROUPPERMISSIONS = "groupPermissions"
    GROUPID = "groupId"
    GUICLIENT = "guiClient"
    HANDLE_IMPLICIT_CLEANUP_RULE = "handled_by_implicit_cleanup_rule"
    HOST_NAME = "host_name"
    HYPERLINK = "hyperlink"
    ID = "id"
    IMPLEMENTATION_PERCENTAGE_THRESHOLD = "implementation_percentage_threshold"
    IMPLEMENTATION_STATUS = "implementation_status"
    IMPLEMENTING_RULE = "implementing_rule"
    IMPLEMENTING_RULES = "implementing_rules"
    IMPLEMENTS_ACCESS_REQUESTS = "implements_access_requests"
    IMPLICIT = "implicit"
    INCOMING_INTERFACE_NAME = "incoming_interface_name"
    INDOMAINELEMENTID = "inDomainElementId"
    INPUT = "input"
    INSTALLABLE_TARGET = "installable_target"
    INSTALLED_ON_MODULE = "installed_on_module"
    INSTANCE_ID = "instance_id"
    INSTANCES_TOTAL = "instances_total"
    INSTRUCTION = "instruction"
    INSTRUCTION_TYPE = "instruction_type"
    INSTRUCTIONS = "instructions"
    INTERFACE = "interface"
    INTERFACES = "interfaces"
    INTERFACE_FOR_NETWORK_OBJECT = "interface_for_network_object"
    INTERFACE_CONNECTION = "interface_connection"
    INTERFACE_CONNECTIONS = "interface_connections"
    INTERFACE_IP = "interface_ip"
    INTERFACE_IPS = "interface_ips"
    INTERFACE_NAME = "interface_name"
    INTERNET_REFERRAL_OBJECT = "internet_referral_object"
    INTERVAL = "interval"
    IP = "ip"
    IP_ADDRESS = "ip_address"
    IP_TYPE = "ip_type"
    IS_ANY = "is_any"
    ISACTIVE = "isActive"
    ISCUSTOM = "isCustom"
    ISDEFAULT = "isDefault"
    ISMANDATORY = "isMandatory"
    IS_PUBLISHED = "is_published"
    ITG = "itg"
    ITG_ID = "itg_id"
    KEY = "key"
    LABEL = "label"
    LABELS = "labels"
    LAST_IP = "last_ip"
    LAST_NAME = "last_name"
    LDAPDN = "ldapDn"
    LDAP_CONFIGURATION = "ldap_configuration"
    LEVEL = "level"
    LINK = "link"
    MANAGEMENT_ID = "management_id"
    MANAGEMENT_IP = "management_ip"
    MANAGEMENTID = "managementId"
    MANAGEMENT_NAME = "management_name"
    MANAGEMENT_TYPE = "management_type"
    MASK = "mask"
    MATCH_FOR_ANY = "match_for_any"
    MATCH_RULE = "match_rule"
    MATRIX_CELL_VIOLATION = "matrix_cell_violation"
    MAX = "max"
    MAX_PROTOCOL = "max_protocol"
    MAX_VALUE_SOURCE = "max_value_source"
    MAXIP = "maxIp"
    MAX_IP = "max_ip"
    MEMBER = "member"
    MEMBER_OF = "member_of"
    MEMBERS = "members"
    MESSAGE = "message"
    MGMT_ANY = "mgmt_any"
    MGMT = "mgmt"
    MGMTS = "mgmts"
    MGMT_ID = "mgmt_id"
    MGMT_NAME = "mgmt_name"
    MIN = "min"
    MINIP = "minIp"
    MIN_IP = "min_ip"
    MIN_PROTOCOL = "min_protocol"
    MIN_VALUE_SOURCE = "min_value_source"
    MODEL = "model"
    MODIFIED = "modified"
    MODIFIED_OBJECT_NAME = "modified_object_name"
    MODULES_AND_POLICY = "modules_and_policy"
    MULTI_ACCESS_REQUESTS = "multi_access_requests"
    MULTI_GROUP_CHANGE = "multi_group_change"
    MUSTCONTAIN = "mustContain"
    NAME = "name"
    NEGATE = "negate"
    NEGATED = "negated"
    NETMASK = "netmask"
    NETWORK = "network"
    NETWORK_ADDRESS = "network_address"
    NETWORK_COLLECTION = "network_collection"
    NETWORK_IP = "network_ip"
    NETWORK_ITEM = "network_item"
    NETWORK_ITEMS = "network_items"
    NETWORK_MASK = "network_mask"
    NETWORK_NAME = "network_name"
    NETWORK_OBJECT = "network_object"
    NETWORK_OBJECTS = "network_objects"
    NETWORKS = "networks"
    NETWORK_UID = "network_uid"
    NEW_REVISION = "new_revision"
    NEW_RULE = "new_rule"
    NEW_RULES = "new_rules"
    NEW_RULES_VIOLATED_TRAFFIC = "new_rules_violated_traffic"
    NEXT_HOP_IP = "next_hop_ip"
    NOT_ALLOWED_SERVICE = "not_allowed_service"
    NOT_ALLOWED_SERVICES = "not_allowed_services"
    NOTES = "notes"
    NUMBER = "number"
    OBJECT = "object"
    OBJECT_DETAILS = "object_details"
    OBJECT_NAME = "object_name"
    OBJECT_TYPE = "object_type"
    OBJECT_UID = "object_UID"
    OFFLINE = "offline"
    OFFLINE_DEVICE = "offline_device"
    OLD_REVISION = "old_revision"
    OLD_RULE = "old_rule"
    OLD_RULES = "old_rules"
    OLD_RULES_VIOLATED_TRAFFIC = "old_rules_violated_traffic"
    OPEN_TICKETS = "open_tickets"
    OPTIONS = "options"
    OPTION = "option"
    ORDER = "order"
    ORIGIN = "origin"
    ORIGINAL_INSTANCE_ID = "original_instance_id"
    OUTGOING_INTERFACE_NAME = "outgoing_interface_name"
    OUT_OF_OFFICE_FROM = "out_of_office_from"
    OUT_OF_OFFICE_UNTIL = "out_of_office_until"
    OWNER = "owner"
    OWNER_USER_ID = "owner_user_id"
    OWNER_DISPLAY_NAME = "owner_display_name"
    PATH = "path"
    PARTIAL_LIST = "partial_list"
    PARTICIPANT_USERNAME = "participant_username"
    PARTICIPANT_ID = "participant_id"
    PARTICIPANTS = "participants"
    PAYLOAD = "payload"
    PHONE = "phone"
    POLICIES = "policies"
    POLICY = "policy"
    POLICYPACKAGE = "policyPackage"
    POLICY_ANALYSIS_QUERY_RESULT = "policy_analysis_query_result"
    POLICY_NAME = "policy_name"
    POLICY_CONTROL_NAME = "policy_control_name"
    POOL_MEMBER = "pool_member"
    POOL_MEMBERS = "pool_members"
    PORT = "port"
    PORT_FROM = "port_from"
    PERCENT_IMPLEMENTED = "percent_implemented"
    PERFORMED_BY = "performed_by"
    PRECEDENCE = "precedence"
    PREDEFINED_NAME = "predefined_name"
    PREDEFINED_SERVICE_ID = "predefined_service_id"
    PREDEFINED_SERVICE_NAME = "predefined_service_name"
    PREDEFINED_SERVICE_RANGE = "predefined_service_range"
    PREDEFINED_SERVICE_RANGES = "predefined_service_ranges"
    PREFIX = "prefix"
    PRIMARY = "primary"
    PRIORITY = "priority"
    PRODUCTS = "products"
    PROTOCOL = "protocol"
    PUSH_STATUS = "push_status"
    QUERY_PARAMS = "query_params"
    RANGE_FIRST_IP = "range_first_ip"
    RANGE_LAST_IP = "range_last_ip"
    READY = "ready"
    READ_ONLY = "read_only"
    REASON = "reason"
    REASSIGN_TASK_COMMENT = "reassign_task_comment"
    RECIPIENT = "recipient"
    RECIPIENTS = "recipients"
    RECIPIENTS_ANY = "recipients_any"
    RECORD_SET = "record_set"
    REDONE = "redone"
    REDO_STEP_COMMENT = "redo_step_comment"
    REFERENCED = "referenced "
    REGION = "region"
    REMEDIATION = "remediation"
    REPORT = "report"
    REPORTS = "reports"
    RESULT = "result"
    REQUESTED_BY = "requested_by"
    REQUESTER = "requester"
    REQUESTER_ID = "requester_id"
    REVISION = "revision"
    REVISION_NUMBER = "revision_number"
    REVISION_ID = "revision_id"
    REVISIONID = "revisionId"
    REVISIONS = "revisions"
    RISK = "risk"
    RISK_ANALYSIS_RESULT = "risk_analysis_result"
    ROLE = "role"
    ROLES = "roles"
    ROUTE = "route"
    ROUTES = "routes"
    RULE = "rule"
    RULES = "rules"
    RULE_COUNT = "rule_count"
    RULE_ID = "rule_id"
    RULE_NUMBER = "rule_number"
    RULE_VIOLATED_TRAFFIC = "rule_violated_traffic"
    RULENUMBER = "ruleNumber"
    RULE_PROPERTIES = "rule_properties"
    RULE_PROPERTY = "rule_property"
    RULE_PROPERTIES_VIOLATIONS = "rule_properties_violations"
    RULE_PROPERTY_VIOLATION = "rule_property_violation"
    RULE_TEXT = "textual_rep"
    SECURE_APP_APPLICATION = "secure_app_application"
    SCORE = "score"
    SCHEDULING = "scheduling"
    SECURITY_GROUP = "security_group"
    SECURITY_GROUPS = "security_groups"
    SECURITY_POLICY = "securityPolicy"
    SECURITY_POLICY_LIST = "SecurityPolicyList"
    SECURITY_POLICY_DEVICE_VIOLATIONS = "security_policy_device_violations"
    SECURITY_POLICY_EXCEPTION = "security_policy_exception"
    SECURITY_POLICY_EXCEPTION_LIST = "security_policy_exception_list"
    SECURITY_POLICY_VIOLATION = "security_policy_violation"
    SECURITY_POLICY_VIOLATIONS = "security_policy_violations"
    SECURITY_REQUIREMENT = "security_requirement"
    SECURITY_REQUIREMENTS = "security_requirements"
    SECURITY_RULE_COUNT = "security_rule_count"
    SECURITY_ZONE_MATRIX = "security_zone_matrix"
    SELECTED_OPTION = "selected_option"
    SELECTED_OPTIONS = "selected_options"
    SELECTION = "selection"
    SEND_EMAIL = "send_email"
    SERVER = "server"
    SERVERS = "servers"
    SERVICE = "service"
    SERVICES = "services"
    SERVICE_COLLECTION = "service_collection"
    SERVICE_ITEM = "service_item"
    SERVICE_ITEMS = "service_items"
    SERVICE_NAME = "service_name"
    SERVICE_UID = "service_uid"
    SEVERITY = "severity"
    SHADOWED_RULE = "shadowed_rule"
    SHADOWED_RULES = "shadowed_rules"
    SHADOWED_RULES_CLEANUP = "shadowed_rules_cleanup"
    SHADOWING_RULES = "shadowing_rules"
    SHARED = "shared"
    SKIPPED = "skipped"
    SLA_OUTCOME = "sla_outcome"
    SLA_STATUS = "sla_status"
    SOURCE = "source"
    SOURCES = "sources"
    SOURCE_DOMAIN = "source_domain"
    SOURCE_NETWORK_COLLECTION = "source_network_collection"
    SOURCES_IN_ZONE = "sources_in_zone"
    SOURCENETWORKS = "sourceNetworks"
    SOURCESERVICES = "sourceServices"
    SRC = "src"
    SRC_NETWORK = "src_network"
    SRC_NETWORKS = "src_networks"
    SRC_NETWORKS_NEGATED = "src_networks_negated"
    SRC_SERVICES_NEGATED = "src_services_negated"
    STATUS = "status"
    STEP = "step"
    STEP_NAME = "step_name"
    STEPS = "steps"
    SUBNET_MASK = "subnet_mask"
    SUBJECT = "subject"
    SUGGESTIONS_PER_BINDING = "suggestions_per_binding"
    SUGGESTIONS_PER_DEVICE = "suggestions_per_device"
    TAG = "tag"
    TAG_SERVERS = "tag_servers"
    TAGS = "tags"
    TAGS_SERVERS = "tags_servers"
    TARGET = "target"
    TARGETS = "targets"
    TASK = "task"
    TASK_NAME = "task_name"
    TASKS = "tasks"
    TECH_OWNER = "tech_owner"
    TESTDEF = "testDef"
    TESTDEFUID = "testDefUid"
    TESTPARAMS = "testParams"
    TEST_PRODUCTS = "test_products"
    TESTUID = "testUid"
    TEXT = "text"
    TEXT_AREA = "text_area"
    TEXT_FIELD = "text_field"
    TICKET = "ticket"
    TICKETS = "tickets"
    TICKET_HISTORY_ACTIVITIES = "ticket_history_activities"
    TICKET_HISTORY_ACTIVITY = "ticket_history_activity"
    TICKET_ID = "ticket_id"
    TICKETCR = "ticketCr"
    TIME = "time"
    TIMEOUT = "timeout"
    TOPOLOGY = "topology"
    TO = "to"
    TO_DOMAIN = "to_domain"
    TO_ZONE = "to_zone"
    TOTAL = "total"
    TRACK = "track"
    TRAFFIC_RANGE = "traffic_range"
    TYPE = "type"
    TYPE_ON_DEVICE = "type_on_device"
    UID = "uid"
    UNAUTHORIZED_OPENED_ACCESS = "unauthorized_opened_access"
    UNAUTHORIZED_CLOSED_ACCESS = "unauthorized_closed_access"
    UNIQUE_ACTIVE_IN_ITG = "unique_active_in_itg"
    URL = "url"
    USER = "user"
    USER_ID = "user_id"
    USERS = "users"
    USAGE_MODE = "usage_mode"
    VALUE = "value"
    VENDOR = "vendor"
    VENDOR_NAME = "vendor_name"
    VERIFIED = "verified"
    VERIFICATION_STATUS = "verification_status"
    VERIFIER_BINDING = "verifier_binding"
    VERIFIER_BINDINGS = "verifier_bindings"
    VERIFIER_RESULT = "verifier_result"
    VERIFIER_TARGET = "verifier_target"
    VERIFIER_TARGETS = "verifier_targets"
    VERIFIER_WARNING = "verifier_warning"
    VERSION_ID = "version_id"
    VISIBILITY = "visibility"
    VIOLATED_TRAFFIC = "violated_traffic"
    VIOLATING_SERVICE = "violating_service"
    VIOLATING_SERVICES = "violating_services"
    VIOLATION = "violation"
    VIOLATIONS = "violations"
    VIOLATING_OBJECT = "violating_object"
    VIOLATING_RULE = "violating_rule"
    VIOLATING_RULES = "violating_rules"
    VIRTUAL_IP = "virtual_ip"
    VIRTUAL_ROUTER = "virtual_router"
    VM_INSTANCE = "vm_instance"
    VM_INSTANCES = "vm_instances"
    VPN = "vpn"
    WORKFLOW = "workflow"
    ZONE = "zone"
    ZONES = "zones"
    ZONE_ID = "zone_id"
    ZONEID = "zoneId"
    ZONE_ENTRY = "zone_entry"
    ZONE_ENTRIES = "zone_entries"
    ZONE_NAME = "zone_name"
    ZONE_NAME_IN_PARENT = "zone_name_in_parent"
    ZONE_TO_ZONE_SECURITY_REQUIREMENT = "zone_to_zone_security_requirement"


@enum.unique
class SeverityLevels(enum.Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    @staticmethod
    def from_string(level_string):
        """
        Get enum from string
        :type level_string: str
        :return:
        """
        try:
            level = [level for level in (SeverityLevels.CRITICAL, SeverityLevels.HIGH,
                                         SeverityLevels.MEDIUM, SeverityLevels.LOW) if level.value == level_string][0]
        except IndexError:
            raise ValueError("String {} doesn't represent any of the severity levels".format(level_string))
        else:
            return level

    def _compare_with_enum(self, level):
        """
        Check if greater than other provided violation severity level
        :type level: SeverityLevels
        :return:
        """
        if self == SeverityLevels.CRITICAL and level == SeverityLevels.CRITICAL:
            return False
        elif self == SeverityLevels.HIGH and level in (SeverityLevels.HIGH, SeverityLevels.CRITICAL):
            return False
        elif self == SeverityLevels.MEDIUM and level in (SeverityLevels.CRITICAL,
                                                         SeverityLevels.HIGH, SeverityLevels.MEDIUM):
            return False
        if self == SeverityLevels.LOW:
            return False
        return True

    def __gt__(self, level):
        """
        Implementation of greater
        :param level:
        :return:
        """
        if isinstance(level, str):
            level = SeverityLevels.from_string(level)
            return self._compare_with_enum(level)
        elif isinstance(level, SeverityLevels):
            return self._compare_with_enum(level)
        else:
            raise TypeError("Wrong type to compare")
