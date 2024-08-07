require 'nokogiri'

class MySAXHandler < Nokogiri::XML::SAX::Document
  def initialize
    @indent = 0
  end

  def start_element(name, attrs = [])
    attributes = attrs.each_slice(2).map { |k, v| "#{k}='#{v}'" }.join(' ')
    attributes = " #{attributes}" unless attributes.empty?
    puts "#{' ' * @indent}<#{name}#{attributes}>"
    @indent += 2
  end

  def characters(string)
    puts "#{' ' * @indent}#{string.strip}" unless string.strip.empty?
  end

  def end_element(name)
    @indent -= 2
    puts "#{' ' * @indent}</#{name}>"
  end
end

# Check if the file name is given as a command-line argument
if ARGV.length != 1
  puts "Usage: ruby sax_parser.rb <file_name>"
  exit
end

file_name = ARGV[0]

begin
  # Read the XML file
  xml_content = File.read(file_name)

  # Parse the XML with the SAX handler
  parser = Nokogiri::XML::SAX::Parser.new(MySAXHandler.new)
  parser.parse(xml_content)

rescue Errno::ENOENT
  puts "File not found: #{file_name}"
rescue Nokogiri::XML::SyntaxError => e
  puts "Failed to parse XML: #{e.message}"
end
