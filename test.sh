testDir='test/'
testFiles='CloudantDbTest.py idRequestHandlerTest.py JsonParserTest.py measureRequestHandlerTest.py
blueprintTest.py'

for i in $testFiles
do
  python3 $testDir$i
done
