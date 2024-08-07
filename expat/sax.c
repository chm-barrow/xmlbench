#include <stdio.h>
#include <expat.h>


// Starting tag handler.
void XMLCALL startElement(void *userData, const char *name, const char **atts) {
    printf("Start element: %s\n", name);
}

// Ending tag handler.
void XMLCALL endElement(void *userData, const char *name) {
    printf("End element: %s\n", name);
}

// Data handler.
void XMLCALL characterData(void *userData, const char *s, int len) {
    printf("Character data: %.*s\n", len, s);
}

int main(void) {
    char buf[BUFSIZ];
    size_t len;
    int done;

    // Parser initialisation.
    XML_Parser parser = XML_ParserCreate(NULL);
    if (!parser) {
        fprintf(stderr, "Couldn't allocate memory for parser\n");
        return 1;
    }

    // Initialisation of tag and data handlers.
    XML_SetElementHandler(parser, startElement, endElement);
    XML_SetCharacterDataHandler(parser, characterData);

    // Parsing.
    while ((len = fread(buf, 1, sizeof(buf), stdin)) > 0) {
        done = len < sizeof(buf);

        if (XML_Parse(parser, buf, len, done) == XML_STATUS_ERROR) {
            fprintf(stderr, "Parse error at line %lu:\n%s\n",
                    XML_GetCurrentLineNumber(parser),
                    XML_ErrorString(XML_GetErrorCode(parser)));
            XML_ParserFree(parser);
            return 1;
        }

        if (done) break;
    }

    XML_ParserFree(parser);
    return 0;
}