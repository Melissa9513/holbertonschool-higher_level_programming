#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary to an XML file.
    """
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Create tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=False)

    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.
    Returns the reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None

