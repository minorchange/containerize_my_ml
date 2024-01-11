img_name := $(shell bash img_name.sh)
img_tag := $(shell bash img_tag.sh)
img_refernece := ${img_name}:${img_tag}


.PHONY: update_requirements
update_requirements:
	pipenv requirements > requirements.txt
	cd .. && pipenv requirements > requirements.txt 

.PHONY: tarball
tarball:
	bash create_tarball.sh

.PHONY: build
build:
	$(MAKE) update_requirements
	cd .. && docker build -f containerize_my_ml/Dockerfile -t ${img_refernece} .  
	# syft --scope all-layers -o syft-text ${img_refernece}

.PHONY: run_locally
run_locally:
	docker run -it ${img_refernece}


# .PHONY: build_and_run_locally
# build_and_run_locally:
# 	$(MAKE) update_requirements
# 	cd .. && docker build -f containerize_my_ml/Dockerfile -t ${img_refernece} .  
# 	# syft --scope all-layers -o syft-text ${img_refernece}
# 	docker run -it ${img_refernece}

.PHONY: SBOM
SBOM:
	# cd .. && syft --scope all-layers -o syft-text ${img_refernece}
	cd .. && syft --scope all-layers -o syft-text ${img_refernece}

.PHONY: vulnerability_scan
vulnerability_scan:
	cd .. && sudo trivy image -o cve_scans/cve_scan_${img_refernece}.txt ${img_refernece}

.PHONY: security_scan
security_scan: 
	$(MAKE) SBOM
	$(MAKE) vulnerability_scan


.PHONY: bnr
bnr:
	$(MAKE) build
	$(MAKE) run_locally
	$(MAKE) security_scan