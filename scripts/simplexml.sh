#!/bin/bash

cd ../simplexml
OUT="../output/simplexml/"

# Valid document tests.
rm ../output/simplexml/dom/valid/*.txt ../output/simplexml/xxe/valid/*.txt
INPUT="../samples/valid/"
for i in {001..060};
do
	php dom.php ${INPUT}${i}.xml >> ${OUT}dom/valid/${i}.txt 2>&1
	php dom_xxe.php ${INPUT}${i}.xml >> ${OUT}xxe/valid/${i}.txt 2>&1
done

# Not well-formed tests.
rm ../output/simplexml/dom/not-wf/*.txt ../output/simplexml/xxe/not-wf/*.txt
INPUT="../samples/not-wf/"
for i in {001..055};
do
	php dom.php  ${INPUT}${i}.xml >> ${OUT}dom/not-wf/${i}.txt 2>&1
	php dom_xxe.php ${INPUT}${i}.xml >> ${OUT}xxe/not-wf/${i}.txt 2>&1
done

# Injection tests.
INPUT="../samples/injections/"
rm ../output/simplexml/dom/other/*.txt ../output/simplexml/xxe/other/*.txt
for i in {001..005}
do
	timeout 2s php dom.php  ${INPUT}${i}.xml >> ${OUT}dom/other/${i}.txt 2>&1
	timeout 2s php dom_xxe.php  ${INPUT}${i}.xml >> ${OUT}xxe/other/${i}.txt 2>&1
done

# Valid schemas tests.
INPUT="../samples/schemas-valid/"
rm ../output/simplexml/valid-schemas/*.txt
for i in {001..005}
do
	php schema_validate.php ${INPUT}${i}.xml ${INPUT}${i}.xsd >> ${OUT}valid-schemas/${i}.txt 2>&1
done

# Invalid schemas tests.
INPUT="../samples/schemas-invalid/"
rm ../output/simplexml/invalid-schemas/*.txt
for i in {001..005}
do
	php schema_validate.php ${INPUT}${i}.xml ${INPUT}${i}.xsd >> ${OUT}invalid-schemas/${i}.txt 2>&1
done

