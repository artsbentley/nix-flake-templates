TENANT=training
VERSION=0.1.0
tagname=arar-test
tenantuserid=1054

DOCKER_REPO_URL=registry.cp.kpn-dsh.com/$(TENANT)
image=$(DOCKER_REPO_URL)/$(tagname):$(VERSION)

build:
	docker build --platform linux/amd64 -t $(tagname) -f Dockerfile --build-arg tenantuserid=$(tenantuserid) .
	docker tag  $(tagname) $(image)
push:
	docker push $(image)
show:
	@echo ""
	@echo "#make file configuration"
	@echo "#URL          :" $(DOCKER_REPO_URL)
	@echo "#PLATFORM     :" $(PLATFORM)
	@echo "#TENANT       :" $(TENANT)
	@echo "#tenantuserid :" $(tenantuserid)
	@echo "#tagname      :" $(tagname)
	@echo "#version      :" $(VERSION)
	@echo "#image        :" $(image)
dive:
	dive $(image)
run:
	docker run --platform linux/amd64 -u $(tenantuserid):$(tenantuserid) -it --entrypoint "/bin/sh" $(image)
all:
	make build
	make push
	make show

