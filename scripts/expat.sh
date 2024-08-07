#!/bin/bash

cd ../expat
OUT="../output/expat/"

# Valid document tests.
rm ../output/expat/sax/valid/*.txt ../output/expat/xxe/valid/*.txt
INPUT="../samples/valid/"
for i in {001..060};
do
	./sax < ${INPUT}${i}.xml >> ${OUT}sax/valid/${i}.txt 2>&1
	./sax_xxe ${INPUT}${i}.xml >> ${OUT}xxe/valid/${i}.txt 2>&1
done

# Not well-formed tests.
rm ../output/expat/sax/not-wf/*.txt ../output/expat/xxe/not-wf/*.txt
INPUT="../samples/not-wf/"
for i in {001..055};
do
	./sax < ${INPUT}${i}.xml >> ${OUT}sax/not-wf/${i}.txt 2>&1
	./sax_xxe ${INPUT}${i}.xml >> ${OUT}xxe/not-wf/${i}.txt 2>&1
done

# Other tests.
INPUT="../samples/injections/"
rm ../output/expat/sax/other/*.txt ../output/expat/xxe/other/*.txt
for i in {001..005}
do
	timeout 2s ./sax < ${INPUT}${i}.xml >> ${OUT}sax/other/${i}.txt 2>&1
	timeout 2s ./sax_xxe  ${INPUT}${i}.xml >> ${OUT}xxe/other/${i}.txt 2>&1
done

