module.exports = {
  devServer: {
    proxy: {
      '/api/*': {
        target: `https://${process.env.BACKEND_HOST ? process.env.BACKEND_HOST : '63f7b30c2db7870008628742--helpful-figolla-146d54.netlify.app/'}`,
        secure: false
      },
      '/django_media/*': {
        target: `https://${process.env.BACKEND_HOST ? process.env.BACKEND_HOST : '63f7b30c2db7870008628742--helpful-figolla-146d54.netlify.app/'}`,
        secure: false
      },
      '/django_static/*': {
        target: `https://${process.env.BACKEND_HOST ? process.env.BACKEND_HOST : '63f7b30c2db7870008628742--helpful-figolla-146d54.netlify.app/'}`,
        secure: false
      }
    }
  },
  chainWebpack: config => {
    config
        .plugin('html')
        .tap(args => {
            args[0].title = "Robotics Club IITJ";
            return args;
        })
    }
}
