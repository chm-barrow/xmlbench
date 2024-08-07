#include <stdio.h>
#include <expat.h>

void XMLCALL startElement(void *userData, const char *name, const char **atts) {
    printf("Start element: %s\n", name);
}

void XMLCALL endElement(void *userData, const char *name) {
    printf("End element: %s\n", name);
}

void XMLCALL characterData(void *userData, const char *s, int len) {
    printf("Character data: %.*s\n", len, s);
}

int XMLCALL externalEntityRefHandler(XML_Parser parser,
                                     const XML_Char *context,
                                     const XML_Char *base,
                                     const XML_Char *systemId,
                                     const XML_Char *publicId) {

    FILE *file = fopen(systemId + 7, "r");  // Skip "file://"
    if (!file) {
        fprintf(stderr, "Couldn't open external entity file: %s\n", systemId + 7);
        return XML_STATUS_ERROR;
    }

    char buf[BUFSIZ];
    size_t len;
    int done;

    XML_Parser entityParser = XML_ExternalEntityParserCreate(parser, context, NULL);
    if (!entityParser) {
        fclose(file);
        return XML_STATUS_ERROR;
    }

    do {
        len = fread(buf, 1, sizeof(buf), file);
        if (ferror(file)) {
            fprintf(stderr, "Read error in external entity file\n");
            fclose(file);
            XML_ParserFree(entityParser);
            return XML_STATUS_ERROR;
        }
        done = feof(file);

        if (XML_Parse(entityParser, buf, len, done) == XML_STATUS_ERROR) {
            fprintf(stderr, "Parse error in external entity file at line %lu:\n%s\n",
                    XML_GetCurrentLineNumber(entityParser),
                    XML_ErrorString(XML_GetErrorCode(entityParser)));
            fclose(file);
            XML_ParserFree(entityParser);
            return XML_STATUS_ERROR;
        }
    } while (!done);

    fclose(file);
    XML_ParserFree(entityParser);
    return XML_STATUS_OK;
}

XML_Parser createParser() {
    XML_Parser parser = XML_ParserCreate(NULL);
    if (!parser) {
        fprintf(stderr, "Couldn't allocate memory for parser\n");
        return NULL;
    }

    XML_SetElementHandler(parser, startElement, endElement);
    XML_SetCharacterDataHandler(parser, characterData);
    XML_SetParamEntityParsing(parser, XML_PARAM_ENTITY_PARSING_ALWAYS);
    XML_SetExternalEntityRefHandler(parser, externalEntityRefHandler);

    return parser;
}

int main(int argc, char * argv[] ) {
    XML_Parser parser = createParser();
    if (!parser) {
        return 1;
    }
    
    if (argc != 2){
	    printf("Please specify the file as a parameter.");
	    return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        fprintf(stderr, "Couldn't open file\n");
        XML_ParserFree(parser);
        return 1;
    }

    char buf[BUFSIZ];
    size_t len;
    int done;

    do {
        len = fread(buf, 1, sizeof(buf), file);
        if (ferror(file)) {
            fprintf(stderr, "Read error\n");
            fclose(file);
            XML_ParserFree(parser);
            return 1;
        }
        done = feof(file);

        if (XML_Parse(parser, buf, len, done) == XML_STATUS_ERROR) {
            fprintf(stderr, "Parse error at line %lu, column %lu:\n%s\n",
                    XML_GetCurrentLineNumber(parser),
                    XML_GetCurrentColumnNumber(parser),
                    XML_ErrorString(XML_GetErrorCode(parser)));
            fclose(file);
            XML_ParserFree(parser);
            return 1;
        }
    } while (!done);

    fclose(file);
    XML_ParserFree(parser);
    return 0;
}
