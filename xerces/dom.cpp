#include <xercesc/util/PlatformUtils.hpp>
#include <xercesc/parsers/XercesDOMParser.hpp>
#include <xercesc/dom/DOM.hpp>
#include <xercesc/sax/HandlerBase.hpp>
#include <xercesc/util/XMLString.hpp>
#include <iostream>

using namespace xercesc;

// Helper function to print the XML document recursively
void printElement(DOMElement* element, int indent = 0) {
    char* tagName = XMLString::transcode(element->getTagName());
    std::cout << std::string(indent, ' ') << "<" << tagName;

    // Print attributes
    DOMNamedNodeMap* attributes = element->getAttributes();
    for (XMLSize_t i = 0; i < attributes->getLength(); ++i) {
        DOMAttr* attr = dynamic_cast<DOMAttr*>(attributes->item(i));
        char* attrName = XMLString::transcode(attr->getName());
        char* attrValue = XMLString::transcode(attr->getValue());
        std::cout << " " << attrName << "=\"" << attrValue << "\"";
        XMLString::release(&attrName);
        XMLString::release(&attrValue);
    }
    std::cout << ">";

    // Print children
    DOMNodeList* children = element->getChildNodes();
    bool hasElementChildren = false;
    for (XMLSize_t i = 0; i < children->getLength(); ++i) {
        DOMNode* child = children->item(i);
        if (child->getNodeType() == DOMNode::TEXT_NODE) {
            char* textContent = XMLString::transcode(child->getNodeValue());
            std::cout << textContent;
            XMLString::release(&textContent);
        } else if (child->getNodeType() == DOMNode::ELEMENT_NODE) {
            hasElementChildren = true;
            std::cout << std::endl;
            printElement(dynamic_cast<DOMElement*>(child), indent + 1);
        }
    }

    if (hasElementChildren) {
        std::cout << std::string(indent, ' ');
    }

    std::cout << "</" << tagName << ">" << std::endl;
    XMLString::release(&tagName);
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <XML file>" << std::endl;
        return 1;
    }

    const char* xmlFile = argv[1];

    try {
        // Initialize the Xerces-C++ XML system
        XMLPlatformUtils::Initialize();
    } catch (const XMLException& e) {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "Error during initialization: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    }

    // Create a DOM parser
    XercesDOMParser* parser = new XercesDOMParser();
    ErrorHandler* errHandler = (ErrorHandler*) new HandlerBase();
    parser->setErrorHandler(errHandler);
    parser->setValidationScheme(XercesDOMParser::Val_Never);
    parser->setLoadExternalDTD(false);

    try {
        // Parse the XML file
        parser->parse(xmlFile);
        DOMDocument* doc = parser->getDocument();
        DOMElement* root = doc->getDocumentElement();
        printElement(root);
    } catch (const XMLException& e) {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "XML Exception: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    } catch (const DOMException& e) {
        char* message = XMLString::transcode(e.msg);
        std::cerr << "DOM Exception: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    } catch (...) {
        std::cerr << "Unexpected Exception" << std::endl;
        return 1;
    }

    // Clean up
    delete parser;
    delete errHandler;

    // Terminate the Xerces-C++ XML system
    XMLPlatformUtils::Terminate();

    return 0;
}