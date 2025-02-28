- description : doxygen 관련 내가 한 내용들을 정리한 것이다. 여기에 추가하여 doxygen의 internal document를 만들어 ebook으로 만들기를 원한다. 
- tag : doxygen , ebook , code-analysis , 
- date : 2024-01-01

TOC
- [1. getting started - 2024Y](#1-getting-started---2024y)
  - [1.1. source synchronization](#11-source-synchronization)
  - [1.2. compile source](#12-compile-source)
  - [1.3. test](#13-test)
  - [1.4. action items : what you will do](#14-action-items--what-you-will-do)
    - [1.4.1. enums type analysis](#141-enums-type-analysis)
    - [1.4.2. convert into C language from python and perl file](#142-convert-into-c-language-from-python-and-perl-file)

------------

# 1. getting started - 2024Y

## 1.1. source synchronization
- git clone https://github.com/cheoljoo/doxygen.git
  - my doxygen's master branch has specific function to get flow and sequence diagrm with plantuml
    - [detailed explanation](https://github.com/cheoljoo/doxygen/blob/FlowChart_SequenceDiagram/src/)doxygen_parse.md
  - so i use clean branch to merge upstream maser branch for starting to modifify the code from original code
- git remote add upstream https://github.com/doxygen/doxygen.git
- **git checkout clean**
- git remote -v
- git fetch upstream
- git merge upstream/master
- git push


## 1.2. compile source
- https://www.doxygen.nl/manual/install.html
- change PATH in linux shell
  - cd ~/.local/bin
  - ln -s ~/code/doxygen/build/doxygen doxygen
  - export PATH=$PATH:~/bin:~/bin/go/bin:~/tools-install/usr/bin:~/tools-install/usr/share:~/.local/bin
  - logout && login
  - which doxygen
    - /home/[your_id]]/.local/bin/doxygen

## 1.3. test
- copy example to ~/ttt
- cd ~/ttt
- doxygen -g
- vi Doxyfile
  - use Doxyfile.my
  - ```
    PROJECT_NAME           = CGADOXYGEN
    OUTPUT_DIRECTORY       = ./DOXYGEN_OUTPUT
    INLINE_INHERITED_MEMB  = YES
    ALIASES                =     ## change ALIASE for you
    EXTRACT_STATIC         = YES
    EXTRACT_LOCAL_METHODS  = YES
    HIDE_UNDOC_MEMBERS     = YES
    HIDE_UNDOC_CLASSES     = YES
    HIDE_FRIEND_COMPOUNDS  = YES
    CASE_SENSE_NAMES       = YES
    HIDE_SCOPE_NAMES       = YES
    HIDE_COMPOUND_REFERENCE= YES
    SHOW_GROUPED_MEMB_INC  = YES
    ENABLED_SECTIONS       = UML    ## just for your code
    INPUT                  = .
    RECURSIVE              = YES
    USE_MDFILE_AS_MAINPAGE = readme.md
    SOURCE_BROWSER         = YES
    STRIP_CODE_COMMENTS    = NO
    REFERENCED_BY_RELATION = YES
    REFERENCES_RELATION    = YES
    GENERATE_TREEVIEW      = YES
    GENERATE_LATEX         = NO
    GENERATE_AUTOGEN_DEF   = YES
    GENERATE_PERLMOD       = YES
    PERLMOD_LATEX          = YES     ## if NO , perlmod's Makefile is not working. so I should change it.
    HAVE_DOT               = YES
    UML_LOOK               = YES
    TEMPLATE_RELATIONS     = YES
    CALL_GRAPH             = YES
    CALLER_GRAPH           = YES
    INTERACTIVE_SVG        = YES
    PLANTUML_JAR_PATH      = ./plantuml.jar
    DOT_GRAPH_MAX_NODES    = 100
    ```

- doxygen
  - if PERLMOD_LATEX is off , perlmod's Makefile is not working.  so i should change it


## 1.4. action items : what you will do
- add enums type 
- enable PERL_MOD
- PERL_MOD files change : Makefile .. .etc.
- convert
  - convert into C language from python and perl file
  - convert perl data to python data
- perl_doc
  - make perl doc basically
  - make basic markdown output
- python_doc
  - make python doc basically
  - make basic markdown output
  - hpp2plantuml test (python) : https://github.com/thibaultmarin/hpp2plantuml
  - add hpp2plantuml 
  - how to show plantuml with proxy server (plantuml server)
- change document
  - PERL_MOD document changes how to use python in Doxyfile
  - change doc in make doc : https://www.doxygen.nl/manual/perlmod.html
    - add python development document

### 1.4.1. enums type analysis
- MR (merged) : https://github.com/doxygen/doxygen/pull/10554
- update Doxyfile : doxygen -u Doxyfile
  - EXTRACT_ALL            = YES
- make markdown document in perlmod
- perlmodgen.cpp
- new idea : PERLMOD does not have type of enum
-  flow :
    - generatePerlMod() -> pmg.generate()->
    - generatePerlModOutput()
        - $doxydocs =
        - iterate class ClassDef :
        - generatePerlModForFile(FileDef *fd) : 
            - generatePerlModSection(fd,fd->getMemberList(MemberListType_decEnumMembers),"enums");   ## file
                - fd->getMemberList(MemberListType_decEnumMembers)
                    - for (auto &ml : m_memberLists) ->  return ml.get();
                        - MemberLists           m_memberLists;
                         - ml.get() -> return class MemberList
                  - openHash("enums") 
                  - openList("members")
                  - void PerlModGenerator::generatePerlModForMember(const MemberDef *md,const Definition *)
                    -   m_output.openHash()
                    -     .addFieldQuotedString("kind", memType)
                    -     .addFieldQuotedString("name", name)
                    -     .addFieldQuotedString("virtualness", getVirtualnessName(md->virtualness()))
                    -     .addFieldQuotedString("protection", getProtectionName(md->protection()))
                    -     .addFieldBoolean("static", md->isStatic());
                    - 
                    -   addPerlModDocBlock(m_output,"brief",md->getDefFileName(),md->getDefLine(),md->getOuterScope(),md,md->briefDescription());
                    -   addPerlModDocBlock(m_output,"detailed",md->getDefFileName(),md->getDefLine(),md->getOuterScope(),md,md->documentation());
                    -   if (md->memberType()!=MemberType_Define &&
                    -       md->memberType()!=MemberType_Enumeration)
                    -     ```m_output.addFieldQuotedString("type", md->typeString());```
                    - this is solution for enum type
                      -   if (md->memberType()==MemberType_Enumeration)
                      -     m_output.addFieldQuotedString("charles-type", md->enumBaseType());
                  - closeList("members")
                  - closeHash("enums")

### 1.4.2. convert into C language from python and perl file
- check architecture
  - i can do manually. but , we need to change several points.
  - perlmodgen.cpp
    - you need to change 3 places.
  - ```cpp
    bool perlmodPython = Config_getBool(PERLMOD_PYTHON);          // **
    pathDoxyRules = perlModAbsPath + "/doxyrules.make";           // **
    void PerlModGenerator::generate()
    {
      Dir perlModDir;
      if (!createOutputDir(perlModDir))                           // **
        return;
      if (!(generatePerlModOutput()
        && generateDoxyStructurePM()
        && generateMakefile()
        && generateDoxyRules()))                                  // **
        return;
    }
    
    bool PerlModGenerator::generateDoxyRules()
    {
      std::ofstream doxyRulesStream;                             // **
      if (!createOutputFile(doxyRulesStream, pathDoxyRules))     // **
        return false;
      doxyRulesStream <<                                         // **
        prefix << "DOXY_EXEC_PATH = " << pathDoxyExec << "\n";
        return true;
    }

    class PerlModGenerator
    {
      QCString pathDoxyRules;
      bool generateDoxyRules();
    }
    ```