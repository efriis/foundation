# Foundation

## Repo structure

There are Python and TypeScript versions of the Foundation types. Both the
Python and the TypeScript projects are rooted at this repo's root.

## Installing

**(These instructions may be out-of-date. Please check with Aaron/Andrey/Erick.)**

If installing from source, run the following commands in this projects root directory

```
pip install .
```

To use this within a service, add the following lines to your Dockerfile (this assumes your build machine has access to the Instabase GitHub org):

```docker
RUN git clone git@github.com:instabase/foundation.git && \ # preferably at some version
    cd foundation && \
    pip install . && \
    cd .. && \
    rm -rf foundation
```

## Changelog

### v0.0.4

- Add TypeScript support.
- Add TS/Py `FOUNDATION_VERSION` globals for runtime version checking.

### v0.0.3
- Removed protos, all types are now dataclasses + JSON.
- Added address components to Address Entity.
- Removed Line entity, please use the more flexible Phrase entity.
- **This is a breaking change** Please upgrade your usage of Foundation with the new API.

### v0.0.2
- Change some type definitions to be more flexible.
- Additional types.

### v0.0.1
- Basic types and serialization/deserialization.
