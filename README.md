# balena + pimoroni enviro pHat

This is a project to get you started with the [Pimoroni Enviro pHat][envirophat] and its awesome [python library][py-envirophat] on balenaOS and balenaCloud.

## usage

### for balenaCloud managed devices

1. Provision a device in your application following the balenaCloud [Getting Started Guide][balena-get-started].
2. Clone this repository locally and add the `balena git remote` to the repo.
3. Run `git push balena master` and wait for the code to be deployed. The code will build and run, you will hear the relay clicking every 5 seconds.

### for unmanaged balenaOS devices

1. Follow the balenaOS [Getting Started Guide][balenaos-get-started] and get your device set up. Make sure you are familiar with [`balena-cli`][balena-cli] and can push a basic container.
2. Once your balenaOS device is showing on the local network, ssh into it doing `balena ssh --host`. On the host load up the i2c kernel module by running: `modprobe i2c-dev`
3. Clone this repository locally and run `balena push balena.local -s .` from the root of the repository folder.

[envirophat]:https://shop.pimoroni.com/products/enviro-phat
[py-envirophat]:https://github.com/pimoroni/enviro-phat
[balena-get-started]:https://balena.io/docs/raspberrypi3/python/getting-started/
[balenaos-get-started]:https://www.balena.io/os/docs/raspberrypi3/getting-started/
[balena-cli]:https://github.com/balena-io/balena-cli
