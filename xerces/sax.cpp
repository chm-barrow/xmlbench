#include <xercesc/sax2/DefaultHandler.hpp>
#include <xercesc/sax2/XMLReaderFactory.hpp>
#include <xercesc/util/PlatformUtils.hpp>
#include <xercesc/util/XMLString.hpp>
#include <iostream>

XERCES_CPP_NAMESPACE_USE

class MySAXHandler : public DefaultHandler {
public:
    MySAXHandler() = default;
    ~MySAXHandler() override = default;

    void startElement(const XMLCh* const uri,
                      const XMLCh* const localname,
                      const XMLCh* const qname,
                      const Attributes& attrs) override {
        char* elementName = XMLString::transcode(localname);
        std::cout << "Start element: " << elementName << std::endl;
        XMLString::release(&elementName);
    }

    void endElement(const XMLCh* const uri,
                    const XMLCh* const localname,
                    const XMLCh* const qname) override {
        char* elementName = XMLString::transcode(localname);
        std::cout << "End element: " << elementName << std::endl;
        XMLString::release(&elementName);
    }

    void characters(const XMLCh* const chars, const XMLSize_t length) override {
        char* text = XMLString::transcode(chars);
        std::cout << "Character data: " << text << std::endl;
        XMLString::release(&text);
    }

    void error(const SAXParseException& e) override {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "Error: " << message << std::endl;
        XMLString::release(&message);
    }

    void fatalError(const SAXParseException& e) override {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "Fatal Error: " << message << std::endl;
        XMLString::release(&message);
    }

    void warning(const SAXParseException& e) override {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "Warning: " << message << std::endl;
        XMLString::release(&message);
    }
};

int main(int argc, char* argv[]) {
    try {
        XMLPlatformUtils::Initialize();
    } catch (const XMLException& e) {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "Error during Xerces initialization: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    }

    struct XercesGuard {
        ~XercesGuard() { XMLPlatformUtils::Terminate(); }
    } guard;

    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <xml-file>" << std::endl;
        return 1;
    }
    const char* xmlFile = argv[1];

    try {
        SAX2XMLReader* parser = XMLReaderFactory::createXMLReader();
        MySAXHandler handler;
        parser->setContentHandler(&handler);
        parser->setErrorHandler(&handler);

        parser->parse(xmlFile);
        delete parser;
    } catch (const XMLException& e) {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "XMLException: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    } catch (const SAXException& e) {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "SAXException: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
