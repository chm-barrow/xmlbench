require 'nokogiri'

def parse_and_print_xml(file_path)
  # Open and parse the XML file with external entity support
  xml_file = File.open(file_path)
  document = Nokogiri::XML(xml_file) do |config|
    config.default_xml.norecover.strict
  end
  xml_file.close

  # Recursively print the tags and data
  print_elements(document.root)
end

def print_elements(element, indent = 0)
  indent_space = ' ' * indent
  puts "#{indent_space}<#{element.name}>"

  element.children.each do |child|
    if child.element?
      print_elements(child, indent + 2)
    elsif child.text? && !child.text.strip.empty?
      puts "#{indent_space}  #{child.text.strip}"
    end
  end

  puts "#{indent_space}</#{element.name}>"
end

# Main script execution
if ARGV.length != 1
  puts "Usage: ruby parse_xml_with_entities.rb path/to/your/file.xml"
  exit
end

file_path = ARGV[0]
parse_and_print_xml(file_path)
