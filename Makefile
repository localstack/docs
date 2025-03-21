all: dev

serve:
	hugo serve

dev:
	hugo serve --watch=true --disableFastRender -D

install:
	git submodule update --init --recursive
	@which hugo || echo "Please install Hugo extended: https://gohugo.io/installation/"

clean:
	hugo mod clean

# Required for updating Developer Hub applications
install_apps:
	@which node || echo "Please install Node.js: https://nodejs.org"
	node scripts/create-applications.js

clean_apps:
	git clean -f content/en/applications

lint:
	@which markdownlint-cli2 > /dev/null || (echo "Please install markdownlint-cli2: npm install -g markdownlint-cli2" && exit 1)
	markdownlint-cli2 --fix

.PHONY: serve dev install clean install_apps clean_apps
