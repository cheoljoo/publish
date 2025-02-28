- description : xml parsing 하는 내용 정리
- tag : doxygen , xml , parsing
- date : 2024-01-01

TOC
- [1. parsing with doxygen xml](#1-parsing-with-doxygen-xml)
  - [1.1. my working area](#11-my-working-area)
- [2. xml 관련 봐야 할 것들을 적어두자.](#2-xml-관련-봐야-할-것들을-적어두자)

------------------

# 1. parsing with doxygen xml

- doxygen xml 에 대해서 parse
  - 예제를 가지고 해보면 xml을 하고 여러 option을 켜면 , switch를 예제로 넣은 것에서 보면 browse 까지 할수 있게 on 시키면 모든것을 볼수 있는 것으로 보인다.
  - 그것을 파싱을 마지막단까지 할수있게 다시 고쳐서 사용해봐야 할 것이다. 
  - https://git.ichec.ie/performance/storage/superdeimos/-/tree/master/external/doxygen-xml-parser?ref_type=heads

- [Managed wrapper for doxygen xml documentation](https://github.com/bdmihai/doxygenxmlparser) -> code is c++
- https://github.com/topics/doxygen-xml

- http://mod.lge.com/hub/cheoljoo.lee/doxygen_flowchart_class_document   에 소스가 만들어졌다.
  - flowchart를 만들어준다.
  - sequence diagram 에 대해서는 ; 으로 나누어야 하고  , 여기서 call 된 것이 함수인것을 먼저 판단해야 한다. 
    - 이를 위해서는 codeline에 <ref refid="classClassA_1a0d0ea557f59ec09c4ff99a4d2944a856" kindref="member">ClassA::classAfunc</ref> 을 보고 살펴봐야 하는데 refid나 kindref만을 보고 함수인지 알수 없기에
    - refid를 모두 따로 모아두어야 한다.   classClassA.xml을 보면 <memberdef kind="function" id="classClassA_1a0d0ea557f59ec09c4ff99a4d2944a856" prot="public" static="no" const="no " explicit="no" inline="no" virt="non-virtual"> 을 보고 function 이라는 것을 알면된다. 
    - 또는 결국은 처음에 함수들의 list를 먼저 얻는다. 이 값을 가지고 있을때 refid 값도 같이 가지고 있으면 된다.
    - index.xml 을 보면 compound -> member
      - ```
        <compound refid="a_8cpp" kind="file"><name>a.cpp</name>
            <member refid="a_8cpp_1ab8ab6458b874d68a456b82dd9df83bab" kind="function"><name>last</name></member>
        <compound refid="classClassA" kind="class"><name>ClassA</name>
            <member refid="classClassA_1ac6cd18e8cb2ef25c17f9036473e9c9bc" kind="function"><name>ClassA</name></member>
            <member refid="classClassA_1a0d0ea557f59ec09c4ff99a4d2944a856" kind="function"><name>classAfunc</name></member>
        ```

- 결과 
  - tiger core module에 대한 class document 및 flow chart 생성 완료
  - deliverables : http://mod.lge.com/hub/cheoljoo.lee/doxygen_flowchart_class_document/-/commit/432392b1e5e05586700e5a6c804a2b18700059e3
  - 추가한 이력
    - flow control : if , for , do , while , switch 
    - template 처리
    - { } 가 없는 syntax에 대한 처리
    - 주석에 대한 처리 : 삭제
    - string literal에 대한 처리
    - do ~ while 처리
    - if ~ else if 처리
    - multiple depth의 combined type
    - nested #if #ifdef 에 대한 해결 : 모든 define된 내용을 파악할수도 입력하기도 문제가 되기에 무조건 #if 부분을 처리하고 # else ~ #endif는 처리하지 않음.
    - closure 처리 : doxygen xml에서 closure 함수 안의  if가 keyword로 잡히지 않는 문제 
  - 결과 :
    - class document만 :: http://tiger02.lge.com/cheoljoo.lee/temp/report-doc
    - class document와 flow chart :: http://tiger02.lge.com/cheoljoo.lee/temp/report-doc-dc

## 1.1. my working area
- doxygen xml
  - ~/code/xml/_output_/xml  ->  code/ssh/xml 에서 doxygen의 xml을 parsing하는 것에 대해서 다룸. a_8cpp.xml 을 분석하면 BROSWER하는 모든 소스들에 대한 flow chart / sequence diagram을 그릴수 있을 것으로 판단됨
  - 그 외의 무슨 c++ xml parsing 관련 link 들이 있는지 알아본다. 
      - gcc에서의 xml (gcc-xml) : https://github.com/gccxml/gccxml/blob/master/README-GCCXML.rst
        - python gcc xml : https://doanminhdang.gitlab.io/notes/Tools/Software/Python/Python_parser_for_C,_C++.html
      - c++ paring CLANG
        - https://sudonull.com/post/907-An-example-of-parsing-C-code-using-libclang-in-Python
        - https://blog.naver.com/PostView.naver?blogId=nswve&logNo=222784304743&parentCategoryNo=&categoryNo=49&viewDate=&isShowPopularPosts=true&from=search
      - doxygen xml to markdown : https://github.com/matusnovak/doxybook2?tab=readme-ov-file
      - Render Doxygen XML via text templates : https://github.com/pcolby/doxlee
      - doxyxml generated : https://github.com/gnuradio/gr-tutorial/tree/master/docs/doxygen/doxyxml/generated
      - my doxygen test sampel code : https://github.com/cheoljoo/doxygen/blob/FlowChart_SequenceDiagram/test/a.cpp
  - xml을 parsing하면 된다. f.py
    - a.cpp -> a_8cpp.xml     . 대신 _8을 붙이고 뒤에 .xml 을 더하면 파일이름이 생성된다.
  - { } braces 가 없는 것이 있다. 이것들을 어떻게 붙여줄수 있는가?  이것이 붙어 있으면 { } 기준으로만 코드를 작성하면 된다.   { } 이 없다면 뒤에 1줄짜리가 오는 경우와 if ()  if() 와 같은 경우에 대한 처리를 해야 한다. 
    - time clang-tidy -checks='-*,readability-braces-around-statements' -fix-errors a.cpp
      - a.cpp의 경우 5초가 걸렸다.   real    0m5.355s
    - 시간이 너무 느려서 stack 을 이용하여 이 부분을 처리 했다.  처음 시작이 { 으로 되는지 아닌지로 구문을 하게 구현을 하였다.


# 2. xml 관련 봐야 할 것들을 적어두자.
0.sample로 이용할 source code : https://github.com/cheoljoo/doxygen/blob/FlowChart_SequenceDiagram/test/a.cpp
1. /home/cheoljoo.lee/temp/ttt/output/superdeimos/external/doxygen-xml-parser/src/xml_to_json_parser
받아둔 것을 봐야 한다.
2. https://pypi.org/project/DoxyXML/  이 동작하는지 확인한다. 
샘플을 하나 정해두고 , 그 내용이 잘 parsing 되는지 본다. 
source browser내용까지도 파싱되는지 봐야 할 것이다.
3. doxygen doxmlparser    https://fossies.org/linux/doxygen/addon/doxmlparser/README.md
The API is generated from the index.xsd and compound.xsd XML schema files using Dave Kuhlman’s generateDS https://www.davekuhlman.org/generateDS.html
The current code is generated with generateDS version 2.37.15.
3-1. https://www.doxygen.nl/manual/starting.html
XML output
The XML output consists of a structured "dump" of the information gathered by doxygen. Each compound (class/namespace/file/...) has its own XML file and there is also an index file called index.xml.
A file called combine.xslt XSLT script is also generated and can be used to combine all XML files into a single file.
Doxygen also generates two XML schema files index.xsd (for the index file) and compound.xsd (for the compound files). This schema file describes the possible elements, their attributes and how they are structured, i.e. it the describes the grammar of the XML files and can be used for validation or to steer XSLT scripts.
In the addon/doxmlparser directory you can find a parser library for reading the XML output produced by doxygen in an incremental way (see addon/doxmlparser/doxmparser/index.py and addon/doxmlparser/doxmlparser/compound.py for the interface of the library)
4. https://rgoswami.me/posts/doc-cpp-dox-sph-exhale/   이것도 따라서 한번 해봐야 할 것 같음
5. https://github.com/breathe-doc/breathe   
