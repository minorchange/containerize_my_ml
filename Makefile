img_name := $(shell bash img_name.sh)
img_tag := $(shell bash img_tag.sh)
img_refernece := ${img_name}:${img_tag}


.PHONY: tarball
tarball:
	bash create_tarball.sh

.PHONY: build_and_run_locally
build_and_run_locally:
	cd .. && docker build -f containerize_my_ml/Dockerfile -t ${img_refernece} .  
	docker run -it ${img_refernece}
