require 'rexml/document'

# Function to print XML content recursively
def print_element(element)
  # Print the element's opening tag with its attributes
  puts "#{' '}<#{element.name}#{format_attributes(element)}>"
  
  # Print the element's text content if it has any
  if element.has_text?
    puts "#{' '}#{element.text.strip}"
  end
  
  # Recursively print each child element
  element.elements.each do |child|
    print_element(child)
  end
  
  # Print the element's closing tag
  puts "#{' '}</#{element.name}>"
end

# Function to format attributes for printing
def format_attributes(element)
  return '' if element.attributes.empty?
  ' ' + element.attributes.map { |name, value| "#{name}='#{value}'" }.join(' ')
end

# Check if the file name is given as a command-line argument
if ARGV.length != 1
  puts "Usage: ruby read_xml.rb <file_name>"
  exit
end

file_name = ARGV[0]

# Read and parse the XML file
begin
  xml_content = File.read(file_name)
  document = REXML::Document.new(xml_content)
rescue Errno::ENOENT
  puts "File not found: #{file_name}"
  exit
rescue REXML::ParseException => e
  puts "Failed to parse XML: #{e.message}"
  exit
end

# Print the XML content
print_element(document.root)
