BUILDDIR = build

html singlehtml:
	sphinx-build -b $@ -d $(BUILDDIR)/doctrees . $(BUILDDIR)/$@

clean:
	rm -r $(BUILDDIR)
