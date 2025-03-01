```plantuml
@startuml total.png

skinparam usecase {
    BackgroundColor<< Execution >> YellowGreen
    BorderColor<< Execution >> YellowGreen

    BackgroundColor<< Email >> LightSeaGreen
    BorderColor<< Email >> LightSeaGreen

    ArrowColor Olive
}
          rectangle processMap-memo {
    usecase (Makefile) as (Makefile) << Execution >>
    usecase (convert_csv_to_md.py) as (convert_csv_to_md.py) << Execution >>
    usecase (get-all-description-and-tag-to-network-graph.py) as (get-all-description-and-tag-to-network-graph.py) << Execution >>
    usecase (get-all-description-and-tag.py) as (get-all-description-and-tag.py) << Execution >>
    usecase (github/publish/memo/revision_creation.py) as (github/publish/memo/revision_creation.py) << Execution >>
    usecase (markdown-pp) as (markdown-pp) << Execution >>
    usecase (memo/revision_creation.py) as (memo/revision_creation.py) << Execution >>
    usecase (mod.lge.com/hub/publish/memo/revision_creation.py) as (mod.lge.com/hub/publish/memo/revision_creation.py) << Execution >>
    usecase (remove_files.py) as (remove_files.py) << Execution >>
    (memo) --> (Makefile) #line:green;line.bold;text:green : _
    (Makefile) --> (get-all-description-and-tag-to-network-graph.py) #line:green;line.bold;text:green : _
    (get-all-description-and-tag.json) --> (get-all-description-and-tag-to-network-graph.py) #line:green;line.bold;text:green : _
    (get-all-description-and-tag-to-network-graph.py) --> (./get-all-description-and-tag-to-network-graph.html) #line:green;line.bold;text:green : <Network Graph>
    (*.md [all directories]) --> (remove_files.py) #line:green;line.bold;text:green : _
    (remove_files.py) --> (github/publish/memo/*) #line:green;line.bold;text:green : <Copy only the files whose tag is neither private nor lge\npublic memo (ex. technology)>
    (remove_files.py) --> (mod.lge.com/hub/publish/memo/*) #line:green;line.bold;text:green : <Copy only the files whose tag is not private\nIt includes lge information>
    (*.md [all directories]) --> (memo/revision_creation.py) #line:green;line.bold;text:green : <private memo>
    (memo/revision_creation.py) --> (memo/revision.md) #line:green;line.bold;text:green : <[[https://github.com/cheoljoo/memo/blob/main/memo/revision.md revision.md]]>
    (github/publish/memo/*) --> (github/publish/memo/revision_creation.py) #line:green;line.bold;text:green : <public memo>
    (github/publish/memo/revision_creation.py) --> (github/publish/memo/revision.md) #line:green;line.bold;text:green : <[[https://github.com/cheoljoo/publish/blob/main/memo/revision.md revision.md]]>
    (mod.lge.com/hub/publish/memo/*) --> (mod.lge.com/hub/publish/memo/revision_creation.py) #line:green;line.bold;text:green : <lge memo>
    (mod.lge.com/hub/publish/memo/revision_creation.py) --> (mod.lge.com/hub/publish/memo/revision.md) #line:green;line.bold;text:green : <[[http://mod.lge.com/hub/cheoljoo.lee/publish/-/blob/main/memo/revision.md revision.md]]>
    (memo/revision.json) --> (memo/revision_creation.py) #line:green;line.bold;text:green : _
    (memo/revision_creation.py) --> (memo/revision.json) #line:green;line.bold;text:green : _
    (github/publish/memo/revision.json) --> (github/publish/memo/revision_creation.py) #line:green;line.bold;text:green : _
    (github/publish/memo/revision_creation.py) --> (github/publish/memo/revision.json) #line:green;line.bold;text:green : _
    (mod.lge.com/hub/publish/memo/revision.json) --> (mod.lge.com/hub/publish/memo/revision_creation.py) #line:green;line.bold;text:green : _
    (mod.lge.com/hub/publish/memo/revision_creation.py) --> (mod.lge.com/hub/publish/memo/revision.json) #line:green;line.bold;text:green : _
    (Makefile) --> (convert_csv_to_md.py) #line:green;line.bold;text:green : _
    (*/index.csv) --> (convert_csv_to_md.py) #line:green;line.bold;text:green : <ai,book,education,youtube>
    (convert_csv_to_md.py) --> (*/index.md) #line:green;line.bold;text:green : <ai,book,education,youtube>
    (convert_csv_to_md.py) --> (*/tag.json) #line:green;line.bold;text:green : <ai,book,education,youtube>
    (*.md [all directories]) --> (get-all-description-and-tag.py) #line:green;line.bold;text:green : _
    (get-all-description-and-tag.py) --> (get-all-description-and-tag.json) #line:green;line.bold;text:green : _
    (*/tag.json) --> (get-all-description-and-tag.py) #line:green;line.bold;text:green : <ai,book,education,youtube>
    (get-all-description-and-tag.py) --> (TOC.md) #line:green;line.bold;text:green : _
    (TOC.md) --> (markdown-pp) #line:green;line.bold;text:green : _
    (markdown-pp) --> (README.md) #line:green;line.bold;text:green : <[[https://github.com/cheoljoo/memo/blob/main/memo/README.md README.md]]>
    (TOC.mdpp) --> (markdown-pp) #line:green;line.bold;text:green : _
    (markdown-pp) --> (github/publish/memo/README.md) #line:green;line.bold;text:green : <[[https://github.com/cheoljoo/publish/blob/main/memo/README.md README.md]]>
    (markdown-pp) --> (mod.lge.com/hub/publish/memo/README.md) #line:green;line.bold;text:green : <[[http://mod.lge.com/hub/cheoljoo.lee/publish/-/blob/main/memo/README.md README.md]]>
  }
@enduml
```
