<?php
libxml_use_internal_errors(true); // Enable user error handling

$xml = new DOMDocument();
$xml->resolveExternals = true;    // Allow resolution of external entities
$xml->validateOnParse = true;     // Enable validation on parse
$xml->load('../samples/simple_dtd.xml');

if ($xml->validate()) {
    echo "XML is valid.\n";
} else {
    echo "XML is not valid.\n";
    $errors = libxml_get_errors();
    foreach ($errors as $error) {
        echo "Error: " . $error->message . "\n";
    }
    libxml_clear_errors();
}
?>
