# znapzend-spec

This is simply a spec file for building an RPM for [znapzend][].

  [znapzend]: http://www.znapzend.org

### Usage

Make sure the `Version` field is set to the latest release for znapzend.
(Check the [znapzend releases page][znapzend-releases] if you're not sure.)

  [znapzend-releases]: https://github.com/oetiker/znapzend/releases

Download the corresponding tarball.  If you have `spectool` installed (in
the `rpmdevtools` package on RHEL/Fedora systems), that's simply:

    spectool -g -R znapzend.spec

Use the spec file to build the RPM.  With `rpmbuild`, that's:

    rpmbuild -ba znapzend.spec
