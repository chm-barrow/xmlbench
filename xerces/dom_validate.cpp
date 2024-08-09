#include <xercesc/dom/DOM.hpp>
#include <xercesc/dom/DOMLSParser.hpp>
#include <xercesc/dom/DOMImplementation.hpp>
#include <xercesc/dom/DOMImplementationLS.hpp>
#include <xercesc/util/PlatformUtils.hpp>
#include <xercesc/util/XMLString.hpp>
#include <xercesc/sax/SAXException.hpp>
#include <iostream>

XERCES_CPP_NAMESPACE_USE

class MyErrorHandler : public DOMErrorHandler {
public:
    bool handleError(const DOMError& domError) override {
        char* message = XMLString::transcode(domError.getMessage());
        std::cerr << "Error: " << message << std::endl;
        XMLString::release(&message);
        return true;  // Return true to continue processing errors
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
        // Get the DOMImplementation
        DOMImplementation* impl = DOMImplementationRegistry::getDOMImplementation(XMLString::transcode("Core"));

        // Create the DOMLSParser (DOM Load and Save Parser)
        DOMLSParser* parser = impl->createLSParser(DOMImplementationLS::MODE_SYNCHRONOUS, 0);

        // Configure parser for validation
        DOMConfiguration* config = parser->getDomConfig();
        config->setParameter(XMLUni::fgDOMValidate, true);
        config->setParameter(XMLUni::fgXercesSchema, true);
        config->setParameter(XMLUni::fgDOMNamespaces, true);
        config->setParameter(XMLUni::fgXercesSchemaFullChecking, true);

        MyErrorHandler errorHandler;
        config->setParameter(XMLUni::fgDOMErrorHandler, &errorHandler);

        // Parse the XML file
        DOMDocument* doc = parser->parseURI(xmlFile);

        if (doc) {
            std::cout << "XML file validated successfully." << std::endl;
        } else {
            std::cerr << "XML file failed validation." << std::endl;
        }

        parser->release();
    } catch (const XMLException& e) {
        char* message = XMLString::transcode(e.getMessage());
        std::cerr << "XMLException: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    } catch (const DOMException& e) {
        char* message = XMLString::transcode(e.msg);
        std::cerr << "DOMException: " << message << std::endl;
        XMLString::release(&message);
        return 1;
    } catch (const std::exception& e) {
        std::cerr << "Exception: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
