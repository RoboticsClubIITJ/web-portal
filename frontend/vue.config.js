module.exports = {
  devServer: {
    proxy: {
      "/api/*": {
        target: `http://${ process.env.BACKEND_HOST !== "" ? process.env.BACKEND_HOST : '127.0.0.1' }:8000`,
        secure: false
      }
    }
  }
};
