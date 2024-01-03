img_name := $(shell source ./create_img_name_and_tag.sh && create_img_name)
img_tag := $(shell source ./create_img_name_and_tag.sh && create_img_tag)
img_refernece := ${img_name}:${img_tag}


.PHONY: tarball
tarball:
	@echo "Am Here"
	echo $(shell pwd)
	bash create_tarball.sh

.PHONY: build_and_run_locally
build_and_run_locally:
	cd .. && docker build -f containerize_my_ml/Dockerfile -t ${img_refernece} .  
	docker run -it ${img_refernece}
