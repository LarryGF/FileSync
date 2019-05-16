# elecnuxt

> Nuxt + Electron

## Build Setup

``` bash
# install dependencies
$ npm install # Or yarn install

# development with vue devtools
$ npm run dev

# build for production
$ npm run build

For detailed explanation on how things work, checkout [Nuxt.js](https://github.com/nuxt/nuxt.js), [Electron.js](https://electronjs.org/), and [electron-builder](https://www.electron.build/).
```

## In Windows
Copy "activate_fix.bat" to "pyenv/Scripts" before create virtualenv, this script is for "virtualenv", don't for "pyenv".

Python 3.7 is prefere because use asyncio native and uvicorn use this library, in older version is need used uvloop and
some version of this library is incopatible for windows