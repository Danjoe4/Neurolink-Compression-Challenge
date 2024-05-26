#include <stdio.h>

void processRawBits(const char* inputFile, const char* outputFile) {
    FILE* input = fopen(inputFile, "rb");
    FILE* output = fopen(outputFile, "wb");

    if (input == NULL || output == NULL) {
        printf("Error opening files.\n");
        return;
    }

    unsigned char buffer;
    while (fread(&buffer, sizeof(unsigned char), 1, input) == 1) {
        fwrite(&buffer, sizeof(unsigned char), 1, output);
    }

    fclose(input);
    fclose(output);
}

int main(int argc, char* argv[]) {
    if (argc != 3) {
        printf("Usage: %s <input_file> <output_location>\n", argv[0]);
        return 1;
    }

    const char* inputFile = argv[1];
    const char* outputFile = argv[2];

    processRawBits(inputFile, outputFile);

    return 0;
}