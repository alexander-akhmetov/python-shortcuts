from subprocess import call


def convert_plist_to_binary(filepath):
    call(['plutil', '-convert', 'binary1', filepath])


def convert_plist_to_xml(filepath):
    call(['plutil', '-convert', 'xml1', filepath])
