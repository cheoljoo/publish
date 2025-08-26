

# change user and passwd if you use it

all: 
	python3 convert_csv_to_md.py
	echo "==> get get-all-description-and-tag.json from get-all-description-and-tag.py"
	python3 get-all-description-and-tag.py
	echo "==> make network-graph map from get-all-description-and-tag.json"
	python3 get-all-description-and-tag-to-network-graph.py
	echo "! $(CURDIR) : make p"
	if [ ! -d  ../processMap ]; then cd ..; git clone --depth 1 https://github.com/cheoljoo/processMap.git ; else cd ../processMap; git pull ; fi
	python3 ../processMap/draw_pm.py --authname cheoljoo.lee --authpasswd your_host_passwd --input processmap.csv
	markdown-pp TOC.mdpp -o README.md
	rm -rf processMap-memo.md ./__debug data.py ./lib ./server-data
	if [ ! -d  ../mod_publish ]; then cd ..; git clone --depth 1 http://mod.lge.com/hub/cheoljoo.lee/publish.git mod_publish ; else cd ../mod_publish ; git pull ; fi
	if [ ! -d  ../github_publish ]; then cd ..; git clone --depth 1 https://github.com/cheoljoo/publish.git github_publish ; else cd ../github_publish ; git pull ; fi
	cp -r ../memo ../github_publish
	cp -r ../memo ../mod_publish
	python3 remove_files.py --dir=../github_publish/memo --remove_tags=private,lge
	python3 remove_files.py --dir=../mod_publish/memo --remove_tags=private
	cd ../github_publish/memo; make simple
	cd ../mod_publish/memo; make simple
	git checkout -f revision.json
	python3 revision_creation.py
	cd ../github_publish/memo; git checkout -f revision.json
	cd ../mod_publish/memo; git checkout -f revision.json
	cd ../github_publish; git add memo
	cd ../github_publish/memo; python3 revision_creation.py
	cd ../mod_publish; git add memo
	cd ../mod_publish/memo; python3 revision_creation.py
simple:
	python3 convert_csv_to_md.py
	echo "==> get get-all-description-and-tag.json from get-all-description-and-tag.py"
	python3 get-all-description-and-tag.py
	echo "==> make network-graph map from get-all-description-and-tag.json"
	python3 get-all-description-and-tag-to-network-graph.py
	markdown-pp TOC.mdpp -o README.md
	rm -rf processMap-memo.md ./__debug data.py ./lib ./server-data
del:
	rm -rf ../github_publish  ../mod_publish
t:
	git checkout -f revision.json
	python3 revision_creation.py
p:
	python3 ../processMap/draw_pm.py --authname cheoljoo.lee --authpasswd your_host_passwd --input processmap.csv
updated-list:
	python3 find-recent-updated-file.py -n 30 --use-git-date --show-size --oneline
updated-list-in-detail:
	python3 find-recent-updated-file.py -n 10 --use-git-date --show-size

