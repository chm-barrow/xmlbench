<?php
// Function to recursively print XML elements
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
    die("Incorrect parameters specified.\n");
}

// Get the file path from the command-line argument
$filePath = $argv[1];

$error = libxml_use_internal_errors(false);

// Load the XML file
$xml = simplexml_load_file($filePath) or die("Error.\n");

// Print the XML content
printXMLElements($xml,1);
?>
