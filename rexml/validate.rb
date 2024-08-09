require 'nokogiri'

def validate_xml(xml_path, xsd_path)
  # Read and parse the XML and XSD files
  xml_doc = Nokogiri::XML(File.read(xml_path))
  xsd = Nokogiri::XML::Schema(File.read(xsd_path))

  # Validate the XML against the schema
  errors = xsd.validate(xml_doc)

  if errors.empty?
    puts "The XML document is valid."
  else
    puts "The XML document is invalid:"
    errors.each do |error|
      puts error.message
    end
  end
end

# Main script execution
if ARGV.length != 2
  puts "Usage: ruby validate_xml.rb path/to/your/file.xml path/to/your/schema.xsd"
  exit
end

xml_path = ARGV[0]
xsd_path = ARGV[1]

validate_xml(xml_path, xsd_path)
