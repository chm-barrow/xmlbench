#!/bin/bash

cd ../rexml
OUT="../output/rexml/"

# Valid document tests.
rm ../output/rexml/dom/valid/*.txt ../output/rexml/sax/valid/*.txt ../output/rexml/xxe/valid/*.txt
INPUT="../samples/valid/"
for i in {001..060};
do
	ruby dom.rb ${INPUT}${i}.xml >> ${OUT}dom/valid/${i}.txt 2>&1
	ruby sax.rb ${INPUT}${i}.xml >> ${OUT}sax/valid/${i}.txt 2>&1
	ruby dom_xxe.rb ${INPUT}${i}.xml >> ${OUT}xxe/valid/${i}.txt 2>&1
done

# Not well-formed tests.
rm ../output/rexml/dom/not-wf/*.txt ../output/rexml/sax/not-wf/*.txt ../output/rexml/xxe/not-wf/*.txt
INPUT="../samples/not-wf/"
for i in {001..055};
do
	ruby dom.rb  ${INPUT}${i}.xml >> ${OUT}dom/not-wf/${i}.txt 2>&1
	ruby sax.rb ${INPUT}${i}.xml >> ${OUT}sax/not-wf/${i}.txt 2>&1
	ruby dom_xxe.rb ${INPUT}${i}.xml >> ${OUT}xxe/not-wf/${i}.txt 2>&1
done

# Injections tests.
INPUT="../samples/injections/"
rm ../output/rexml/dom/other/*.txt ../output/rexml/sax/other/*.txt ../output/rexml/xxe/other/*.txt
for i in {001..005}
do
	timeout 2s ruby dom.rb  ${INPUT}${i}.xml >> ${OUT}dom/other/${i}.txt 2>&1
	timeout 2s ruby sax.rb  ${INPUT}${i}.xml >> ${OUT}sax/other/${i}.txt 2>&1
	timeout 2s ruby dom_xxe.rb  ${INPUT}${i}.xml >> ${OUT}xxe/other/${i}.txt 2>&1
done

# Valid schemas tests.
INPUT="../samples/schemas-valid/"

rm ../output/rexml/valid-schemas/*.txt
for i in {001..005}
do
	ruby validate.rb ${INPUT}${i}.xml ${INPUT}${i}.xsd >> ${OUT}valid-schemas/${i}.txt 2>&1
done

INPUT="../samples/schemas-invalid/"

# Invalid schemas tests.
rm ../output/rexml/invalid-schemas/*.txt
for i in {001..005}
do
	ruby validate.rb ${INPUT}${i}.xml ${INPUT}${i}.xsd >> ${OUT}invalid-schemas/${i}.txt 2>&1
done
