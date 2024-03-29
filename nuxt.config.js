module.exports = {
    modules: ['@nuxtjs/axios', '@nuxtjs/vuetify'],
    mode: 'spa',
    head: {
        title: 'FileSync',
        meta: [{
                charset: 'utf-8'
            },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1'
            },
            {
                hid: 'description',
                name: 'description',
                content: 'Nuxt.js + Vuetify.js project'
            }
        ],
        link: [{
                rel: 'icon',
                type: 'image/x-icon',
                href: '/favicon.ico'
            },
            {
                rel: 'stylesheet',
                href: '/material.css'
            }
        ],
    },
    loading: {
        color: 'white',
        height: '8px'
    }, // Disable default loading bar
    build: {
        extend(config, {
            isDev,
            isClient
        }) {
            if (isDev && isClient) {
                // Run ESLint on save
                config.module.rules.push({
                    enforce: 'pre',
                    test: /\.(js|vue)$/,
                    loader: 'eslint-loader',
                    exclude: /(node_modules)/
                })
            }
            // Extend only webpack config for client-bundle
            if (isClient) {
                config.target = 'electron-renderer'
            }
        }
    },
    dev: process.env.NODE_ENV === 'DEV',
    css: [
        '@/assets/css/global.css'
    ]
}