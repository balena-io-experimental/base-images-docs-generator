# BaseImages documentation generator

### base-images-ref

Generates [this](https://www.balena.io/docs/reference/base-images/base-images-ref/) page on the docs repo.

`python3 base-images-ref.py > output/base-images-ref.md`

Then copy the resulting file to `/pages/reference/base-images/base-images-ref.md` on the docs repo. Then build and check for broken links using npm broken link checker

`blc --get --input http://localhost:3333/docs/reference/base-images/base-images-ref/ > base-images-ref.md` then `cat base-images-ref.md | grep "BROKEN"`.

### machine-names.py

Generates [this](https://www.balena.io/docs/reference/base-images/devicetypes/) page on the docs repo.

`python3 machine-names.py > output/machine-names.md`

Then copy the resulting output to `/shared/deviceTypeNames.md` on the docs repo. Then build and check for broken links:

`blc --get --input http://localhost:3333/docs/reference/base-images/devicetypes/ > device_types.md` then `cat device-types.md | grep "BROKEN"`.

### base-images

Used to update text on [this](https://www.balena.io/docs/reference/base-images/base-images/) page.