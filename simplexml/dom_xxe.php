<?php
// Enable error reporting for better debugging
//error_reporting(E_ALL);
//ini_set('display_errors', 1);

// Function to recursively print XML elements
// function printXMLElements($xml, $indent = 0) {
//     foreach ($xml->children() as $child) {
//         if ($child->count() == 0) {
//             echo str_repeat(" ", $indent) . $child->getName() . ": " . $child . "\n";
//         } else {
//             echo str_repeat(" ", $indent) . $child->getName() . ":\n";
//             printXMLElements($child, $indent + 2);
//         }
//     }
// }

function printXMLElements($xml, $indent = 0) {
    // Iterate through each child of the current XML element
    foreach ($xml->children() as $child) {
	// Print the element name and value if it has no children
	echo "<" . $xml->getName() . ">\n";
        if ($child->count() == 0) {
            echo str_repeat(" ", $indent) . "<" . $child->getName() . ">" . $child . "</" . $child->getName() . ">\n";
        } else {
            // Print the element name and recurse into its children
            echo str_repeat(" ", $indent) . $child->getName() . ":\n";
            printXMLElements($child, $indent + 2);
	}
	echo "</" . $xml->getName() . ">\n";
    }
}

// Check if the file path is provided as a command-line argument
if ($argc != 2) {
    die("Usage: php print_xml_generic.php <path_to_xml_file>\n");
}

// Get the file path from the command-line argument
$filePath = $argv[1];

// Load the XML file with LIBXML_NOENT to include external entities
libxml_disable_entity_loader(false); // Enable loading external entities
libxml_use_internal_errors(true); // Disables error output
$xml = simplexml_load_file($filePath, 'SimpleXMLElement', LIBXML_NOENT) or die("Error.\n");

// Print the XML content
printXMLElements($xml);
?>
