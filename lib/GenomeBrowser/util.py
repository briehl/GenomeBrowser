import re
from Workspace.WorkspaceClient import Workspace

def test_reference(ref):
    """
    Tests the given ref string to make sure it conforms to the expected
    object reference format. Returns True if it passes, False otherwise.
    """
    obj_ref_regex = re.compile('^(?P<wsid>\d+)\/(?P<objid>\d+)(\/(?P<ver>\d+))?$')
    if not obj_ref_regex.match(ref):
        return False
    return True

def test_reference_type(ref, allowed_types, ws_url):
    """
    Tests whether the given object refrence is one of the allowed types.
    Specifically, it tests whether the list of allowed_types strings is a substring
    of the ref object's name.
    E.g. if ".Genome" is an allowed type, it'll pass if the object is a "KBaseGenomes.Genome"
    """
    ws = Workspace(ws_url)
    info = ws.get_object_info3({'objects': [{'ref': ref}]}).get('infos')[0]
    passes = False
    for t in allowed_types:
        if t in info[2]:
            passes = True
    return passes