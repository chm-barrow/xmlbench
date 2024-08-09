<?php
// Ensure that the correct number of arguments is passed
if ($argc != 3) {
    echo "Usage: php validate_xml.php <xml_file> <xsd_file>\n";
    exit(1);
}

// Get the XML and XSD file paths from the command-line arguments
$xmlFile = $argv[1];
$xsdFile = $argv[2];

// Check if the XML file exists
if (!file_exists($xmlFile)) {
    echo "Error: XML file '$xmlFile' not found.\n";
    exit(1);
}

// Check if the XSD file exists
if (!file_exists($xsdFile)) {
    echo "Error: XSD file '$xsdFile' not found.\n";
    exit(1);
}

// Load the XML file with SimpleXML
$xml = simplexml_load_file($xmlFile);

// Check if loading was successful
if ($xml === false) {
    echo "Failed to load XML file '$xmlFile'.\n";
    exit(1);
}

// Create a new DOMDocument
$dom = new DOMDocument();

// Load the XML into DOMDocument (which gives more control for validation)
$dom->loadXML($xml->asXML());

// Validate the XML against the XSD schema
if ($dom->schemaValidate($xsdFile)) {
    echo "XML is valid.\n";
} else {
    echo "XML is not valid.\n";
}
?>
