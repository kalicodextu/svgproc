from xml.etree.ElementTree import ElementTree,Element
 
def read_xml(filePath):
    tree = ElementTree()
    tree.parse(filePath)
    return tree
 
def write_xml(tree, out_path):
    tree.write(out_path, encoding="utf-8",xml_declaration=True)
 
def if_match(node, kv_map):
    # have all given attrs or not
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True
 
def find_nodes(tree, path):
    # get all nodes by path
    return tree.findall(path)
 
def get_node_by_keyvalue(nodelist, kv_map):
    # get all modes by attr's k_v
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes
 
def change_node_properties(nodelist, kv_map, is_delete=False):
    # change node property
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
              node.set(key, kv_map.get(key))
 
def change_node_text(nodelist, text, is_add=False, is_delete=False):
    # change node text
    for node in nodelist:
        if is_add:
            node.text += text
        elif is_delete:
             node.text = ""
        else:
            node.text = text
 
def create_node(tag, property_map, content):
    element = Element(tag, property_map)
    element.text = content
    return element
 
def add_child_node(nodelist, element):
    for node in nodelist:
        node.append(element)
 
def del_node_by_tagkeyvalue(nodelist, tag, kv_map):
    for parent_node in nodelist:
        children = parent_node.getchildren()
        for child in children:
            if child.tag == tag and if_match(child, kv_map):
                parent_node.remove(child)
