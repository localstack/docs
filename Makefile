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

.PHONY: serve dev install clean
