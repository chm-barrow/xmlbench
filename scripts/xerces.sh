#!/bin/bash

cd ../xerces
OUT="../output/xerces/"

# Valid document tests.
rm ../output/xerces/dom/valid/*.txt ../output/xerces/sax/valid/*.txt ../output/xerces/xxe/valid/*.txt
INPUT="../samples/valid/"
for i in {001..060};
do
	./dom ${INPUT}${i}.xml >> ${OUT}dom/valid/${i}.txt 2>&1
	./sax ${INPUT}${i}.xml >> ${OUT}sax/valid/${i}.txt 2>&1
	./dom_xxe ${INPUT}${i}.xml >> ${OUT}xxe/valid/${i}.txt 2>&1
done

# Not well-formed tests.
rm ../output/xerces/dom/not-wf/*.txt ../output/xerces/sax/not-wf/*.txt ../output/xerces/xxe/not-wf/*.txt
INPUT="../samples/not-wf/"
for i in {001..055};
do
	./dom  ${INPUT}${i}.xml >> ${OUT}dom/not-wf/${i}.txt 2>&1
	./sax ${INPUT}${i}.xml >> ${OUT}sax/not-wf/${i}.txt 2>&1
	./dom_xxe ${INPUT}${i}.xml >> ${OUT}xxe/not-wf/${i}.txt 2>&1
done

# Injections tests.
INPUT="../samples/injections/"
rm ../output/xerces/dom/other/*.txt ../output/xerces/sax/other/*.txt ../output/xerces/xxe/other/*.txt
for i in {001..005}
do
	timeout 2s ./dom  ${INPUT}${i}.xml >> ${OUT}dom/other/${i}.txt 2>&1
	timeout 2s ./sax  ${INPUT}${i}.xml >> ${OUT}sax/other/${i}.txt 2>&1
	timeout 2s ./dom_xxe  ${INPUT}${i}.xml >> ${OUT}xxe/other/${i}.txt 2>&1
done

# Valid schemas tests.
INPUT="../samples/xerces-schemas/schemas-valid/"
rm ../output/xerces/dom/valid-schemas/*.txt ../output/xerces/sax/valid-schemas/*.txt
for i in {001..005}
do
	./validate ${INPUT}${i}.xml >> ${OUT}dom/valid-schemas/${i}.txt 2>&1
	./sax ${INPUT}${i}.xml >> ${OUT}sax/valid-schemas/${i}.txt 2>&1
done

# Invalid schemas tests.
INPUT="../samples/xerces-schemas/schemas-invalid/"
rm ../output/xerces/dom/invalid-schemas/*.txt ../output/xerces/sax/invalid-schemas/*.txt
for i in {001..005}
do
	./validate ${INPUT}${i}.xml >> ${OUT}dom/invalid-schemas/${i}.txt 2>&1
	./sax ${INPUT}${i}.xml >> ${OUT}sax/invalid-schemas/${i}.txt 2>&1
done

