# Word format - Direct references
format_word = {
    '.docx': int(16),
    '.doc': int(0),
    '.rtf': int(6),
    '.odt': int(23),
    '.txt': int(2),
    '.pdf': int(17),
    '.xml': int(11),
}

# Commuter format control
format_commute = {
    1: '.docx',
    2: '.doc',
    3: '.rtf',
    4: '.pdf',
    5: '.odt',
    6: '.txt',
    7: '.xml',
}

# Exceptions strings
exception_type = {
    'generic': "\nSomething went wrong.",
    'file_not_found': "\nFile not found.",
    'os': "\nFile name error.",
    'permission': "\nPermission not granted. File open or locked.",
    'index': "\nIndexation error.",
    'format': "\nFormat out error.",
    'value': "\nValue error.",
    'package': "\nPackage error.",
    'type': "\nType error."
}

# Info response
message_info = {
    'conversion_not': "\nNo conversion required.",
    'format_type_not': "\nFormat type not designed.",
    'docx_success': "\nDOCx standardized."
}

# Publication format - Standardize driver
format_diagramming = {
    'company_employer_title_flowing': 1,
    'name_flowing': 2,
    'flowing': 3,
    'hash_DOU': 4,
}

urls = {
    'api': "http://api:8003/create_publication",
}
