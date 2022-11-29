CYRILLIC_TO_LATIN = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya', 'і': 'i', 'є': 'e', 'ї': 'i',
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 'З': 'Z', 'И': 'I',
    'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': '', 'Ы': 'Y', 'Ь': '',
    'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya', 'І': 'I', 'Є': 'E', 'Ї': 'I'
}

FILE_TYPES = {
    'images': ['jpeg', 'png', 'jpg', 'svg', 'webp'],
    'video': ['avi', 'mp4', 'mov', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xls', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'mov', 'amr'],
    'archives': ['zip', 'gz', 'tar']
}

COMMANDS_HELP = [
    ' - hello',
    '____________________________________________________',
    ' - add contact <name> ',
    ' - remove contact <name>  |  delete contact <name>',
    ' - change contact <name old> <name new>',
    '____________________________________________________',
    ' - add address <name> <address>',
    ' - remove address <name>  |  delete address <name>',
    ' - change address <name> <address>',
    '____________________________________________________',
    ' - add email <name> <email>',
    ' - remove email <name>  |  delete email <name>',
    ' - change email <name> <email>',
    '____________________________________________________',
    ' - add birthday <name> <birthday>',
    ' - remove birthday <name>  |  delete birthday <name>',
    ' - change birthday <name> <birthday>',
    '____________________________________________________',
    ' - add phone <name> <phone>',
    ' - remove phone <name> <phone>  |  delete phone <name> <phone>',
    ' - change phone <name> <old phone> <new phone>',
    '____________________________________________________',
    ' - show all contacts',
    ' - show contact <name>',
    ' - show birthdays <days>',
    ' - find contact <keys characters>',
    '____________________________________________________',
    ' - add note <title>',
    ' - remove note <title>  |  delete note <title>',
    ' - change note <old title> <new title>',
    '____________________________________________________',
    ' - add text <title> <text>',
    ' - remove text <title>  |  delete text <title>',
    ' - change text <title> <text>',
    '____________________________________________________',
    ' - add tag <name> <tag>',
    ' - remove tag <name> <tag>  |  delete tag <name> <tag>',
    ' - change tag <name> <old tag> <new tag>',
    '____________________________________________________',
    ' - show all notes',
    ' - show note <title>',
    ' - find note <keys characters> {-r (for reverse sort)}',
    ' - find tag <tag> {-r (for reverse sort)}',
    ' - clear notes',
    '____________________________________________________',
    ' - sort folder <folder>',
    ' - goodbye || close || exit || quit'
]

HEADER_ADDRESSBOOK = {
    'name': 'Name',
    'address': 'Address',
    'email': 'Email',
    'birthday': 'Birthday',
    'phones': 'Phone'
}