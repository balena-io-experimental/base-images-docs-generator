# BaseImages documentation generator

A series of tools to aid in autogenerating documentation for the [base images section](https://www.balena.io/docs/reference/base-images/base-images/) of the [balena documentation](https://www.balena.io/docs/).

## Base Image List

Generates the full [base images listings](https://www.balena.io/docs/reference/base-images/base-images-ref/). Uses the [base contracts](https://github.com/balena-io/contracts) to generate the listings.

```shell
python3 base-images-ref.py > output/base-images-ref.md
```

Once output, copy the resulting file to `/pages/reference/base-images/base-images-ref.md` on the docs repo. Then build and check for broken links using npm broken link checker e.g.

```shell
blc --get --input http://localhost:3000/docs/reference/base-images/base-images-ref/ > base-images-ref.md
```

Followed by `cat base-images-ref.md | grep "BROKEN"` to identify any broken links.

## Machine names and architectures

Generates [this listing](https://www.balena.io/docs/reference/base-images/devicetypes/) of machine names and architectures from the [base contracts](https://github.com/balena-io/contracts).

```shell
python3 machine-names.py > output/machine-names.md
```

Once output, copy the resulting output to `/shared/deviceTypeNames.md` on the docs repo. Then build and check for broken links:

```shell
blc --get --input http://localhost:3000/docs/reference/base-images/devicetypes/ > device_types.md
```

Followed by `cat device-types.md | grep "BROKEN"` to identify broken links.

## Balena base images

A quick helper script to output latest and all version information to update the text on the [base images overview](https://www.balena.io/docs/reference/base-images/base-images/) page. #TODO restructure that page to apply updates automatically.

```shell
python3 base-images.py
```
