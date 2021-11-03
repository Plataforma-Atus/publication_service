# Formats - Driver references
formats = {"word": {
    '.docx': int(16),
    '.doc': int(0),
    '.rtf': int(6),
    '.odt': int(23),
    '.txt': int(2),
    '.pdf': int(17),
    '.xml': int(11),
},
    "font": {
        1: str('Arial'),
        2: str('Times New Roman'),
        3: str('Helvetica'),
        4: str('Verdana'),
        5: str('Calibri'),
        6: str('Arial Narrow'),
},
    "commute": {
        1: str('.docx'),
        2: str('.doc'),
        3: str('.rtf'),
        4: str('.pdf'),
        5: str('.odt'),
        6: str('.txt'),
        7: str('.xml'),
    },    
    "content": {
        'company_employer_title_flowing': int(1),
        'name_flowing': int(2),
        'flowing': int(3),
        'hash_DOU': int(4),
    },
    "http": {
        'json': "application/json",
    }
}

# Console messages - Driver references
message = {"info": {
           'conversion_not': "\nNo conversion required.",
           'format_type_not': "\nFormat type not designed.",
           'docx_success': "\nDOCx standardized.",
           'process_success': "\nSuccess!",
           'standard_start': "\nStandardize start."
},
    "exception": {
        'generic': "\nSomething went wrong.",
        'file_not_found': "\nFile not found.",
        'os': "\nFile name error.",
        'permission': "\nPermission not granted. File open or locked.",
        'index': "\nIndexation error.",
        'format': "\nFormat out error.",
        'value': "\nValue error.",
        'package': "\nPackage error.",
        'type': "\nType error.",
        'format_allowed': "\nFormat not allowed."
    },
    "http": {
        '404': "\nSomething was wrong...",
    }
}

# Paths - Driver references
paths = {'poppler': r"C:\Program Files (x86)\poppler-0.68.0\bin",
         'documents': r"documents/",
         'model': r"documents/model/default.docx",
         }
