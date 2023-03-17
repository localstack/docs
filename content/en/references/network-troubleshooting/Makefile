all: images/1.svg images/2.svg images/3.svg images/4.svg images/5.svg images/6.svg images/7.svg images/8.svg images/9.svg images/10.svg images/11.svg images/12.svg images/overview-1.svg images/overview-2.svg images/overview-3.svg

images/%.svg: images-src/%.d2
	d2 --sketch --theme 0 --pad 8 --layout elk $< $@
