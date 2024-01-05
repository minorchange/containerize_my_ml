img_name := $(shell bash img_name.sh)
img_tag := $(shell bash img_tag.sh)
img_refernece := ${img_name}:${img_tag}


.PHONY: tarball
tarball:
	bash create_tarball.sh

.PHONY: build_and_run_locally
build_and_run_locally:
	cd .. && docker build -f containerize_my_ml/Dockerfile -t ${img_refernece} .  
	# syft --scope all-layers -o syft-text ${img_refernece}
	docker run -it ${img_refernece}

.PHONY: SBOM
SBOM:
	# cd .. && syft --scope all-layers -o syft-text ${img_refernece}
	cd .. && syft --scope all-layers -o syft-text ${img_refernece}

.PHONY:  vulnerability_scan
vulnerability_scan:
	sudo trivy image -o sec_scan_${img_refernece}.txt ${img_refernece}

.PHONY: security_scan
security_scan: SBOM vulnerability_scan
	@echo "----> Scanning Imgage" ${img_refernece} ...